import os
import shutil
import configparser


from stm32parser.parser import STM32Parser


class STM32F4HalParser(STM32Parser):
    def __init__(self, path):
        super().__init__(path, 'stm32f4')

    def output(self, dir):
        if os.path.exists(dir):
            shutil.rmtree(dir)

        os.mkdir(dir)

        fmap = {}
        for board in self.boards:
            config = configparser.ConfigParser()            

            for name in sorted(board.peripheral.keys()):
                perip = board.peripheral[name]
                config[perip.peripname] = perip.keys

            with open('/tmp/tmp.ql', 'w') as f:
                config.write(f)
            with open('/tmp/tmp.ql', 'r') as f:
                configstring = f.read()

            if configstring not in fmap:
                fmap[configstring] = []
                        
            fmap[configstring].append(board.version)

        # 
        used = set()
        for k in sorted(fmap.keys(), key=lambda x: -len(fmap[x])):
            li = fmap[k]
            fi = li[0]
            version = fi[:-2] if fi[:-2] not in used else fi
            used.add(version)

            print(li)
            path = os.path.join(dir, f'{version}.ql')
            with open(path, 'w') as f:
                f.write(k)