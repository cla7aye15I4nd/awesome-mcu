[ADC1]
type = peripheral
base = 0x40012000
class = STM32F4xxAdc

[ADC1_COMMON]
type = peripheral
base = 0x40012300
class = STM32F4xxAdc_common

[CRC]
type = peripheral
base = 0x40023000
class = STM32F4xxCrc

[DAC]
type = peripheral
base = 0x40007400
class = STM32F4xxDac

[DAC1]
type = peripheral
base = 0x40007400
class = STM32F4xxDac

[DBGMCU]
type = peripheral
base = 0xe0042000
class = STM32F4xxDbgmcu

[DMA1]
type = peripheral
base = 0x40026000
class = STM32F4xxDma

[DMA1_Stream0]
type = peripheral
base = 0x40026010
class = STM32F4xxDma_stream
intn = 11

[DMA1_Stream1]
type = peripheral
base = 0x40026028
class = STM32F4xxDma_stream
intn = 12

[DMA1_Stream2]
type = peripheral
base = 0x40026040
class = STM32F4xxDma_stream
intn = 13

[DMA1_Stream3]
type = peripheral
base = 0x40026058
class = STM32F4xxDma_stream
intn = 14

[DMA1_Stream4]
type = peripheral
base = 0x40026070
class = STM32F4xxDma_stream
intn = 15

[DMA1_Stream5]
type = peripheral
base = 0x40026088
class = STM32F4xxDma_stream
intn = 16

[DMA1_Stream6]
type = peripheral
base = 0x400260a0
class = STM32F4xxDma_stream
intn = 17

[DMA1_Stream7]
type = peripheral
base = 0x400260b8
class = STM32F4xxDma_stream
intn = 47

[DMA2]
type = peripheral
base = 0x40026400
class = STM32F4xxDma

[DMA2_Stream0]
type = peripheral
base = 0x40026410
class = STM32F4xxDma_stream
intn = 56

[DMA2_Stream1]
type = peripheral
base = 0x40026428
class = STM32F4xxDma_stream
intn = 57

[DMA2_Stream2]
type = peripheral
base = 0x40026440
class = STM32F4xxDma_stream
intn = 58

[DMA2_Stream3]
type = peripheral
base = 0x40026458
class = STM32F4xxDma_stream
intn = 59

[DMA2_Stream4]
type = peripheral
base = 0x40026470
class = STM32F4xxDma_stream
intn = 60

[DMA2_Stream5]
type = peripheral
base = 0x40026488
class = STM32F4xxDma_stream
intn = 68

[DMA2_Stream6]
type = peripheral
base = 0x400264a0
class = STM32F4xxDma_stream
intn = 69

[DMA2_Stream7]
type = peripheral
base = 0x400264b8
class = STM32F4xxDma_stream
intn = 70

[EXTI]
type = peripheral
base = 0x40013c00
class = STM32F4xxExti

[FLASH]
type = peripheral
base = 0x40023c00
class = STM32F4xxFlash
intn = 4

[FMPI2C1]
type = peripheral
base = 0x40006000
class = STM32F4xxFmpi2c
ev_intn = 95
er_intn = 96

[GPIOA]
type = peripheral
base = 0x40020000
class = STM32F4xxGpio

[GPIOB]
type = peripheral
base = 0x40020400
class = STM32F4xxGpio

[GPIOC]
type = peripheral
base = 0x40020800
class = STM32F4xxGpio

[GPIOH]
type = peripheral
base = 0x40021c00
class = STM32F4xxGpio

[I2C1]
type = peripheral
base = 0x40005400
class = STM32F4xxI2c
ev_intn = 31
er_intn = 32

[I2C2]
type = peripheral
base = 0x40005800
class = STM32F4xxI2c
ev_intn = 33
er_intn = 34

[IWDG]
type = peripheral
base = 0x40003000
class = STM32F4xxIwdg

[LPTIM1]
type = peripheral
base = 0x40002400
class = STM32F4xxLptim
intn = 97

[PWR]
type = peripheral
base = 0x40007000
class = STM32F4xxPwr

[RCC]
type = peripheral
base = 0x40023800
class = STM32F4xxRccV2
intn = 5

[RNG]
type = peripheral
base = 0x40080000
class = STM32F4xxRng
intn = 80

[RTC]
type = peripheral
base = 0x40002800
class = STM32F4xxRtc
wkup_intn = 3
alarm_intn = 41

[SPI1]
type = peripheral
base = 0x40013000
class = STM32F4xxSpi
intn = 35

[SYSCFG]
type = peripheral
base = 0x40013800
class = STM32F4xxSyscfgV1

[TIM1]
type = peripheral
base = 0x40010000
class = STM32F4xxTim
brk_tim9_intn = 24
up_intn = 25
trg_com_tim11_intn = 26
cc_intn = 27

[TIM11]
type = peripheral
base = 0x40014800
class = STM32F4xxTim

[TIM5]
type = peripheral
base = 0x40000c00
class = STM32F4xxTim
intn = 50

[TIM6]
type = peripheral
base = 0x40001000
class = STM32F4xxTim
dac_intn = 54

[TIM9]
type = peripheral
base = 0x40014000
class = STM32F4xxTim

[USART1]
type = peripheral
base = 0x40011000
class = STM32F4xxUsart
intn = 37

[USART2]
type = peripheral
base = 0x40004400
class = STM32F4xxUsart
intn = 38

[WWDG]
type = peripheral
base = 0x40002c00
class = STM32F4xxWwdg
intn = 0

