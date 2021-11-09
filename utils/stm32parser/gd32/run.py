import configparser
import xml.etree.ElementTree as ET

tree = ET.parse('gd32vf103.xml')
root = tree.getroot()

for child in root:
    if child.tag == 'peripherals':
        perips = child
        break

config = {}
for perip in perips:
    if perip.tag == 'peripheral':
        info = {
            'type' : 'peripheral'
        }
        pname = ''
        classname = ''
        for attr in perip:            
            if attr.tag == 'name':
                pname = attr.text
                config[pname] = info  

            elif attr.tag == 'groupName':
                classname = f'GD32VF1xx{attr.text.capitalize()}'
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
                
        
with open('gd32vf103.ql', 'w') as f:
    new_config = configparser.ConfigParser()
    for key, val in config.items():
        new_config[key] = val

    new_config.write(f)
            