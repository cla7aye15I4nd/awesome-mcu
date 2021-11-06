from stm32parser.struct import Peripheral


class Board:
    def __init__(self, version, content):
        self.version = version
        self.content = content
        
        self.structs = []
        self.context = {}
        self.used = set()

        self.peripheral = {}
        self.validset = set()

        self.lines = []
        for line in content.splitlines():
            if len(self.lines) > 0 and self.lines[-1].endswith('\\'):
                self.lines[-1] = self.lines[-1][:-1] + line
            else:
                self.lines.append(line)

    def add_struct(self, perip):
        self.structs.append(perip)

    def add_peripheral(self, peripname, classname, address):
        perip = Peripheral(peripname, classname, address)
        self.peripheral[peripname] = perip
        for struct in self.structs:
            if classname == struct.classname: 
                perip.struct = struct               
                break
        else:
            print(f'Error classtype: {classname}')
            return

    def find_key(self):
        for perip in sorted(self.peripheral.values(), key=lambda x: -len(x.peripname)):
            name = perip.peripname

            print(f'Peripheral {name}:')
            for key, val in self.context.items():
                if key in self.used:
                    continue

                if key.startswith(name + '_'):
                    self.used.add(key)
                    key = key[len(name)+1:]                    

