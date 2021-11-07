import string

class Struct:
    def __init__(self):        
        self.classname = ''
        self.aliasname = ''
        self.variables = []
        self.files = []

    def add_variable(self, item):
        self.variables.append(item)
        
        error_message = f'Invalid variable {item}'
        letters = string.ascii_letters + string.digits + '_'
        for c in item[1]: # varname
            assert c in letters, error_message

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Struct):
            return False

        if len(self.variables) != len(o.variables):
            return False
        
        for a, b in zip(self.variables, o.variables):
            if a[0] != b[0] or a[1] != b[1]:
                return False

        return True

class Peripheral:
    def __init__(self, peripname, classname, address):
        self.peripname = peripname
        self.classname = classname
        self.address = address
        self.struct = None

        self.keys = {
            'type': 'peripheral',
            'base': hex(address),
            'class': classname,
        }
