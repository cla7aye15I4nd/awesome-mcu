import os
import re
import json


def parse_bes(path, model):
    title = model.replace('best', 'bes')
    print(f'Parsing {title}')

    config = {}
    peripheral = {}
    layout = ''

    specpath = os.path.join(path, model)
    with open(f'{title}.py', 'w') as f:
        f.write('import ctypes\n\n')

        for filename in os.listdir(path):
            if filename.startswith('reg_'):
                parse_peripheral(path, filename, f, title, peripheral)

        for filename in os.listdir(specpath):
            if filename.startswith('reg_'):
                parse_peripheral(specpath, filename, f, title, peripheral)
            
            elif filename.startswith('plat'):
                print(f'memory layout => {filename}')
                layout = filename
        
        print(peripheral)
        parse_layout(os.path.join(specpath, layout), config, peripheral)

        output = re.sub(' (\d+)', lambda i: hex(int(i.group(0))), json.dumps(config, indent=4))
        f.write(f'{title} = {output}')

def parse_peripheral(path, filename, f, title, peripheral):
    type_mapper = {
        'uint8_t' : 'ctypes.c_uint8',
        'uint16_t': 'ctypes.c_uint16',
        'uint32_t': 'ctypes.c_uint32',
    }

    perip = filename.split('.')[0].split('_')[1]

    if perip.endswith('ip'):
        perip = perip[:-2]
    print(f'{perip} => {filename}')

    with open(os.path.join(path, filename)) as fn:
        lines = fn.read().splitlines()

    items = []
    parsing = False

    try:
        for line in lines:
            if line.startswith('struct'):
                parsing = True

            elif line.startswith('{') and parsing:
                continue

            elif line.startswith('};') and parsing:
                break

            elif parsing:
                if '//' in line:
                    variable, comment = line.split('//')
                else:
                    variable, comment = line, ''

                atoms = variable.split()

                if atoms[0].startswith('_'):
                    atoms.pop(0)
                
                vtype = type_mapper[atoms[0]]
                vname = atoms[1].strip(';')

                if '[' in vname:
                    vname, number = vname.strip(']').split('[')
                    vtype = f'{vtype} * {number}'
                
                items.append((vtype, vname, comment))

    except:
        print('ERROR')

    struct = f'{title.upper()}{perip.capitalize()}'
    peripheral[perip.upper()] = struct

    if items:
        maxname = max(len(name) for _, name, _ in items)
        maxtype = max(len(name) for name, _, _ in items)

        f.write(f'class {struct}:\n')
        f.write(f'    class Type(ctypes.Structure):\n')
        f.write('        _fields_ = [\n')

        for vtype, vname, comm in items:
            f.write(f'            ("{vname}"{" " * (maxname - len(vname))}, {vtype}),{" " * (maxtype - len(vtype))} # {comm}\n')

        f.write('        ]\n')
        f.write('\n')

def parse_layout(path, config, peripheral):
    with open(path) as f:
        lines = f.read().splitlines()

    context = {}
    for line in lines:
        if line.startswith('#define') and len(line.split()) > 2:
            _, name, expr = line.split()
            context[name] = eval(expr, context)

    for key, val in context.items():
        if key.endswith('_BASE'):
            for pkey, pval in peripheral.items():
                if key.startswith(pkey):
                    config[key[:-5]] = {
                        'struct': pval,
                        'base': val,
                        'type': 'peripheral'
                    }
                    break
            else:
                size = key.replace('BASE', 'SIZE')
                if size in context:
                    name = key[:-5]
                    if name != 'RAMRET':
                        config[name] = {
                            'base': val,
                            'size': context[size],
                            'type': 'memory'
                        }
                else:
                    print(key)
