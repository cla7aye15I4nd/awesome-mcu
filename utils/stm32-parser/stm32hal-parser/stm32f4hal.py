class STM32F4HalParser:
    def __init__(self, path):
        self.path = path


if __name__ == '__main__':
    parser = STM32F4HalParser()
    parser.run()
