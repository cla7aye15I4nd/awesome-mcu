import os
import re

from stm32parser.board import Board
from stm32parser.struct import Struct
from stm32parser.utils import lcutstrip, rcutstrip, split_comment, strip_unsigned

class STM32Parser:
    def __init__(self, path, version):
        self.path = path
        self.version = version
        self.type_table = {
            'uint8_t' : 'ctypes.c_uint8',
            'uint16_t': 'ctypes.c_uint16',
            'uint32_t': 'ctypes.c_uint32',
        }

        self.structs = {}
        self.load_board()
        self.load_all_peripheral()
        self.compare_peripheral()        

    def gettypename(self, name: str) -> str:
        if name in self.type_table:
            return self.type_table[name]

        if name.endswith('_TypeDef'):
            return name[:-8]

    def load_board(self):
        self.boards = []
        regex = f'^{self.version}[0-9][0-9][a-z][a-z]\.h$'

        for file in sorted(os.listdir(self.path)):
            if re.match(regex, file):
                with open(os.path.join(self.path, file)) as f:
                    self.boards.append(Board(file[:-2], f.read()))

    def load_all_peripheral(self):
        for board in self.boards:  
            print(f'Find version: {board.version}')

            self.load_enum(board)          
            self.load_struct(board)
            self.load_consts(board)
            
            board.find_key()

    def load_enum(self, board: Board):
        lines = []

        i = 0
        while i < len(board.lines):
            line = board.lines[i].strip()

            if line == 'typedef enum':
                i += 2
                
                while board.lines[i].strip()[0] != '}':
                    line = board.lines[i].strip()
                    line, _ = split_comment(line)
                    if len(line.strip()) > 0:
                        name, irq = line.strip(', ').split('=')
                        name = name.strip()
                        board.context[name] = eval(irq)                        
                    i += 1
            else:
                lines.append(line)

            i += 1


        board.lines = lines
    
    def load_struct(self, board: Board):
        lines = []

        i = 0
        while i < len(board.lines):
            line = board.lines[i].strip()
            
            if line == 'typedef struct':
                i += 2 # skip 'typedef struct\n{'

                struct = Struct()
                while board.lines[i].strip()[0] != '}':
                    line = board.lines[i].strip()
                    
                    comment = ''
                    if '/*' in line:
                        line, comment = line.split(';', maxsplit=1)

                        comment = comment.strip()
                        while not comment.endswith('*/'):
                            i += 1
                            comment = comment + ' ' + board.lines[i].strip()

                        comment = comment.strip('*!</ ')

                    line = lcutstrip(lcutstrip(line, '__IO'), 'const')
                    typename, varname = line.split()
                    
                    typename = self.gettypename(typename)
                    varname = varname.strip().strip(';')
                    if ']' == varname[-1]:
                        varname, number = varname[:-1].split('[')
                        typename = typename + f' * {eval(number)}'

                    struct.add_variable((typename, varname, comment))
                    
                    i += 1

                struct.classname = rcutstrip(board.lines[i].strip('}; '), 'TypeDef').strip('_')
                board.add_struct(struct)
            else:
                lines.append(line)

            i += 1

        board.lines = lines

    def load_consts(self, board: Board):
        lines = []
        for line in board.lines:
            if line.startswith('#define'):
                info, _ = split_comment(line)
                items = info.split(maxsplit=2)

                if len(items) != 3:
                    assert len(items) < 3
                    continue

                _, name, expr = info.split(maxsplit=2)
                
                expr = strip_unsigned(expr).replace('(uint32_t)', '')
                if name.startswith('IS_') or name.endswith('_IRQHandler'):
                    continue

                if 'TypeDef *)' in expr:
                    typename, address = expr.strip('()').split('TypeDef *)')
                    typename = typename.strip('_')
                    address = eval(address, board.context)
                    board.context[name] = address
                    board.add_peripheral(name, typename, address)
                
                else:
                    try:
                        board.context[name] = eval(expr, board.context)
                    except:
                        print(f'Error transfer {repr(line)} => {[name, expr]} {board.version}')
            else:
                lines.append(line)

        board.lines = lines

    def compare_peripheral(self):
        for board in self.boards:
            for _, perip in board.peripheral.items():
                self.find_struct(perip.classname)

    def find_struct(self, name):
        if name in self.structs:
            return

        print(f'Check {name}')
        perips = []
        self.structs[name] = []

        for board in self.boards:
            for _, perip in board.peripheral.items():
                if perip.classname == name:
                    perips.append((board, perip.struct))

        for board, struct in perips:
            for st in self.structs[name]:
                if st == struct:
                    if board.version not in st.files:
                        st.files.append(board.version)
                    break
            else:
                struct.files.append(board.version)
                self.structs[name].append(struct)

        verno = 0
        size = len(self.structs[name])
        for struct in self.structs[name]:
            if 'stm32f411xe' in struct.files or size == 1:
                struct.aliasname = f'STM32F4xx{name.capitalize()}'
            else:
                verno += 1
                struct.aliasname = f'STM32F4xx{name.capitalize()}V{verno}'

            print(struct.aliasname, struct.files)

        for board in self.boards:
            for _, perip in board.peripheral.items():
                if perip.classname == name:
                    for struct in self.structs[name]:
                        if perip.struct == struct:
                            perip.struct = struct
                            perip.keys['class'] = struct.aliasname
                            break