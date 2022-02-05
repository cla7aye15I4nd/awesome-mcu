#!/usr/bin/env python3
#
# Cross Platform and Multi Architecture Advanced Binary Emulation Framework
#

stm32f100xe = {
    "TIM2": {
        "type": "peripheral",
        "base": 0x40000000,
        "class": "STM32F1xxTim",
        "kwargs": {
            "intn": 0x1c
        }
    },
    "TIM3": {
        "type": "peripheral",
        "base": 0x40000400,
        "class": "STM32F1xxTim",
        "kwargs": {
            "intn": 0x1d
        }
    },
    "TIM4": {
        "type": "peripheral",
        "base": 0x40000800,
        "class": "STM32F1xxTim",
        "kwargs": {
            "intn": 0x1e
        }
    },
    "TIM5": {
        "type": "peripheral",
        "base": 0x40000c00,
        "class": "STM32F1xxTim",
        "kwargs": {
            "intn": 0x32
        }
    },
    "TIM6": {
        "type": "peripheral",
        "base": 0x40001000,
        "class": "STM32F1xxTim",
        "kwargs": {
            "dac_intn": 0x36,
            "intn": 0x36
        }
    },
    "TIM7": {
        "type": "peripheral",
        "base": 0x40001400,
        "class": "STM32F1xxTim",
        "kwargs": {
            "intn": 0x37
        }
    },
    "TIM12": {
        "type": "peripheral",
        "base": 0x40001800,
        "class": "STM32F1xxTim",
        "kwargs": {
            "intn": 0x2b
        }
    },
    "TIM13": {
        "type": "peripheral",
        "base": 0x40001c00,
        "class": "STM32F1xxTim",
        "kwargs": {
            "intn": 0x2c
        }
    },
    "TIM14": {
        "type": "peripheral",
        "base": 0x40002000,
        "class": "STM32F1xxTim",
        "kwargs": {
            "intn": 0x2d
        }
    },
    "RTC": {
        "type": "peripheral",
        "base": 0x40002800,
        "class": "STM32F1xxRtc",
        "kwargs": {
            "intn": 0x3,
            "alarm_intn": 0x29
        }
    },
    "WWDG": {
        "type": "peripheral",
        "base": 0x40002c00,
        "class": "STM32F1xxWwdg",
        "kwargs": {
            "intn": 0x0
        }
    },
    "IWDG": {
        "type": "peripheral",
        "base": 0x40003000,
        "class": "STM32F1xxIwdg"
    },
    "SPI2": {
        "type": "peripheral",
        "base": 0x40003800,
        "class": "STM32F1xxSpiV1",
        "kwargs": {
            "intn": 0x24
        }
    },
    "SPI3": {
        "type": "peripheral",
        "base": 0x40003c00,
        "class": "STM32F1xxSpiV1",
        "kwargs": {
            "intn": 0x33
        }
    },
    "USART2": {
        "type": "peripheral",
        "base": 0x40004400,
        "class": "STM32F1xxUsart",
        "kwargs": {
            "intn": 0x26
        }
    },
    "USART3": {
        "type": "peripheral",
        "base": 0x40004800,
        "class": "STM32F1xxUsart",
        "kwargs": {
            "intn": 0x27
        }
    },
    "UART4": {
        "type": "peripheral",
        "base": 0x40004c00,
        "class": "STM32F1xxUsart",
        "kwargs": {
            "intn": 0x34
        }
    },
    "UART5": {
        "type": "peripheral",
        "base": 0x40005000,
        "class": "STM32F1xxUsart",
        "kwargs": {
            "intn": 0x35
        }
    },
    "I2C1": {
        "type": "peripheral",
        "base": 0x40005400,
        "class": "STM32F1xxI2c",
        "kwargs": {
            "ev_intn": 0x1f,
            "er_intn": 0x20
        }
    },
    "I2C2": {
        "type": "peripheral",
        "base": 0x40005800,
        "class": "STM32F1xxI2c",
        "kwargs": {
            "ev_intn": 0x21,
            "er_intn": 0x22
        }
    },
    "BKP": {
        "type": "peripheral",
        "base": 0x40006c00,
        "class": "STM32F1xxBkpV1"
    },
    "PWR": {
        "type": "peripheral",
        "base": 0x40007000,
        "class": "STM32F1xxPwr"
    },
    "DAC1": {
        "type": "peripheral",
        "base": 0x40007400,
        "class": "STM32F1xxDacV1"
    },
    "CEC": {
        "type": "peripheral",
        "base": 0x40007800,
        "class": "STM32F1xxCec",
        "kwargs": {
            "intn": 0x2a
        }
    },
    "AFIO": {
        "type": "peripheral",
        "base": 0x40010000,
        "class": "STM32F1xxAfio"
    },
    "EXTI": {
        "type": "peripheral",
        "base": 0x40010400,
        "class": "STM32F1xxExti"
    },
    "GPIOA": {
        "type": "peripheral",
        "base": 0x40010800,
        "class": "STM32F1xxGpio"
    },
    "GPIOB": {
        "type": "peripheral",
        "base": 0x40010c00,
        "class": "STM32F1xxGpio"
    },
    "GPIOC": {
        "type": "peripheral",
        "base": 0x40011000,
        "class": "STM32F1xxGpio"
    },
    "GPIOD": {
        "type": "peripheral",
        "base": 0x40011400,
        "class": "STM32F1xxGpio"
    },
    "GPIOE": {
        "type": "peripheral",
        "base": 0x40011800,
        "class": "STM32F1xxGpio"
    },
    "GPIOF": {
        "type": "peripheral",
        "base": 0x40011c00,
        "class": "STM32F1xxGpio"
    },
    "GPIOG": {
        "type": "peripheral",
        "base": 0x40012000,
        "class": "STM32F1xxGpio"
    },
    "ADC1": {
        "type": "peripheral",
        "base": 0x40012400,
        "class": "STM32F1xxAdc",
        "kwargs": {
            "intn": 0x12
        }
    },
    "TIM1": {
        "type": "peripheral",
        "base": 0x40012c00,
        "class": "STM32F1xxTim",
        "kwargs": {
            "brk_tim15_intn": 0x18,
            "up_tim16_intn": 0x19,
            "trg_com_tim17_intn": 0x1a,
            "cc_intn": 0x1b,
            "brk_intn": 0x18,
            "brk_tim9_intn": 0x18,
            "trg_com_tim11_intn": 0x1a,
            "trg_com_intn": 0x1a,
            "up_tim10_intn": 0x19,
            "up_intn": 0x19
        }
    },
    "SPI1": {
        "type": "peripheral",
        "base": 0x40013000,
        "class": "STM32F1xxSpiV1",
        "kwargs": {
            "intn": 0x23
        }
    },
    "USART1": {
        "type": "peripheral",
        "base": 0x40013800,
        "class": "STM32F1xxUsart",
        "kwargs": {
            "intn": 0x25
        }
    },
    "TIM15": {
        "type": "peripheral",
        "base": 0x40014000,
        "class": "STM32F1xxTim"
    },
    "TIM16": {
        "type": "peripheral",
        "base": 0x40014400,
        "class": "STM32F1xxTim"
    },
    "TIM17": {
        "type": "peripheral",
        "base": 0x40014800,
        "class": "STM32F1xxTim"
    },
    "DMA1": {
        "type": "peripheral",
        "base": 0x40020000,
        "class": "STM32F1xxDma"
    },
    "DMA2": {
        "type": "peripheral",
        "base": 0x40020400,
        "class": "STM32F1xxDma"
    },
    "RCC": {
        "type": "peripheral",
        "base": 0x40021000,
        "class": "STM32F1xxRccV1",
        "kwargs": {
            "intn": 0x5
        }
    },
    "FLASH": {
        "type": "peripheral",
        "base": 0x40022000,
        "class": "STM32F1xxFlash",
        "kwargs": {
            "intn": 0x4
        }
    },
    "CRC": {
        "type": "peripheral",
        "base": 0x40023000,
        "class": "STM32F1xxCrc"
    },
    "FSMC_Bank1": {
        "type": "peripheral",
        "base": 0xa0000000,
        "class": "STM32F1xxFsmc_bank1"
    },
    "FSMC_Bank1E": {
        "type": "peripheral",
        "base": 0xa0000104,
        "class": "STM32F1xxFsmc_bank1e"
    },
    "DBGMCU": {
        "type": "peripheral",
        "base": 0xe0042000,
        "class": "STM32F1xxDbgmcu"
    }
}