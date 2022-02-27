import os
import shutil

from pathlib import Path
from xml.etree import ElementTree

header = """#!/usr/bin/env python3
#
# Cross Platform and Multi Architecture Advanced Binary Emulation Framework
#

from enum import IntEnum


"""

def xml_get(node, name):
    return next(filter(lambda o: o.tag == name, node), None)

def parse_register_field(filename):
    mcuname = Path(os.path.basename(filename)).stem.lower()

    for peripheral in xml_get(ElementTree.parse(filename).getroot(), 'peripherals'):
        if peripheral.tag == 'peripheral':
            if xml_get(peripheral, 'groupName') is None:
                groupname = xml_get(peripheral, 'name').text.lower().rstrip('0123456789')
            else:
                groupname = xml_get(peripheral, 'groupName').text.lower()

            filename  = f'output/{mcuname}_{groupname}.py'
            if os.path.exists(filename):
                continue
            
            with open(filename, 'w') as f:
                f.write(header)

                for register in xml_get(peripheral, 'registers'):
                    regname = xml_get(register, 'name').text
                    if regname.startswith(groupname.upper() + '_'):
                        regname = regname[len(groupname) + 1 : ]

                    fields = xml_get(register, 'fields')

                    pool = []
                    maxname, maxvalue = 0, 0
                    for field in fields:
                        desc = getattr(xml_get(field, 'description'), 'text', '')

                        name = xml_get(field, 'name').text
                        offset = int(xml_get(field, 'bitOffset').text)
                        mask = hex((1 << int(xml_get(field, 'bitWidth').text)) - 1)

                        value = f'{mask} << {offset}'
                        
                        pool.append((name, value, desc))
                        maxname  = max(maxname, len(name))
                        maxvalue = max(maxvalue, len(value))                        

                    f.write(f'class {regname}(IntEnum):\n')
                    for name, value, desc in pool:
                        f.write(f'    {name}{" " * (maxname - len(name))} = {value}{" " * (maxvalue - len(value))}   # {desc}\n')
                    f.write('\n')

def parse_peripheral_struct(filename):
    mcuname = Path(os.path.basename(filename)).stem.lower()

    with open(f'output/{mcuname}.py', 'w') as f:
        f.write('import ctypes\n\n')

        visit = set()
        for peripheral in xml_get(ElementTree.parse(filename).getroot(), 'peripherals'):
            if peripheral.tag == 'peripheral':
                if xml_get(peripheral, 'groupName') is None:
                    groupname = xml_get(peripheral, 'name').text.lower().rstrip('0123456789')
                else:
                    groupname = xml_get(peripheral, 'groupName').text.lower()

                registers = []
                max_rname = 0
                max_rtype = 0
                for register in xml_get(peripheral, 'registers'):
                    rname = xml_get(register, 'name').text
                    rcomm = xml_get(register, 'description').text
                    rtype = size2type = {
                        '0x08': 'ctypes.c_uint8',
                        '0x10': 'ctypes.c_uint16',
                        '0x20': 'ctypes.c_uint32',
                        '8'   : 'ctypes.c_uint8',
                        '16'  : 'ctypes.c_uint16',
                        '32'  : 'ctypes.c_uint32',
                    }[xml_get(register, 'size').text]

                    registers.append((rname, rcomm, rtype))
                    max_rname = max(max_rname, len(rname))
                    max_rtype = max(max_rname, len(rtype))

                comment = getattr(xml_get(peripheral, 'description'), 'text', '')
                if groupname not in visit:
                    visit.add(groupname)
                    f.write(f'class {mcuname.upper()}{groupname.capitalize()}:\n')
                    f.write(f'    class Type(ctypes.Structure):\n')
                    f.write(f'        """ {comment} """  \n')
                    f.write(f'        _fields_ = [\n')
                    for rname, rcomm, rtype in registers:
                        f.write(f'            ("{rname}"{" " * (max_rname - len(rname))}, {rtype}),{" " * (max_rtype - len(rtype))} # {rcomm}\n')            
                    f.write(f'        ]\n\n')


def parse(filename):
    parse_register_field(filename)
    parse_peripheral_struct(filename)
                        
if __name__ == '__main__':
    if os.path.exists('output'):
        shutil.rmtree('output')
        os.mkdir('output')

    parse('config/SAM3X8E.svd')
    parse('config/MK64F12.svd')