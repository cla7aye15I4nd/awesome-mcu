import ctypes

class STM32F1xxTim:
    class Type(ctypes.Structure):
        """ the structure available in :
                stm32f100xb
                stm32f100xe
                stm32f101xb
                stm32f101xe
                stm32f101xg
                stm32f102xb
                stm32f103xb
                stm32f103xe
                stm32f103xg
                stm32f105xc
                stm32f107xc
        """

        _fields_ = [
            ("CR1"  , ctypes.c_uint32), #TIM control register 1,                      Address offset: 0x00
            ("CR2"  , ctypes.c_uint32), #TIM control register 2,                      Address offset: 0x04
            ("SMCR" , ctypes.c_uint32), #TIM slave Mode Control register,             Address offset: 0x08
            ("DIER" , ctypes.c_uint32), #TIM DMA/interrupt enable register,           Address offset: 0x0C
            ("SR"   , ctypes.c_uint32), #TIM status register,                         Address offset: 0x10
            ("EGR"  , ctypes.c_uint32), #TIM event generation register,               Address offset: 0x14
            ("CCMR1", ctypes.c_uint32), #TIM  capture/compare mode register 1,        Address offset: 0x18
            ("CCMR2", ctypes.c_uint32), #TIM  capture/compare mode register 2,        Address offset: 0x1C
            ("CCER" , ctypes.c_uint32), #TIM capture/compare enable register,         Address offset: 0x20
            ("CNT"  , ctypes.c_uint32), #TIM counter register,                        Address offset: 0x24
            ("PSC"  , ctypes.c_uint32), #TIM prescaler register,                      Address offset: 0x28
            ("ARR"  , ctypes.c_uint32), #TIM auto-reload register,                    Address offset: 0x2C
            ("RCR"  , ctypes.c_uint32), #TIM  repetition counter register,            Address offset: 0x30
            ("CCR1" , ctypes.c_uint32), #TIM capture/compare register 1,              Address offset: 0x34
            ("CCR2" , ctypes.c_uint32), #TIM capture/compare register 2,              Address offset: 0x38
            ("CCR3" , ctypes.c_uint32), #TIM capture/compare register 3,              Address offset: 0x3C
            ("CCR4" , ctypes.c_uint32), #TIM capture/compare register 4,              Address offset: 0x40
            ("BDTR" , ctypes.c_uint32), #TIM break and dead-time register,            Address offset: 0x44
            ("DCR"  , ctypes.c_uint32), #TIM DMA control register,                    Address offset: 0x48
            ("DMAR" , ctypes.c_uint32), #TIM DMA address for full transfer register,  Address offset: 0x4C
            ("OR"   , ctypes.c_uint32), #TIM option register,                         Address offset: 0x50
        ]

class STM32F1xxRtc:
    class Type(ctypes.Structure):
        """ the structure available in :
                stm32f100xb
                stm32f100xe
                stm32f101xb
                stm32f101xe
                stm32f101xg
                stm32f102xb
                stm32f103xb
                stm32f103xe
                stm32f103xg
                stm32f105xc
                stm32f107xc
        """

        _fields_ = [
            ("CRH" , ctypes.c_uint32), #
            ("CRL" , ctypes.c_uint32), #
            ("PRLH", ctypes.c_uint32), #
            ("PRLL", ctypes.c_uint32), #
            ("DIVH", ctypes.c_uint32), #
            ("DIVL", ctypes.c_uint32), #
            ("CNTH", ctypes.c_uint32), #
            ("CNTL", ctypes.c_uint32), #
            ("ALRH", ctypes.c_uint32), #
            ("ALRL", ctypes.c_uint32), #
        ]

class STM32F1xxWwdg:
    class Type(ctypes.Structure):
        """ the structure available in :
                stm32f100xb
                stm32f100xe
                stm32f101xb
                stm32f101xe
                stm32f101xg
                stm32f102xb
                stm32f103xb
                stm32f103xe
                stm32f103xg
                stm32f105xc
                stm32f107xc
        """

        _fields_ = [
            ("CR" , ctypes.c_uint32), #WWDG Control register,       Address offset: 0x00
            ("CFR", ctypes.c_uint32), #WWDG Configuration register, Address offset: 0x04
            ("SR" , ctypes.c_uint32), #WWDG Status register,        Address offset: 0x08
        ]

class STM32F1xxIwdg:
    class Type(ctypes.Structure):
        """ the structure available in :
                stm32f100xb
                stm32f100xe
                stm32f101xb
                stm32f101xe
                stm32f101xg
                stm32f102xb
                stm32f103xb
                stm32f103xe
                stm32f103xg
                stm32f105xc
                stm32f107xc
        """

        _fields_ = [
            ("KR" , ctypes.c_uint32), #Key register,                                Address offset: 0x00
            ("PR" , ctypes.c_uint32), #Prescaler register,                          Address offset: 0x04
            ("RLR", ctypes.c_uint32), #Reload register,                             Address offset: 0x08
            ("SR" , ctypes.c_uint32), #Status register,                             Address offset: 0x0C
        ]

class STM32F1xxSpiV1:
    class Type(ctypes.Structure):
        """ the structure available in :
                stm32f100xb
                stm32f100xe
        """

        _fields_ = [
            ("CR1"   , ctypes.c_uint32), #
            ("CR2"   , ctypes.c_uint32), #
            ("SR"    , ctypes.c_uint32), #
            ("DR"    , ctypes.c_uint32), #
            ("CRCPR" , ctypes.c_uint32), #
            ("RXCRCR", ctypes.c_uint32), #
            ("TXCRCR", ctypes.c_uint32), #
        ]

class STM32F1xxSpi:
    class Type(ctypes.Structure):
        """ the structure available in :
                stm32f101xb
                stm32f102xb
                stm32f103xb
        """

        _fields_ = [
            ("CR1"    , ctypes.c_uint32), #
            ("CR2"    , ctypes.c_uint32), #
            ("SR"     , ctypes.c_uint32), #
            ("DR"     , ctypes.c_uint32), #
            ("CRCPR"  , ctypes.c_uint32), #
            ("RXCRCR" , ctypes.c_uint32), #
            ("TXCRCR" , ctypes.c_uint32), #
            ("I2SCFGR", ctypes.c_uint32), #
        ]

class STM32F1xxSpiV2:
    class Type(ctypes.Structure):
        """ the structure available in :
                stm32f101xe
                stm32f101xg
                stm32f103xe
                stm32f103xg
                stm32f105xc
                stm32f107xc
        """

        _fields_ = [
            ("CR1"    , ctypes.c_uint32), #
            ("CR2"    , ctypes.c_uint32), #
            ("SR"     , ctypes.c_uint32), #
            ("DR"     , ctypes.c_uint32), #
            ("CRCPR"  , ctypes.c_uint32), #
            ("RXCRCR" , ctypes.c_uint32), #
            ("TXCRCR" , ctypes.c_uint32), #
            ("I2SCFGR", ctypes.c_uint32), #
            ("I2SPR"  , ctypes.c_uint32), #
        ]

class STM32F1xxUsart:
    class Type(ctypes.Structure):
        """ the structure available in :
                stm32f100xb
                stm32f100xe
                stm32f101xb
                stm32f101xe
                stm32f101xg
                stm32f102xb
                stm32f103xb
                stm32f103xe
                stm32f103xg
                stm32f105xc
                stm32f107xc
        """

        _fields_ = [
            ("SR"  , ctypes.c_uint32), #USART Status register,                   Address offset: 0x00
            ("DR"  , ctypes.c_uint32), #USART Data register,                     Address offset: 0x04
            ("BRR" , ctypes.c_uint32), #USART Baud rate register,                Address offset: 0x08
            ("CR1" , ctypes.c_uint32), #USART Control register 1,                Address offset: 0x0C
            ("CR2" , ctypes.c_uint32), #USART Control register 2,                Address offset: 0x10
            ("CR3" , ctypes.c_uint32), #USART Control register 3,                Address offset: 0x14
            ("GTPR", ctypes.c_uint32), #USART Guard time and prescaler register, Address offset: 0x18
        ]

class STM32F1xxI2c:
    class Type(ctypes.Structure):
        """ the structure available in :
                stm32f100xb
                stm32f100xe
                stm32f101xb
                stm32f101xe
                stm32f101xg
                stm32f102xb
                stm32f103xb
                stm32f103xe
                stm32f103xg
                stm32f105xc
                stm32f107xc
        """

        _fields_ = [
            ("CR1"  , ctypes.c_uint32), #
            ("CR2"  , ctypes.c_uint32), #
            ("OAR1" , ctypes.c_uint32), #
            ("OAR2" , ctypes.c_uint32), #
            ("DR"   , ctypes.c_uint32), #
            ("SR1"  , ctypes.c_uint32), #
            ("SR2"  , ctypes.c_uint32), #
            ("CCR"  , ctypes.c_uint32), #
            ("TRISE", ctypes.c_uint32), #
        ]

class STM32F1xxBkp:
    class Type(ctypes.Structure):
        """ the structure available in :
                stm32f100xb
                stm32f101xb
                stm32f102xb
                stm32f103xb
        """

        _fields_ = [
            ("RESERVED0", ctypes.c_uint32), #
            ("DR1"      , ctypes.c_uint32), #
            ("DR2"      , ctypes.c_uint32), #
            ("DR3"      , ctypes.c_uint32), #
            ("DR4"      , ctypes.c_uint32), #
            ("DR5"      , ctypes.c_uint32), #
            ("DR6"      , ctypes.c_uint32), #
            ("DR7"      , ctypes.c_uint32), #
            ("DR8"      , ctypes.c_uint32), #
            ("DR9"      , ctypes.c_uint32), #
            ("DR10"     , ctypes.c_uint32), #
            ("RTCCR"    , ctypes.c_uint32), #
            ("CR"       , ctypes.c_uint32), #
            ("CSR"      , ctypes.c_uint32), #
        ]

class STM32F1xxBkpV1:
    class Type(ctypes.Structure):
        """ the structure available in :
                stm32f100xe
                stm32f101xe
                stm32f101xg
                stm32f103xe
                stm32f103xg
                stm32f105xc
                stm32f107xc
        """

        _fields_ = [
            ("RESERVED0" , ctypes.c_uint32),     #
            ("DR1"       , ctypes.c_uint32),     #
            ("DR2"       , ctypes.c_uint32),     #
            ("DR3"       , ctypes.c_uint32),     #
            ("DR4"       , ctypes.c_uint32),     #
            ("DR5"       , ctypes.c_uint32),     #
            ("DR6"       , ctypes.c_uint32),     #
            ("DR7"       , ctypes.c_uint32),     #
            ("DR8"       , ctypes.c_uint32),     #
            ("DR9"       , ctypes.c_uint32),     #
            ("DR10"      , ctypes.c_uint32),     #
            ("RTCCR"     , ctypes.c_uint32),     #
            ("CR"        , ctypes.c_uint32),     #
            ("CSR"       , ctypes.c_uint32),     #
            ("RESERVED13", ctypes.c_uint32 * 2), #
            ("DR11"      , ctypes.c_uint32),     #
            ("DR12"      , ctypes.c_uint32),     #
            ("DR13"      , ctypes.c_uint32),     #
            ("DR14"      , ctypes.c_uint32),     #
            ("DR15"      , ctypes.c_uint32),     #
            ("DR16"      , ctypes.c_uint32),     #
            ("DR17"      , ctypes.c_uint32),     #
            ("DR18"      , ctypes.c_uint32),     #
            ("DR19"      , ctypes.c_uint32),     #
            ("DR20"      , ctypes.c_uint32),     #
            ("DR21"      , ctypes.c_uint32),     #
            ("DR22"      , ctypes.c_uint32),     #
            ("DR23"      , ctypes.c_uint32),     #
            ("DR24"      , ctypes.c_uint32),     #
            ("DR25"      , ctypes.c_uint32),     #
            ("DR26"      , ctypes.c_uint32),     #
            ("DR27"      , ctypes.c_uint32),     #
            ("DR28"      , ctypes.c_uint32),     #
            ("DR29"      , ctypes.c_uint32),     #
            ("DR30"      , ctypes.c_uint32),     #
            ("DR31"      , ctypes.c_uint32),     #
            ("DR32"      , ctypes.c_uint32),     #
            ("DR33"      , ctypes.c_uint32),     #
            ("DR34"      , ctypes.c_uint32),     #
            ("DR35"      , ctypes.c_uint32),     #
            ("DR36"      , ctypes.c_uint32),     #
            ("DR37"      , ctypes.c_uint32),     #
            ("DR38"      , ctypes.c_uint32),     #
            ("DR39"      , ctypes.c_uint32),     #
            ("DR40"      , ctypes.c_uint32),     #
            ("DR41"      , ctypes.c_uint32),     #
            ("DR42"      , ctypes.c_uint32),     #
        ]

class STM32F1xxPwr:
    class Type(ctypes.Structure):
        """ the structure available in :
                stm32f100xb
                stm32f100xe
                stm32f101xb
                stm32f101xe
                stm32f101xg
                stm32f102xb
                stm32f103xb
                stm32f103xe
                stm32f103xg
                stm32f105xc
                stm32f107xc
        """

        _fields_ = [
            ("CR" , ctypes.c_uint32), #
            ("CSR", ctypes.c_uint32), #
        ]

class STM32F1xxDacV1:
    class Type(ctypes.Structure):
        """ the structure available in :
                stm32f100xb
                stm32f100xe
        """

        _fields_ = [
            ("CR"     , ctypes.c_uint32), #
            ("SWTRIGR", ctypes.c_uint32), #
            ("DHR12R1", ctypes.c_uint32), #
            ("DHR12L1", ctypes.c_uint32), #
            ("DHR8R1" , ctypes.c_uint32), #
            ("DHR12R2", ctypes.c_uint32), #
            ("DHR12L2", ctypes.c_uint32), #
            ("DHR8R2" , ctypes.c_uint32), #
            ("DHR12RD", ctypes.c_uint32), #
            ("DHR12LD", ctypes.c_uint32), #
            ("DHR8RD" , ctypes.c_uint32), #
            ("DOR1"   , ctypes.c_uint32), #
            ("DOR2"   , ctypes.c_uint32), #
            ("SR"     , ctypes.c_uint32), #
        ]

class STM32F1xxDacV2:
    class Type(ctypes.Structure):
        """ the structure available in :
                stm32f101xe
                stm32f101xg
                stm32f103xe
                stm32f103xg
                stm32f105xc
                stm32f107xc
        """

        _fields_ = [
            ("CR"     , ctypes.c_uint32), #
            ("SWTRIGR", ctypes.c_uint32), #
            ("DHR12R1", ctypes.c_uint32), #
            ("DHR12L1", ctypes.c_uint32), #
            ("DHR8R1" , ctypes.c_uint32), #
            ("DHR12R2", ctypes.c_uint32), #
            ("DHR12L2", ctypes.c_uint32), #
            ("DHR8R2" , ctypes.c_uint32), #
            ("DHR12RD", ctypes.c_uint32), #
            ("DHR12LD", ctypes.c_uint32), #
            ("DHR8RD" , ctypes.c_uint32), #
            ("DOR1"   , ctypes.c_uint32), #
            ("DOR2"   , ctypes.c_uint32), #
        ]

class STM32F1xxCec:
    class Type(ctypes.Structure):
        """ the structure available in :
                stm32f100xb
                stm32f100xe
        """

        _fields_ = [
            ("CFGR", ctypes.c_uint32), #
            ("OAR" , ctypes.c_uint32), #
            ("PRES", ctypes.c_uint32), #
            ("ESR" , ctypes.c_uint32), #
            ("CSR" , ctypes.c_uint32), #
            ("TXD" , ctypes.c_uint32), #
            ("RXD" , ctypes.c_uint32), #
        ]

class STM32F1xxAfio:
    class Type(ctypes.Structure):
        """ the structure available in :
                stm32f100xb
                stm32f100xe
                stm32f101xb
                stm32f101xe
                stm32f101xg
                stm32f102xb
                stm32f103xb
                stm32f103xe
                stm32f103xg
                stm32f105xc
                stm32f107xc
        """

        _fields_ = [
            ("EVCR"     , ctypes.c_uint32),     #
            ("MAPR"     , ctypes.c_uint32),     #
            ("EXTICR"   , ctypes.c_uint32 * 4), #
            ("RESERVED0", ctypes.c_uint32),     #
            ("MAPR2"    , ctypes.c_uint32),     #
        ]

class STM32F1xxExti:
    class Type(ctypes.Structure):
        """ the structure available in :
                stm32f100xb
                stm32f100xe
                stm32f101xb
                stm32f101xe
                stm32f101xg
                stm32f102xb
                stm32f103xb
                stm32f103xe
                stm32f103xg
                stm32f105xc
                stm32f107xc
        """

        _fields_ = [
            ("IMR"  , ctypes.c_uint32), #
            ("EMR"  , ctypes.c_uint32), #
            ("RTSR" , ctypes.c_uint32), #
            ("FTSR" , ctypes.c_uint32), #
            ("SWIER", ctypes.c_uint32), #
            ("PR"   , ctypes.c_uint32), #
        ]

class STM32F1xxGpio:
    class Type(ctypes.Structure):
        """ the structure available in :
                stm32f100xb
                stm32f100xe
                stm32f101xb
                stm32f101xe
                stm32f101xg
                stm32f102xb
                stm32f103xb
                stm32f103xe
                stm32f103xg
                stm32f105xc
                stm32f107xc
        """

        _fields_ = [
            ("CRL" , ctypes.c_uint32), #
            ("CRH" , ctypes.c_uint32), #
            ("IDR" , ctypes.c_uint32), #
            ("ODR" , ctypes.c_uint32), #
            ("BSRR", ctypes.c_uint32), #
            ("BRR" , ctypes.c_uint32), #
            ("LCKR", ctypes.c_uint32), #
        ]

class STM32F1xxAdc:
    class Type(ctypes.Structure):
        """ the structure available in :
                stm32f100xb
                stm32f100xe
                stm32f101xb
                stm32f101xe
                stm32f101xg
                stm32f102xb
                stm32f103xb
                stm32f103xe
                stm32f103xg
                stm32f105xc
                stm32f107xc
        """

        _fields_ = [
            ("SR"   , ctypes.c_uint32), #
            ("CR1"  , ctypes.c_uint32), #
            ("CR2"  , ctypes.c_uint32), #
            ("SMPR1", ctypes.c_uint32), #
            ("SMPR2", ctypes.c_uint32), #
            ("JOFR1", ctypes.c_uint32), #
            ("JOFR2", ctypes.c_uint32), #
            ("JOFR3", ctypes.c_uint32), #
            ("JOFR4", ctypes.c_uint32), #
            ("HTR"  , ctypes.c_uint32), #
            ("LTR"  , ctypes.c_uint32), #
            ("SQR1" , ctypes.c_uint32), #
            ("SQR2" , ctypes.c_uint32), #
            ("SQR3" , ctypes.c_uint32), #
            ("JSQR" , ctypes.c_uint32), #
            ("JDR1" , ctypes.c_uint32), #
            ("JDR2" , ctypes.c_uint32), #
            ("JDR3" , ctypes.c_uint32), #
            ("JDR4" , ctypes.c_uint32), #
            ("DR"   , ctypes.c_uint32), #
        ]

class STM32F1xxAdc_common:
    class Type(ctypes.Structure):
        """ the structure available in :
                stm32f100xb
                stm32f100xe
                stm32f101xb
                stm32f101xe
                stm32f101xg
                stm32f102xb
                stm32f103xb
                stm32f103xe
                stm32f103xg
                stm32f105xc
                stm32f107xc
        """

        _fields_ = [
            ("SR"      , ctypes.c_uint32),      #ADC status register,    used for ADC multimode (bits common to several ADC instances). Address offset: ADC1 base address
            ("CR1"     , ctypes.c_uint32),      #ADC control register 1, used for ADC multimode (bits common to several ADC instances). Address offset: ADC1 base address + 0x04
            ("CR2"     , ctypes.c_uint32),      #ADC control register 2, used for ADC multimode (bits common to several ADC instances). Address offset: ADC1 base address + 0x08
            ("RESERVED", ctypes.c_uint32 * 16), #
            ("DR"      , ctypes.c_uint32),      #ADC data register,      used for ADC multimode (bits common to several ADC instances). Address offset: ADC1 base address + 0x4C
        ]

class STM32F1xxDma:
    class Type(ctypes.Structure):
        """ the structure available in :
                stm32f100xb
                stm32f100xe
                stm32f101xb
                stm32f101xe
                stm32f101xg
                stm32f102xb
                stm32f103xb
                stm32f103xe
                stm32f103xg
                stm32f105xc
                stm32f107xc
        """

        _fields_ = [
            ("ISR" , ctypes.c_uint32), #
            ("IFCR", ctypes.c_uint32), #
        ]

class STM32F1xxDma_channel:
    class Type(ctypes.Structure):
        """ the structure available in :
                stm32f100xb
                stm32f100xe
                stm32f101xb
                stm32f101xe
                stm32f101xg
                stm32f102xb
                stm32f103xb
                stm32f103xe
                stm32f103xg
                stm32f105xc
                stm32f107xc
        """

        _fields_ = [
            ("CCR"  , ctypes.c_uint32), #
            ("CNDTR", ctypes.c_uint32), #
            ("CPAR" , ctypes.c_uint32), #
            ("CMAR" , ctypes.c_uint32), #
        ]

class STM32F1xxRccV1:
    class Type(ctypes.Structure):
        """ the structure available in :
                stm32f100xb
                stm32f100xe
        """

        _fields_ = [
            ("CR"       , ctypes.c_uint32), #
            ("CFGR"     , ctypes.c_uint32), #
            ("CIR"      , ctypes.c_uint32), #
            ("APB2RSTR" , ctypes.c_uint32), #
            ("APB1RSTR" , ctypes.c_uint32), #
            ("AHBENR"   , ctypes.c_uint32), #
            ("APB2ENR"  , ctypes.c_uint32), #
            ("APB1ENR"  , ctypes.c_uint32), #
            ("BDCR"     , ctypes.c_uint32), #
            ("CSR"      , ctypes.c_uint32), #
            ("RESERVED0", ctypes.c_uint32), #
            ("CFGR2"    , ctypes.c_uint32), #
        ]

class STM32F1xxRcc:
    class Type(ctypes.Structure):
        """ the structure available in :
                stm32f101xb
                stm32f101xe
                stm32f101xg
                stm32f102xb
                stm32f103xb
                stm32f103xe
                stm32f103xg
        """

        _fields_ = [
            ("CR"      , ctypes.c_uint32), #
            ("CFGR"    , ctypes.c_uint32), #
            ("CIR"     , ctypes.c_uint32), #
            ("APB2RSTR", ctypes.c_uint32), #
            ("APB1RSTR", ctypes.c_uint32), #
            ("AHBENR"  , ctypes.c_uint32), #
            ("APB2ENR" , ctypes.c_uint32), #
            ("APB1ENR" , ctypes.c_uint32), #
            ("BDCR"    , ctypes.c_uint32), #
            ("CSR"     , ctypes.c_uint32), #
        ]

class STM32F1xxRccV2:
    class Type(ctypes.Structure):
        """ the structure available in :
                stm32f105xc
                stm32f107xc
        """

        _fields_ = [
            ("CR"      , ctypes.c_uint32), #
            ("CFGR"    , ctypes.c_uint32), #
            ("CIR"     , ctypes.c_uint32), #
            ("APB2RSTR", ctypes.c_uint32), #
            ("APB1RSTR", ctypes.c_uint32), #
            ("AHBENR"  , ctypes.c_uint32), #
            ("APB2ENR" , ctypes.c_uint32), #
            ("APB1ENR" , ctypes.c_uint32), #
            ("BDCR"    , ctypes.c_uint32), #
            ("CSR"     , ctypes.c_uint32), #
            ("AHBRSTR" , ctypes.c_uint32), #
            ("CFGR2"   , ctypes.c_uint32), #
        ]

class STM32F1xxCrc:
    class Type(ctypes.Structure):
        """ the structure available in :
                stm32f100xb
                stm32f100xe
                stm32f101xb
                stm32f101xe
                stm32f101xg
                stm32f102xb
                stm32f103xb
                stm32f103xe
                stm32f103xg
                stm32f105xc
                stm32f107xc
        """

        _fields_ = [
            ("DR"       , ctypes.c_uint32), #CRC Data register,                           Address offset: 0x00
            ("IDR"      , ctypes.c_uint8),  #CRC Independent data register,               Address offset: 0x04
            ("RESERVED0", ctypes.c_uint8),  #Reserved,                                    Address offset: 0x05
            ("RESERVED1", ctypes.c_uint16), #Reserved,                                    Address offset: 0x06
            ("CR"       , ctypes.c_uint32), #CRC Control register,                        Address offset: 0x08
        ]

class STM32F1xxFlash:
    class Type(ctypes.Structure):
        """ the structure available in :
                stm32f100xb
                stm32f100xe
                stm32f101xb
                stm32f101xe
                stm32f102xb
                stm32f103xb
                stm32f103xe
                stm32f105xc
                stm32f107xc
        """

        _fields_ = [
            ("ACR"     , ctypes.c_uint32), #
            ("KEYR"    , ctypes.c_uint32), #
            ("OPTKEYR" , ctypes.c_uint32), #
            ("SR"      , ctypes.c_uint32), #
            ("CR"      , ctypes.c_uint32), #
            ("AR"      , ctypes.c_uint32), #
            ("RESERVED", ctypes.c_uint32), #
            ("OBR"     , ctypes.c_uint32), #
            ("WRPR"    , ctypes.c_uint32), #
        ]

class STM32F1xxFlashV1:
    class Type(ctypes.Structure):
        """ the structure available in :
                stm32f101xg
                stm32f103xg
        """

        _fields_ = [
            ("ACR"      , ctypes.c_uint32),     #
            ("KEYR"     , ctypes.c_uint32),     #
            ("OPTKEYR"  , ctypes.c_uint32),     #
            ("SR"       , ctypes.c_uint32),     #
            ("CR"       , ctypes.c_uint32),     #
            ("AR"       , ctypes.c_uint32),     #
            ("RESERVED" , ctypes.c_uint32),     #
            ("OBR"      , ctypes.c_uint32),     #
            ("WRPR"     , ctypes.c_uint32),     #
            ("RESERVED1", ctypes.c_uint32 * 8), #
            ("KEYR2"    , ctypes.c_uint32),     #
            ("RESERVED2", ctypes.c_uint32),     #
            ("SR2"      , ctypes.c_uint32),     #
            ("CR2"      , ctypes.c_uint32),     #
            ("AR2"      , ctypes.c_uint32),     #
        ]

class STM32F1xxOb:
    class Type(ctypes.Structure):
        """ the structure available in :
                stm32f100xb
                stm32f100xe
                stm32f101xb
                stm32f101xe
                stm32f101xg
                stm32f102xb
                stm32f103xb
                stm32f103xe
                stm32f103xg
                stm32f105xc
                stm32f107xc
        """

        _fields_ = [
            ("RDP"  , ctypes.c_uint16), #
            ("USER" , ctypes.c_uint16), #
            ("Data0", ctypes.c_uint16), #
            ("Data1", ctypes.c_uint16), #
            ("WRP0" , ctypes.c_uint16), #
            ("WRP1" , ctypes.c_uint16), #
            ("WRP2" , ctypes.c_uint16), #
            ("WRP3" , ctypes.c_uint16), #
        ]

class STM32F1xxDbgmcu:
    class Type(ctypes.Structure):
        """ the structure available in :
                stm32f100xb
                stm32f100xe
                stm32f101xb
                stm32f101xe
                stm32f101xg
                stm32f102xb
                stm32f103xb
                stm32f103xe
                stm32f103xg
                stm32f105xc
                stm32f107xc
        """

        _fields_ = [
            ("IDCODE", ctypes.c_uint32), #
            ("CR"    , ctypes.c_uint32), #
        ]

class STM32F1xxFsmc_bank1:
    class Type(ctypes.Structure):
        """ the structure available in :
                stm32f100xe
                stm32f101xe
                stm32f101xg
                stm32f103xe
                stm32f103xg
        """

        _fields_ = [
            ("BTCR", ctypes.c_uint32 * 8), #
        ]

class STM32F1xxFsmc_bank1e:
    class Type(ctypes.Structure):
        """ the structure available in :
                stm32f100xe
                stm32f101xe
                stm32f101xg
                stm32f103xe
                stm32f103xg
        """

        _fields_ = [
            ("BWTR", ctypes.c_uint32 * 7), #
        ]

class STM32F1xxFsmc_bank2_3:
    class Type(ctypes.Structure):
        """ the structure available in :
                stm32f101xe
                stm32f101xg
                stm32f103xe
                stm32f103xg
        """

        _fields_ = [
            ("PCR2"     , ctypes.c_uint32), #NAND Flash control register 2,                       Address offset: 0x60
            ("SR2"      , ctypes.c_uint32), #NAND Flash FIFO status and interrupt register 2,     Address offset: 0x64
            ("PMEM2"    , ctypes.c_uint32), #NAND Flash Common memory space timing register 2,    Address offset: 0x68
            ("PATT2"    , ctypes.c_uint32), #NAND Flash Attribute memory space timing register 2, Address offset: 0x6C
            ("RESERVED0", ctypes.c_uint32), #Reserved, 0x70
            ("ECCR2"    , ctypes.c_uint32), #NAND Flash ECC result registers 2,                   Address offset: 0x74
            ("RESERVED1", ctypes.c_uint32), #Reserved, 0x78
            ("RESERVED2", ctypes.c_uint32), #Reserved, 0x7C
            ("PCR3"     , ctypes.c_uint32), #NAND Flash control register 3,                       Address offset: 0x80
            ("SR3"      , ctypes.c_uint32), #NAND Flash FIFO status and interrupt register 3,     Address offset: 0x84
            ("PMEM3"    , ctypes.c_uint32), #NAND Flash Common memory space timing register 3,    Address offset: 0x88
            ("PATT3"    , ctypes.c_uint32), #NAND Flash Attribute memory space timing register 3, Address offset: 0x8C
            ("RESERVED3", ctypes.c_uint32), #Reserved, 0x90
            ("ECCR3"    , ctypes.c_uint32), #NAND Flash ECC result registers 3,                   Address offset: 0x94
        ]

class STM32F1xxFsmc_bank4:
    class Type(ctypes.Structure):
        """ the structure available in :
                stm32f101xe
                stm32f101xg
                stm32f103xe
                stm32f103xg
        """

        _fields_ = [
            ("PCR4" , ctypes.c_uint32), #
            ("SR4"  , ctypes.c_uint32), #
            ("PMEM4", ctypes.c_uint32), #
            ("PATT4", ctypes.c_uint32), #
            ("PIO4" , ctypes.c_uint32), #
        ]

class STM32F1xxUsb:
    class Type(ctypes.Structure):
        """ the structure available in :
                stm32f102xb
                stm32f103xb
                stm32f103xe
                stm32f103xg
        """

        _fields_ = [
            ("EP0R"     , ctypes.c_uint16),      #USB Endpoint 0 register,                   Address offset: 0x00
            ("RESERVED0", ctypes.c_uint16),      #Reserved
            ("EP1R"     , ctypes.c_uint16),      #USB Endpoint 1 register,                   Address offset: 0x04
            ("RESERVED1", ctypes.c_uint16),      #Reserved
            ("EP2R"     , ctypes.c_uint16),      #USB Endpoint 2 register,                   Address offset: 0x08
            ("RESERVED2", ctypes.c_uint16),      #Reserved
            ("EP3R"     , ctypes.c_uint16),      #USB Endpoint 3 register,                   Address offset: 0x0C
            ("RESERVED3", ctypes.c_uint16),      #Reserved
            ("EP4R"     , ctypes.c_uint16),      #USB Endpoint 4 register,                   Address offset: 0x10
            ("RESERVED4", ctypes.c_uint16),      #Reserved
            ("EP5R"     , ctypes.c_uint16),      #USB Endpoint 5 register,                   Address offset: 0x14
            ("RESERVED5", ctypes.c_uint16),      #Reserved
            ("EP6R"     , ctypes.c_uint16),      #USB Endpoint 6 register,                   Address offset: 0x18
            ("RESERVED6", ctypes.c_uint16),      #Reserved
            ("EP7R"     , ctypes.c_uint16),      #USB Endpoint 7 register,                   Address offset: 0x1C
            ("RESERVED7", ctypes.c_uint16 * 17), #Reserved
            ("CNTR"     , ctypes.c_uint16),      #Control register,                          Address offset: 0x40
            ("RESERVED8", ctypes.c_uint16),      #Reserved
            ("ISTR"     , ctypes.c_uint16),      #Interrupt status register,                 Address offset: 0x44
            ("RESERVED9", ctypes.c_uint16),      #Reserved
            ("FNR"      , ctypes.c_uint16),      #Frame number register,                     Address offset: 0x48
            ("RESERVEDA", ctypes.c_uint16),      #Reserved
            ("DADDR"    , ctypes.c_uint16),      #Device address register,                   Address offset: 0x4C
            ("RESERVEDB", ctypes.c_uint16),      #Reserved
            ("BTABLE"   , ctypes.c_uint16),      #Buffer Table address register,             Address offset: 0x50
            ("RESERVEDC", ctypes.c_uint16),      #Reserved
        ]

class STM32F1xxCan:
    class Type(ctypes.Structure):
        """ the structure available in :
                stm32f103xb
                stm32f103xe
                stm32f103xg
        """

        _fields_ = [
            ("MCR"            , ctypes.c_uint32),         #
            ("MSR"            , ctypes.c_uint32),         #
            ("TSR"            , ctypes.c_uint32),         #
            ("RF0R"           , ctypes.c_uint32),         #
            ("RF1R"           , ctypes.c_uint32),         #
            ("IER"            , ctypes.c_uint32),         #
            ("ESR"            , ctypes.c_uint32),         #
            ("BTR"            , ctypes.c_uint32),         #
            ("RESERVED0"      , ctypes.c_uint32 * 88),    #
            ("sTxMailBox"     , CAN_TxMailBox * 3),       #
            ("sFIFOMailBox"   , CAN_FIFOMailBox * 2),     #
            ("RESERVED1"      , ctypes.c_uint32 * 12),    #
            ("FMR"            , ctypes.c_uint32),         #
            ("FM1R"           , ctypes.c_uint32),         #
            ("RESERVED2"      , ctypes.c_uint32),         #
            ("FS1R"           , ctypes.c_uint32),         #
            ("RESERVED3"      , ctypes.c_uint32),         #
            ("FFA1R"          , ctypes.c_uint32),         #
            ("RESERVED4"      , ctypes.c_uint32),         #
            ("FA1R"           , ctypes.c_uint32),         #
            ("RESERVED5"      , ctypes.c_uint32 * 8),     #
            ("sFilterRegister", CAN_FilterRegister * 14), #
        ]

class STM32F1xxCanV1:
    class Type(ctypes.Structure):
        """ the structure available in :
                stm32f105xc
                stm32f107xc
        """

        _fields_ = [
            ("MCR"            , ctypes.c_uint32),         #
            ("MSR"            , ctypes.c_uint32),         #
            ("TSR"            , ctypes.c_uint32),         #
            ("RF0R"           , ctypes.c_uint32),         #
            ("RF1R"           , ctypes.c_uint32),         #
            ("IER"            , ctypes.c_uint32),         #
            ("ESR"            , ctypes.c_uint32),         #
            ("BTR"            , ctypes.c_uint32),         #
            ("RESERVED0"      , ctypes.c_uint32 * 88),    #
            ("sTxMailBox"     , CAN_TxMailBox * 3),       #
            ("sFIFOMailBox"   , CAN_FIFOMailBox * 2),     #
            ("RESERVED1"      , ctypes.c_uint32 * 12),    #
            ("FMR"            , ctypes.c_uint32),         #
            ("FM1R"           , ctypes.c_uint32),         #
            ("RESERVED2"      , ctypes.c_uint32),         #
            ("FS1R"           , ctypes.c_uint32),         #
            ("RESERVED3"      , ctypes.c_uint32),         #
            ("FFA1R"          , ctypes.c_uint32),         #
            ("RESERVED4"      , ctypes.c_uint32),         #
            ("FA1R"           , ctypes.c_uint32),         #
            ("RESERVED5"      , ctypes.c_uint32 * 8),     #
            ("sFilterRegister", CAN_FilterRegister * 28), #
        ]

class STM32F1xxSdio:
    class Type(ctypes.Structure):
        """ the structure available in :
                stm32f103xe
                stm32f103xg
        """

        _fields_ = [
            ("POWER"    , ctypes.c_uint32),      #
            ("CLKCR"    , ctypes.c_uint32),      #
            ("ARG"      , ctypes.c_uint32),      #
            ("CMD"      , ctypes.c_uint32),      #
            ("RESPCMD"  , ctypes.c_uint32),      #
            ("RESP1"    , ctypes.c_uint32),      #
            ("RESP2"    , ctypes.c_uint32),      #
            ("RESP3"    , ctypes.c_uint32),      #
            ("RESP4"    , ctypes.c_uint32),      #
            ("DTIMER"   , ctypes.c_uint32),      #
            ("DLEN"     , ctypes.c_uint32),      #
            ("DCTRL"    , ctypes.c_uint32),      #
            ("DCOUNT"   , ctypes.c_uint32),      #
            ("STA"      , ctypes.c_uint32),      #
            ("ICR"      , ctypes.c_uint32),      #
            ("MASK"     , ctypes.c_uint32),      #
            ("RESERVED0", ctypes.c_uint32 * 2),  #
            ("FIFOCNT"  , ctypes.c_uint32),      #
            ("RESERVED1", ctypes.c_uint32 * 13), #
            ("FIFO"     , ctypes.c_uint32),      #
        ]

class STM32F1xxUsb_otg_global:
    class Type(ctypes.Structure):
        """ the structure available in :
                stm32f105xc
                stm32f107xc
        """

        _fields_ = [
            ("GOTGCTL"           , ctypes.c_uint32),      #USB_OTG Control and Status Register       Address offset: 000h
            ("GOTGINT"           , ctypes.c_uint32),      #USB_OTG Interrupt Register                Address offset: 004h
            ("GAHBCFG"           , ctypes.c_uint32),      #Core AHB Configuration Register           Address offset: 008h
            ("GUSBCFG"           , ctypes.c_uint32),      #Core USB Configuration Register           Address offset: 00Ch
            ("GRSTCTL"           , ctypes.c_uint32),      #Core Reset Register                       Address offset: 010h
            ("GINTSTS"           , ctypes.c_uint32),      #Core Interrupt Register                   Address offset: 014h
            ("GINTMSK"           , ctypes.c_uint32),      #Core Interrupt Mask Register              Address offset: 018h
            ("GRXSTSR"           , ctypes.c_uint32),      #Receive Sts Q Read Register               Address offset: 01Ch
            ("GRXSTSP"           , ctypes.c_uint32),      #Receive Sts Q Read & POP Register         Address offset: 020h
            ("GRXFSIZ"           , ctypes.c_uint32),      #Receive FIFO Size Register                 Address offset: 024h
            ("DIEPTXF0_HNPTXFSIZ", ctypes.c_uint32),      #EP0 / Non Periodic Tx FIFO Size Register  Address offset: 028h
            ("HNPTXSTS"          , ctypes.c_uint32),      #Non Periodic Tx FIFO/Queue Sts reg        Address offset: 02Ch
            ("Reserved30"        , ctypes.c_uint32 * 2),  #Reserved 030h
            ("GCCFG"             , ctypes.c_uint32),      #General Purpose IO Register                Address offset: 038h
            ("CID"               , ctypes.c_uint32),      #User ID Register                           Address offset: 03Ch
            ("Reserved40"        , ctypes.c_uint32 * 48), #Reserved 040h-0FFh
            ("HPTXFSIZ"          , ctypes.c_uint32),      #Host Periodic Tx FIFO Size Reg             Address offset: 100h
            ("DIEPTXF"           , ctypes.c_uint32 * 15), #dev Periodic Transmit FIFO                 Address offset: 0x104
        ]

class STM32F1xxEth:
    class Type(ctypes.Structure):
        """ the structure available in :
                stm32f107xc
        """

        _fields_ = [
            ("MACCR"      , ctypes.c_uint32),       #
            ("MACFFR"     , ctypes.c_uint32),       #
            ("MACHTHR"    , ctypes.c_uint32),       #
            ("MACHTLR"    , ctypes.c_uint32),       #
            ("MACMIIAR"   , ctypes.c_uint32),       #
            ("MACMIIDR"   , ctypes.c_uint32),       #
            ("MACFCR"     , ctypes.c_uint32),       #
            ("MACVLANTR"  , ctypes.c_uint32),       #8
            ("RESERVED0"  , ctypes.c_uint32 * 2),   #
            ("MACRWUFFR"  , ctypes.c_uint32),       #11
            ("MACPMTCSR"  , ctypes.c_uint32),       #
            ("RESERVED1"  , ctypes.c_uint32 * 2),   #
            ("MACSR"      , ctypes.c_uint32),       #15
            ("MACIMR"     , ctypes.c_uint32),       #
            ("MACA0HR"    , ctypes.c_uint32),       #
            ("MACA0LR"    , ctypes.c_uint32),       #
            ("MACA1HR"    , ctypes.c_uint32),       #
            ("MACA1LR"    , ctypes.c_uint32),       #
            ("MACA2HR"    , ctypes.c_uint32),       #
            ("MACA2LR"    , ctypes.c_uint32),       #
            ("MACA3HR"    , ctypes.c_uint32),       #
            ("MACA3LR"    , ctypes.c_uint32),       #24
            ("RESERVED2"  , ctypes.c_uint32 * 40),  #
            ("MMCCR"      , ctypes.c_uint32),       #65
            ("MMCRIR"     , ctypes.c_uint32),       #
            ("MMCTIR"     , ctypes.c_uint32),       #
            ("MMCRIMR"    , ctypes.c_uint32),       #
            ("MMCTIMR"    , ctypes.c_uint32),       #69
            ("RESERVED3"  , ctypes.c_uint32 * 14),  #
            ("MMCTGFSCCR" , ctypes.c_uint32),       #84
            ("MMCTGFMSCCR", ctypes.c_uint32),       #
            ("RESERVED4"  , ctypes.c_uint32 * 5),   #
            ("MMCTGFCR"   , ctypes.c_uint32),       #
            ("RESERVED5"  , ctypes.c_uint32 * 10),  #
            ("MMCRFCECR"  , ctypes.c_uint32),       #
            ("MMCRFAECR"  , ctypes.c_uint32),       #
            ("RESERVED6"  , ctypes.c_uint32 * 10),  #
            ("MMCRGUFCR"  , ctypes.c_uint32),       #
            ("RESERVED7"  , ctypes.c_uint32 * 334), #
            ("PTPTSCR"    , ctypes.c_uint32),       #
            ("PTPSSIR"    , ctypes.c_uint32),       #
            ("PTPTSHR"    , ctypes.c_uint32),       #
            ("PTPTSLR"    , ctypes.c_uint32),       #
            ("PTPTSHUR"   , ctypes.c_uint32),       #
            ("PTPTSLUR"   , ctypes.c_uint32),       #
            ("PTPTSAR"    , ctypes.c_uint32),       #
            ("PTPTTHR"    , ctypes.c_uint32),       #
            ("PTPTTLR"    , ctypes.c_uint32),       #
            ("RESERVED8"  , ctypes.c_uint32 * 567), #
            ("DMABMR"     , ctypes.c_uint32),       #
            ("DMATPDR"    , ctypes.c_uint32),       #
            ("DMARPDR"    , ctypes.c_uint32),       #
            ("DMARDLAR"   , ctypes.c_uint32),       #
            ("DMATDLAR"   , ctypes.c_uint32),       #
            ("DMASR"      , ctypes.c_uint32),       #
            ("DMAOMR"     , ctypes.c_uint32),       #
            ("DMAIER"     , ctypes.c_uint32),       #
            ("DMAMFBOCR"  , ctypes.c_uint32),       #
            ("RESERVED9"  , ctypes.c_uint32 * 9),   #
            ("DMACHTDR"   , ctypes.c_uint32),       #
            ("DMACHRDR"   , ctypes.c_uint32),       #
            ("DMACHTBAR"  , ctypes.c_uint32),       #
            ("DMACHRBAR"  , ctypes.c_uint32),       #
        ]

