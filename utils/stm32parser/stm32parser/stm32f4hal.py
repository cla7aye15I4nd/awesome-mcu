import os
import shutil
import configparser
from tempfile import TemporaryFile


from stm32parser.parser import STM32Parser


class STM32F4HalParser(STM32Parser):
    def __init__(self, path):
        super().__init__(path, 'stm32f4')
        
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

    def output(self, dir):
        def get_config_text(config):
            with TemporaryFile('w+t') as f:
                config.write(f)
                f.seek(0)
                return f.read()

        if os.path.exists(dir):
            shutil.rmtree(dir)

        os.mkdir(dir)

        config_map = {}
        for board in self.boards:
            config = configparser.ConfigParser()            

            for name in sorted(board.peripheral.keys()):
                perip = board.peripheral[name]
                config[perip.peripname] = perip.keys

            text = get_config_text(config)
            if text not in config_map:
                config_map[text] = []
                        
            config_map[text].append(board.version)

        used = set()
        for key in sorted(config_map.keys(), key=lambda x: -len(config_map[x])):
            file_list = config_map[key]
            print(file_list)

            first = file_list[0]
            version = first[:-2] if first[:-2] not in used else first
            used.add(version)
            
            with open(os.path.join(dir, f'{version}.ql'), 'w') as f:
                f.write(key)
