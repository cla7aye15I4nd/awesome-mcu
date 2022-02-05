import os
import re
import json
import shutil
import configparser

from collections import OrderedDict
from tempfile import TemporaryFile


from stm32parser.parser import STM32Parser


class STM32F1HalParser(STM32Parser):
    def __init__(self, path):
        super().__init__(path, 'stm32f1')
        
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
            if 'stm32f103xb' in struct.files or size == 1:
                struct.aliasname = f'STM32F1xx{name.capitalize()}'
            else:
                verno += 1
                struct.aliasname = f'STM32F1xx{name.capitalize()}V{verno}'

            print(struct.aliasname, struct.files)

        for board in self.boards:
            for _, perip in board.peripheral.items():
                if perip.classname == name:
                    for struct in self.structs[name]:
                        if perip.struct == struct:
                            perip.struct = struct
                            perip.keys['class'] = struct.aliasname
                            break

    def print_code(self, dir):
        with open(os.path.join(dir, 'stm32f1.py'), 'w') as f:
            f.write('import ctypes\n\n')

            for _, perip_set in self.structs.items():
                for perip in perip_set:
                    f.write(f'class {perip.aliasname}:\n')
                    f.write(f'    class Type(ctypes.Structure):\n')
                    f.write(f'        """ the structure available in :\n')

                    for file in perip.files:
                        f.write(f'                {file}\n')
                    
                    f.write(f'        """\n\n')
                    f.write(f'        _fields_ = [\n')

                    varname_maxlen = 0
                    typename_maxlen = 0
                    for typename, varname, _ in perip.variables:
                        varname_maxlen = max(varname_maxlen, len(varname))
                        typename_maxlen = max(typename_maxlen, len(typename))

                    for typename, varname, comment in perip.variables:
                        f.write(f'            ("{varname}"{" " * (varname_maxlen - len(varname))}, {typename}),{" " * (typename_maxlen - len(typename))} #{comment}\n')

                    f.write(f'        ]\n')
                    f.write('\n')

    def print_config(self, dir):
        config_map = {}
        for board in self.boards:
            items = []
            for name, perip in board.peripheral.items():
                if '_Channel' in perip.peripname or '_COMMON' in perip.peripname or 'DAC' == perip.peripname or 'OB' == perip.peripname:
                    continue
                if "base" in perip.keys:
                    perip.keys["base"] = int(perip.keys["base"], 16)
                keys = {}
                for k, v in perip.keys.items():
                    if k in ['type', 'base', 'class']:
                        keys[k] = v
                    elif k != "2_intn":
                        if 'kwargs' not in keys:
                            keys["kwargs"] = {}
                        keys["kwargs"][k] = v
                items.append((perip.peripname, keys))
            
            def cmpp(a, b):
                a1, b1 = a[1], b[1]
                if a1['type'] != b1['type']:
                    return -1 if a1['type'] < b1['type'] else 1
                if a1['base'] != b1['base']:
                    return -1 if a1['base'] < b1['base'] else 1
                return 0
            def cmp_to_key(mycmp):
                'Convert a cmp= function into a key= function'
                class K:
                    def __init__(self, obj, *args):
                        self.obj = obj
                    def __lt__(self, other):
                        return mycmp(self.obj, other.obj) < 0
                    def __gt__(self, other):
                        return mycmp(self.obj, other.obj) > 0
                    def __eq__(self, other):
                        return mycmp(self.obj, other.obj) == 0
                    def __le__(self, other):
                        return mycmp(self.obj, other.obj) <= 0
                    def __ge__(self, other):
                        return mycmp(self.obj, other.obj) >= 0
                    def __ne__(self, other):
                        return mycmp(self.obj, other.obj) != 0
                return K
                
            items = sorted(items, key=cmp_to_key(cmpp))
            newmap = OrderedDict(items)
            # text = get_config_text(config)
            text = re.sub(' (\d+)', lambda i: ' ' + hex(int(i.group(0))), json.dumps(newmap, indent=4))

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
            
            header = """#!/usr/bin/env python3
#
# Cross Platform and Multi Architecture Advanced Binary Emulation Framework
#

"""
            with open(os.path.join(dir, f'{version}.py'), 'w') as f:
                f.write(header + f'{version} = ' + key)
    
    def output(self, dir):
        if os.path.exists(dir):
            shutil.rmtree(dir)

        os.mkdir(dir)

        self.print_code(dir)
        self.print_config(dir)
