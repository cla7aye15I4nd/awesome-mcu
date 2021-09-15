import re
import os
import sys
import logging
import configparser

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

parse_type = 'stm32f1'
c_header_path = '../../packages/STM32F1/Drivers/CMSIS/Device/ST/STM32F1xx/Include'

def readfile(filename):
    print(filename)
    with open(os.path.join(c_header_path, filename), 'rb') as f:
        text = f.read().replace(b'\x92', b'')

    return text.decode()

def get_all_available_files():
    parse_files = []
    for filename in os.listdir(c_header_path):
        if re.match(f'^{parse_type}[0-9]+[a-z]+[.]h$', filename):
            parse_files.append(filename)
        
    return parse_files

def format_struct(typename, fields):    
    ctype_map = {
        'uint32_t': 'ctypes.c_uint32',
        'uint16_t': 'ctypes.c_uint8',
        'uint8_t': 'ctypes.c_uint8',
    }

    code  = '\tclass Type(ctypes.Structure):\n'
    code += f'\t\t""" COMMENT \n'
    code += f'\t\t"""\n\n'
    code += '        _fields_ = [\n'

    newfields = []
    varname_maxlen = 0
    typename_maxlen = 0

    for typename, varname, comment in fields:
        if typename not in ctype_map:            
            logging.warning(f'Undefined type {typename}')
            typename = f'{typename}.Type'
        else:
            typename = ctype_map[typename]
        if '[' in varname:
            res = varname.split('[')
            varname = res[0]

            num = eval(res[1][:-1])
            if num > 1:
                typename = f'{typename} * {num}'

        varname = f"'{varname}'"
        comment.lstrip('/*!< ').rstrip('*/ ')
        if comment:
            comment = ' # ' + comment.lstrip('/*!< ').rstrip('*/ ')

        varname_maxlen = max(varname_maxlen, len(varname))
        typename_maxlen = max(typename_maxlen, len(typename))
        newfields.append((typename, varname, comment))

    for typename, varname, comment in newfields:
        code += f'\t\t\t({varname}{" " * (varname_maxlen - len(varname))}, {typename}),{" " * (typename_maxlen - len(typename))} {comment}\n'

    code += '\t\t]\n'

    logging.info(code)
    return (code, newfields)

def extract_peripheral_struct(filename):    
    logging.info('Extracting the peripheral struct')

    code = readfile(filename)
    state = False
    concat = False
    fields = []
    struct = {}

    for line in code.splitlines():
        line = line.strip()
        if concat:
            fields[-1][-1] += ' ' + line
            concat = False
            continue

        if state:
            if line == '{':
                continue
            
            elif line.endswith('Def;'):
                state = False
                typename = line.rstrip(';').lstrip('} ')
                struct[typename] = format_struct(typename, fields)

                logging.info(f'Find struct {typename}')
                fields = []

            else:
                if not line:
                    continue

                line = line.replace('__IO', '').strip()
                line = line.replace('const', '').strip()
                
                if '/*' in line:
                    typename, varname, comment = line.split(maxsplit=2)
                else:
                    typename, varname = line.split(maxsplit=1)
                    comment = ''

                fields.append([typename, varname[:-1], comment])
                if '/*' in line and '*/' not in line:
                    concat = True

        elif line == 'typedef struct':
            state = True

    return struct

def struct_equal(lhs, rhs):
    lhs, rhs = lhs[1], rhs[1]
    
    if len(lhs) != len(rhs):
        return False

    for i in range(len(lhs)):
        for j in range(2):
            if lhs[i][j] != rhs[i][j]:
                return False
        
    return True

def parse_all_peripheral(parse_files):
    perip = {}
    for filename in parse_files:
        info = {}

        logging.info(f'Parsing "{filename}"')
        structs = extract_peripheral_struct(filename)

        info[filename] = structs
        for typename, content in structs.items():
            if typename not in perip:
                perip[typename] = [{'filenames': [filename], 'struct': content}]
            else:
                for item in perip[typename]:
                    if struct_equal(content, item['struct']):
                        item['filenames'].append(filename)
                        break
                else:
                    perip[typename].append({'filenames': [filename], 'struct': content})

    return perip

def generate_python(perip):
    with open(os.path.join(parse_type, f'{parse_type}.py'), 'w') as f:
        f.write('import ctypes\n\n')

        for perip_name, perip_set in perip.items():
            logging.info(f'About {perip_name}')
            
            if perip_name.endswith('TypeDef'):
                perip_name = perip_name[:-7].strip('_')

            perip_name = perip_name.capitalize()
            version_number = 1

            for item in perip_set:
                filenames = item['filenames']
                code = item['struct'][0]

                if len(filenames) == 1:
                    item['type'] = f'STM32F4{filenames[0][7:9]}{perip_name}'                
                elif 'stm32f103xb.h' in filenames or len(perip_set) == 1:
                    item['type'] = f'STM32F4xx{perip_name}'                    
                else:
                    item['type'] = f'STM32F4xx{perip_name}V{version_number}'
                    version_number += 1

                f.write(f"class {item['type']}:\n")

                filename_list = ''
                for filename in filenames:
                    filename_list += f'\t\t{" " * 8}{filename}\n'
                filename_list = filename_list[:-1]

                code = code.replace('COMMENT', f"the structure is available in :\n{filename_list}")

                logging.info(f"{filenames}")
                logging.info(f"{code}")

                f.write(code + '\n')

def findtype(c_header_file, typedef, perip):
    for item in perip[typedef]:
        if c_header_file in item['filenames']:
            return item['type']

def parse_defines(c_header_file):
    logging.info(f'Get Defines {c_header_file}')
    code = readfile(c_header_file)
    defines = {}

    code = re.sub(r'[^a-rA-Zy-z][0-9A-F]+UL', lambda o: o.group(0)[:-2], code)    
    code = re.sub(r'[^a-rA-Zy-z][0-9A-F]+U' , lambda o: o.group(0)[:-1], code)
    code = re.sub(re.compile(r'/\*.*?\*/', re.S), "", code)

    for line in code.splitlines():
        if not line.startswith('#define'):
            continue
        
        res = line.split(maxsplit=2)
        if len(res) != 3:
            continue

        _, name, expr = res
        if '_BASE' in name or '_END' in name:
            for key in sorted(defines.keys(), key=lambda x:-len(x)):
                expr = expr.replace(key, str(defines[key]))
            defines[name] = eval(expr)

    irq = {}
    for line in code.splitlines():
        if '_IRQ' in line and '=' in line:
            name, number = line.split('=', maxsplit=1)
            
            name = name.strip()
            number = int(number.strip(' ,'))
            
            tag, mask = name.split('_', maxsplit=1)
            if tag not in irq:
                irq[tag] = {}

            irq[tag][mask.replace('IRQn', 'intn')] = number

    return defines, irq

def generate_config(c_header_file, perip):
    code = readfile(c_header_file)
    
    config = configparser.ConfigParser()
    base_address, irq = parse_defines(c_header_file)

    def align(size):
        return (size + 0x400 - 1) // 0x400 * 0x400
    config['FLASH'] = {
        'type' : 'memory',
        'size': hex(base_address['FLASH_BANK1_END'] - base_address['FLASH_BASE'] + 1), # write in comment
        'base': hex(base_address['FLASH_BASE']),        
    }

    # config['FLASH OTP'] = {
    #     'type' : 'memory',
    #     'size': hex(align(base_address['FLASH_OTP_END'] - base_address['FLASH_OTP_BASE'] + 1)), # write in comment
    #     'base': hex(base_address['FLASH_OTP_BASE']),        
    # }

    config['SRAM'] = {
        'type' : 'memory',
        'size': "0x20000", # write in comment
        'base': hex(base_address['SRAM_BASE']),
    }

    config['SYSTEM'] = {
        'type' : 'memory',
        'size': "0x7800", # write in comment
        'base': "0x1FFF0000",        
    }    

    config['SRAM BB'] = {
        'type': 'bitband',
        'size': '0x100000', # write in comment
        'base': hex(base_address['SRAM_BASE']),
        'alias': hex(base_address['SRAM_BB_BASE'])
    }

    config['PERIP'] = {
        'type' : 'mmio',
        'size': '0x100000', # write in comment
        'base': hex(base_address['PERIPH_BASE']),        
    }    

    config['PERIP BB'] = {
        'type': 'bitband',
        'size': '0x100000', # write in comment
        'base': hex(base_address['PERIPH_BASE']),
        'alias': hex(base_address['PERIPH_BB_BASE'])
    }

    config['PPB'] = {
        'type' : 'mmio',
        'size': '0x10000', # write in comment
        'base': "0xE0000000",        
    }

    config['SYSTICK'] = {
        'type' : 'core periperal',
        'base': '0xE000E010', # write in comment
        'class': "CortexM4SysTick",        
    }

    config['NVIC'] = {
        'type' : 'core periperal',
        'base': '0xE000E100', # write in comment
        'class': "CortexM4Nvic",        
    }

    config['SCB'] = {
        'type' : 'core periperal',
        'base': '0xE000ED00', # write in comment
        'class': "CortexM4Scb",        
    }
    
    for line in code.splitlines():
        line = line.strip()

        if not re.match('#define\s+[0-9A-Z]+.*_BASE\)', line):
            continue

        _, perip_tag, info = line.split(maxsplit=2)
        if perip_tag == 'FLASH': # flash alias
            continue

        if '_' in perip_tag:            
            continue

        typedef = info.split('*')[0].strip('( ')
        base = info.split(')')[1].strip()


        info = {
            'type': 'periperal',
            'base': hex(base_address[base]),
            'class': findtype(c_header_file, typedef, perip),            
        }

        if perip_tag in irq:
            info.update(irq[perip_tag])

        config[perip_tag] = info

    with open(os.path.join(parse_type, c_header_file[:-4] + '.ql'), 'w') as f:
        config.write(f)

if __name__ == '__main__':
    parse_files = get_all_available_files()
    perip = parse_all_peripheral(parse_files)

    generate_python(perip)                 
    
    for fn in parse_files:
        generate_config(fn, perip)