import os

from stm32parser.stm32f1hal import STM32F1HalParser

if __name__ == '__main__':
    path = '../../packages/STM32F1/Drivers/CMSIS/Device/ST/STM32F1xx/Include'

    parser = STM32F1HalParser(path)
    parser.output(os.path.join(os.path.curdir, 'stm32f1hal'))