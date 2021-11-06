from stm32parser.parser import STM32Parser


class STM32F4HalParser(STM32Parser):
    def __init__(self, path):
        super().__init__(path, 'stm32f4')

    def run(self):
        pass