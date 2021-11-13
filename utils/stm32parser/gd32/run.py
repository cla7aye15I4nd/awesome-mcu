import configparser
from re import T
import xml.etree.ElementTree as ET

tree = ET.parse('gd32vf103.xml')
root = tree.getroot()

for child in root:
    if child.tag == 'peripherals':
        perips = child
        break

config = {}
peripherals = set()
for perip in perips:
    if perip.tag == 'peripheral':
        info = {
            'type' : 'peripheral'
        }

        pname = ''
        oname = ''
        pcomment = ''
        classname = ''
        filename  = ''
        const_file = ''
        item_list = []
        node = {}

        derive = perip.attrib.get('derivedFrom', None)
        if derive:
            info['class'] = config[derive]['class']
            
        for attr in perip:      

            if attr.tag == 'name':
                pname = attr.text
                config[pname] = info  

            if attr.tag == 'description':
                pcomment = attr.text

            elif attr.tag == 'groupName':
                oname = attr.text.lower()
                classname = f'GD32VF1xx{attr.text.capitalize()}'
                filename  = f'gd32vf1xx_{attr.text.lower()}.py'
                const_file = f'gd32vf1xx_{attr.text.lower()}_const.py'
                info['class'] = classname 

            elif attr.tag == 'baseAddress':
                if attr.text.startswith('0xD'):
                    info['type'] = 'core peripheral'

                info['base'] = attr.text.lower()
            
            elif attr.tag == 'interrupt':
                name, value = '', 0
                for irq in attr:
                    if irq.tag == 'name':
                        name = irq.text
                    if irq.tag == 'value':
                        value = irq.text
                
                if name in ['ADC0_1', pname]:
                    info['intn'] = value 
                
                elif pname.startswith('DMA'):
                    name = name[len(pname) + 1:].replace('Channel', 'stream')
                    info[f'{name}_intn'] = value

                elif name.startswith(pname + '_'):
                    name = name[len(pname) + 1:]
                    info[f'{name.lower()}_intn'] = value
                
            elif attr.tag == 'registers':
                for reg in attr:                    
                    if reg.tag == 'register':
                        typename, varname, comment, reset = '', '', '', 0
                        for regattr in reg:
                            if regattr.tag == 'name':
                                varname = regattr.text
                            
                            elif regattr.tag == 'description':
                                comment = ' '.join(regattr.text.strip().split())

                            elif regattr.tag == 'resetValue':
                                reset = int(regattr.text, 16)

                            elif regattr.tag == 'addressOffset':
                                comment = f' Address offset: {regattr.text}, ' + comment

                            elif regattr.tag == 'size':
                                typename = {
                                    '0x08': 'ctypes.c_uint8',
                                    '0x10': 'ctypes.c_uint16',
                                    '0x20': 'ctypes.c_uint32',
                                }[regattr.text]

                            elif regattr.tag == 'fields':
                                node[varname] = regattr

                        item_list.append((typename, varname, comment, reset))

        if filename in ['', 'gd32vf1xx_uart.py'] or filename in peripherals:
            continue

        peripherals.add(filename)
        with open(filename, 'w') as f:
            f.write('import ctypes\n\n\n')
            f.write(f'class {classname}:\n')
            f.write(f'    class Type(ctypes.Structure):\n')
            f.write(f'        """ {pcomment} \n')
            f.write(f'        """\n\n')
            f.write(f'        _fields_ = [\n')

            varname_maxlen = 0
            typename_maxlen = 0
            for typename, varname, _, _ in item_list:
                varname_maxlen = max(varname_maxlen, len(varname))
                typename_maxlen = max(typename_maxlen, len(typename))

            for typename, varname, comment, _ in item_list:
                f.write(f'            ("{varname}"{" " * (varname_maxlen - len(varname))}, {typename}),{" " * (typename_maxlen - len(typename))} #{comment}\n')            

            f.write(f'        ]\n\n')

            f.write(f'    def __init__(self, ql, label):\n')
            f.write(f'        super().__init__(ql, label)\n\n')
            
            f.write(f'        self.{oname} = self.struct(\n')
            for _, varname, _, reset in item_list:
                f.write(f'            {varname}{" " * (varname_maxlen - len(varname))} = {reset: #011x},\n')
            f.write(f'        )\n')

            f.write('\n')

        with open('const/'+const_file, 'w') as f:
            f.write('from enum import IntEnum\n\n\n')
            for key, val in node.items():
                f.write(f'class {key}(IntEnum):\n')
                maxlen = 0
                maxlen2 = 0
                fields = []
                for field in val:
                    name = ''
                    comment = ''
                    offset = 0
                    mask = 0
                    
                    for attr in field:
                        if attr.tag == 'name':
                            name = attr.text
                            maxlen = max(maxlen, len(name))

                        elif attr.tag == 'description':
                            comment = ' '.join(attr.text.split())

                        elif attr.tag == 'bitOffset':
                            offset = int(attr.text)

                        elif attr.tag == 'bitWidth':
                            mask = hex((1 << int(attr.text)) - 1)
                    
                    value = f'{mask} << {offset}'
                    fields.append((name, comment, value))
                    maxlen2 = max(maxlen2, len(value))

                for name, comment, value in  fields:
                    f.write(f'    {name}{" " * (maxlen - len(name))} = {value}{" " * (maxlen2 - len(value))}   # {comment}\n')

                f.write('\n')

with open('gd32vf103.ql', 'w') as f:
    new_config = configparser.ConfigParser()
    for key, val in config.items():
        new_config[key] = val

    new_config.write(f)
