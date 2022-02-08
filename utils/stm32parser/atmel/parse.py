import os
import re
import json

config = {}

with open('input.txt') as f:
    for line in f.read().splitlines():
        
        if line.startswith('#define'):
            _, name, info = line.split('/*')[0].split(maxsplit=2)
            
            struct, address = info.strip('() ').rstrip('U').split('*)')

            struct = f'SAM3xa{struct.strip()}'
            address = int(address, 16)

            config[name] = {
                "base": address,
                "struct": struct,
                "type": "peripheral",
            }

        elif 'IRQn' in line:
            name, intn = line.split(',')[0].split('=')
            name = name.strip().split('_')[0]
            intn = int(intn)

            if name in config:
                config[name]["kwargs"] = {"intn": intn}
            else:
                print('Not found ' + name)

    text = re.sub(' (\d+)', lambda i: ' ' + hex(int(i.group(0))), json.dumps(config, indent=4))
    with open('sam3x8e_config.py', 'w') as f:
        f.write(text)

path = '/home/moe/.arduino15/packages/arduino/hardware/sam/1.6.12/system/CMSIS/Device/ATMEL/sam3xa/include/component/'

with open('sam3x8e_struct.py', 'w') as f:
    f.write("import ctypes\n\n")

    for filename in os.listdir(path):
        with open(os.path.join(path, filename)) as fr:
            text = fr.read()

            name = filename.split('.')[0].split('_')[1].capitalize()
            struct = f'SAM3xa{name}'
            
            print(struct)
            
            i = 0
            lines = text.splitlines()
            while i < len(lines):
                line = lines[i]
                if line == 'typedef struct {':
                    i += 1
                    item_list = []
                    while True:
                        line = lines[i]
                        if line[0] == '}':
                            break
                        
                        define, comment = line.split(';')
                        typename, varname = define.split()

                        comment = comment.strip('/* ')
                        if comment.startswith('< \\brief '):
                            comment = comment[9:]

                        mapper = {
                            'WoReg': 'ctypes.c_uint32',
                            'RwReg': 'ctypes.c_uint32',
                            'RoReg': 'ctypes.c_uint32',
                        }

                        typename = mapper.get(typename, typename)
                        if varname.endswith(']'):
                            varname, num = varname.rstrip(']').split('[')

                            if num != '1':
                                typename = f'{typename} * {num}'

                        if varname.startswith(name.upper() + '_'):
                            varname = varname[len(name) + 1:]

                        item_list.append((typename, varname, comment))
                        
                        i += 1

                    sname = line.lstrip('} ').rstrip('; ')
                    if sname == name:
                        f.write(f"class {struct}:\n")
                        f.write(f"    class Type(ctypes.Structure):\n")
                        f.write(f"        _fields_ = [\n")
                        varname_maxlen = 0
                        typename_maxlen = 0
                        for typename, varname, _ in item_list:
                            varname_maxlen = max(varname_maxlen, len(varname))
                            typename_maxlen = max(typename_maxlen, len(typename))

                        for typename, varname, comment in item_list:
                            f.write(f'            ("{varname}"{" " * (varname_maxlen - len(varname))}, {typename}),{" " * (typename_maxlen - len(typename))} # {comment}\n')
                        f.write(f"        ]\n\n")

                        
                
                i += 1

        

