import string

class Struct:
    def __init__(self):        
        self.classname = ''
        self.variables = []

    def add_variable(self, item):
        self.variables.append(item)
        
        error_message = f'Invalid variable {item}'
        letters = string.ascii_letters + string.digits + '_'
        for c in item[1]: # varname
            assert c in letters, error_message

class Peripheral:
    def __init__(self, peripname, classname, address):
        self.peripname = peripname
        self.classname = classname
        self.address = address

        self.keys = {
            'base': hex(address),
            'class': classname,
        }
