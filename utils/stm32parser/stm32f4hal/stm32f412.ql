[ADC1]
type = peripheral
base = 0x40012000
class = STM32F4xxAdc

[ADC1_COMMON]
type = peripheral
base = 0x40012300
class = STM32F4xxAdc_common

[CAN1]
type = peripheral
base = 0x40006400
class = STM32F4xxCan
tx_intn = 19
rx0_intn = 20
rx1_intn = 21
sce_intn = 22

[CAN2]
type = peripheral
base = 0x40006800
class = STM32F4xxCan
tx_intn = 63
rx0_intn = 64
rx1_intn = 65
sce_intn = 66

[CRC]
type = peripheral
base = 0x40023000
class = STM32F4xxCrc

[DBGMCU]
type = peripheral
base = 0xe0042000
class = STM32F4xxDbgmcu

[DFSDM1_Channel0]
type = peripheral
base = 0x40016000
class = STM32F4xxDfsdm_channel

[DFSDM1_Channel1]
type = peripheral
base = 0x40016020
class = STM32F4xxDfsdm_channel

[DFSDM1_Channel2]
type = peripheral
base = 0x40016040
class = STM32F4xxDfsdm_channel

[DFSDM1_Channel3]
type = peripheral
base = 0x40016060
class = STM32F4xxDfsdm_channel

[DFSDM1_Filter0]
type = peripheral
base = 0x40016100
class = STM32F4xxDfsdm_filter

[DFSDM1_Filter1]
type = peripheral
base = 0x40016180
class = STM32F4xxDfsdm_filter

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

[I2C3]
type = peripheral
base = 0x40005c00
class = STM32F4xxI2c
ev_intn = 72
er_intn = 73

[I2S2ext]
type = peripheral
base = 0x40003400
class = STM32F4xxSpi

[I2S3ext]
type = peripheral
base = 0x40004000
class = STM32F4xxSpi

[IWDG]
type = peripheral
base = 0x40003000
class = STM32F4xxIwdg

[PWR]
type = peripheral
base = 0x40007000
class = STM32F4xxPwr

[RCC]
type = peripheral
base = 0x40023800
class = STM32F4xxRccV3
intn = 5

[RNG]
type = peripheral
base = 0x50060800
class = STM32F4xxRng
intn = 80

[RTC]
type = peripheral
base = 0x40002800
class = STM32F4xxRtc
wkup_intn = 3
alarm_intn = 41

[SDIO]
type = peripheral
base = 0x40012c00
class = STM32F4xxSdio
intn = 49

[SPI1]
type = peripheral
base = 0x40013000
class = STM32F4xxSpi
intn = 35

[SPI2]
type = peripheral
base = 0x40003800
class = STM32F4xxSpi
intn = 36

[SPI3]
type = peripheral
base = 0x40003c00
class = STM32F4xxSpi
intn = 51

[SPI4]
type = peripheral
base = 0x40013400
class = STM32F4xxSpi
intn = 84

[SPI5]
type = peripheral
base = 0x40015000
class = STM32F4xxSpi
intn = 85

[SYSCFG]
type = peripheral
base = 0x40013800
class = STM32F4xxSyscfgV1

[TIM1]
type = peripheral
base = 0x40010000
class = STM32F4xxTim
brk_tim9_intn = 24
up_tim10_intn = 25
trg_com_tim11_intn = 26
cc_intn = 27

[TIM10]
type = peripheral
base = 0x40014400
class = STM32F4xxTim

[TIM11]
type = peripheral
base = 0x40014800
class = STM32F4xxTim

[TIM12]
type = peripheral
base = 0x40001800
class = STM32F4xxTim

[TIM13]
type = peripheral
base = 0x40001c00
class = STM32F4xxTim

[TIM14]
type = peripheral
base = 0x40002000
class = STM32F4xxTim

[TIM2]
type = peripheral
base = 0x40000000
class = STM32F4xxTim
intn = 28

[TIM3]
type = peripheral
base = 0x40000400
class = STM32F4xxTim
intn = 29

[TIM4]
type = peripheral
base = 0x40000800
class = STM32F4xxTim
intn = 30

[TIM5]
type = peripheral
base = 0x40000c00
class = STM32F4xxTim
intn = 50

[TIM6]
type = peripheral
base = 0x40001000
class = STM32F4xxTim
intn = 54

[TIM7]
type = peripheral
base = 0x40001400
class = STM32F4xxTim
intn = 55

[TIM8]
type = peripheral
base = 0x40010400
class = STM32F4xxTim
brk_tim12_intn = 43
up_tim13_intn = 44
trg_com_tim14_intn = 45
cc_intn = 46

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

[USART3]
type = peripheral
base = 0x40004800
class = STM32F4xxUsart
intn = 39

[USART6]
type = peripheral
base = 0x40011400
class = STM32F4xxUsart
intn = 71

[USB_OTG_FS]
type = peripheral
base = 0x50000000
class = STM32F4xxUsb_otg_globalV1

[WWDG]
type = peripheral
base = 0x40002c00
class = STM32F4xxWwdg
intn = 0

