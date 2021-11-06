[FLASH]
type = memory
size = 0x20000
base = 0x8000000

[SRAM]
type = memory
size = 0x20000
base = 0x20000000

[SYSTEM]
type = memory
size = 0x7800
base = 0x1FFF0000

[SRAM BB]
type = bitband
size = 0x100000
base = 0x20000000
alias = 0x22000000

[PERIP]
type = mmio
size = 0x100000
base = 0x40000000

[PERIP BB]
type = bitband
size = 0x100000
base = 0x40000000
alias = 0x42000000

[PPB]
type = mmio
size = 0x10000
base = 0xE0000000

[SYSTICK]
type = core periperal
base = 0xE000E010
class = CortexM4SysTick

[NVIC]
type = core periperal
base = 0xE000E100
class = CortexM4Nvic

[SCB]
type = core periperal
base = 0xE000ED00
class = CortexM4Scb

[TIM2]
type = periperal
base = 0x40000000
class = STM32F4xxTim
intn = 28

[TIM3]
type = periperal
base = 0x40000400
class = STM32F4xxTim
intn = 29

[TIM4]
type = periperal
base = 0x40000800
class = STM32F4xxTim
intn = 30

[TIM6]
type = periperal
base = 0x40001000
class = STM32F4xxTim
dac_intn = 54

[TIM7]
type = periperal
base = 0x40001400
class = STM32F4xxTim
intn = 55

[RTC]
type = periperal
base = 0x40002800
class = STM32F4xxRtc
intn = 3
alarm_intn = 41

[WWDG]
type = periperal
base = 0x40002c00
class = STM32F4xxWwdg
intn = 0

[IWDG]
type = periperal
base = 0x40003000
class = STM32F4xxIwdg

[SPI2]
type = periperal
base = 0x40003800
class = STM32F4xxSpiV2
intn = 36

[USART2]
type = periperal
base = 0x40004400
class = STM32F4xxUsart
intn = 38

[USART3]
type = periperal
base = 0x40004800
class = STM32F4xxUsart
intn = 39

[I2C1]
type = periperal
base = 0x40005400
class = STM32F4xxI2c
ev_intn = 31
er_intn = 32

[I2C2]
type = periperal
base = 0x40005800
class = STM32F4xxI2c
ev_intn = 33
er_intn = 34

[BKP]
type = periperal
base = 0x40006c00
class = STM32F4xxBkp

[PWR]
type = periperal
base = 0x40007000
class = STM32F4xxPwr

[DAC1]
type = periperal
base = 0x40007400
class = STM32F4xxDacV2

[DAC]
type = periperal
base = 0x40007400
class = STM32F4xxDacV2

[CEC]
type = periperal
base = 0x40007800
class = STM32F4xxCec
intn = 42

[AFIO]
type = periperal
base = 0x40010000
class = STM32F4xxAfio

[EXTI]
type = periperal
base = 0x40010400
class = STM32F4xxExti

[GPIOA]
type = periperal
base = 0x40010800
class = STM32F4xxGpio

[GPIOB]
type = periperal
base = 0x40010c00
class = STM32F4xxGpio

[GPIOC]
type = periperal
base = 0x40011000
class = STM32F4xxGpio

[GPIOD]
type = periperal
base = 0x40011400
class = STM32F4xxGpio

[GPIOE]
type = periperal
base = 0x40011800
class = STM32F4xxGpio

[ADC1]
type = periperal
base = 0x40012400
class = STM32F4xxAdc
intn = 18

[TIM1]
type = periperal
base = 0x40012c00
class = STM32F4xxTim
brk_tim15_intn = 24
up_tim16_intn = 25
trg_com_tim17_intn = 26
cc_intn = 27

[SPI1]
type = periperal
base = 0x40013000
class = STM32F4xxSpiV2
intn = 35

[USART1]
type = periperal
base = 0x40013800
class = STM32F4xxUsart
intn = 37

[TIM15]
type = periperal
base = 0x40014000
class = STM32F4xxTim

[TIM16]
type = periperal
base = 0x40014400
class = STM32F4xxTim

[TIM17]
type = periperal
base = 0x40014800
class = STM32F4xxTim

[DMA1]
type = periperal
base = 0x40020000
class = STM32F4xxDma
channel1_intn = 11
channel2_intn = 12
channel3_intn = 13
channel4_intn = 14
channel5_intn = 15
channel6_intn = 16
channel7_intn = 17

[RCC]
type = periperal
base = 0x40021000
class = STM32F4xxRccV2
intn = 5

[CRC]
type = periperal
base = 0x40023000
class = STM32F4xxCrc

[OB]
type = periperal
base = 0x1ffff800
class = STM32F4xxOb

[DBGMCU]
type = periperal
base = 0xe0042000
class = STM32F4xxDbgmcu

