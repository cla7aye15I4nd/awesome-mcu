import os

from stm32parser.stm32f4hal import STM32F4HalParser

if __name__ == '__main__':
    path = '../../packages/STM32F4/Drivers/CMSIS/Device/ST/STM32F4xx/Include'

    parser = STM32F4HalParser(path)
