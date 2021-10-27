import re

path = '../../packages/STM32F4/Drivers/CMSIS/Device/ST/STM32F4xx/Include/stm32f411xe.h'

with open(path) as f:
    code = f.read()

def get(tag):
    prefix = '#define ' + tag + '_'
    defines = {}
    cr = []
    maxlen = 0

    for line in code.splitlines():
        if line.startswith(prefix):
            if '/*' in line:
                line = line.split('/*')[0].strip()        

            line = re.sub(r'[^a-rA-Zy-z][0-9A-F]+UL', lambda o: o.group(0)[:-2], line)    
            line = re.sub(r'[^a-rA-Zy-z][0-9A-F]+U' , lambda o: o.group(0)[:-1], line)

            _, name, expr = line.split(maxsplit=2)

            if name.endswith('_Pos'):
                defines[name] = eval(expr)
            elif name.endswith('_Msk'):
                for k, v in defines.items():
                    expr = expr.replace(k, str(v))
                name = name[len(prefix) - 8: -4]
                expr = expr.lstrip('(').rstrip(')')
                expr = expr.replace('0x1 ', '1 ').lower()

                cr.append((name, expr))
                maxlen = max(maxlen, len(name))

    print(f'class {tag}(IntEnum):')
    for k, v in cr:
        print(f'\t{k}{" " * (maxlen - len(k))} = {v}')
    print()

def getall(tag):
    prefix = '#define ' + tag + '_'
    names = set()
    for line in code.splitlines():
        if line.startswith(prefix):
            if '/*' in line:
                line = line.split('/*')[0].strip()        

            line = re.sub(r'[^a-rA-Zy-z][0-9A-F]+UL', lambda o: o.group(0)[:-2], line)    
            line = re.sub(r'[^a-rA-Zy-z][0-9A-F]+U' , lambda o: o.group(0)[:-1], line)

            try:            
                _, name, expr = line.split(maxsplit=2)
                
                name = '_'.join(name.split('_')[:2])
                if name not in names:
                    get(name)

                names.add(name)
            except:
                pass    

print('from enum import IntEnum\n\n')
getall('DMA')
