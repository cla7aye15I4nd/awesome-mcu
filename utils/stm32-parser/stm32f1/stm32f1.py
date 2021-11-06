import ctypes

class STM32F4xxAdc:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f101xg.h
		        stm32f103xe.h
		        stm32f107xc.h
		        stm32f103xg.h
		        stm32f105xc.h
		        stm32f102xb.h
		        stm32f100xe.h
		        stm32f100xb.h
		        stm32f101xb.h
		        stm32f101xe.h
		        stm32f103xb.h 
		"""

        _fields_ = [
			('SR'   , ctypes.c_uint32), 
			('CR1'  , ctypes.c_uint32), 
			('CR2'  , ctypes.c_uint32), 
			('SMPR1', ctypes.c_uint32), 
			('SMPR2', ctypes.c_uint32), 
			('JOFR1', ctypes.c_uint32), 
			('JOFR2', ctypes.c_uint32), 
			('JOFR3', ctypes.c_uint32), 
			('JOFR4', ctypes.c_uint32), 
			('HTR'  , ctypes.c_uint32), 
			('LTR'  , ctypes.c_uint32), 
			('SQR1' , ctypes.c_uint32), 
			('SQR2' , ctypes.c_uint32), 
			('SQR3' , ctypes.c_uint32), 
			('JSQR' , ctypes.c_uint32), 
			('JDR1' , ctypes.c_uint32), 
			('JDR2' , ctypes.c_uint32), 
			('JDR3' , ctypes.c_uint32), 
			('JDR4' , ctypes.c_uint32), 
			('DR'   , ctypes.c_uint32), 
		]

class STM32F4xxAdc_common:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f101xg.h
		        stm32f103xe.h
		        stm32f107xc.h
		        stm32f103xg.h
		        stm32f105xc.h
		        stm32f102xb.h
		        stm32f100xe.h
		        stm32f100xb.h
		        stm32f101xb.h
		        stm32f101xe.h
		        stm32f103xb.h 
		"""

        _fields_ = [
			('SR'      , ctypes.c_uint32),       # ADC status register,    used for ADC multimode (bits common to several ADC instances). Address offset: ADC1 base address
			('CR1'     , ctypes.c_uint32),       # ADC control register 1, used for ADC multimode (bits common to several ADC instances). Address offset: ADC1 base address + 0x04
			('CR2'     , ctypes.c_uint32),       # ADC control register 2, used for ADC multimode (bits common to several ADC instances). Address offset: ADC1 base address + 0x08
			('RESERVED', ctypes.c_uint32 * 16), 
			('DR'      , ctypes.c_uint32),       # ADC data register,      used for ADC multimode (bits common to several ADC instances). Address offset: ADC1 base address + 0x4C
		]

class STM32F4xxBkpV1:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f101xg.h
		        stm32f103xe.h
		        stm32f107xc.h
		        stm32f103xg.h
		        stm32f105xc.h
		        stm32f100xe.h
		        stm32f101xe.h 
		"""

        _fields_ = [
			('RESERVED0' , ctypes.c_uint32),     
			('DR1'       , ctypes.c_uint32),     
			('DR2'       , ctypes.c_uint32),     
			('DR3'       , ctypes.c_uint32),     
			('DR4'       , ctypes.c_uint32),     
			('DR5'       , ctypes.c_uint32),     
			('DR6'       , ctypes.c_uint32),     
			('DR7'       , ctypes.c_uint32),     
			('DR8'       , ctypes.c_uint32),     
			('DR9'       , ctypes.c_uint32),     
			('DR10'      , ctypes.c_uint32),     
			('RTCCR'     , ctypes.c_uint32),     
			('CR'        , ctypes.c_uint32),     
			('CSR'       , ctypes.c_uint32),     
			('RESERVED13', ctypes.c_uint32 * 2), 
			('DR11'      , ctypes.c_uint32),     
			('DR12'      , ctypes.c_uint32),     
			('DR13'      , ctypes.c_uint32),     
			('DR14'      , ctypes.c_uint32),     
			('DR15'      , ctypes.c_uint32),     
			('DR16'      , ctypes.c_uint32),     
			('DR17'      , ctypes.c_uint32),     
			('DR18'      , ctypes.c_uint32),     
			('DR19'      , ctypes.c_uint32),     
			('DR20'      , ctypes.c_uint32),     
			('DR21'      , ctypes.c_uint32),     
			('DR22'      , ctypes.c_uint32),     
			('DR23'      , ctypes.c_uint32),     
			('DR24'      , ctypes.c_uint32),     
			('DR25'      , ctypes.c_uint32),     
			('DR26'      , ctypes.c_uint32),     
			('DR27'      , ctypes.c_uint32),     
			('DR28'      , ctypes.c_uint32),     
			('DR29'      , ctypes.c_uint32),     
			('DR30'      , ctypes.c_uint32),     
			('DR31'      , ctypes.c_uint32),     
			('DR32'      , ctypes.c_uint32),     
			('DR33'      , ctypes.c_uint32),     
			('DR34'      , ctypes.c_uint32),     
			('DR35'      , ctypes.c_uint32),     
			('DR36'      , ctypes.c_uint32),     
			('DR37'      , ctypes.c_uint32),     
			('DR38'      , ctypes.c_uint32),     
			('DR39'      , ctypes.c_uint32),     
			('DR40'      , ctypes.c_uint32),     
			('DR41'      , ctypes.c_uint32),     
			('DR42'      , ctypes.c_uint32),     
		]

class STM32F4xxBkp:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f102xb.h
		        stm32f100xb.h
		        stm32f101xb.h
		        stm32f103xb.h 
		"""

        _fields_ = [
			('RESERVED0', ctypes.c_uint32), 
			('DR1'      , ctypes.c_uint32), 
			('DR2'      , ctypes.c_uint32), 
			('DR3'      , ctypes.c_uint32), 
			('DR4'      , ctypes.c_uint32), 
			('DR5'      , ctypes.c_uint32), 
			('DR6'      , ctypes.c_uint32), 
			('DR7'      , ctypes.c_uint32), 
			('DR8'      , ctypes.c_uint32), 
			('DR9'      , ctypes.c_uint32), 
			('DR10'     , ctypes.c_uint32), 
			('RTCCR'    , ctypes.c_uint32), 
			('CR'       , ctypes.c_uint32), 
			('CSR'      , ctypes.c_uint32), 
		]

class STM32F4xxCrc:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f101xg.h
		        stm32f103xe.h
		        stm32f107xc.h
		        stm32f103xg.h
		        stm32f105xc.h
		        stm32f102xb.h
		        stm32f100xe.h
		        stm32f100xb.h
		        stm32f101xb.h
		        stm32f101xe.h
		        stm32f103xb.h 
		"""

        _fields_ = [
			('DR'       , ctypes.c_uint32),  # CRC Data register,                           Address offset: 0x00
			('IDR'      , ctypes.c_uint8),   # CRC Independent data register,               Address offset: 0x04
			('RESERVED0', ctypes.c_uint8),   # Reserved,                                    Address offset: 0x05
			('RESERVED1', ctypes.c_uint8),   # Reserved,                                    Address offset: 0x06
			('CR'       , ctypes.c_uint32),  # CRC Control register,                        Address offset: 0x08
		]

class STM32F4xxDacV1:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f101xg.h
		        stm32f103xe.h
		        stm32f107xc.h
		        stm32f103xg.h
		        stm32f105xc.h
		        stm32f101xe.h 
		"""

        _fields_ = [
			('CR'     , ctypes.c_uint32), 
			('SWTRIGR', ctypes.c_uint32), 
			('DHR12R1', ctypes.c_uint32), 
			('DHR12L1', ctypes.c_uint32), 
			('DHR8R1' , ctypes.c_uint32), 
			('DHR12R2', ctypes.c_uint32), 
			('DHR12L2', ctypes.c_uint32), 
			('DHR8R2' , ctypes.c_uint32), 
			('DHR12RD', ctypes.c_uint32), 
			('DHR12LD', ctypes.c_uint32), 
			('DHR8RD' , ctypes.c_uint32), 
			('DOR1'   , ctypes.c_uint32), 
			('DOR2'   , ctypes.c_uint32), 
		]

class STM32F4xxDacV2:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f100xe.h
		        stm32f100xb.h 
		"""

        _fields_ = [
			('CR'     , ctypes.c_uint32), 
			('SWTRIGR', ctypes.c_uint32), 
			('DHR12R1', ctypes.c_uint32), 
			('DHR12L1', ctypes.c_uint32), 
			('DHR8R1' , ctypes.c_uint32), 
			('DHR12R2', ctypes.c_uint32), 
			('DHR12L2', ctypes.c_uint32), 
			('DHR8R2' , ctypes.c_uint32), 
			('DHR12RD', ctypes.c_uint32), 
			('DHR12LD', ctypes.c_uint32), 
			('DHR8RD' , ctypes.c_uint32), 
			('DOR1'   , ctypes.c_uint32), 
			('DOR2'   , ctypes.c_uint32), 
			('SR'     , ctypes.c_uint32), 
		]

class STM32F4xxDbgmcu:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f101xg.h
		        stm32f103xe.h
		        stm32f107xc.h
		        stm32f103xg.h
		        stm32f105xc.h
		        stm32f102xb.h
		        stm32f100xe.h
		        stm32f100xb.h
		        stm32f101xb.h
		        stm32f101xe.h
		        stm32f103xb.h 
		"""

        _fields_ = [
			('IDCODE', ctypes.c_uint32), 
			('CR'    , ctypes.c_uint32), 
		]

class STM32F4xxDma_channel:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f101xg.h
		        stm32f103xe.h
		        stm32f107xc.h
		        stm32f103xg.h
		        stm32f105xc.h
		        stm32f102xb.h
		        stm32f100xe.h
		        stm32f100xb.h
		        stm32f101xb.h
		        stm32f101xe.h
		        stm32f103xb.h 
		"""

        _fields_ = [
			('CCR'  , ctypes.c_uint32), 
			('CNDTR', ctypes.c_uint32), 
			('CPAR' , ctypes.c_uint32), 
			('CMAR' , ctypes.c_uint32), 
		]

class STM32F4xxDma:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f101xg.h
		        stm32f103xe.h
		        stm32f107xc.h
		        stm32f103xg.h
		        stm32f105xc.h
		        stm32f102xb.h
		        stm32f100xe.h
		        stm32f100xb.h
		        stm32f101xb.h
		        stm32f101xe.h
		        stm32f103xb.h 
		"""

        _fields_ = [
			('ISR' , ctypes.c_uint32), 
			('IFCR', ctypes.c_uint32), 
		]

class STM32F4xxExti:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f101xg.h
		        stm32f103xe.h
		        stm32f107xc.h
		        stm32f103xg.h
		        stm32f105xc.h
		        stm32f102xb.h
		        stm32f100xe.h
		        stm32f100xb.h
		        stm32f101xb.h
		        stm32f101xe.h
		        stm32f103xb.h 
		"""

        _fields_ = [
			('IMR'  , ctypes.c_uint32), 
			('EMR'  , ctypes.c_uint32), 
			('RTSR' , ctypes.c_uint32), 
			('FTSR' , ctypes.c_uint32), 
			('SWIER', ctypes.c_uint32), 
			('PR'   , ctypes.c_uint32), 
		]

class STM32F4xxFlashV1:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f101xg.h
		        stm32f103xg.h 
		"""

        _fields_ = [
			('ACR'      , ctypes.c_uint32),     
			('KEYR'     , ctypes.c_uint32),     
			('OPTKEYR'  , ctypes.c_uint32),     
			('SR'       , ctypes.c_uint32),     
			('CR'       , ctypes.c_uint32),     
			('AR'       , ctypes.c_uint32),     
			('RESERVED' , ctypes.c_uint32),     
			('OBR'      , ctypes.c_uint32),     
			('WRPR'     , ctypes.c_uint32),     
			('RESERVED1', ctypes.c_uint32 * 8), 
			('KEYR2'    , ctypes.c_uint32),     
			('RESERVED2', ctypes.c_uint32),     
			('SR2'      , ctypes.c_uint32),     
			('CR2'      , ctypes.c_uint32),     
			('AR2'      , ctypes.c_uint32),     
		]

class STM32F4xxFlash:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f103xe.h
		        stm32f107xc.h
		        stm32f105xc.h
		        stm32f102xb.h
		        stm32f100xe.h
		        stm32f100xb.h
		        stm32f101xb.h
		        stm32f101xe.h
		        stm32f103xb.h 
		"""

        _fields_ = [
			('ACR'     , ctypes.c_uint32), 
			('KEYR'    , ctypes.c_uint32), 
			('OPTKEYR' , ctypes.c_uint32), 
			('SR'      , ctypes.c_uint32), 
			('CR'      , ctypes.c_uint32), 
			('AR'      , ctypes.c_uint32), 
			('RESERVED', ctypes.c_uint32), 
			('OBR'     , ctypes.c_uint32), 
			('WRPR'    , ctypes.c_uint32), 
		]

class STM32F4xxOb:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f101xg.h
		        stm32f103xe.h
		        stm32f107xc.h
		        stm32f103xg.h
		        stm32f105xc.h
		        stm32f102xb.h
		        stm32f100xe.h
		        stm32f100xb.h
		        stm32f101xb.h
		        stm32f101xe.h
		        stm32f103xb.h 
		"""

        _fields_ = [
			('RDP'  , ctypes.c_uint8), 
			('USER' , ctypes.c_uint8), 
			('Data0', ctypes.c_uint8), 
			('Data1', ctypes.c_uint8), 
			('WRP0' , ctypes.c_uint8), 
			('WRP1' , ctypes.c_uint8), 
			('WRP2' , ctypes.c_uint8), 
			('WRP3' , ctypes.c_uint8), 
		]

class STM32F4xxFsmc_bank1:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f101xg.h
		        stm32f103xe.h
		        stm32f103xg.h
		        stm32f100xe.h
		        stm32f101xe.h 
		"""

        _fields_ = [
			('BTCR', ctypes.c_uint32 * 8), 
		]

class STM32F4xxFsmc_bank1e:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f101xg.h
		        stm32f103xe.h
		        stm32f103xg.h
		        stm32f100xe.h
		        stm32f101xe.h 
		"""

        _fields_ = [
			('BWTR', ctypes.c_uint32 * 7), 
		]

class STM32F4xxFsmc_bank2_3:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f101xg.h
		        stm32f103xe.h
		        stm32f103xg.h
		        stm32f101xe.h 
		"""

        _fields_ = [
			('PCR2'     , ctypes.c_uint32),  # NAND Flash control register 2,                       Address offset: 0x60
			('SR2'      , ctypes.c_uint32),  # NAND Flash FIFO status and interrupt register 2,     Address offset: 0x64
			('PMEM2'    , ctypes.c_uint32),  # NAND Flash Common memory space timing register 2,    Address offset: 0x68
			('PATT2'    , ctypes.c_uint32),  # NAND Flash Attribute memory space timing register 2, Address offset: 0x6C
			('RESERVED0', ctypes.c_uint32),  # Reserved, 0x70
			('ECCR2'    , ctypes.c_uint32),  # NAND Flash ECC result registers 2,                   Address offset: 0x74
			('RESERVED1', ctypes.c_uint32),  # Reserved, 0x78
			('RESERVED2', ctypes.c_uint32),  # Reserved, 0x7C
			('PCR3'     , ctypes.c_uint32),  # NAND Flash control register 3,                       Address offset: 0x80
			('SR3'      , ctypes.c_uint32),  # NAND Flash FIFO status and interrupt register 3,     Address offset: 0x84
			('PMEM3'    , ctypes.c_uint32),  # NAND Flash Common memory space timing register 3,    Address offset: 0x88
			('PATT3'    , ctypes.c_uint32),  # NAND Flash Attribute memory space timing register 3, Address offset: 0x8C
			('RESERVED3', ctypes.c_uint32),  # Reserved, 0x90
			('ECCR3'    , ctypes.c_uint32),  # NAND Flash ECC result registers 3,                   Address offset: 0x94
		]

class STM32F4xxFsmc_bank4:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f101xg.h
		        stm32f103xe.h
		        stm32f103xg.h
		        stm32f101xe.h 
		"""

        _fields_ = [
			('PCR4' , ctypes.c_uint32), 
			('SR4'  , ctypes.c_uint32), 
			('PMEM4', ctypes.c_uint32), 
			('PATT4', ctypes.c_uint32), 
			('PIO4' , ctypes.c_uint32), 
		]

class STM32F4xxGpio:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f101xg.h
		        stm32f103xe.h
		        stm32f107xc.h
		        stm32f103xg.h
		        stm32f105xc.h
		        stm32f102xb.h
		        stm32f100xe.h
		        stm32f100xb.h
		        stm32f101xb.h
		        stm32f101xe.h
		        stm32f103xb.h 
		"""

        _fields_ = [
			('CRL' , ctypes.c_uint32), 
			('CRH' , ctypes.c_uint32), 
			('IDR' , ctypes.c_uint32), 
			('ODR' , ctypes.c_uint32), 
			('BSRR', ctypes.c_uint32), 
			('BRR' , ctypes.c_uint32), 
			('LCKR', ctypes.c_uint32), 
		]

class STM32F4xxAfio:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f101xg.h
		        stm32f103xe.h
		        stm32f107xc.h
		        stm32f103xg.h
		        stm32f105xc.h
		        stm32f102xb.h
		        stm32f100xe.h
		        stm32f100xb.h
		        stm32f101xb.h
		        stm32f101xe.h
		        stm32f103xb.h 
		"""

        _fields_ = [
			('EVCR'     , ctypes.c_uint32),     
			('MAPR'     , ctypes.c_uint32),     
			('EXTICR'   , ctypes.c_uint32 * 4), 
			('RESERVED0', ctypes.c_uint32),     
			('MAPR2'    , ctypes.c_uint32),     
		]

class STM32F4xxI2c:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f101xg.h
		        stm32f103xe.h
		        stm32f107xc.h
		        stm32f103xg.h
		        stm32f105xc.h
		        stm32f102xb.h
		        stm32f100xe.h
		        stm32f100xb.h
		        stm32f101xb.h
		        stm32f101xe.h
		        stm32f103xb.h 
		"""

        _fields_ = [
			('CR1'  , ctypes.c_uint32), 
			('CR2'  , ctypes.c_uint32), 
			('OAR1' , ctypes.c_uint32), 
			('OAR2' , ctypes.c_uint32), 
			('DR'   , ctypes.c_uint32), 
			('SR1'  , ctypes.c_uint32), 
			('SR2'  , ctypes.c_uint32), 
			('CCR'  , ctypes.c_uint32), 
			('TRISE', ctypes.c_uint32), 
		]

class STM32F4xxIwdg:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f101xg.h
		        stm32f103xe.h
		        stm32f107xc.h
		        stm32f103xg.h
		        stm32f105xc.h
		        stm32f102xb.h
		        stm32f100xe.h
		        stm32f100xb.h
		        stm32f101xb.h
		        stm32f101xe.h
		        stm32f103xb.h 
		"""

        _fields_ = [
			('KR' , ctypes.c_uint32),  # Key register,                                Address offset: 0x00
			('PR' , ctypes.c_uint32),  # Prescaler register,                          Address offset: 0x04
			('RLR', ctypes.c_uint32),  # Reload register,                             Address offset: 0x08
			('SR' , ctypes.c_uint32),  # Status register,                             Address offset: 0x0C
		]

class STM32F4xxPwr:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f101xg.h
		        stm32f103xe.h
		        stm32f107xc.h
		        stm32f103xg.h
		        stm32f105xc.h
		        stm32f102xb.h
		        stm32f100xe.h
		        stm32f100xb.h
		        stm32f101xb.h
		        stm32f101xe.h
		        stm32f103xb.h 
		"""

        _fields_ = [
			('CR' , ctypes.c_uint32), 
			('CSR', ctypes.c_uint32), 
		]

class STM32F4xxRcc:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f101xg.h
		        stm32f103xe.h
		        stm32f103xg.h
		        stm32f102xb.h
		        stm32f101xb.h
		        stm32f101xe.h
		        stm32f103xb.h 
		"""

        _fields_ = [
			('CR'      , ctypes.c_uint32), 
			('CFGR'    , ctypes.c_uint32), 
			('CIR'     , ctypes.c_uint32), 
			('APB2RSTR', ctypes.c_uint32), 
			('APB1RSTR', ctypes.c_uint32), 
			('AHBENR'  , ctypes.c_uint32), 
			('APB2ENR' , ctypes.c_uint32), 
			('APB1ENR' , ctypes.c_uint32), 
			('BDCR'    , ctypes.c_uint32), 
			('CSR'     , ctypes.c_uint32), 
		]

class STM32F4xxRccV1:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f107xc.h
		        stm32f105xc.h 
		"""

        _fields_ = [
			('CR'      , ctypes.c_uint32), 
			('CFGR'    , ctypes.c_uint32), 
			('CIR'     , ctypes.c_uint32), 
			('APB2RSTR', ctypes.c_uint32), 
			('APB1RSTR', ctypes.c_uint32), 
			('AHBENR'  , ctypes.c_uint32), 
			('APB2ENR' , ctypes.c_uint32), 
			('APB1ENR' , ctypes.c_uint32), 
			('BDCR'    , ctypes.c_uint32), 
			('CSR'     , ctypes.c_uint32), 
			('AHBRSTR' , ctypes.c_uint32), 
			('CFGR2'   , ctypes.c_uint32), 
		]

class STM32F4xxRccV2:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f100xe.h
		        stm32f100xb.h 
		"""

        _fields_ = [
			('CR'       , ctypes.c_uint32), 
			('CFGR'     , ctypes.c_uint32), 
			('CIR'      , ctypes.c_uint32), 
			('APB2RSTR' , ctypes.c_uint32), 
			('APB1RSTR' , ctypes.c_uint32), 
			('AHBENR'   , ctypes.c_uint32), 
			('APB2ENR'  , ctypes.c_uint32), 
			('APB1ENR'  , ctypes.c_uint32), 
			('BDCR'     , ctypes.c_uint32), 
			('CSR'      , ctypes.c_uint32), 
			('RESERVED0', ctypes.c_uint32), 
			('CFGR2'    , ctypes.c_uint32), 
		]

class STM32F4xxRtc:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f101xg.h
		        stm32f103xe.h
		        stm32f107xc.h
		        stm32f103xg.h
		        stm32f105xc.h
		        stm32f102xb.h
		        stm32f100xe.h
		        stm32f100xb.h
		        stm32f101xb.h
		        stm32f101xe.h
		        stm32f103xb.h 
		"""

        _fields_ = [
			('CRH' , ctypes.c_uint32), 
			('CRL' , ctypes.c_uint32), 
			('PRLH', ctypes.c_uint32), 
			('PRLL', ctypes.c_uint32), 
			('DIVH', ctypes.c_uint32), 
			('DIVL', ctypes.c_uint32), 
			('CNTH', ctypes.c_uint32), 
			('CNTL', ctypes.c_uint32), 
			('ALRH', ctypes.c_uint32), 
			('ALRL', ctypes.c_uint32), 
		]

class STM32F4xxSpiV1:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f101xg.h
		        stm32f103xe.h
		        stm32f107xc.h
		        stm32f103xg.h
		        stm32f105xc.h
		        stm32f101xe.h 
		"""

        _fields_ = [
			('CR1'    , ctypes.c_uint32), 
			('CR2'    , ctypes.c_uint32), 
			('SR'     , ctypes.c_uint32), 
			('DR'     , ctypes.c_uint32), 
			('CRCPR'  , ctypes.c_uint32), 
			('RXCRCR' , ctypes.c_uint32), 
			('TXCRCR' , ctypes.c_uint32), 
			('I2SCFGR', ctypes.c_uint32), 
			('I2SPR'  , ctypes.c_uint32), 
		]

class STM32F4xxSpi:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f102xb.h
		        stm32f101xb.h
		        stm32f103xb.h 
		"""

        _fields_ = [
			('CR1'    , ctypes.c_uint32), 
			('CR2'    , ctypes.c_uint32), 
			('SR'     , ctypes.c_uint32), 
			('DR'     , ctypes.c_uint32), 
			('CRCPR'  , ctypes.c_uint32), 
			('RXCRCR' , ctypes.c_uint32), 
			('TXCRCR' , ctypes.c_uint32), 
			('I2SCFGR', ctypes.c_uint32), 
		]

class STM32F4xxSpiV2:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f100xe.h
		        stm32f100xb.h 
		"""

        _fields_ = [
			('CR1'   , ctypes.c_uint32), 
			('CR2'   , ctypes.c_uint32), 
			('SR'    , ctypes.c_uint32), 
			('DR'    , ctypes.c_uint32), 
			('CRCPR' , ctypes.c_uint32), 
			('RXCRCR', ctypes.c_uint32), 
			('TXCRCR', ctypes.c_uint32), 
		]

class STM32F4xxTim:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f101xg.h
		        stm32f103xe.h
		        stm32f107xc.h
		        stm32f103xg.h
		        stm32f105xc.h
		        stm32f102xb.h
		        stm32f100xe.h
		        stm32f100xb.h
		        stm32f101xb.h
		        stm32f101xe.h
		        stm32f103xb.h 
		"""

        _fields_ = [
			('CR1'  , ctypes.c_uint32),  # TIM control register 1,                      Address offset: 0x00
			('CR2'  , ctypes.c_uint32),  # TIM control register 2,                      Address offset: 0x04
			('SMCR' , ctypes.c_uint32),  # TIM slave Mode Control register,             Address offset: 0x08
			('DIER' , ctypes.c_uint32),  # TIM DMA/interrupt enable register,           Address offset: 0x0C
			('SR'   , ctypes.c_uint32),  # TIM status register,                         Address offset: 0x10
			('EGR'  , ctypes.c_uint32),  # TIM event generation register,               Address offset: 0x14
			('CCMR1', ctypes.c_uint32),  # TIM  capture/compare mode register 1,        Address offset: 0x18
			('CCMR2', ctypes.c_uint32),  # TIM  capture/compare mode register 2,        Address offset: 0x1C
			('CCER' , ctypes.c_uint32),  # TIM capture/compare enable register,         Address offset: 0x20
			('CNT'  , ctypes.c_uint32),  # TIM counter register,                        Address offset: 0x24
			('PSC'  , ctypes.c_uint32),  # TIM prescaler register,                      Address offset: 0x28
			('ARR'  , ctypes.c_uint32),  # TIM auto-reload register,                    Address offset: 0x2C
			('RCR'  , ctypes.c_uint32),  # TIM  repetition counter register,            Address offset: 0x30
			('CCR1' , ctypes.c_uint32),  # TIM capture/compare register 1,              Address offset: 0x34
			('CCR2' , ctypes.c_uint32),  # TIM capture/compare register 2,              Address offset: 0x38
			('CCR3' , ctypes.c_uint32),  # TIM capture/compare register 3,              Address offset: 0x3C
			('CCR4' , ctypes.c_uint32),  # TIM capture/compare register 4,              Address offset: 0x40
			('BDTR' , ctypes.c_uint32),  # TIM break and dead-time register,            Address offset: 0x44
			('DCR'  , ctypes.c_uint32),  # TIM DMA control register,                    Address offset: 0x48
			('DMAR' , ctypes.c_uint32),  # TIM DMA address for full transfer register,  Address offset: 0x4C
			('OR'   , ctypes.c_uint32),  # TIM option register,                         Address offset: 0x50
		]

class STM32F4xxUsart:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f101xg.h
		        stm32f103xe.h
		        stm32f107xc.h
		        stm32f103xg.h
		        stm32f105xc.h
		        stm32f102xb.h
		        stm32f100xe.h
		        stm32f100xb.h
		        stm32f101xb.h
		        stm32f101xe.h
		        stm32f103xb.h 
		"""

        _fields_ = [
			('SR'  , ctypes.c_uint32),  # USART Status register,                   Address offset: 0x00
			('DR'  , ctypes.c_uint32),  # USART Data register,                     Address offset: 0x04
			('BRR' , ctypes.c_uint32),  # USART Baud rate register,                Address offset: 0x08
			('CR1' , ctypes.c_uint32),  # USART Control register 1,                Address offset: 0x0C
			('CR2' , ctypes.c_uint32),  # USART Control register 2,                Address offset: 0x10
			('CR3' , ctypes.c_uint32),  # USART Control register 3,                Address offset: 0x14
			('GTPR', ctypes.c_uint32),  # USART Guard time and prescaler register, Address offset: 0x18
		]

class STM32F4xxWwdg:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f101xg.h
		        stm32f103xe.h
		        stm32f107xc.h
		        stm32f103xg.h
		        stm32f105xc.h
		        stm32f102xb.h
		        stm32f100xe.h
		        stm32f100xb.h
		        stm32f101xb.h
		        stm32f101xe.h
		        stm32f103xb.h 
		"""

        _fields_ = [
			('CR' , ctypes.c_uint32),  # WWDG Control register,       Address offset: 0x00
			('CFR', ctypes.c_uint32),  # WWDG Configuration register, Address offset: 0x04
			('SR' , ctypes.c_uint32),  # WWDG Status register,        Address offset: 0x08
		]

class STM32F4xxCan_txmailbox:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f103xe.h
		        stm32f107xc.h
		        stm32f103xg.h
		        stm32f105xc.h
		        stm32f103xb.h 
		"""

        _fields_ = [
			('TIR' , ctypes.c_uint32), 
			('TDTR', ctypes.c_uint32), 
			('TDLR', ctypes.c_uint32), 
			('TDHR', ctypes.c_uint32), 
		]

class STM32F4xxCan_fifomailbox:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f103xe.h
		        stm32f107xc.h
		        stm32f103xg.h
		        stm32f105xc.h
		        stm32f103xb.h 
		"""

        _fields_ = [
			('RIR' , ctypes.c_uint32), 
			('RDTR', ctypes.c_uint32), 
			('RDLR', ctypes.c_uint32), 
			('RDHR', ctypes.c_uint32), 
		]

class STM32F4xxCan_filterregister:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f103xe.h
		        stm32f107xc.h
		        stm32f103xg.h
		        stm32f105xc.h
		        stm32f103xb.h 
		"""

        _fields_ = [
			('FR1', ctypes.c_uint32), 
			('FR2', ctypes.c_uint32), 
		]

class STM32F4xxCan:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f103xe.h
		        stm32f103xg.h
		        stm32f103xb.h 
		"""

        _fields_ = [
			('MCR'            , ctypes.c_uint32),                      
			('MSR'            , ctypes.c_uint32),                      
			('TSR'            , ctypes.c_uint32),                      
			('RF0R'           , ctypes.c_uint32),                      
			('RF1R'           , ctypes.c_uint32),                      
			('IER'            , ctypes.c_uint32),                      
			('ESR'            , ctypes.c_uint32),                      
			('BTR'            , ctypes.c_uint32),                      
			('RESERVED0'      , ctypes.c_uint32 * 88),                 
			('sTxMailBox'     , CAN_TxMailBox_TypeDef.Type * 3),       
			('sFIFOMailBox'   , CAN_FIFOMailBox_TypeDef.Type * 2),     
			('RESERVED1'      , ctypes.c_uint32 * 12),                 
			('FMR'            , ctypes.c_uint32),                      
			('FM1R'           , ctypes.c_uint32),                      
			('RESERVED2'      , ctypes.c_uint32),                      
			('FS1R'           , ctypes.c_uint32),                      
			('RESERVED3'      , ctypes.c_uint32),                      
			('FFA1R'          , ctypes.c_uint32),                      
			('RESERVED4'      , ctypes.c_uint32),                      
			('FA1R'           , ctypes.c_uint32),                      
			('RESERVED5'      , ctypes.c_uint32 * 8),                  
			('sFilterRegister', CAN_FilterRegister_TypeDef.Type * 14), 
		]

class STM32F4xxCanV1:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f107xc.h
		        stm32f105xc.h 
		"""

        _fields_ = [
			('MCR'            , ctypes.c_uint32),                      
			('MSR'            , ctypes.c_uint32),                      
			('TSR'            , ctypes.c_uint32),                      
			('RF0R'           , ctypes.c_uint32),                      
			('RF1R'           , ctypes.c_uint32),                      
			('IER'            , ctypes.c_uint32),                      
			('ESR'            , ctypes.c_uint32),                      
			('BTR'            , ctypes.c_uint32),                      
			('RESERVED0'      , ctypes.c_uint32 * 88),                 
			('sTxMailBox'     , CAN_TxMailBox_TypeDef.Type * 3),       
			('sFIFOMailBox'   , CAN_FIFOMailBox_TypeDef.Type * 2),     
			('RESERVED1'      , ctypes.c_uint32 * 12),                 
			('FMR'            , ctypes.c_uint32),                      
			('FM1R'           , ctypes.c_uint32),                      
			('RESERVED2'      , ctypes.c_uint32),                      
			('FS1R'           , ctypes.c_uint32),                      
			('RESERVED3'      , ctypes.c_uint32),                      
			('FFA1R'          , ctypes.c_uint32),                      
			('RESERVED4'      , ctypes.c_uint32),                      
			('FA1R'           , ctypes.c_uint32),                      
			('RESERVED5'      , ctypes.c_uint32 * 8),                  
			('sFilterRegister', CAN_FilterRegister_TypeDef.Type * 28), 
		]

class STM32F4xxSdio:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f103xe.h
		        stm32f103xg.h 
		"""

        _fields_ = [
			('POWER'           , ctypes.c_uint32),      
			('CLKCR'           , ctypes.c_uint32),      
			('ARG'             , ctypes.c_uint32),      
			('CMD'             , ctypes.c_uint32),      
			('uint32_t RESPCMD', __I.Type),             
			('uint32_t RESP1'  , __I.Type),             
			('uint32_t RESP2'  , __I.Type),             
			('uint32_t RESP3'  , __I.Type),             
			('uint32_t RESP4'  , __I.Type),             
			('DTIMER'          , ctypes.c_uint32),      
			('DLEN'            , ctypes.c_uint32),      
			('DCTRL'           , ctypes.c_uint32),      
			('uint32_t DCOUNT' , __I.Type),             
			('uint32_t STA'    , __I.Type),             
			('ICR'             , ctypes.c_uint32),      
			('MASK'            , ctypes.c_uint32),      
			('RESERVED0'       , ctypes.c_uint32 * 2),  
			('uint32_t FIFOCNT', __I.Type),             
			('RESERVED1'       , ctypes.c_uint32 * 13), 
			('FIFO'            , ctypes.c_uint32),      
		]

class STM32F4xxUsb:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f103xe.h
		        stm32f103xg.h
		        stm32f102xb.h
		        stm32f103xb.h 
		"""

        _fields_ = [
			('EP0R'     , ctypes.c_uint8),       # USB Endpoint 0 register,                   Address offset: 0x00
			('RESERVED0', ctypes.c_uint8),       # Reserved
			('EP1R'     , ctypes.c_uint8),       # USB Endpoint 1 register,                   Address offset: 0x04
			('RESERVED1', ctypes.c_uint8),       # Reserved
			('EP2R'     , ctypes.c_uint8),       # USB Endpoint 2 register,                   Address offset: 0x08
			('RESERVED2', ctypes.c_uint8),       # Reserved
			('EP3R'     , ctypes.c_uint8),       # USB Endpoint 3 register,                   Address offset: 0x0C
			('RESERVED3', ctypes.c_uint8),       # Reserved
			('EP4R'     , ctypes.c_uint8),       # USB Endpoint 4 register,                   Address offset: 0x10
			('RESERVED4', ctypes.c_uint8),       # Reserved
			('EP5R'     , ctypes.c_uint8),       # USB Endpoint 5 register,                   Address offset: 0x14
			('RESERVED5', ctypes.c_uint8),       # Reserved
			('EP6R'     , ctypes.c_uint8),       # USB Endpoint 6 register,                   Address offset: 0x18
			('RESERVED6', ctypes.c_uint8),       # Reserved
			('EP7R'     , ctypes.c_uint8),       # USB Endpoint 7 register,                   Address offset: 0x1C
			('RESERVED7', ctypes.c_uint8 * 17),  # Reserved
			('CNTR'     , ctypes.c_uint8),       # Control register,                          Address offset: 0x40
			('RESERVED8', ctypes.c_uint8),       # Reserved
			('ISTR'     , ctypes.c_uint8),       # Interrupt status register,                 Address offset: 0x44
			('RESERVED9', ctypes.c_uint8),       # Reserved
			('FNR'      , ctypes.c_uint8),       # Frame number register,                     Address offset: 0x48
			('RESERVEDA', ctypes.c_uint8),       # Reserved
			('DADDR'    , ctypes.c_uint8),       # Device address register,                   Address offset: 0x4C
			('RESERVEDB', ctypes.c_uint8),       # Reserved
			('BTABLE'   , ctypes.c_uint8),       # Buffer Table address register,             Address offset: 0x50
			('RESERVEDC', ctypes.c_uint8),       # Reserved
		]

class STM32F407Eth:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f107xc.h 
		"""

        _fields_ = [
			('MACCR'      , ctypes.c_uint32),       
			('MACFFR'     , ctypes.c_uint32),       
			('MACHTHR'    , ctypes.c_uint32),       
			('MACHTLR'    , ctypes.c_uint32),       
			('MACMIIAR'   , ctypes.c_uint32),       
			('MACMIIDR'   , ctypes.c_uint32),       
			('MACFCR'     , ctypes.c_uint32),       
			('MACVLANTR'  , ctypes.c_uint32),        # 8
			('RESERVED0'  , ctypes.c_uint32 * 2),   
			('MACRWUFFR'  , ctypes.c_uint32),        # 11
			('MACPMTCSR'  , ctypes.c_uint32),       
			('RESERVED1'  , ctypes.c_uint32 * 2),   
			('MACSR'      , ctypes.c_uint32),        # 15
			('MACIMR'     , ctypes.c_uint32),       
			('MACA0HR'    , ctypes.c_uint32),       
			('MACA0LR'    , ctypes.c_uint32),       
			('MACA1HR'    , ctypes.c_uint32),       
			('MACA1LR'    , ctypes.c_uint32),       
			('MACA2HR'    , ctypes.c_uint32),       
			('MACA2LR'    , ctypes.c_uint32),       
			('MACA3HR'    , ctypes.c_uint32),       
			('MACA3LR'    , ctypes.c_uint32),        # 24
			('RESERVED2'  , ctypes.c_uint32 * 40),  
			('MMCCR'      , ctypes.c_uint32),        # 65
			('MMCRIR'     , ctypes.c_uint32),       
			('MMCTIR'     , ctypes.c_uint32),       
			('MMCRIMR'    , ctypes.c_uint32),       
			('MMCTIMR'    , ctypes.c_uint32),        # 69
			('RESERVED3'  , ctypes.c_uint32 * 14),  
			('MMCTGFSCCR' , ctypes.c_uint32),        # 84
			('MMCTGFMSCCR', ctypes.c_uint32),       
			('RESERVED4'  , ctypes.c_uint32 * 5),   
			('MMCTGFCR'   , ctypes.c_uint32),       
			('RESERVED5'  , ctypes.c_uint32 * 10),  
			('MMCRFCECR'  , ctypes.c_uint32),       
			('MMCRFAECR'  , ctypes.c_uint32),       
			('RESERVED6'  , ctypes.c_uint32 * 10),  
			('MMCRGUFCR'  , ctypes.c_uint32),       
			('RESERVED7'  , ctypes.c_uint32 * 334), 
			('PTPTSCR'    , ctypes.c_uint32),       
			('PTPSSIR'    , ctypes.c_uint32),       
			('PTPTSHR'    , ctypes.c_uint32),       
			('PTPTSLR'    , ctypes.c_uint32),       
			('PTPTSHUR'   , ctypes.c_uint32),       
			('PTPTSLUR'   , ctypes.c_uint32),       
			('PTPTSAR'    , ctypes.c_uint32),       
			('PTPTTHR'    , ctypes.c_uint32),       
			('PTPTTLR'    , ctypes.c_uint32),       
			('RESERVED8'  , ctypes.c_uint32 * 567), 
			('DMABMR'     , ctypes.c_uint32),       
			('DMATPDR'    , ctypes.c_uint32),       
			('DMARPDR'    , ctypes.c_uint32),       
			('DMARDLAR'   , ctypes.c_uint32),       
			('DMATDLAR'   , ctypes.c_uint32),       
			('DMASR'      , ctypes.c_uint32),       
			('DMAOMR'     , ctypes.c_uint32),       
			('DMAIER'     , ctypes.c_uint32),       
			('DMAMFBOCR'  , ctypes.c_uint32),       
			('RESERVED9'  , ctypes.c_uint32 * 9),   
			('DMACHTDR'   , ctypes.c_uint32),       
			('DMACHRDR'   , ctypes.c_uint32),       
			('DMACHTBAR'  , ctypes.c_uint32),       
			('DMACHRBAR'  , ctypes.c_uint32),       
		]

class STM32F4xxUsb_otg_global:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f107xc.h
		        stm32f105xc.h 
		"""

        _fields_ = [
			('GOTGCTL'           , ctypes.c_uint32),       # USB_OTG Control and Status Register       Address offset: 000h
			('GOTGINT'           , ctypes.c_uint32),       # USB_OTG Interrupt Register                Address offset: 004h
			('GAHBCFG'           , ctypes.c_uint32),       # Core AHB Configuration Register           Address offset: 008h
			('GUSBCFG'           , ctypes.c_uint32),       # Core USB Configuration Register           Address offset: 00Ch
			('GRSTCTL'           , ctypes.c_uint32),       # Core Reset Register                       Address offset: 010h
			('GINTSTS'           , ctypes.c_uint32),       # Core Interrupt Register                   Address offset: 014h
			('GINTMSK'           , ctypes.c_uint32),       # Core Interrupt Mask Register              Address offset: 018h
			('GRXSTSR'           , ctypes.c_uint32),       # Receive Sts Q Read Register               Address offset: 01Ch
			('GRXSTSP'           , ctypes.c_uint32),       # Receive Sts Q Read & POP Register         Address offset: 020h
			('GRXFSIZ'           , ctypes.c_uint32),       # Receive FIFO Size Register                 Address offset: 024h
			('DIEPTXF0_HNPTXFSIZ', ctypes.c_uint32),       # EP0 / Non Periodic Tx FIFO Size Register  Address offset: 028h
			('HNPTXSTS'          , ctypes.c_uint32),       # Non Periodic Tx FIFO/Queue Sts reg        Address offset: 02Ch
			('Reserved30'        , ctypes.c_uint32 * 2),   # Reserved 030h
			('GCCFG'             , ctypes.c_uint32),       # General Purpose IO Register                Address offset: 038h
			('CID'               , ctypes.c_uint32),       # User ID Register                           Address offset: 03Ch
			('Reserved40'        , ctypes.c_uint32 * 48),  # Reserved 040h-0FFh
			('HPTXFSIZ'          , ctypes.c_uint32),       # Host Periodic Tx FIFO Size Reg             Address offset: 100h
			('DIEPTXF'           , ctypes.c_uint32 * 15),  # dev Periodic Transmit FIFO                 Address offset: 0x104
		]

class STM32F4xxUsb_otg_device:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f107xc.h
		        stm32f105xc.h 
		"""

        _fields_ = [
			('DCFG'      , ctypes.c_uint32),       # dev Configuration Register                 Address offset: 800h
			('DCTL'      , ctypes.c_uint32),       # dev Control Register                       Address offset: 804h
			('DSTS'      , ctypes.c_uint32),       # dev Status Register (RO)                   Address offset: 808h
			('Reserved0C', ctypes.c_uint32),       # Reserved 80Ch
			('DIEPMSK'   , ctypes.c_uint32),       # dev IN Endpoint Mask                       Address offset: 810h
			('DOEPMSK'   , ctypes.c_uint32),       # dev OUT Endpoint Mask                      Address offset: 814h
			('DAINT'     , ctypes.c_uint32),       # dev All Endpoints Itr Reg                  Address offset: 818h
			('DAINTMSK'  , ctypes.c_uint32),       # dev All Endpoints Itr Mask                 Address offset: 81Ch
			('Reserved20', ctypes.c_uint32),       # Reserved 820h
			('Reserved9' , ctypes.c_uint32),       # Reserved 824h
			('DVBUSDIS'  , ctypes.c_uint32),       # dev VBUS discharge Register                Address offset: 828h
			('DVBUSPULSE', ctypes.c_uint32),       # dev VBUS Pulse Register                    Address offset: 82Ch
			('DTHRCTL'   , ctypes.c_uint32),       # dev thr                                    Address offset: 830h
			('DIEPEMPMSK', ctypes.c_uint32),       # dev empty msk                              Address offset: 834h
			('DEACHINT'  , ctypes.c_uint32),       # dedicated EP interrupt                     Address offset: 838h
			('DEACHMSK'  , ctypes.c_uint32),       # dedicated EP msk                           Address offset: 83Ch
			('Reserved40', ctypes.c_uint32),       # dedicated EP mask                          Address offset: 840h
			('DINEP1MSK' , ctypes.c_uint32),       # dedicated EP mask                          Address offset: 844h
			('Reserved44', ctypes.c_uint32 * 15),  # Reserved 844-87Ch
			('DOUTEP1MSK', ctypes.c_uint32),       # dedicated EP msk                           Address offset: 884h
		]

class STM32F4xxUsb_otg_inendpoint:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f107xc.h
		        stm32f105xc.h 
		"""

        _fields_ = [
			('DIEPCTL'   , ctypes.c_uint32),  # dev IN Endpoint Control Reg                900h + (ep_num * 20h) + 00h
			('Reserved04', ctypes.c_uint32),  # Reserved                                   900h + (ep_num * 20h) + 04h
			('DIEPINT'   , ctypes.c_uint32),  # dev IN Endpoint Itr Reg                    900h + (ep_num * 20h) + 08h
			('Reserved0C', ctypes.c_uint32),  # Reserved                                   900h + (ep_num * 20h) + 0Ch
			('DIEPTSIZ'  , ctypes.c_uint32),  # IN Endpoint Txfer Size                     900h + (ep_num * 20h) + 10h
			('DIEPDMA'   , ctypes.c_uint32),  # IN Endpoint DMA Address Reg                900h + (ep_num * 20h) + 14h
			('DTXFSTS'   , ctypes.c_uint32),  # IN Endpoint Tx FIFO Status Reg             900h + (ep_num * 20h) + 18h
			('Reserved18', ctypes.c_uint32),  # Reserved                                   900h+(ep_num*20h)+1Ch-900h+ (ep_num * 20h) + 1Ch
		]

class STM32F4xxUsb_otg_outendpoint:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f107xc.h
		        stm32f105xc.h 
		"""

        _fields_ = [
			('DOEPCTL'   , ctypes.c_uint32),      # dev OUT Endpoint Control Reg               B00h + (ep_num * 20h) + 00h
			('Reserved04', ctypes.c_uint32),      # Reserved                                   B00h + (ep_num * 20h) + 04h
			('DOEPINT'   , ctypes.c_uint32),      # dev OUT Endpoint Itr Reg                   B00h + (ep_num * 20h) + 08h
			('Reserved0C', ctypes.c_uint32),      # Reserved                                   B00h + (ep_num * 20h) + 0Ch
			('DOEPTSIZ'  , ctypes.c_uint32),      # dev OUT Endpoint Txfer Size                B00h + (ep_num * 20h) + 10h
			('DOEPDMA'   , ctypes.c_uint32),      # dev OUT Endpoint DMA Address               B00h + (ep_num * 20h) + 14h
			('Reserved18', ctypes.c_uint32 * 2),  # Reserved                                   B00h + (ep_num * 20h) + 18h - B00h + (ep_num * 20h) + 1Ch
		]

class STM32F4xxUsb_otg_host:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f107xc.h
		        stm32f105xc.h 
		"""

        _fields_ = [
			('HCFG'       , ctypes.c_uint32),  # Host Configuration Register    400h
			('HFIR'       , ctypes.c_uint32),  # Host Frame Interval Register   404h
			('HFNUM'      , ctypes.c_uint32),  # Host Frame Nbr/Frame Remaining 408h
			('Reserved40C', ctypes.c_uint32),  # Reserved                       40Ch
			('HPTXSTS'    , ctypes.c_uint32),  # Host Periodic Tx FIFO/ Queue Status 410h
			('HAINT'      , ctypes.c_uint32),  # Host All Channels Interrupt Register 414h
			('HAINTMSK'   , ctypes.c_uint32),  # Host All Channels Interrupt Mask 418h
		]

class STM32F4xxUsb_otg_hostchannel:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f107xc.h
		        stm32f105xc.h 
		"""

        _fields_ = [
			('HCCHAR'  , ctypes.c_uint32),     
			('HCSPLT'  , ctypes.c_uint32),     
			('HCINT'   , ctypes.c_uint32),     
			('HCINTMSK', ctypes.c_uint32),     
			('HCTSIZ'  , ctypes.c_uint32),     
			('HCDMA'   , ctypes.c_uint32),     
			('Reserved', ctypes.c_uint32 * 2), 
		]

class STM32F4xxCec:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f100xe.h
		        stm32f100xb.h 
		"""

        _fields_ = [
			('CFGR', ctypes.c_uint32), 
			('OAR' , ctypes.c_uint32), 
			('PRES', ctypes.c_uint32), 
			('ESR' , ctypes.c_uint32), 
			('CSR' , ctypes.c_uint32), 
			('TXD' , ctypes.c_uint32), 
			('RXD' , ctypes.c_uint32), 
		]

