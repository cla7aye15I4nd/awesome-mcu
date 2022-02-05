#!/usr/bin/env python3
#
# Cross Platform and Multi Architecture Advanced Binary Emulation Framework
#

stm32f101 = {
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
        "class": "STM32F1xxSpi",
        "kwargs": {
            "intn": 0x24
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
        "class": "STM32F1xxBkp"
    },
    "PWR": {
        "type": "peripheral",
        "base": 0x40007000,
        "class": "STM32F1xxPwr"
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
    "ADC1": {
        "type": "peripheral",
        "base": 0x40012400,
        "class": "STM32F1xxAdc",
        "kwargs": {
            "intn": 0x12
        }
    },
    "SPI1": {
        "type": "peripheral",
        "base": 0x40013000,
        "class": "STM32F1xxSpi",
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
    "DMA1": {
        "type": "peripheral",
        "base": 0x40020000,
        "class": "STM32F1xxDma"
    },
    "RCC": {
        "type": "peripheral",
        "base": 0x40021000,
        "class": "STM32F1xxRcc",
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
    "DBGMCU": {
        "type": "peripheral",
        "base": 0xe0042000,
        "class": "STM32F1xxDbgmcu"
    }
}