import ctypes

class STM32F4xxAdc:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f423xx.h
		        stm32f469xx.h
		        stm32f427xx.h
		        stm32f479xx.h
		        stm32f413xx.h
		        stm32f429xx.h
		        stm32f439xx.h
		        stm32f415xx.h
		        stm32f412cx.h
		        stm32f412rx.h
		        stm32f410tx.h
		        stm32f410cx.h
		        stm32f412zx.h
		        stm32f405xx.h
		        stm32f407xx.h
		        stm32f417xx.h
		        stm32f446xx.h
		        stm32f401xc.h
		        stm32f437xx.h
		        stm32f401xe.h
		        stm32f412vx.h
		        stm32f410rx.h
		        stm32f411xe.h 
		"""

        _fields_ = [
			('SR'   , ctypes.c_uint32),  # ADC status register,                         Address offset: 0x00
			('CR1'  , ctypes.c_uint32),  # ADC control register 1,                      Address offset: 0x04
			('CR2'  , ctypes.c_uint32),  # ADC control register 2,                      Address offset: 0x08
			('SMPR1', ctypes.c_uint32),  # ADC sample time register 1,                  Address offset: 0x0C
			('SMPR2', ctypes.c_uint32),  # ADC sample time register 2,                  Address offset: 0x10
			('JOFR1', ctypes.c_uint32),  # ADC injected channel data offset register 1, Address offset: 0x14
			('JOFR2', ctypes.c_uint32),  # ADC injected channel data offset register 2, Address offset: 0x18
			('JOFR3', ctypes.c_uint32),  # ADC injected channel data offset register 3, Address offset: 0x1C
			('JOFR4', ctypes.c_uint32),  # ADC injected channel data offset register 4, Address offset: 0x20
			('HTR'  , ctypes.c_uint32),  # ADC watchdog higher threshold register,      Address offset: 0x24
			('LTR'  , ctypes.c_uint32),  # ADC watchdog lower threshold register,       Address offset: 0x28
			('SQR1' , ctypes.c_uint32),  # ADC regular sequence register 1,             Address offset: 0x2C
			('SQR2' , ctypes.c_uint32),  # ADC regular sequence register 2,             Address offset: 0x30
			('SQR3' , ctypes.c_uint32),  # ADC regular sequence register 3,             Address offset: 0x34
			('JSQR' , ctypes.c_uint32),  # ADC injected sequence register,              Address offset: 0x38
			('JDR1' , ctypes.c_uint32),  # ADC injected data register 1,                Address offset: 0x3C
			('JDR2' , ctypes.c_uint32),  # ADC injected data register 2,                Address offset: 0x40
			('JDR3' , ctypes.c_uint32),  # ADC injected data register 3,                Address offset: 0x44
			('JDR4' , ctypes.c_uint32),  # ADC injected data register 4,                Address offset: 0x48
			('DR'   , ctypes.c_uint32),  # ADC regular data register,                   Address offset: 0x4C
		]

class STM32F4xxAdc_common:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f423xx.h
		        stm32f469xx.h
		        stm32f427xx.h
		        stm32f479xx.h
		        stm32f413xx.h
		        stm32f429xx.h
		        stm32f439xx.h
		        stm32f415xx.h
		        stm32f412cx.h
		        stm32f412rx.h
		        stm32f410tx.h
		        stm32f410cx.h
		        stm32f412zx.h
		        stm32f405xx.h
		        stm32f407xx.h
		        stm32f417xx.h
		        stm32f446xx.h
		        stm32f401xc.h
		        stm32f437xx.h
		        stm32f401xe.h
		        stm32f412vx.h
		        stm32f410rx.h
		        stm32f411xe.h 
		"""

        _fields_ = [
			('CSR', ctypes.c_uint32),  # ADC Common status register,                  Address offset: ADC1 base address + 0x300
			('CCR', ctypes.c_uint32),  # ADC common control register,                 Address offset: ADC1 base address + 0x304
			('CDR', ctypes.c_uint32),  # ADC common regular data register for dual AND triple modes,                            Address offset: ADC1 base address + 0x308
		]

class STM32F4xxCan_txmailbox:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f423xx.h
		        stm32f469xx.h
		        stm32f427xx.h
		        stm32f479xx.h
		        stm32f413xx.h
		        stm32f429xx.h
		        stm32f439xx.h
		        stm32f415xx.h
		        stm32f412cx.h
		        stm32f412rx.h
		        stm32f412zx.h
		        stm32f405xx.h
		        stm32f407xx.h
		        stm32f417xx.h
		        stm32f446xx.h
		        stm32f437xx.h
		        stm32f412vx.h 
		"""

        _fields_ = [
			('TIR' , ctypes.c_uint32),  # CAN TX mailbox identifier register
			('TDTR', ctypes.c_uint32),  # CAN mailbox data length control and time stamp register
			('TDLR', ctypes.c_uint32),  # CAN mailbox data low register
			('TDHR', ctypes.c_uint32),  # CAN mailbox data high register
		]

class STM32F4xxCan_fifomailbox:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f423xx.h
		        stm32f469xx.h
		        stm32f427xx.h
		        stm32f479xx.h
		        stm32f413xx.h
		        stm32f429xx.h
		        stm32f439xx.h
		        stm32f415xx.h
		        stm32f412cx.h
		        stm32f412rx.h
		        stm32f412zx.h
		        stm32f405xx.h
		        stm32f407xx.h
		        stm32f417xx.h
		        stm32f446xx.h
		        stm32f437xx.h
		        stm32f412vx.h 
		"""

        _fields_ = [
			('RIR' , ctypes.c_uint32),  # CAN receive FIFO mailbox identifier register
			('RDTR', ctypes.c_uint32),  # CAN receive FIFO mailbox data length control and time stamp register
			('RDLR', ctypes.c_uint32),  # CAN receive FIFO mailbox data low register
			('RDHR', ctypes.c_uint32),  # CAN receive FIFO mailbox data high register
		]

class STM32F4xxCan_filterregister:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f423xx.h
		        stm32f469xx.h
		        stm32f427xx.h
		        stm32f479xx.h
		        stm32f413xx.h
		        stm32f429xx.h
		        stm32f439xx.h
		        stm32f415xx.h
		        stm32f412cx.h
		        stm32f412rx.h
		        stm32f412zx.h
		        stm32f405xx.h
		        stm32f407xx.h
		        stm32f417xx.h
		        stm32f446xx.h
		        stm32f437xx.h
		        stm32f412vx.h 
		"""

        _fields_ = [
			('FR1', ctypes.c_uint32),  # CAN Filter bank register 1
			('FR2', ctypes.c_uint32),  # CAN Filter bank register 1
		]

class STM32F4xxCan:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f423xx.h
		        stm32f469xx.h
		        stm32f427xx.h
		        stm32f479xx.h
		        stm32f413xx.h
		        stm32f429xx.h
		        stm32f439xx.h
		        stm32f415xx.h
		        stm32f412cx.h
		        stm32f412rx.h
		        stm32f412zx.h
		        stm32f405xx.h
		        stm32f407xx.h
		        stm32f417xx.h
		        stm32f446xx.h
		        stm32f437xx.h
		        stm32f412vx.h 
		"""

        _fields_ = [
			('MCR'            , ctypes.c_uint32),                       # CAN master control register,         Address offset: 0x00
			('MSR'            , ctypes.c_uint32),                       # CAN master status register,          Address offset: 0x04
			('TSR'            , ctypes.c_uint32),                       # CAN transmit status register,        Address offset: 0x08
			('RF0R'           , ctypes.c_uint32),                       # CAN receive FIFO 0 register,         Address offset: 0x0C
			('RF1R'           , ctypes.c_uint32),                       # CAN receive FIFO 1 register,         Address offset: 0x10
			('IER'            , ctypes.c_uint32),                       # CAN interrupt enable register,       Address offset: 0x14
			('ESR'            , ctypes.c_uint32),                       # CAN error status register,           Address offset: 0x18
			('BTR'            , ctypes.c_uint32),                       # CAN bit timing register,             Address offset: 0x1C
			('RESERVED0'      , ctypes.c_uint32 * 88),                  # Reserved, 0x020 - 0x17F
			('sTxMailBox'     , CAN_TxMailBox_TypeDef.Type * 3),        # CAN Tx MailBox,                      Address offset: 0x180 - 0x1AC
			('sFIFOMailBox'   , CAN_FIFOMailBox_TypeDef.Type * 2),      # CAN FIFO MailBox,                    Address offset: 0x1B0 - 0x1CC
			('RESERVED1'      , ctypes.c_uint32 * 12),                  # Reserved, 0x1D0 - 0x1FF
			('FMR'            , ctypes.c_uint32),                       # CAN filter master register,          Address offset: 0x200
			('FM1R'           , ctypes.c_uint32),                       # CAN filter mode register,            Address offset: 0x204
			('RESERVED2'      , ctypes.c_uint32),                       # Reserved, 0x208
			('FS1R'           , ctypes.c_uint32),                       # CAN filter scale register,           Address offset: 0x20C
			('RESERVED3'      , ctypes.c_uint32),                       # Reserved, 0x210
			('FFA1R'          , ctypes.c_uint32),                       # CAN filter FIFO assignment register, Address offset: 0x214
			('RESERVED4'      , ctypes.c_uint32),                       # Reserved, 0x218
			('FA1R'           , ctypes.c_uint32),                       # CAN filter activation register,      Address offset: 0x21C
			('RESERVED5'      , ctypes.c_uint32 * 8),                   # Reserved, 0x220-0x23F
			('sFilterRegister', CAN_FilterRegister_TypeDef.Type * 28),  # CAN Filter Register,                 Address offset: 0x240-0x31C
		]

class STM32F4xxCrc:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f423xx.h
		        stm32f469xx.h
		        stm32f427xx.h
		        stm32f479xx.h
		        stm32f413xx.h
		        stm32f429xx.h
		        stm32f439xx.h
		        stm32f415xx.h
		        stm32f412cx.h
		        stm32f412rx.h
		        stm32f410tx.h
		        stm32f410cx.h
		        stm32f412zx.h
		        stm32f405xx.h
		        stm32f407xx.h
		        stm32f417xx.h
		        stm32f446xx.h
		        stm32f401xc.h
		        stm32f437xx.h
		        stm32f401xe.h
		        stm32f412vx.h
		        stm32f410rx.h
		        stm32f411xe.h 
		"""

        _fields_ = [
			('DR'       , ctypes.c_uint32),  # CRC Data register,             Address offset: 0x00
			('IDR'      , ctypes.c_uint8),   # CRC Independent data register, Address offset: 0x04
			('RESERVED0', ctypes.c_uint8),   # Reserved, 0x05
			('RESERVED1', ctypes.c_uint8),   # Reserved, 0x06
			('CR'       , ctypes.c_uint32),  # CRC Control register,          Address offset: 0x08
		]

class STM32F4xxDfsdm_filter:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f423xx.h
		        stm32f413xx.h
		        stm32f412cx.h
		        stm32f412rx.h
		        stm32f412zx.h
		        stm32f412vx.h 
		"""

        _fields_ = [
			('FLTCR1'    , ctypes.c_uint32),  # DFSDM control register1,                          Address offset: 0x100
			('FLTCR2'    , ctypes.c_uint32),  # DFSDM control register2,                          Address offset: 0x104
			('FLTISR'    , ctypes.c_uint32),  # DFSDM interrupt and status register,              Address offset: 0x108
			('FLTICR'    , ctypes.c_uint32),  # DFSDM interrupt flag clear register,              Address offset: 0x10C
			('FLTJCHGR'  , ctypes.c_uint32),  # DFSDM injected channel group selection register,  Address offset: 0x110
			('FLTFCR'    , ctypes.c_uint32),  # DFSDM filter control register,                    Address offset: 0x114
			('FLTJDATAR' , ctypes.c_uint32),  # DFSDM data register for injected group,           Address offset: 0x118
			('FLTRDATAR' , ctypes.c_uint32),  # DFSDM data register for regular group,            Address offset: 0x11C
			('FLTAWHTR'  , ctypes.c_uint32),  # DFSDM analog watchdog high threshold register,    Address offset: 0x120
			('FLTAWLTR'  , ctypes.c_uint32),  # DFSDM analog watchdog low threshold register,     Address offset: 0x124
			('FLTAWSR'   , ctypes.c_uint32),  # DFSDM analog watchdog status register             Address offset: 0x128
			('FLTAWCFR'  , ctypes.c_uint32),  # DFSDM analog watchdog clear flag register         Address offset: 0x12C
			('FLTEXMAX'  , ctypes.c_uint32),  # DFSDM extreme detector maximum register,          Address offset: 0x130
			('FLTEXMIN'  , ctypes.c_uint32),  # DFSDM extreme detector minimum register           Address offset: 0x134
			('FLTCNVTIMR', ctypes.c_uint32),  # DFSDM conversion timer,                           Address offset: 0x138
		]

class STM32F4xxDfsdm_channel:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f423xx.h
		        stm32f413xx.h
		        stm32f412cx.h
		        stm32f412rx.h
		        stm32f412zx.h
		        stm32f412vx.h 
		"""

        _fields_ = [
			('CHCFGR1' , ctypes.c_uint32),  # DFSDM channel configuration register1,            Address offset: 0x00
			('CHCFGR2' , ctypes.c_uint32),  # DFSDM channel configuration register2,            Address offset: 0x04
			('CHAWSCDR', ctypes.c_uint32),  # DFSDM channel analog watchdog and short circuit detector register,                  Address offset: 0x08
			('CHWDATAR', ctypes.c_uint32),  # DFSDM channel watchdog filter data register,      Address offset: 0x0C
			('CHDATINR', ctypes.c_uint32),  # DFSDM channel data input register,                Address offset: 0x10
		]

class STM32F4xxDac:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f423xx.h
		        stm32f469xx.h
		        stm32f427xx.h
		        stm32f479xx.h
		        stm32f413xx.h
		        stm32f429xx.h
		        stm32f439xx.h
		        stm32f415xx.h
		        stm32f410tx.h
		        stm32f410cx.h
		        stm32f405xx.h
		        stm32f407xx.h
		        stm32f417xx.h
		        stm32f446xx.h
		        stm32f437xx.h
		        stm32f410rx.h 
		"""

        _fields_ = [
			('CR'     , ctypes.c_uint32),  # DAC control register,                                    Address offset: 0x00
			('SWTRIGR', ctypes.c_uint32),  # DAC software trigger register,                           Address offset: 0x04
			('DHR12R1', ctypes.c_uint32),  # DAC channel1 12-bit right-aligned data holding register, Address offset: 0x08
			('DHR12L1', ctypes.c_uint32),  # DAC channel1 12-bit left aligned data holding register,  Address offset: 0x0C
			('DHR8R1' , ctypes.c_uint32),  # DAC channel1 8-bit right aligned data holding register,  Address offset: 0x10
			('DHR12R2', ctypes.c_uint32),  # DAC channel2 12-bit right aligned data holding register, Address offset: 0x14
			('DHR12L2', ctypes.c_uint32),  # DAC channel2 12-bit left aligned data holding register,  Address offset: 0x18
			('DHR8R2' , ctypes.c_uint32),  # DAC channel2 8-bit right-aligned data holding register,  Address offset: 0x1C
			('DHR12RD', ctypes.c_uint32),  # Dual DAC 12-bit right-aligned data holding register,     Address offset: 0x20
			('DHR12LD', ctypes.c_uint32),  # DUAL DAC 12-bit left aligned data holding register,      Address offset: 0x24
			('DHR8RD' , ctypes.c_uint32),  # DUAL DAC 8-bit right aligned data holding register,      Address offset: 0x28
			('DOR1'   , ctypes.c_uint32),  # DAC channel1 data output register,                       Address offset: 0x2C
			('DOR2'   , ctypes.c_uint32),  # DAC channel2 data output register,                       Address offset: 0x30
			('SR'     , ctypes.c_uint32),  # DAC status register,                                     Address offset: 0x34
		]

class STM32F4xxDbgmcu:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f423xx.h
		        stm32f469xx.h
		        stm32f427xx.h
		        stm32f479xx.h
		        stm32f413xx.h
		        stm32f429xx.h
		        stm32f439xx.h
		        stm32f415xx.h
		        stm32f412cx.h
		        stm32f412rx.h
		        stm32f410tx.h
		        stm32f410cx.h
		        stm32f412zx.h
		        stm32f405xx.h
		        stm32f407xx.h
		        stm32f417xx.h
		        stm32f446xx.h
		        stm32f401xc.h
		        stm32f437xx.h
		        stm32f401xe.h
		        stm32f412vx.h
		        stm32f410rx.h
		        stm32f411xe.h 
		"""

        _fields_ = [
			('IDCODE', ctypes.c_uint32),  # MCU device ID code,               Address offset: 0x00
			('CR'    , ctypes.c_uint32),  # Debug MCU configuration register, Address offset: 0x04
			('APB1FZ', ctypes.c_uint32),  # Debug MCU APB1 freeze register,   Address offset: 0x08
			('APB2FZ', ctypes.c_uint32),  # Debug MCU APB2 freeze register,   Address offset: 0x0C
		]

class STM32F4xxDma_stream:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f423xx.h
		        stm32f469xx.h
		        stm32f427xx.h
		        stm32f479xx.h
		        stm32f413xx.h
		        stm32f429xx.h
		        stm32f439xx.h
		        stm32f415xx.h
		        stm32f412cx.h
		        stm32f412rx.h
		        stm32f410tx.h
		        stm32f410cx.h
		        stm32f412zx.h
		        stm32f405xx.h
		        stm32f407xx.h
		        stm32f417xx.h
		        stm32f446xx.h
		        stm32f401xc.h
		        stm32f437xx.h
		        stm32f401xe.h
		        stm32f412vx.h
		        stm32f410rx.h
		        stm32f411xe.h 
		"""

        _fields_ = [
			('CR'  , ctypes.c_uint32),  # DMA stream x configuration register
			('NDTR', ctypes.c_uint32),  # DMA stream x number of data register
			('PAR' , ctypes.c_uint32),  # DMA stream x peripheral address register
			('M0AR', ctypes.c_uint32),  # DMA stream x memory 0 address register
			('M1AR', ctypes.c_uint32),  # DMA stream x memory 1 address register
			('FCR' , ctypes.c_uint32),  # DMA stream x FIFO control register
		]

class STM32F4xxDma:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f423xx.h
		        stm32f469xx.h
		        stm32f427xx.h
		        stm32f479xx.h
		        stm32f413xx.h
		        stm32f429xx.h
		        stm32f439xx.h
		        stm32f415xx.h
		        stm32f412cx.h
		        stm32f412rx.h
		        stm32f410tx.h
		        stm32f410cx.h
		        stm32f412zx.h
		        stm32f405xx.h
		        stm32f407xx.h
		        stm32f417xx.h
		        stm32f446xx.h
		        stm32f401xc.h
		        stm32f437xx.h
		        stm32f401xe.h
		        stm32f412vx.h
		        stm32f410rx.h
		        stm32f411xe.h 
		"""

        _fields_ = [
			('LISR' , ctypes.c_uint32),  # DMA low interrupt status register,      Address offset: 0x00
			('HISR' , ctypes.c_uint32),  # DMA high interrupt status register,     Address offset: 0x04
			('LIFCR', ctypes.c_uint32),  # DMA low interrupt flag clear register,  Address offset: 0x08
			('HIFCR', ctypes.c_uint32),  # DMA high interrupt flag clear register, Address offset: 0x0C
		]

class STM32F4xxExti:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f423xx.h
		        stm32f469xx.h
		        stm32f427xx.h
		        stm32f479xx.h
		        stm32f413xx.h
		        stm32f429xx.h
		        stm32f439xx.h
		        stm32f415xx.h
		        stm32f412cx.h
		        stm32f412rx.h
		        stm32f410tx.h
		        stm32f410cx.h
		        stm32f412zx.h
		        stm32f405xx.h
		        stm32f407xx.h
		        stm32f417xx.h
		        stm32f446xx.h
		        stm32f401xc.h
		        stm32f437xx.h
		        stm32f401xe.h
		        stm32f412vx.h
		        stm32f410rx.h
		        stm32f411xe.h 
		"""

        _fields_ = [
			('IMR'  , ctypes.c_uint32),  # EXTI Interrupt mask register,            Address offset: 0x00
			('EMR'  , ctypes.c_uint32),  # EXTI Event mask register,                Address offset: 0x04
			('RTSR' , ctypes.c_uint32),  # EXTI Rising trigger selection register,  Address offset: 0x08
			('FTSR' , ctypes.c_uint32),  # EXTI Falling trigger selection register, Address offset: 0x0C
			('SWIER', ctypes.c_uint32),  # EXTI Software interrupt event register,  Address offset: 0x10
			('PR'   , ctypes.c_uint32),  # EXTI Pending register,                   Address offset: 0x14
		]

class STM32F4xxFlash:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f423xx.h
		        stm32f469xx.h
		        stm32f427xx.h
		        stm32f479xx.h
		        stm32f413xx.h
		        stm32f429xx.h
		        stm32f439xx.h
		        stm32f415xx.h
		        stm32f412cx.h
		        stm32f412rx.h
		        stm32f410tx.h
		        stm32f410cx.h
		        stm32f412zx.h
		        stm32f405xx.h
		        stm32f407xx.h
		        stm32f417xx.h
		        stm32f446xx.h
		        stm32f401xc.h
		        stm32f437xx.h
		        stm32f401xe.h
		        stm32f412vx.h
		        stm32f410rx.h
		        stm32f411xe.h 
		"""

        _fields_ = [
			('ACR'    , ctypes.c_uint32),  # FLASH access control register,   Address offset: 0x00
			('KEYR'   , ctypes.c_uint32),  # FLASH key register,              Address offset: 0x04
			('OPTKEYR', ctypes.c_uint32),  # FLASH option key register,       Address offset: 0x08
			('SR'     , ctypes.c_uint32),  # FLASH status register,           Address offset: 0x0C
			('CR'     , ctypes.c_uint32),  # FLASH control register,          Address offset: 0x10
			('OPTCR'  , ctypes.c_uint32),  # FLASH option control register ,  Address offset: 0x14
			('OPTCR1' , ctypes.c_uint32),  # FLASH option control register 1, Address offset: 0x18
		]

class STM32F4xxFsmc_bank1:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f423xx.h
		        stm32f413xx.h
		        stm32f415xx.h
		        stm32f412rx.h
		        stm32f412zx.h
		        stm32f405xx.h
		        stm32f407xx.h
		        stm32f417xx.h
		        stm32f412vx.h 
		"""

        _fields_ = [
			('BTCR', ctypes.c_uint32 * 8),  # NOR/PSRAM chip-select control register(BCR) and chip-select timing register(BTR), Address offset: 0x00-1C
		]

class STM32F4xxFsmc_bank1e:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f423xx.h
		        stm32f413xx.h
		        stm32f415xx.h
		        stm32f412rx.h
		        stm32f412zx.h
		        stm32f405xx.h
		        stm32f407xx.h
		        stm32f417xx.h
		        stm32f412vx.h 
		"""

        _fields_ = [
			('BWTR', ctypes.c_uint32 * 7),  # NOR/PSRAM write timing registers, Address offset: 0x104-0x11C
		]

class STM32F4xxGpio:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f423xx.h
		        stm32f469xx.h
		        stm32f427xx.h
		        stm32f479xx.h
		        stm32f413xx.h
		        stm32f429xx.h
		        stm32f439xx.h
		        stm32f415xx.h
		        stm32f412cx.h
		        stm32f412rx.h
		        stm32f410tx.h
		        stm32f410cx.h
		        stm32f412zx.h
		        stm32f405xx.h
		        stm32f407xx.h
		        stm32f417xx.h
		        stm32f446xx.h
		        stm32f401xc.h
		        stm32f437xx.h
		        stm32f401xe.h
		        stm32f412vx.h
		        stm32f410rx.h
		        stm32f411xe.h 
		"""

        _fields_ = [
			('MODER'  , ctypes.c_uint32),      # GPIO port mode register,               Address offset: 0x00
			('OTYPER' , ctypes.c_uint32),      # GPIO port output type register,        Address offset: 0x04
			('OSPEEDR', ctypes.c_uint32),      # GPIO port output speed register,       Address offset: 0x08
			('PUPDR'  , ctypes.c_uint32),      # GPIO port pull-up/pull-down register,  Address offset: 0x0C
			('IDR'    , ctypes.c_uint32),      # GPIO port input data register,         Address offset: 0x10
			('ODR'    , ctypes.c_uint32),      # GPIO port output data register,        Address offset: 0x14
			('BSRR'   , ctypes.c_uint32),      # GPIO port bit set/reset register,      Address offset: 0x18
			('LCKR'   , ctypes.c_uint32),      # GPIO port configuration lock register, Address offset: 0x1C
			('AFR'    , ctypes.c_uint32 * 2),  # GPIO alternate function registers,     Address offset: 0x20-0x24
		]

class STM32F4xxSyscfgV1:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f423xx.h
		        stm32f413xx.h 
		"""

        _fields_ = [
			('MEMRMP'   , ctypes.c_uint32),      # SYSCFG memory remap register,                      Address offset: 0x00
			('PMC'      , ctypes.c_uint32),      # SYSCFG peripheral mode configuration register,     Address offset: 0x04
			('EXTICR'   , ctypes.c_uint32 * 4),  # SYSCFG external interrupt configuration registers, Address offset: 0x08-0x14
			('RESERVED' , ctypes.c_uint32),      # Reserved, 0x18
			('CFGR2'    , ctypes.c_uint32),      # SYSCFG Configuration register2,                    Address offset: 0x1C
			('CMPCR'    , ctypes.c_uint32),      # SYSCFG Compensation cell control register,         Address offset: 0x20
			('RESERVED1', ctypes.c_uint32 * 2),  # Reserved, 0x24-0x28
			('CFGR'     , ctypes.c_uint32),      # SYSCFG Configuration register,                     Address offset: 0x2C
			('MCHDLYCR' , ctypes.c_uint32),      # SYSCFG multi-channel delay register,               Address offset: 0x30
		]

class STM32F4xxSyscfg:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f469xx.h
		        stm32f427xx.h
		        stm32f479xx.h
		        stm32f429xx.h
		        stm32f439xx.h
		        stm32f415xx.h
		        stm32f405xx.h
		        stm32f407xx.h
		        stm32f417xx.h
		        stm32f401xc.h
		        stm32f437xx.h
		        stm32f401xe.h
		        stm32f411xe.h 
		"""

        _fields_ = [
			('MEMRMP'  , ctypes.c_uint32),      # SYSCFG memory remap register,                      Address offset: 0x00
			('PMC'     , ctypes.c_uint32),      # SYSCFG peripheral mode configuration register,     Address offset: 0x04
			('EXTICR'  , ctypes.c_uint32 * 4),  # SYSCFG external interrupt configuration registers, Address offset: 0x08-0x14
			('RESERVED', ctypes.c_uint32 * 2),  # Reserved, 0x18-0x1C
			('CMPCR'   , ctypes.c_uint32),      # SYSCFG Compensation cell control register,         Address offset: 0x20
		]

class STM32F4xxSyscfgV2:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f412cx.h
		        stm32f412rx.h
		        stm32f410tx.h
		        stm32f410cx.h
		        stm32f412zx.h
		        stm32f412vx.h
		        stm32f410rx.h 
		"""

        _fields_ = [
			('MEMRMP'  , ctypes.c_uint32),      # SYSCFG memory remap register,                      Address offset: 0x00
			('PMC'     , ctypes.c_uint32),      # SYSCFG peripheral mode configuration register,     Address offset: 0x04
			('EXTICR'  , ctypes.c_uint32 * 4),  # SYSCFG external interrupt configuration registers, Address offset: 0x08-0x14
			('RESERVED', ctypes.c_uint32),      # Reserved, 0x18
			('CFGR2'   , ctypes.c_uint32),      # SYSCFG Configuration register2,                    Address offset: 0x1C
			('CMPCR'   , ctypes.c_uint32),      # SYSCFG Compensation cell control register,         Address offset: 0x20
			('CFGR'    , ctypes.c_uint32),      # SYSCFG Configuration register,                     Address offset: 0x24
		]

class STM32F446Syscfg:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f446xx.h 
		"""

        _fields_ = [
			('MEMRMP'   , ctypes.c_uint32),      # SYSCFG memory remap register,                      Address offset: 0x00
			('PMC'      , ctypes.c_uint32),      # SYSCFG peripheral mode configuration register,     Address offset: 0x04
			('EXTICR'   , ctypes.c_uint32 * 4),  # SYSCFG external interrupt configuration registers, Address offset: 0x08-0x14
			('RESERVED' , ctypes.c_uint32 * 2),  # Reserved, 0x18-0x1C
			('CMPCR'    , ctypes.c_uint32),      # SYSCFG Compensation cell control register,         Address offset: 0x20
			('RESERVED1', ctypes.c_uint32 * 2),  # Reserved, 0x24-0x28
			('CFGR'     , ctypes.c_uint32),      # SYSCFG Configuration register,                     Address offset: 0x2C
		]

class STM32F4xxI2c:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f423xx.h
		        stm32f469xx.h
		        stm32f427xx.h
		        stm32f479xx.h
		        stm32f413xx.h
		        stm32f429xx.h
		        stm32f439xx.h
		        stm32f412cx.h
		        stm32f412rx.h
		        stm32f410tx.h
		        stm32f410cx.h
		        stm32f412zx.h
		        stm32f446xx.h
		        stm32f401xc.h
		        stm32f437xx.h
		        stm32f401xe.h
		        stm32f412vx.h
		        stm32f410rx.h
		        stm32f411xe.h 
		"""

        _fields_ = [
			('CR1'  , ctypes.c_uint32),  # I2C Control register 1,     Address offset: 0x00
			('CR2'  , ctypes.c_uint32),  # I2C Control register 2,     Address offset: 0x04
			('OAR1' , ctypes.c_uint32),  # I2C Own address register 1, Address offset: 0x08
			('OAR2' , ctypes.c_uint32),  # I2C Own address register 2, Address offset: 0x0C
			('DR'   , ctypes.c_uint32),  # I2C Data register,          Address offset: 0x10
			('SR1'  , ctypes.c_uint32),  # I2C Status register 1,      Address offset: 0x14
			('SR2'  , ctypes.c_uint32),  # I2C Status register 2,      Address offset: 0x18
			('CCR'  , ctypes.c_uint32),  # I2C Clock control register, Address offset: 0x1C
			('TRISE', ctypes.c_uint32),  # I2C TRISE register,         Address offset: 0x20
			('FLTR' , ctypes.c_uint32),  # I2C FLTR register,          Address offset: 0x24
		]

class STM32F4xxI2cV1:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f415xx.h
		        stm32f405xx.h
		        stm32f407xx.h
		        stm32f417xx.h 
		"""

        _fields_ = [
			('CR1'  , ctypes.c_uint32),  # I2C Control register 1,     Address offset: 0x00
			('CR2'  , ctypes.c_uint32),  # I2C Control register 2,     Address offset: 0x04
			('OAR1' , ctypes.c_uint32),  # I2C Own address register 1, Address offset: 0x08
			('OAR2' , ctypes.c_uint32),  # I2C Own address register 2, Address offset: 0x0C
			('DR'   , ctypes.c_uint32),  # I2C Data register,          Address offset: 0x10
			('SR1'  , ctypes.c_uint32),  # I2C Status register 1,      Address offset: 0x14
			('SR2'  , ctypes.c_uint32),  # I2C Status register 2,      Address offset: 0x18
			('CCR'  , ctypes.c_uint32),  # I2C Clock control register, Address offset: 0x1C
			('TRISE', ctypes.c_uint32),  # I2C TRISE register,         Address offset: 0x20
		]

class STM32F4xxFmpi2c:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f423xx.h
		        stm32f413xx.h
		        stm32f412cx.h
		        stm32f412rx.h
		        stm32f410tx.h
		        stm32f410cx.h
		        stm32f412zx.h
		        stm32f446xx.h
		        stm32f412vx.h
		        stm32f410rx.h 
		"""

        _fields_ = [
			('CR1'     , ctypes.c_uint32),  # FMPI2C Control register 1,            Address offset: 0x00
			('CR2'     , ctypes.c_uint32),  # FMPI2C Control register 2,            Address offset: 0x04
			('OAR1'    , ctypes.c_uint32),  # FMPI2C Own address 1 register,        Address offset: 0x08
			('OAR2'    , ctypes.c_uint32),  # FMPI2C Own address 2 register,        Address offset: 0x0C
			('TIMINGR' , ctypes.c_uint32),  # FMPI2C Timing register,               Address offset: 0x10
			('TIMEOUTR', ctypes.c_uint32),  # FMPI2C Timeout register,              Address offset: 0x14
			('ISR'     , ctypes.c_uint32),  # FMPI2C Interrupt and status register, Address offset: 0x18
			('ICR'     , ctypes.c_uint32),  # FMPI2C Interrupt clear register,      Address offset: 0x1C
			('PECR'    , ctypes.c_uint32),  # FMPI2C PEC register,                  Address offset: 0x20
			('RXDR'    , ctypes.c_uint32),  # FMPI2C Receive data register,         Address offset: 0x24
			('TXDR'    , ctypes.c_uint32),  # FMPI2C Transmit data register,        Address offset: 0x28
		]

class STM32F4xxIwdg:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f423xx.h
		        stm32f469xx.h
		        stm32f427xx.h
		        stm32f479xx.h
		        stm32f413xx.h
		        stm32f429xx.h
		        stm32f439xx.h
		        stm32f415xx.h
		        stm32f412cx.h
		        stm32f412rx.h
		        stm32f410tx.h
		        stm32f410cx.h
		        stm32f412zx.h
		        stm32f405xx.h
		        stm32f407xx.h
		        stm32f417xx.h
		        stm32f446xx.h
		        stm32f401xc.h
		        stm32f437xx.h
		        stm32f401xe.h
		        stm32f412vx.h
		        stm32f410rx.h
		        stm32f411xe.h 
		"""

        _fields_ = [
			('KR' , ctypes.c_uint32),  # IWDG Key register,       Address offset: 0x00
			('PR' , ctypes.c_uint32),  # IWDG Prescaler register, Address offset: 0x04
			('RLR', ctypes.c_uint32),  # IWDG Reload register,    Address offset: 0x08
			('SR' , ctypes.c_uint32),  # IWDG Status register,    Address offset: 0x0C
		]

class STM32F4xxPwr:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f423xx.h
		        stm32f469xx.h
		        stm32f427xx.h
		        stm32f479xx.h
		        stm32f413xx.h
		        stm32f429xx.h
		        stm32f439xx.h
		        stm32f415xx.h
		        stm32f412cx.h
		        stm32f412rx.h
		        stm32f410tx.h
		        stm32f410cx.h
		        stm32f412zx.h
		        stm32f405xx.h
		        stm32f407xx.h
		        stm32f417xx.h
		        stm32f446xx.h
		        stm32f401xc.h
		        stm32f437xx.h
		        stm32f401xe.h
		        stm32f412vx.h
		        stm32f410rx.h
		        stm32f411xe.h 
		"""

        _fields_ = [
			('CR' , ctypes.c_uint32),  # PWR power control register,        Address offset: 0x00
			('CSR', ctypes.c_uint32),  # PWR power control/status register, Address offset: 0x04
		]

class STM32F4xxRccV1:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f423xx.h
		        stm32f413xx.h
		        stm32f412rx.h
		        stm32f412zx.h
		        stm32f412vx.h 
		"""

        _fields_ = [
			('CR'        , ctypes.c_uint32),      # RCC clock control register,                                  Address offset: 0x00
			('PLLCFGR'   , ctypes.c_uint32),      # RCC PLL configuration register,                              Address offset: 0x04
			('CFGR'      , ctypes.c_uint32),      # RCC clock configuration register,                            Address offset: 0x08
			('CIR'       , ctypes.c_uint32),      # RCC clock interrupt register,                                Address offset: 0x0C
			('AHB1RSTR'  , ctypes.c_uint32),      # RCC AHB1 peripheral reset register,                          Address offset: 0x10
			('AHB2RSTR'  , ctypes.c_uint32),      # RCC AHB2 peripheral reset register,                          Address offset: 0x14
			('AHB3RSTR'  , ctypes.c_uint32),      # RCC AHB3 peripheral reset register,                          Address offset: 0x18
			('RESERVED0' , ctypes.c_uint32),      # Reserved, 0x1C
			('APB1RSTR'  , ctypes.c_uint32),      # RCC APB1 peripheral reset register,                          Address offset: 0x20
			('APB2RSTR'  , ctypes.c_uint32),      # RCC APB2 peripheral reset register,                          Address offset: 0x24
			('RESERVED1' , ctypes.c_uint32 * 2),  # Reserved, 0x28-0x2C
			('AHB1ENR'   , ctypes.c_uint32),      # RCC AHB1 peripheral clock register,                          Address offset: 0x30
			('AHB2ENR'   , ctypes.c_uint32),      # RCC AHB2 peripheral clock register,                          Address offset: 0x34
			('AHB3ENR'   , ctypes.c_uint32),      # RCC AHB3 peripheral clock register,                          Address offset: 0x38
			('RESERVED2' , ctypes.c_uint32),      # Reserved, 0x3C
			('APB1ENR'   , ctypes.c_uint32),      # RCC APB1 peripheral clock enable register,                   Address offset: 0x40
			('APB2ENR'   , ctypes.c_uint32),      # RCC APB2 peripheral clock enable register,                   Address offset: 0x44
			('RESERVED3' , ctypes.c_uint32 * 2),  # Reserved, 0x48-0x4C
			('AHB1LPENR' , ctypes.c_uint32),      # RCC AHB1 peripheral clock enable in low power mode register, Address offset: 0x50
			('AHB2LPENR' , ctypes.c_uint32),      # RCC AHB2 peripheral clock enable in low power mode register, Address offset: 0x54
			('AHB3LPENR' , ctypes.c_uint32),      # RCC AHB3 peripheral clock enable in low power mode register, Address offset: 0x58
			('RESERVED4' , ctypes.c_uint32),      # Reserved, 0x5C
			('APB1LPENR' , ctypes.c_uint32),      # RCC APB1 peripheral clock enable in low power mode register, Address offset: 0x60
			('APB2LPENR' , ctypes.c_uint32),      # RCC APB2 peripheral clock enable in low power mode register, Address offset: 0x64
			('RESERVED5' , ctypes.c_uint32 * 2),  # Reserved, 0x68-0x6C
			('BDCR'      , ctypes.c_uint32),      # RCC Backup domain control register,                          Address offset: 0x70
			('CSR'       , ctypes.c_uint32),      # RCC clock control & status register,                         Address offset: 0x74
			('RESERVED6' , ctypes.c_uint32 * 2),  # Reserved, 0x78-0x7C
			('SSCGR'     , ctypes.c_uint32),      # RCC spread spectrum clock generation register,               Address offset: 0x80
			('PLLI2SCFGR', ctypes.c_uint32),      # RCC PLLI2S configuration register,                           Address offset: 0x84
			('RESERVED7' , ctypes.c_uint32),      # Reserved, 0x84
			('DCKCFGR'   , ctypes.c_uint32),      # RCC Dedicated Clocks configuration register,                 Address offset: 0x8C
			('CKGATENR'  , ctypes.c_uint32),      # RCC Clocks Gated ENable Register,                            Address offset: 0x90
			('DCKCFGR2'  , ctypes.c_uint32),      # RCC Dedicated Clocks configuration register 2,               Address offset: 0x94
		]

class STM32F4xxRccV2:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f469xx.h
		        stm32f427xx.h
		        stm32f479xx.h
		        stm32f429xx.h
		        stm32f439xx.h
		        stm32f437xx.h 
		"""

        _fields_ = [
			('CR'        , ctypes.c_uint32),      # RCC clock control register,                                  Address offset: 0x00
			('PLLCFGR'   , ctypes.c_uint32),      # RCC PLL configuration register,                              Address offset: 0x04
			('CFGR'      , ctypes.c_uint32),      # RCC clock configuration register,                            Address offset: 0x08
			('CIR'       , ctypes.c_uint32),      # RCC clock interrupt register,                                Address offset: 0x0C
			('AHB1RSTR'  , ctypes.c_uint32),      # RCC AHB1 peripheral reset register,                          Address offset: 0x10
			('AHB2RSTR'  , ctypes.c_uint32),      # RCC AHB2 peripheral reset register,                          Address offset: 0x14
			('AHB3RSTR'  , ctypes.c_uint32),      # RCC AHB3 peripheral reset register,                          Address offset: 0x18
			('RESERVED0' , ctypes.c_uint32),      # Reserved, 0x1C
			('APB1RSTR'  , ctypes.c_uint32),      # RCC APB1 peripheral reset register,                          Address offset: 0x20
			('APB2RSTR'  , ctypes.c_uint32),      # RCC APB2 peripheral reset register,                          Address offset: 0x24
			('RESERVED1' , ctypes.c_uint32 * 2),  # Reserved, 0x28-0x2C
			('AHB1ENR'   , ctypes.c_uint32),      # RCC AHB1 peripheral clock register,                          Address offset: 0x30
			('AHB2ENR'   , ctypes.c_uint32),      # RCC AHB2 peripheral clock register,                          Address offset: 0x34
			('AHB3ENR'   , ctypes.c_uint32),      # RCC AHB3 peripheral clock register,                          Address offset: 0x38
			('RESERVED2' , ctypes.c_uint32),      # Reserved, 0x3C
			('APB1ENR'   , ctypes.c_uint32),      # RCC APB1 peripheral clock enable register,                   Address offset: 0x40
			('APB2ENR'   , ctypes.c_uint32),      # RCC APB2 peripheral clock enable register,                   Address offset: 0x44
			('RESERVED3' , ctypes.c_uint32 * 2),  # Reserved, 0x48-0x4C
			('AHB1LPENR' , ctypes.c_uint32),      # RCC AHB1 peripheral clock enable in low power mode register, Address offset: 0x50
			('AHB2LPENR' , ctypes.c_uint32),      # RCC AHB2 peripheral clock enable in low power mode register, Address offset: 0x54
			('AHB3LPENR' , ctypes.c_uint32),      # RCC AHB3 peripheral clock enable in low power mode register, Address offset: 0x58
			('RESERVED4' , ctypes.c_uint32),      # Reserved, 0x5C
			('APB1LPENR' , ctypes.c_uint32),      # RCC APB1 peripheral clock enable in low power mode register, Address offset: 0x60
			('APB2LPENR' , ctypes.c_uint32),      # RCC APB2 peripheral clock enable in low power mode register, Address offset: 0x64
			('RESERVED5' , ctypes.c_uint32 * 2),  # Reserved, 0x68-0x6C
			('BDCR'      , ctypes.c_uint32),      # RCC Backup domain control register,                          Address offset: 0x70
			('CSR'       , ctypes.c_uint32),      # RCC clock control & status register,                         Address offset: 0x74
			('RESERVED6' , ctypes.c_uint32 * 2),  # Reserved, 0x78-0x7C
			('SSCGR'     , ctypes.c_uint32),      # RCC spread spectrum clock generation register,               Address offset: 0x80
			('PLLI2SCFGR', ctypes.c_uint32),      # RCC PLLI2S configuration register,                           Address offset: 0x84
			('PLLSAICFGR', ctypes.c_uint32),      # RCC PLLSAI configuration register,                           Address offset: 0x88
			('DCKCFGR'   , ctypes.c_uint32),      # RCC Dedicated Clocks configuration register,                 Address offset: 0x8C
		]

class STM32F4xxRccV3:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f415xx.h
		        stm32f405xx.h
		        stm32f407xx.h
		        stm32f417xx.h 
		"""

        _fields_ = [
			('CR'        , ctypes.c_uint32),      # RCC clock control register,                                  Address offset: 0x00
			('PLLCFGR'   , ctypes.c_uint32),      # RCC PLL configuration register,                              Address offset: 0x04
			('CFGR'      , ctypes.c_uint32),      # RCC clock configuration register,                            Address offset: 0x08
			('CIR'       , ctypes.c_uint32),      # RCC clock interrupt register,                                Address offset: 0x0C
			('AHB1RSTR'  , ctypes.c_uint32),      # RCC AHB1 peripheral reset register,                          Address offset: 0x10
			('AHB2RSTR'  , ctypes.c_uint32),      # RCC AHB2 peripheral reset register,                          Address offset: 0x14
			('AHB3RSTR'  , ctypes.c_uint32),      # RCC AHB3 peripheral reset register,                          Address offset: 0x18
			('RESERVED0' , ctypes.c_uint32),      # Reserved, 0x1C
			('APB1RSTR'  , ctypes.c_uint32),      # RCC APB1 peripheral reset register,                          Address offset: 0x20
			('APB2RSTR'  , ctypes.c_uint32),      # RCC APB2 peripheral reset register,                          Address offset: 0x24
			('RESERVED1' , ctypes.c_uint32 * 2),  # Reserved, 0x28-0x2C
			('AHB1ENR'   , ctypes.c_uint32),      # RCC AHB1 peripheral clock register,                          Address offset: 0x30
			('AHB2ENR'   , ctypes.c_uint32),      # RCC AHB2 peripheral clock register,                          Address offset: 0x34
			('AHB3ENR'   , ctypes.c_uint32),      # RCC AHB3 peripheral clock register,                          Address offset: 0x38
			('RESERVED2' , ctypes.c_uint32),      # Reserved, 0x3C
			('APB1ENR'   , ctypes.c_uint32),      # RCC APB1 peripheral clock enable register,                   Address offset: 0x40
			('APB2ENR'   , ctypes.c_uint32),      # RCC APB2 peripheral clock enable register,                   Address offset: 0x44
			('RESERVED3' , ctypes.c_uint32 * 2),  # Reserved, 0x48-0x4C
			('AHB1LPENR' , ctypes.c_uint32),      # RCC AHB1 peripheral clock enable in low power mode register, Address offset: 0x50
			('AHB2LPENR' , ctypes.c_uint32),      # RCC AHB2 peripheral clock enable in low power mode register, Address offset: 0x54
			('AHB3LPENR' , ctypes.c_uint32),      # RCC AHB3 peripheral clock enable in low power mode register, Address offset: 0x58
			('RESERVED4' , ctypes.c_uint32),      # Reserved, 0x5C
			('APB1LPENR' , ctypes.c_uint32),      # RCC APB1 peripheral clock enable in low power mode register, Address offset: 0x60
			('APB2LPENR' , ctypes.c_uint32),      # RCC APB2 peripheral clock enable in low power mode register, Address offset: 0x64
			('RESERVED5' , ctypes.c_uint32 * 2),  # Reserved, 0x68-0x6C
			('BDCR'      , ctypes.c_uint32),      # RCC Backup domain control register,                          Address offset: 0x70
			('CSR'       , ctypes.c_uint32),      # RCC clock control & status register,                         Address offset: 0x74
			('RESERVED6' , ctypes.c_uint32 * 2),  # Reserved, 0x78-0x7C
			('SSCGR'     , ctypes.c_uint32),      # RCC spread spectrum clock generation register,               Address offset: 0x80
			('PLLI2SCFGR', ctypes.c_uint32),      # RCC PLLI2S configuration register,                           Address offset: 0x84
		]

class STM32F412Rcc:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f412cx.h 
		"""

        _fields_ = [
			('CR'        , ctypes.c_uint32),      # RCC clock control register,                                  Address offset: 0x00
			('PLLCFGR'   , ctypes.c_uint32),      # RCC PLL configuration register,                              Address offset: 0x04
			('CFGR'      , ctypes.c_uint32),      # RCC clock configuration register,                            Address offset: 0x08
			('CIR'       , ctypes.c_uint32),      # RCC clock interrupt register,                                Address offset: 0x0C
			('AHB1RSTR'  , ctypes.c_uint32),      # RCC AHB1 peripheral reset register,                          Address offset: 0x10
			('AHB2RSTR'  , ctypes.c_uint32),      # RCC AHB2 peripheral reset register,                          Address offset: 0x14
			('RESERVED0' , ctypes.c_uint32 * 2),  # Reserved, 0x18-0x1C
			('APB1RSTR'  , ctypes.c_uint32),      # RCC APB1 peripheral reset register,                          Address offset: 0x20
			('APB2RSTR'  , ctypes.c_uint32),      # RCC APB2 peripheral reset register,                          Address offset: 0x24
			('RESERVED1' , ctypes.c_uint32 * 2),  # Reserved, 0x28-0x2C
			('AHB1ENR'   , ctypes.c_uint32),      # RCC AHB1 peripheral clock register,                          Address offset: 0x30
			('AHB2ENR'   , ctypes.c_uint32),      # RCC AHB2 peripheral clock register,                          Address offset: 0x34
			('RESERVED2' , ctypes.c_uint32 * 2),  # Reserved, 0x38-0x3C
			('APB1ENR'   , ctypes.c_uint32),      # RCC APB1 peripheral clock enable register,                   Address offset: 0x40
			('APB2ENR'   , ctypes.c_uint32),      # RCC APB2 peripheral clock enable register,                   Address offset: 0x44
			('RESERVED3' , ctypes.c_uint32 * 2),  # Reserved, 0x48-0x4C
			('AHB1LPENR' , ctypes.c_uint32),      # RCC AHB1 peripheral clock enable in low power mode register, Address offset: 0x50
			('AHB2LPENR' , ctypes.c_uint32),      # RCC AHB2 peripheral clock enable in low power mode register, Address offset: 0x54
			('RESERVED4' , ctypes.c_uint32 * 2),  # Reserved, 0x58-0x5C
			('APB1LPENR' , ctypes.c_uint32),      # RCC APB1 peripheral clock enable in low power mode register, Address offset: 0x60
			('APB2LPENR' , ctypes.c_uint32),      # RCC APB2 peripheral clock enable in low power mode register, Address offset: 0x64
			('RESERVED5' , ctypes.c_uint32 * 2),  # Reserved, 0x68-0x6C
			('BDCR'      , ctypes.c_uint32),      # RCC Backup domain control register,                          Address offset: 0x70
			('CSR'       , ctypes.c_uint32),      # RCC clock control & status register,                         Address offset: 0x74
			('RESERVED6' , ctypes.c_uint32 * 2),  # Reserved, 0x78-0x7C
			('SSCGR'     , ctypes.c_uint32),      # RCC spread spectrum clock generation register,               Address offset: 0x80
			('PLLI2SCFGR', ctypes.c_uint32),      # RCC PLLI2S configuration register,                           Address offset: 0x84
			('RESERVED7' , ctypes.c_uint32),      # Reserved, 0x88
			('DCKCFGR'   , ctypes.c_uint32),      # RCC Dedicated Clocks configuration register,                 Address offset: 0x8C
			('CKGATENR'  , ctypes.c_uint32),      # RCC Clocks Gated ENable Register,                           Address offset: 0x90
			('DCKCFGR2'  , ctypes.c_uint32),      # RCC Dedicated Clocks configuration register 2,               Address offset: 0x94
		]

class STM32F4xxRccV4:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f410tx.h
		        stm32f410cx.h
		        stm32f410rx.h 
		"""

        _fields_ = [
			('CR'       , ctypes.c_uint32),      # RCC clock control register,                                  Address offset: 0x00
			('PLLCFGR'  , ctypes.c_uint32),      # RCC PLL configuration register,                              Address offset: 0x04
			('CFGR'     , ctypes.c_uint32),      # RCC clock configuration register,                            Address offset: 0x08
			('CIR'      , ctypes.c_uint32),      # RCC clock interrupt register,                                Address offset: 0x0C
			('AHB1RSTR' , ctypes.c_uint32),      # RCC AHB1 peripheral reset register,                          Address offset: 0x10
			('RESERVED0', ctypes.c_uint32 * 3),  # Reserved, 0x14-0x1C
			('APB1RSTR' , ctypes.c_uint32),      # RCC APB1 peripheral reset register,                          Address offset: 0x20
			('APB2RSTR' , ctypes.c_uint32),      # RCC APB2 peripheral reset register,                          Address offset: 0x24
			('RESERVED1', ctypes.c_uint32 * 2),  # Reserved, 0x28-0x2C
			('AHB1ENR'  , ctypes.c_uint32),      # RCC AHB1 peripheral clock register,                          Address offset: 0x30
			('RESERVED2', ctypes.c_uint32 * 3),  # Reserved, 0x34-0x3C
			('APB1ENR'  , ctypes.c_uint32),      # RCC APB1 peripheral clock enable register,                   Address offset: 0x40
			('APB2ENR'  , ctypes.c_uint32),      # RCC APB2 peripheral clock enable register,                   Address offset: 0x44
			('RESERVED3', ctypes.c_uint32 * 2),  # Reserved, 0x48-0x4C
			('AHB1LPENR', ctypes.c_uint32),      # RCC AHB1 peripheral clock enable in low power mode register, Address offset: 0x50
			('RESERVED4', ctypes.c_uint32 * 3),  # Reserved, 0x54-0x5C
			('APB1LPENR', ctypes.c_uint32),      # RCC APB1 peripheral clock enable in low power mode register, Address offset: 0x60
			('APB2LPENR', ctypes.c_uint32),      # RCC APB2 peripheral clock enable in low power mode register, Address offset: 0x64
			('RESERVED5', ctypes.c_uint32 * 2),  # Reserved, 0x68-0x6C
			('BDCR'     , ctypes.c_uint32),      # RCC Backup domain control register,                          Address offset: 0x70
			('CSR'      , ctypes.c_uint32),      # RCC clock control & status register,                         Address offset: 0x74
			('RESERVED6', ctypes.c_uint32 * 2),  # Reserved, 0x78-0x7C
			('SSCGR'    , ctypes.c_uint32),      # RCC spread spectrum clock generation register,               Address offset: 0x80
			('RESERVED7', ctypes.c_uint32 * 2),  # Reserved, 0x84-0x88
			('DCKCFGR'  , ctypes.c_uint32),      # RCC DCKCFGR configuration register,                         Address offset: 0x8C
			('CKGATENR' , ctypes.c_uint32),      # RCC Clocks Gated ENable Register,                           Address offset: 0x90
			('DCKCFGR2' , ctypes.c_uint32),      # RCC Dedicated Clocks configuration register 2,               Address offset: 0x94
		]

class STM32F446Rcc:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f446xx.h 
		"""

        _fields_ = [
			('CR'        , ctypes.c_uint32),      # RCC clock control register,                                  Address offset: 0x00
			('PLLCFGR'   , ctypes.c_uint32),      # RCC PLL configuration register,                              Address offset: 0x04
			('CFGR'      , ctypes.c_uint32),      # RCC clock configuration register,                            Address offset: 0x08
			('CIR'       , ctypes.c_uint32),      # RCC clock interrupt register,                                Address offset: 0x0C
			('AHB1RSTR'  , ctypes.c_uint32),      # RCC AHB1 peripheral reset register,                          Address offset: 0x10
			('AHB2RSTR'  , ctypes.c_uint32),      # RCC AHB2 peripheral reset register,                          Address offset: 0x14
			('AHB3RSTR'  , ctypes.c_uint32),      # RCC AHB3 peripheral reset register,                          Address offset: 0x18
			('RESERVED0' , ctypes.c_uint32),      # Reserved, 0x1C
			('APB1RSTR'  , ctypes.c_uint32),      # RCC APB1 peripheral reset register,                          Address offset: 0x20
			('APB2RSTR'  , ctypes.c_uint32),      # RCC APB2 peripheral reset register,                          Address offset: 0x24
			('RESERVED1' , ctypes.c_uint32 * 2),  # Reserved, 0x28-0x2C
			('AHB1ENR'   , ctypes.c_uint32),      # RCC AHB1 peripheral clock register,                          Address offset: 0x30
			('AHB2ENR'   , ctypes.c_uint32),      # RCC AHB2 peripheral clock register,                          Address offset: 0x34
			('AHB3ENR'   , ctypes.c_uint32),      # RCC AHB3 peripheral clock register,                          Address offset: 0x38
			('RESERVED2' , ctypes.c_uint32),      # Reserved, 0x3C
			('APB1ENR'   , ctypes.c_uint32),      # RCC APB1 peripheral clock enable register,                   Address offset: 0x40
			('APB2ENR'   , ctypes.c_uint32),      # RCC APB2 peripheral clock enable register,                   Address offset: 0x44
			('RESERVED3' , ctypes.c_uint32 * 2),  # Reserved, 0x48-0x4C
			('AHB1LPENR' , ctypes.c_uint32),      # RCC AHB1 peripheral clock enable in low power mode register, Address offset: 0x50
			('AHB2LPENR' , ctypes.c_uint32),      # RCC AHB2 peripheral clock enable in low power mode register, Address offset: 0x54
			('AHB3LPENR' , ctypes.c_uint32),      # RCC AHB3 peripheral clock enable in low power mode register, Address offset: 0x58
			('RESERVED4' , ctypes.c_uint32),      # Reserved, 0x5C
			('APB1LPENR' , ctypes.c_uint32),      # RCC APB1 peripheral clock enable in low power mode register, Address offset: 0x60
			('APB2LPENR' , ctypes.c_uint32),      # RCC APB2 peripheral clock enable in low power mode register, Address offset: 0x64
			('RESERVED5' , ctypes.c_uint32 * 2),  # Reserved, 0x68-0x6C
			('BDCR'      , ctypes.c_uint32),      # RCC Backup domain control register,                          Address offset: 0x70
			('CSR'       , ctypes.c_uint32),      # RCC clock control & status register,                         Address offset: 0x74
			('RESERVED6' , ctypes.c_uint32 * 2),  # Reserved, 0x78-0x7C
			('SSCGR'     , ctypes.c_uint32),      # RCC spread spectrum clock generation register,               Address offset: 0x80
			('PLLI2SCFGR', ctypes.c_uint32),      # RCC PLLI2S configuration register,                           Address offset: 0x84
			('PLLSAICFGR', ctypes.c_uint32),      # RCC PLLSAI configuration register,                           Address offset: 0x88
			('DCKCFGR'   , ctypes.c_uint32),      # RCC Dedicated Clocks configuration register,                 Address offset: 0x8C
			('CKGATENR'  , ctypes.c_uint32),      # RCC Clocks Gated ENable Register,                            Address offset: 0x90
			('DCKCFGR2'  , ctypes.c_uint32),      # RCC Dedicated Clocks configuration register 2,               Address offset: 0x94
		]

class STM32F4xxRcc:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f401xc.h
		        stm32f401xe.h
		        stm32f411xe.h 
		"""

        _fields_ = [
			('CR'        , ctypes.c_uint32),      # RCC clock control register,                                  Address offset: 0x00
			('PLLCFGR'   , ctypes.c_uint32),      # RCC PLL configuration register,                              Address offset: 0x04
			('CFGR'      , ctypes.c_uint32),      # RCC clock configuration register,                            Address offset: 0x08
			('CIR'       , ctypes.c_uint32),      # RCC clock interrupt register,                                Address offset: 0x0C
			('AHB1RSTR'  , ctypes.c_uint32),      # RCC AHB1 peripheral reset register,                          Address offset: 0x10
			('AHB2RSTR'  , ctypes.c_uint32),      # RCC AHB2 peripheral reset register,                          Address offset: 0x14
			('AHB3RSTR'  , ctypes.c_uint32),      # RCC AHB3 peripheral reset register,                          Address offset: 0x18
			('RESERVED0' , ctypes.c_uint32),      # Reserved, 0x1C
			('APB1RSTR'  , ctypes.c_uint32),      # RCC APB1 peripheral reset register,                          Address offset: 0x20
			('APB2RSTR'  , ctypes.c_uint32),      # RCC APB2 peripheral reset register,                          Address offset: 0x24
			('RESERVED1' , ctypes.c_uint32 * 2),  # Reserved, 0x28-0x2C
			('AHB1ENR'   , ctypes.c_uint32),      # RCC AHB1 peripheral clock register,                          Address offset: 0x30
			('AHB2ENR'   , ctypes.c_uint32),      # RCC AHB2 peripheral clock register,                          Address offset: 0x34
			('AHB3ENR'   , ctypes.c_uint32),      # RCC AHB3 peripheral clock register,                          Address offset: 0x38
			('RESERVED2' , ctypes.c_uint32),      # Reserved, 0x3C
			('APB1ENR'   , ctypes.c_uint32),      # RCC APB1 peripheral clock enable register,                   Address offset: 0x40
			('APB2ENR'   , ctypes.c_uint32),      # RCC APB2 peripheral clock enable register,                   Address offset: 0x44
			('RESERVED3' , ctypes.c_uint32 * 2),  # Reserved, 0x48-0x4C
			('AHB1LPENR' , ctypes.c_uint32),      # RCC AHB1 peripheral clock enable in low power mode register, Address offset: 0x50
			('AHB2LPENR' , ctypes.c_uint32),      # RCC AHB2 peripheral clock enable in low power mode register, Address offset: 0x54
			('AHB3LPENR' , ctypes.c_uint32),      # RCC AHB3 peripheral clock enable in low power mode register, Address offset: 0x58
			('RESERVED4' , ctypes.c_uint32),      # Reserved, 0x5C
			('APB1LPENR' , ctypes.c_uint32),      # RCC APB1 peripheral clock enable in low power mode register, Address offset: 0x60
			('APB2LPENR' , ctypes.c_uint32),      # RCC APB2 peripheral clock enable in low power mode register, Address offset: 0x64
			('RESERVED5' , ctypes.c_uint32 * 2),  # Reserved, 0x68-0x6C
			('BDCR'      , ctypes.c_uint32),      # RCC Backup domain control register,                          Address offset: 0x70
			('CSR'       , ctypes.c_uint32),      # RCC clock control & status register,                         Address offset: 0x74
			('RESERVED6' , ctypes.c_uint32 * 2),  # Reserved, 0x78-0x7C
			('SSCGR'     , ctypes.c_uint32),      # RCC spread spectrum clock generation register,               Address offset: 0x80
			('PLLI2SCFGR', ctypes.c_uint32),      # RCC PLLI2S configuration register,                           Address offset: 0x84
			('RESERVED7' , ctypes.c_uint32),      # Reserved, 0x88
			('DCKCFGR'   , ctypes.c_uint32),      # RCC Dedicated Clocks configuration register,                 Address offset: 0x8C
		]

class STM32F4xxRtc:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f423xx.h
		        stm32f469xx.h
		        stm32f427xx.h
		        stm32f479xx.h
		        stm32f413xx.h
		        stm32f429xx.h
		        stm32f439xx.h
		        stm32f415xx.h
		        stm32f412cx.h
		        stm32f412rx.h
		        stm32f410tx.h
		        stm32f410cx.h
		        stm32f412zx.h
		        stm32f405xx.h
		        stm32f407xx.h
		        stm32f417xx.h
		        stm32f446xx.h
		        stm32f401xc.h
		        stm32f437xx.h
		        stm32f401xe.h
		        stm32f412vx.h
		        stm32f410rx.h
		        stm32f411xe.h 
		"""

        _fields_ = [
			('TR'          , ctypes.c_uint32),  # RTC time register,                                        Address offset: 0x00
			('DR'          , ctypes.c_uint32),  # RTC date register,                                        Address offset: 0x04
			('CR'          , ctypes.c_uint32),  # RTC control register,                                     Address offset: 0x08
			('ISR'         , ctypes.c_uint32),  # RTC initialization and status register,                   Address offset: 0x0C
			('PRER'        , ctypes.c_uint32),  # RTC prescaler register,                                   Address offset: 0x10
			('WUTR'        , ctypes.c_uint32),  # RTC wakeup timer register,                                Address offset: 0x14
			('CALIBR'      , ctypes.c_uint32),  # RTC calibration register,                                 Address offset: 0x18
			('ALRMAR'      , ctypes.c_uint32),  # RTC alarm A register,                                     Address offset: 0x1C
			('ALRMBR'      , ctypes.c_uint32),  # RTC alarm B register,                                     Address offset: 0x20
			('WPR'         , ctypes.c_uint32),  # RTC write protection register,                            Address offset: 0x24
			('SSR'         , ctypes.c_uint32),  # RTC sub second register,                                  Address offset: 0x28
			('SHIFTR'      , ctypes.c_uint32),  # RTC shift control register,                               Address offset: 0x2C
			('TSTR'        , ctypes.c_uint32),  # RTC time stamp time register,                             Address offset: 0x30
			('TSDR'        , ctypes.c_uint32),  # RTC time stamp date register,                             Address offset: 0x34
			('TSSSR'       , ctypes.c_uint32),  # RTC time-stamp sub second register,                       Address offset: 0x38
			('CALR'        , ctypes.c_uint32),  # RTC calibration register,                                 Address offset: 0x3C
			('TAFCR'       , ctypes.c_uint32),  # RTC tamper and alternate function configuration register, Address offset: 0x40
			('ALRMASSR;/*!', ctypes.c_uint32),  # RTC alarm A sub second register,                          Address offset: 0x44
			('ALRMBSSR;/*!', ctypes.c_uint32),  # RTC alarm B sub second register,                          Address offset: 0x48
			('RESERVED7'   , ctypes.c_uint32),  # Reserved, 0x4C
			('BKP0R'       , ctypes.c_uint32),  # RTC backup register 1,                                    Address offset: 0x50
			('BKP1R'       , ctypes.c_uint32),  # RTC backup register 1,                                    Address offset: 0x54
			('BKP2R'       , ctypes.c_uint32),  # RTC backup register 2,                                    Address offset: 0x58
			('BKP3R'       , ctypes.c_uint32),  # RTC backup register 3,                                    Address offset: 0x5C
			('BKP4R'       , ctypes.c_uint32),  # RTC backup register 4,                                    Address offset: 0x60
			('BKP5R'       , ctypes.c_uint32),  # RTC backup register 5,                                    Address offset: 0x64
			('BKP6R'       , ctypes.c_uint32),  # RTC backup register 6,                                    Address offset: 0x68
			('BKP7R'       , ctypes.c_uint32),  # RTC backup register 7,                                    Address offset: 0x6C
			('BKP8R'       , ctypes.c_uint32),  # RTC backup register 8,                                    Address offset: 0x70
			('BKP9R'       , ctypes.c_uint32),  # RTC backup register 9,                                    Address offset: 0x74
			('BKP10R'      , ctypes.c_uint32),  # RTC backup register 10,                                   Address offset: 0x78
			('BKP11R'      , ctypes.c_uint32),  # RTC backup register 11,                                   Address offset: 0x7C
			('BKP12R'      , ctypes.c_uint32),  # RTC backup register 12,                                   Address offset: 0x80
			('BKP13R'      , ctypes.c_uint32),  # RTC backup register 13,                                   Address offset: 0x84
			('BKP14R'      , ctypes.c_uint32),  # RTC backup register 14,                                   Address offset: 0x88
			('BKP15R'      , ctypes.c_uint32),  # RTC backup register 15,                                   Address offset: 0x8C
			('BKP16R'      , ctypes.c_uint32),  # RTC backup register 16,                                   Address offset: 0x90
			('BKP17R'      , ctypes.c_uint32),  # RTC backup register 17,                                   Address offset: 0x94
			('BKP18R'      , ctypes.c_uint32),  # RTC backup register 18,                                   Address offset: 0x98
			('BKP19R'      , ctypes.c_uint32),  # RTC backup register 19,                                   Address offset: 0x9C
		]

class STM32F4xxSai:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f423xx.h
		        stm32f469xx.h
		        stm32f427xx.h
		        stm32f479xx.h
		        stm32f413xx.h
		        stm32f429xx.h
		        stm32f439xx.h
		        stm32f446xx.h
		        stm32f437xx.h 
		"""

        _fields_ = [
			('GCR', ctypes.c_uint32),  # SAI global configuration register,        Address offset: 0x00
		]

class STM32F4xxSai_block:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f423xx.h
		        stm32f469xx.h
		        stm32f427xx.h
		        stm32f479xx.h
		        stm32f413xx.h
		        stm32f429xx.h
		        stm32f439xx.h
		        stm32f446xx.h
		        stm32f437xx.h 
		"""

        _fields_ = [
			('CR1'  , ctypes.c_uint32),  # SAI block x configuration register 1,     Address offset: 0x04
			('CR2'  , ctypes.c_uint32),  # SAI block x configuration register 2,     Address offset: 0x08
			('FRCR' , ctypes.c_uint32),  # SAI block x frame configuration register, Address offset: 0x0C
			('SLOTR', ctypes.c_uint32),  # SAI block x slot register,                Address offset: 0x10
			('IMR'  , ctypes.c_uint32),  # SAI block x interrupt mask register,      Address offset: 0x14
			('SR'   , ctypes.c_uint32),  # SAI block x status register,              Address offset: 0x18
			('CLRFR', ctypes.c_uint32),  # SAI block x clear flag register,          Address offset: 0x1C
			('DR'   , ctypes.c_uint32),  # SAI block x data register,                Address offset: 0x20
		]

class STM32F4xxSdio:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f423xx.h
		        stm32f469xx.h
		        stm32f427xx.h
		        stm32f479xx.h
		        stm32f413xx.h
		        stm32f429xx.h
		        stm32f439xx.h
		        stm32f415xx.h
		        stm32f412cx.h
		        stm32f412rx.h
		        stm32f412zx.h
		        stm32f405xx.h
		        stm32f407xx.h
		        stm32f417xx.h
		        stm32f446xx.h
		        stm32f401xc.h
		        stm32f437xx.h
		        stm32f401xe.h
		        stm32f412vx.h
		        stm32f411xe.h 
		"""

        _fields_ = [
			('POWER'    , ctypes.c_uint32),       # SDIO power control register,    Address offset: 0x00
			('CLKCR'    , ctypes.c_uint32),       # SDI clock control register,     Address offset: 0x04
			('ARG'      , ctypes.c_uint32),       # SDIO argument register,         Address offset: 0x08
			('CMD'      , ctypes.c_uint32),       # SDIO command register,          Address offset: 0x0C
			('RESPCMD'  , ctypes.c_uint32),       # SDIO command response register, Address offset: 0x10
			('RESP1'    , ctypes.c_uint32),       # SDIO response 1 register,       Address offset: 0x14
			('RESP2'    , ctypes.c_uint32),       # SDIO response 2 register,       Address offset: 0x18
			('RESP3'    , ctypes.c_uint32),       # SDIO response 3 register,       Address offset: 0x1C
			('RESP4'    , ctypes.c_uint32),       # SDIO response 4 register,       Address offset: 0x20
			('DTIMER'   , ctypes.c_uint32),       # SDIO data timer register,       Address offset: 0x24
			('DLEN'     , ctypes.c_uint32),       # SDIO data length register,      Address offset: 0x28
			('DCTRL'    , ctypes.c_uint32),       # SDIO data control register,     Address offset: 0x2C
			('DCOUNT'   , ctypes.c_uint32),       # SDIO data counter register,     Address offset: 0x30
			('STA'      , ctypes.c_uint32),       # SDIO status register,           Address offset: 0x34
			('ICR'      , ctypes.c_uint32),       # SDIO interrupt clear register,  Address offset: 0x38
			('MASK'     , ctypes.c_uint32),       # SDIO mask register,             Address offset: 0x3C
			('RESERVED0', ctypes.c_uint32 * 2),   # Reserved, 0x40-0x44
			('FIFOCNT'  , ctypes.c_uint32),       # SDIO FIFO counter register,     Address offset: 0x48
			('RESERVED1', ctypes.c_uint32 * 13),  # Reserved, 0x4C-0x7C
			('FIFO'     , ctypes.c_uint32),       # SDIO data FIFO register,        Address offset: 0x80
		]

class STM32F4xxSpi:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f423xx.h
		        stm32f469xx.h
		        stm32f427xx.h
		        stm32f479xx.h
		        stm32f413xx.h
		        stm32f429xx.h
		        stm32f439xx.h
		        stm32f415xx.h
		        stm32f412cx.h
		        stm32f412rx.h
		        stm32f410tx.h
		        stm32f410cx.h
		        stm32f412zx.h
		        stm32f405xx.h
		        stm32f407xx.h
		        stm32f417xx.h
		        stm32f446xx.h
		        stm32f401xc.h
		        stm32f437xx.h
		        stm32f401xe.h
		        stm32f412vx.h
		        stm32f410rx.h
		        stm32f411xe.h 
		"""

        _fields_ = [
			('CR1'    , ctypes.c_uint32),  # SPI control register 1 (not used in I2S mode),      Address offset: 0x00
			('CR2'    , ctypes.c_uint32),  # SPI control register 2,                             Address offset: 0x04
			('SR'     , ctypes.c_uint32),  # SPI status register,                                Address offset: 0x08
			('DR'     , ctypes.c_uint32),  # SPI data register,                                  Address offset: 0x0C
			('CRCPR'  , ctypes.c_uint32),  # SPI CRC polynomial register (not used in I2S mode), Address offset: 0x10
			('RXCRCR' , ctypes.c_uint32),  # SPI RX CRC register (not used in I2S mode),         Address offset: 0x14
			('TXCRCR' , ctypes.c_uint32),  # SPI TX CRC register (not used in I2S mode),         Address offset: 0x18
			('I2SCFGR', ctypes.c_uint32),  # SPI_I2S configuration register,                     Address offset: 0x1C
			('I2SPR'  , ctypes.c_uint32),  # SPI_I2S prescaler register,                         Address offset: 0x20
		]

class STM32F4xxQuadspi:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f423xx.h
		        stm32f469xx.h
		        stm32f479xx.h
		        stm32f413xx.h
		        stm32f412rx.h
		        stm32f412zx.h
		        stm32f446xx.h
		        stm32f412vx.h 
		"""

        _fields_ = [
			('CR'   , ctypes.c_uint32),  # QUADSPI Control register,                           Address offset: 0x00
			('DCR'  , ctypes.c_uint32),  # QUADSPI Device Configuration register,              Address offset: 0x04
			('SR'   , ctypes.c_uint32),  # QUADSPI Status register,                            Address offset: 0x08
			('FCR'  , ctypes.c_uint32),  # QUADSPI Flag Clear register,                        Address offset: 0x0C
			('DLR'  , ctypes.c_uint32),  # QUADSPI Data Length register,                       Address offset: 0x10
			('CCR'  , ctypes.c_uint32),  # QUADSPI Communication Configuration register,       Address offset: 0x14
			('AR'   , ctypes.c_uint32),  # QUADSPI Address register,                           Address offset: 0x18
			('ABR'  , ctypes.c_uint32),  # QUADSPI Alternate Bytes register,                   Address offset: 0x1C
			('DR'   , ctypes.c_uint32),  # QUADSPI Data register,                              Address offset: 0x20
			('PSMKR', ctypes.c_uint32),  # QUADSPI Polling Status Mask register,               Address offset: 0x24
			('PSMAR', ctypes.c_uint32),  # QUADSPI Polling Status Match register,              Address offset: 0x28
			('PIR'  , ctypes.c_uint32),  # QUADSPI Polling Interval register,                  Address offset: 0x2C
			('LPTR' , ctypes.c_uint32),  # QUADSPI Low Power Timeout register,                 Address offset: 0x30
		]

class STM32F4xxTim:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f423xx.h
		        stm32f469xx.h
		        stm32f427xx.h
		        stm32f479xx.h
		        stm32f413xx.h
		        stm32f429xx.h
		        stm32f439xx.h
		        stm32f415xx.h
		        stm32f412cx.h
		        stm32f412rx.h
		        stm32f410tx.h
		        stm32f410cx.h
		        stm32f412zx.h
		        stm32f405xx.h
		        stm32f407xx.h
		        stm32f417xx.h
		        stm32f446xx.h
		        stm32f401xc.h
		        stm32f437xx.h
		        stm32f401xe.h
		        stm32f412vx.h
		        stm32f410rx.h
		        stm32f411xe.h 
		"""

        _fields_ = [
			('CR1'  , ctypes.c_uint32),  # TIM control register 1,              Address offset: 0x00
			('CR2'  , ctypes.c_uint32),  # TIM control register 2,              Address offset: 0x04
			('SMCR' , ctypes.c_uint32),  # TIM slave mode control register,     Address offset: 0x08
			('DIER' , ctypes.c_uint32),  # TIM DMA/interrupt enable register,   Address offset: 0x0C
			('SR'   , ctypes.c_uint32),  # TIM status register,                 Address offset: 0x10
			('EGR'  , ctypes.c_uint32),  # TIM event generation register,       Address offset: 0x14
			('CCMR1', ctypes.c_uint32),  # TIM capture/compare mode register 1, Address offset: 0x18
			('CCMR2', ctypes.c_uint32),  # TIM capture/compare mode register 2, Address offset: 0x1C
			('CCER' , ctypes.c_uint32),  # TIM capture/compare enable register, Address offset: 0x20
			('CNT'  , ctypes.c_uint32),  # TIM counter register,                Address offset: 0x24
			('PSC'  , ctypes.c_uint32),  # TIM prescaler,                       Address offset: 0x28
			('ARR'  , ctypes.c_uint32),  # TIM auto-reload register,            Address offset: 0x2C
			('RCR'  , ctypes.c_uint32),  # TIM repetition counter register,     Address offset: 0x30
			('CCR1' , ctypes.c_uint32),  # TIM capture/compare register 1,      Address offset: 0x34
			('CCR2' , ctypes.c_uint32),  # TIM capture/compare register 2,      Address offset: 0x38
			('CCR3' , ctypes.c_uint32),  # TIM capture/compare register 3,      Address offset: 0x3C
			('CCR4' , ctypes.c_uint32),  # TIM capture/compare register 4,      Address offset: 0x40
			('BDTR' , ctypes.c_uint32),  # TIM break and dead-time register,    Address offset: 0x44
			('DCR'  , ctypes.c_uint32),  # TIM DMA control register,            Address offset: 0x48
			('DMAR' , ctypes.c_uint32),  # TIM DMA address for full transfer,   Address offset: 0x4C
			('OR'   , ctypes.c_uint32),  # TIM option register,                 Address offset: 0x50
		]

class STM32F4xxUsart:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f423xx.h
		        stm32f469xx.h
		        stm32f427xx.h
		        stm32f479xx.h
		        stm32f413xx.h
		        stm32f429xx.h
		        stm32f439xx.h
		        stm32f415xx.h
		        stm32f412cx.h
		        stm32f412rx.h
		        stm32f410tx.h
		        stm32f410cx.h
		        stm32f412zx.h
		        stm32f405xx.h
		        stm32f407xx.h
		        stm32f417xx.h
		        stm32f446xx.h
		        stm32f401xc.h
		        stm32f437xx.h
		        stm32f401xe.h
		        stm32f412vx.h
		        stm32f410rx.h
		        stm32f411xe.h 
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
		        stm32f423xx.h
		        stm32f469xx.h
		        stm32f427xx.h
		        stm32f479xx.h
		        stm32f413xx.h
		        stm32f429xx.h
		        stm32f439xx.h
		        stm32f415xx.h
		        stm32f412cx.h
		        stm32f412rx.h
		        stm32f410tx.h
		        stm32f410cx.h
		        stm32f412zx.h
		        stm32f405xx.h
		        stm32f407xx.h
		        stm32f417xx.h
		        stm32f446xx.h
		        stm32f401xc.h
		        stm32f437xx.h
		        stm32f401xe.h
		        stm32f412vx.h
		        stm32f410rx.h
		        stm32f411xe.h 
		"""

        _fields_ = [
			('CR' , ctypes.c_uint32),  # WWDG Control register,       Address offset: 0x00
			('CFR', ctypes.c_uint32),  # WWDG Configuration register, Address offset: 0x04
			('SR' , ctypes.c_uint32),  # WWDG Status register,        Address offset: 0x08
		]

class STM32F423Aes:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f423xx.h 
		"""

        _fields_ = [
			('CR'    , ctypes.c_uint32),  # AES control register,                        Address offset: 0x00
			('SR'    , ctypes.c_uint32),  # AES status register,                         Address offset: 0x04
			('DINR'  , ctypes.c_uint32),  # AES data input register,                     Address offset: 0x08
			('DOUTR' , ctypes.c_uint32),  # AES data output register,                    Address offset: 0x0C
			('KEYR0' , ctypes.c_uint32),  # AES key register 0,                          Address offset: 0x10
			('KEYR1' , ctypes.c_uint32),  # AES key register 1,                          Address offset: 0x14
			('KEYR2' , ctypes.c_uint32),  # AES key register 2,                          Address offset: 0x18
			('KEYR3' , ctypes.c_uint32),  # AES key register 3,                          Address offset: 0x1C
			('IVR0'  , ctypes.c_uint32),  # AES initialization vector register 0,        Address offset: 0x20
			('IVR1'  , ctypes.c_uint32),  # AES initialization vector register 1,        Address offset: 0x24
			('IVR2'  , ctypes.c_uint32),  # AES initialization vector register 2,        Address offset: 0x28
			('IVR3'  , ctypes.c_uint32),  # AES initialization vector register 3,        Address offset: 0x2C
			('KEYR4' , ctypes.c_uint32),  # AES key register 4,                          Address offset: 0x30
			('KEYR5' , ctypes.c_uint32),  # AES key register 5,                          Address offset: 0x34
			('KEYR6' , ctypes.c_uint32),  # AES key register 6,                          Address offset: 0x38
			('KEYR7' , ctypes.c_uint32),  # AES key register 7,                          Address offset: 0x3C
			('SUSP0R', ctypes.c_uint32),  # AES Suspend register 0,                      Address offset: 0x40
			('SUSP1R', ctypes.c_uint32),  # AES Suspend register 1,                      Address offset: 0x44
			('SUSP2R', ctypes.c_uint32),  # AES Suspend register 2,                      Address offset: 0x48
			('SUSP3R', ctypes.c_uint32),  # AES Suspend register 3,                      Address offset: 0x4C
			('SUSP4R', ctypes.c_uint32),  # AES Suspend register 4,                      Address offset: 0x50
			('SUSP5R', ctypes.c_uint32),  # AES Suspend register 5,                      Address offset: 0x54
			('SUSP6R', ctypes.c_uint32),  # AES Suspend register 6,                      Address offset: 0x58
			('SUSP7R', ctypes.c_uint32),  # AES Suspend register 7,                      Address offset: 0x6C
		]

class STM32F4xxRng:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f423xx.h
		        stm32f469xx.h
		        stm32f427xx.h
		        stm32f479xx.h
		        stm32f413xx.h
		        stm32f429xx.h
		        stm32f439xx.h
		        stm32f415xx.h
		        stm32f412cx.h
		        stm32f412rx.h
		        stm32f410tx.h
		        stm32f410cx.h
		        stm32f412zx.h
		        stm32f405xx.h
		        stm32f407xx.h
		        stm32f417xx.h
		        stm32f437xx.h
		        stm32f412vx.h
		        stm32f410rx.h 
		"""

        _fields_ = [
			('CR', ctypes.c_uint32),  # RNG control register, Address offset: 0x00
			('SR', ctypes.c_uint32),  # RNG status register,  Address offset: 0x04
			('DR', ctypes.c_uint32),  # RNG data register,    Address offset: 0x08
		]

class STM32F4xxUsb_otg_globalV1:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f423xx.h
		        stm32f469xx.h
		        stm32f479xx.h
		        stm32f413xx.h
		        stm32f412cx.h
		        stm32f412rx.h
		        stm32f412zx.h
		        stm32f446xx.h
		        stm32f412vx.h 
		"""

        _fields_ = [
			('GOTGCTL'           , ctypes.c_uint32),       # USB_OTG Control and Status Register          000h
			('GOTGINT'           , ctypes.c_uint32),       # USB_OTG Interrupt Register                   004h
			('GAHBCFG'           , ctypes.c_uint32),       # Core AHB Configuration Register              008h
			('GUSBCFG'           , ctypes.c_uint32),       # Core USB Configuration Register              00Ch
			('GRSTCTL'           , ctypes.c_uint32),       # Core Reset Register                          010h
			('GINTSTS'           , ctypes.c_uint32),       # Core Interrupt Register                      014h
			('GINTMSK'           , ctypes.c_uint32),       # Core Interrupt Mask Register                 018h
			('GRXSTSR'           , ctypes.c_uint32),       # Receive Sts Q Read Register                  01Ch
			('GRXSTSP'           , ctypes.c_uint32),       # Receive Sts Q Read & POP Register            020h
			('GRXFSIZ'           , ctypes.c_uint32),       # Receive FIFO Size Register                   024h
			('DIEPTXF0_HNPTXFSIZ', ctypes.c_uint32),       # EP0 / Non Periodic Tx FIFO Size Register     028h
			('HNPTXSTS'          , ctypes.c_uint32),       # Non Periodic Tx FIFO/Queue Sts reg           02Ch
			('Reserved30'        , ctypes.c_uint32 * 2),   # Reserved                                     030h
			('GCCFG'             , ctypes.c_uint32),       # General Purpose IO Register                  038h
			('CID'               , ctypes.c_uint32),       # User ID Register                             03Ch
			('Reserved5'         , ctypes.c_uint32 * 3),   # Reserved                                040h-048h
			('GHWCFG3'           , ctypes.c_uint32),       # User HW config3                              04Ch
			('Reserved6'         , ctypes.c_uint32),       # Reserved                                     050h
			('GLPMCFG'           , ctypes.c_uint32),       # LPM Register                                 054h
			('Reserved'          , ctypes.c_uint32),       # Reserved                                     058h
			('GDFIFOCFG'         , ctypes.c_uint32),       # DFIFO Software Config Register               05Ch
			('Reserved43'        , ctypes.c_uint32 * 40),  # Reserved                                058h-0FFh
			('HPTXFSIZ'          , ctypes.c_uint32),       # Host Periodic Tx FIFO Size Reg               100h
			('DIEPTXF'           , ctypes.c_uint32 * 15),  # dev Periodic Transmit FIFO
		]

class STM32F4xxUsb_otg_global:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f427xx.h
		        stm32f429xx.h
		        stm32f439xx.h
		        stm32f415xx.h
		        stm32f405xx.h
		        stm32f407xx.h
		        stm32f417xx.h
		        stm32f401xc.h
		        stm32f437xx.h
		        stm32f401xe.h
		        stm32f411xe.h 
		"""

        _fields_ = [
			('GOTGCTL'           , ctypes.c_uint32),       # USB_OTG Control and Status Register          000h
			('GOTGINT'           , ctypes.c_uint32),       # USB_OTG Interrupt Register                   004h
			('GAHBCFG'           , ctypes.c_uint32),       # Core AHB Configuration Register              008h
			('GUSBCFG'           , ctypes.c_uint32),       # Core USB Configuration Register              00Ch
			('GRSTCTL'           , ctypes.c_uint32),       # Core Reset Register                          010h
			('GINTSTS'           , ctypes.c_uint32),       # Core Interrupt Register                      014h
			('GINTMSK'           , ctypes.c_uint32),       # Core Interrupt Mask Register                 018h
			('GRXSTSR'           , ctypes.c_uint32),       # Receive Sts Q Read Register                  01Ch
			('GRXSTSP'           , ctypes.c_uint32),       # Receive Sts Q Read & POP Register            020h
			('GRXFSIZ'           , ctypes.c_uint32),       # Receive FIFO Size Register                   024h
			('DIEPTXF0_HNPTXFSIZ', ctypes.c_uint32),       # EP0 / Non Periodic Tx FIFO Size Register     028h
			('HNPTXSTS'          , ctypes.c_uint32),       # Non Periodic Tx FIFO/Queue Sts reg           02Ch
			('Reserved30'        , ctypes.c_uint32 * 2),   # Reserved                                     030h
			('GCCFG'             , ctypes.c_uint32),       # General Purpose IO Register                  038h
			('CID'               , ctypes.c_uint32),       # User ID Register                             03Ch
			('Reserved40'        , ctypes.c_uint32 * 48),  # Reserved                                0x40-0xFF
			('HPTXFSIZ'          , ctypes.c_uint32),       # Host Periodic Tx FIFO Size Reg               100h
			('DIEPTXF'           , ctypes.c_uint32 * 15),  # dev Periodic Transmit FIFO
		]

class STM32F4xxUsb_otg_device:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f423xx.h
		        stm32f469xx.h
		        stm32f427xx.h
		        stm32f479xx.h
		        stm32f413xx.h
		        stm32f429xx.h
		        stm32f439xx.h
		        stm32f415xx.h
		        stm32f412cx.h
		        stm32f412rx.h
		        stm32f412zx.h
		        stm32f405xx.h
		        stm32f407xx.h
		        stm32f417xx.h
		        stm32f446xx.h
		        stm32f401xc.h
		        stm32f437xx.h
		        stm32f401xe.h
		        stm32f412vx.h
		        stm32f411xe.h 
		"""

        _fields_ = [
			('DCFG'      , ctypes.c_uint32),       # dev Configuration Register   800h
			('DCTL'      , ctypes.c_uint32),       # dev Control Register         804h
			('DSTS'      , ctypes.c_uint32),       # dev Status Register (RO)     808h
			('Reserved0C', ctypes.c_uint32),       # Reserved                     80Ch
			('DIEPMSK'   , ctypes.c_uint32),       # dev IN Endpoint Mask         810h
			('DOEPMSK'   , ctypes.c_uint32),       # dev OUT Endpoint Mask        814h
			('DAINT'     , ctypes.c_uint32),       # dev All Endpoints Itr Reg    818h
			('DAINTMSK'  , ctypes.c_uint32),       # dev All Endpoints Itr Mask   81Ch
			('Reserved20', ctypes.c_uint32),       # Reserved                     820h
			('Reserved9' , ctypes.c_uint32),       # Reserved                     824h
			('DVBUSDIS'  , ctypes.c_uint32),       # dev VBUS discharge Register  828h
			('DVBUSPULSE', ctypes.c_uint32),       # dev VBUS Pulse Register      82Ch
			('DTHRCTL'   , ctypes.c_uint32),       # dev threshold                830h
			('DIEPEMPMSK', ctypes.c_uint32),       # dev empty msk                834h
			('DEACHINT'  , ctypes.c_uint32),       # dedicated EP interrupt       838h
			('DEACHMSK'  , ctypes.c_uint32),       # dedicated EP msk             83Ch
			('Reserved40', ctypes.c_uint32),       # dedicated EP mask            840h
			('DINEP1MSK' , ctypes.c_uint32),       # dedicated EP mask            844h
			('Reserved44', ctypes.c_uint32 * 15),  # Reserved                 844-87Ch
			('DOUTEP1MSK', ctypes.c_uint32),       # dedicated EP msk             884h
		]

class STM32F4xxUsb_otg_inendpoint:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f423xx.h
		        stm32f469xx.h
		        stm32f427xx.h
		        stm32f479xx.h
		        stm32f413xx.h
		        stm32f429xx.h
		        stm32f439xx.h
		        stm32f415xx.h
		        stm32f412cx.h
		        stm32f412rx.h
		        stm32f412zx.h
		        stm32f405xx.h
		        stm32f407xx.h
		        stm32f417xx.h
		        stm32f446xx.h
		        stm32f401xc.h
		        stm32f437xx.h
		        stm32f401xe.h
		        stm32f412vx.h
		        stm32f411xe.h 
		"""

        _fields_ = [
			('DIEPCTL'   , ctypes.c_uint32),  # dev IN Endpoint Control Reg    900h + (ep_num * 20h) + 00h
			('Reserved04', ctypes.c_uint32),  # Reserved                       900h + (ep_num * 20h) + 04h
			('DIEPINT'   , ctypes.c_uint32),  # dev IN Endpoint Itr Reg        900h + (ep_num * 20h) + 08h
			('Reserved0C', ctypes.c_uint32),  # Reserved                       900h + (ep_num * 20h) + 0Ch
			('DIEPTSIZ'  , ctypes.c_uint32),  # IN Endpoint Txfer Size         900h + (ep_num * 20h) + 10h
			('DIEPDMA'   , ctypes.c_uint32),  # IN Endpoint DMA Address Reg    900h + (ep_num * 20h) + 14h
			('DTXFSTS'   , ctypes.c_uint32),  # IN Endpoint Tx FIFO Status Reg 900h + (ep_num * 20h) + 18h
			('Reserved18', ctypes.c_uint32),  # Reserved  900h+(ep_num*20h)+1Ch-900h+ (ep_num * 20h) + 1Ch
		]

class STM32F4xxUsb_otg_outendpoint:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f423xx.h
		        stm32f469xx.h
		        stm32f427xx.h
		        stm32f479xx.h
		        stm32f413xx.h
		        stm32f429xx.h
		        stm32f439xx.h
		        stm32f415xx.h
		        stm32f412cx.h
		        stm32f412rx.h
		        stm32f412zx.h
		        stm32f405xx.h
		        stm32f407xx.h
		        stm32f417xx.h
		        stm32f446xx.h
		        stm32f401xc.h
		        stm32f437xx.h
		        stm32f401xe.h
		        stm32f412vx.h
		        stm32f411xe.h 
		"""

        _fields_ = [
			('DOEPCTL'   , ctypes.c_uint32),      # dev OUT Endpoint Control Reg           B00h + (ep_num * 20h) + 00h
			('Reserved04', ctypes.c_uint32),      # Reserved                               B00h + (ep_num * 20h) + 04h
			('DOEPINT'   , ctypes.c_uint32),      # dev OUT Endpoint Itr Reg               B00h + (ep_num * 20h) + 08h
			('Reserved0C', ctypes.c_uint32),      # Reserved                               B00h + (ep_num * 20h) + 0Ch
			('DOEPTSIZ'  , ctypes.c_uint32),      # dev OUT Endpoint Txfer Size            B00h + (ep_num * 20h) + 10h
			('DOEPDMA'   , ctypes.c_uint32),      # dev OUT Endpoint DMA Address           B00h + (ep_num * 20h) + 14h
			('Reserved18', ctypes.c_uint32 * 2),  # Reserved B00h + (ep_num * 20h) + 18h - B00h + (ep_num * 20h) + 1Ch
		]

class STM32F4xxUsb_otg_host:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f423xx.h
		        stm32f469xx.h
		        stm32f427xx.h
		        stm32f479xx.h
		        stm32f413xx.h
		        stm32f429xx.h
		        stm32f439xx.h
		        stm32f415xx.h
		        stm32f412cx.h
		        stm32f412rx.h
		        stm32f412zx.h
		        stm32f405xx.h
		        stm32f407xx.h
		        stm32f417xx.h
		        stm32f446xx.h
		        stm32f401xc.h
		        stm32f437xx.h
		        stm32f401xe.h
		        stm32f412vx.h
		        stm32f411xe.h 
		"""

        _fields_ = [
			('HCFG'       , ctypes.c_uint32),  # Host Configuration Register          400h
			('HFIR'       , ctypes.c_uint32),  # Host Frame Interval Register         404h
			('HFNUM'      , ctypes.c_uint32),  # Host Frame Nbr/Frame Remaining       408h
			('Reserved40C', ctypes.c_uint32),  # Reserved                             40Ch
			('HPTXSTS'    , ctypes.c_uint32),  # Host Periodic Tx FIFO/ Queue Status  410h
			('HAINT'      , ctypes.c_uint32),  # Host All Channels Interrupt Register 414h
			('HAINTMSK'   , ctypes.c_uint32),  # Host All Channels Interrupt Mask     418h
		]

class STM32F4xxUsb_otg_hostchannel:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f423xx.h
		        stm32f469xx.h
		        stm32f427xx.h
		        stm32f479xx.h
		        stm32f413xx.h
		        stm32f429xx.h
		        stm32f439xx.h
		        stm32f415xx.h
		        stm32f412cx.h
		        stm32f412rx.h
		        stm32f412zx.h
		        stm32f405xx.h
		        stm32f407xx.h
		        stm32f417xx.h
		        stm32f446xx.h
		        stm32f401xc.h
		        stm32f437xx.h
		        stm32f401xe.h
		        stm32f412vx.h
		        stm32f411xe.h 
		"""

        _fields_ = [
			('HCCHAR'  , ctypes.c_uint32),      # Host Channel Characteristics Register    500h
			('HCSPLT'  , ctypes.c_uint32),      # Host Channel Split Control Register      504h
			('HCINT'   , ctypes.c_uint32),      # Host Channel Interrupt Register          508h
			('HCINTMSK', ctypes.c_uint32),      # Host Channel Interrupt Mask Register     50Ch
			('HCTSIZ'  , ctypes.c_uint32),      # Host Channel Transfer Size Register      510h
			('HCDMA'   , ctypes.c_uint32),      # Host Channel DMA Address Register        514h
			('Reserved', ctypes.c_uint32 * 2),  # Reserved
		]

class STM32F4xxLptim:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f423xx.h
		        stm32f413xx.h
		        stm32f410tx.h
		        stm32f410cx.h
		        stm32f410rx.h 
		"""

        _fields_ = [
			('ISR' , ctypes.c_uint32),  # LPTIM Interrupt and Status register,                Address offset: 0x00
			('ICR' , ctypes.c_uint32),  # LPTIM Interrupt Clear register,                     Address offset: 0x04
			('IER' , ctypes.c_uint32),  # LPTIM Interrupt Enable register,                    Address offset: 0x08
			('CFGR', ctypes.c_uint32),  # LPTIM Configuration register,                       Address offset: 0x0C
			('CR'  , ctypes.c_uint32),  # LPTIM Control register,                             Address offset: 0x10
			('CMP' , ctypes.c_uint32),  # LPTIM Compare register,                             Address offset: 0x14
			('ARR' , ctypes.c_uint32),  # LPTIM Autoreload register,                          Address offset: 0x18
			('CNT' , ctypes.c_uint32),  # LPTIM Counter register,                             Address offset: 0x1C
			('OR'  , ctypes.c_uint32),  # LPTIM Option register,                              Address offset: 0x20
		]

class STM32F4xxDcmi:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f469xx.h
		        stm32f427xx.h
		        stm32f479xx.h
		        stm32f429xx.h
		        stm32f439xx.h
		        stm32f407xx.h
		        stm32f417xx.h
		        stm32f446xx.h
		        stm32f437xx.h 
		"""

        _fields_ = [
			('CR'     , ctypes.c_uint32),  # DCMI control register 1,                       Address offset: 0x00
			('SR'     , ctypes.c_uint32),  # DCMI status register,                          Address offset: 0x04
			('RISR'   , ctypes.c_uint32),  # DCMI raw interrupt status register,            Address offset: 0x08
			('IER'    , ctypes.c_uint32),  # DCMI interrupt enable register,                Address offset: 0x0C
			('MISR'   , ctypes.c_uint32),  # DCMI masked interrupt status register,         Address offset: 0x10
			('ICR'    , ctypes.c_uint32),  # DCMI interrupt clear register,                 Address offset: 0x14
			('ESCR'   , ctypes.c_uint32),  # DCMI embedded synchronization code register,   Address offset: 0x18
			('ESUR'   , ctypes.c_uint32),  # DCMI embedded synchronization unmask register, Address offset: 0x1C
			('CWSTRTR', ctypes.c_uint32),  # DCMI crop window start,                        Address offset: 0x20
			('CWSIZER', ctypes.c_uint32),  # DCMI crop window size,                         Address offset: 0x24
			('DR'     , ctypes.c_uint32),  # DCMI data register,                            Address offset: 0x28
		]

class STM32F4xxDma2d:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f469xx.h
		        stm32f427xx.h
		        stm32f479xx.h
		        stm32f429xx.h
		        stm32f439xx.h
		        stm32f437xx.h 
		"""

        _fields_ = [
			('CR'      , ctypes.c_uint32),        # DMA2D Control Register,                         Address offset: 0x00
			('ISR'     , ctypes.c_uint32),        # DMA2D Interrupt Status Register,                Address offset: 0x04
			('IFCR'    , ctypes.c_uint32),        # DMA2D Interrupt Flag Clear Register,            Address offset: 0x08
			('FGMAR'   , ctypes.c_uint32),        # DMA2D Foreground Memory Address Register,       Address offset: 0x0C
			('FGOR'    , ctypes.c_uint32),        # DMA2D Foreground Offset Register,               Address offset: 0x10
			('BGMAR'   , ctypes.c_uint32),        # DMA2D Background Memory Address Register,       Address offset: 0x14
			('BGOR'    , ctypes.c_uint32),        # DMA2D Background Offset Register,               Address offset: 0x18
			('FGPFCCR' , ctypes.c_uint32),        # DMA2D Foreground PFC Control Register,          Address offset: 0x1C
			('FGCOLR'  , ctypes.c_uint32),        # DMA2D Foreground Color Register,                Address offset: 0x20
			('BGPFCCR' , ctypes.c_uint32),        # DMA2D Background PFC Control Register,          Address offset: 0x24
			('BGCOLR'  , ctypes.c_uint32),        # DMA2D Background Color Register,                Address offset: 0x28
			('FGCMAR'  , ctypes.c_uint32),        # DMA2D Foreground CLUT Memory Address Register,  Address offset: 0x2C
			('BGCMAR'  , ctypes.c_uint32),        # DMA2D Background CLUT Memory Address Register,  Address offset: 0x30
			('OPFCCR'  , ctypes.c_uint32),        # DMA2D Output PFC Control Register,              Address offset: 0x34
			('OCOLR'   , ctypes.c_uint32),        # DMA2D Output Color Register,                    Address offset: 0x38
			('OMAR'    , ctypes.c_uint32),        # DMA2D Output Memory Address Register,           Address offset: 0x3C
			('OOR'     , ctypes.c_uint32),        # DMA2D Output Offset Register,                   Address offset: 0x40
			('NLR'     , ctypes.c_uint32),        # DMA2D Number of Line Register,                  Address offset: 0x44
			('LWR'     , ctypes.c_uint32),        # DMA2D Line Watermark Register,                  Address offset: 0x48
			('AMTCR'   , ctypes.c_uint32),        # DMA2D AHB Master Timer Configuration Register,  Address offset: 0x4C
			('RESERVED', ctypes.c_uint32 * 236),  # Reserved, 0x50-0x3FF
			('FGCLUT'  , ctypes.c_uint32 * 256),  # DMA2D Foreground CLUT,                          Address offset:400-7FF
			('BGCLUT'  , ctypes.c_uint32 * 256),  # DMA2D Background CLUT,                          Address offset:800-BFF
		]

class STM32F4xxDsi:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f469xx.h
		        stm32f479xx.h 
		"""

        _fields_ = [
			('VR'        , ctypes.c_uint32),        # DSI Host Version Register,                                 Address offset: 0x00
			('CR'        , ctypes.c_uint32),        # DSI Host Control Register,                                 Address offset: 0x04
			('CCR'       , ctypes.c_uint32),        # DSI HOST Clock Control Register,                           Address offset: 0x08
			('LVCIDR'    , ctypes.c_uint32),        # DSI Host LTDC VCID Register,                               Address offset: 0x0C
			('LCOLCR'    , ctypes.c_uint32),        # DSI Host LTDC Color Coding Register,                       Address offset: 0x10
			('LPCR'      , ctypes.c_uint32),        # DSI Host LTDC Polarity Configuration Register,             Address offset: 0x14
			('LPMCR'     , ctypes.c_uint32),        # DSI Host Low-Power Mode Configuration Register,            Address offset: 0x18
			('RESERVED0' , ctypes.c_uint32 * 4),    # Reserved, 0x1C - 0x2B
			('PCR'       , ctypes.c_uint32),        # DSI Host Protocol Configuration Register,                  Address offset: 0x2C
			('GVCIDR'    , ctypes.c_uint32),        # DSI Host Generic VCID Register,                            Address offset: 0x30
			('MCR'       , ctypes.c_uint32),        # DSI Host Mode Configuration Register,                      Address offset: 0x34
			('VMCR'      , ctypes.c_uint32),        # DSI Host Video Mode Configuration Register,                Address offset: 0x38
			('VPCR'      , ctypes.c_uint32),        # DSI Host Video Packet Configuration Register,              Address offset: 0x3C
			('VCCR'      , ctypes.c_uint32),        # DSI Host Video Chunks Configuration Register,              Address offset: 0x40
			('VNPCR'     , ctypes.c_uint32),        # DSI Host Video Null Packet Configuration Register,         Address offset: 0x44
			('VHSACR'    , ctypes.c_uint32),        # DSI Host Video HSA Configuration Register,                 Address offset: 0x48
			('VHBPCR'    , ctypes.c_uint32),        # DSI Host Video HBP Configuration Register,                 Address offset: 0x4C
			('VLCR'      , ctypes.c_uint32),        # DSI Host Video Line Configuration Register,                Address offset: 0x50
			('VVSACR'    , ctypes.c_uint32),        # DSI Host Video VSA Configuration Register,                 Address offset: 0x54
			('VVBPCR'    , ctypes.c_uint32),        # DSI Host Video VBP Configuration Register,                 Address offset: 0x58
			('VVFPCR'    , ctypes.c_uint32),        # DSI Host Video VFP Configuration Register,                 Address offset: 0x5C
			('VVACR'     , ctypes.c_uint32),        # DSI Host Video VA Configuration Register,                  Address offset: 0x60
			('LCCR'      , ctypes.c_uint32),        # DSI Host LTDC Command Configuration Register,              Address offset: 0x64
			('CMCR'      , ctypes.c_uint32),        # DSI Host Command Mode Configuration Register,              Address offset: 0x68
			('GHCR'      , ctypes.c_uint32),        # DSI Host Generic Header Configuration Register,            Address offset: 0x6C
			('GPDR'      , ctypes.c_uint32),        # DSI Host Generic Payload Data Register,                    Address offset: 0x70
			('GPSR'      , ctypes.c_uint32),        # DSI Host Generic Packet Status Register,                   Address offset: 0x74
			('TCCR'      , ctypes.c_uint32 * 6),    # DSI Host Timeout Counter Configuration Register,           Address offset: 0x78-0x8F
			('TDCR'      , ctypes.c_uint32),        # DSI Host 3D Configuration Register,                        Address offset: 0x90
			('CLCR'      , ctypes.c_uint32),        # DSI Host Clock Lane Configuration Register,                Address offset: 0x94
			('CLTCR'     , ctypes.c_uint32),        # DSI Host Clock Lane Timer Configuration Register,          Address offset: 0x98
			('DLTCR'     , ctypes.c_uint32),        # DSI Host Data Lane Timer Configuration Register,           Address offset: 0x9C
			('PCTLR'     , ctypes.c_uint32),        # DSI Host PHY Control Register,                             Address offset: 0xA0
			('PCONFR'    , ctypes.c_uint32),        # DSI Host PHY Configuration Register,                       Address offset: 0xA4
			('PUCR'      , ctypes.c_uint32),        # DSI Host PHY ULPS Control Register,                        Address offset: 0xA8
			('PTTCR'     , ctypes.c_uint32),        # DSI Host PHY TX Triggers Configuration Register,           Address offset: 0xAC
			('PSR'       , ctypes.c_uint32),        # DSI Host PHY Status Register,                              Address offset: 0xB0
			('RESERVED1' , ctypes.c_uint32 * 2),    # Reserved, 0xB4 - 0xBB
			('ISR'       , ctypes.c_uint32 * 2),    # DSI Host Interrupt & Status Register,                      Address offset: 0xBC-0xC3
			('IER'       , ctypes.c_uint32 * 2),    # DSI Host Interrupt Enable Register,                        Address offset: 0xC4-0xCB
			('RESERVED2' , ctypes.c_uint32 * 3),    # Reserved, 0xD0 - 0xD7
			('FIR'       , ctypes.c_uint32 * 2),    # DSI Host Force Interrupt Register,                         Address offset: 0xD8-0xDF
			('RESERVED3' , ctypes.c_uint32 * 8),    # Reserved, 0xE0 - 0xFF
			('VSCR'      , ctypes.c_uint32),        # DSI Host Video Shadow Control Register,                    Address offset: 0x100
			('RESERVED4' , ctypes.c_uint32 * 2),    # Reserved, 0x104 - 0x10B
			('LCVCIDR'   , ctypes.c_uint32),        # DSI Host LTDC Current VCID Register,                       Address offset: 0x10C
			('LCCCR'     , ctypes.c_uint32),        # DSI Host LTDC Current Color Coding Register,               Address offset: 0x110
			('RESERVED5' , ctypes.c_uint32),        # Reserved, 0x114
			('LPMCCR'    , ctypes.c_uint32),        # DSI Host Low-power Mode Current Configuration Register,    Address offset: 0x118
			('RESERVED6' , ctypes.c_uint32 * 7),    # Reserved, 0x11C - 0x137
			('VMCCR'     , ctypes.c_uint32),        # DSI Host Video Mode Current Configuration Register,        Address offset: 0x138
			('VPCCR'     , ctypes.c_uint32),        # DSI Host Video Packet Current Configuration Register,      Address offset: 0x13C
			('VCCCR'     , ctypes.c_uint32),        # DSI Host Video Chuncks Current Configuration Register,     Address offset: 0x140
			('VNPCCR'    , ctypes.c_uint32),        # DSI Host Video Null Packet Current Configuration Register, Address offset: 0x144
			('VHSACCR'   , ctypes.c_uint32),        # DSI Host Video HSA Current Configuration Register,         Address offset: 0x148
			('VHBPCCR'   , ctypes.c_uint32),        # DSI Host Video HBP Current Configuration Register,         Address offset: 0x14C
			('VLCCR'     , ctypes.c_uint32),        # DSI Host Video Line Current Configuration Register,        Address offset: 0x150
			('VVSACCR'   , ctypes.c_uint32),        # DSI Host Video VSA Current Configuration Register,         Address offset: 0x154
			('VVBPCCR'   , ctypes.c_uint32),        # DSI Host Video VBP Current Configuration Register,         Address offset: 0x158
			('VVFPCCR'   , ctypes.c_uint32),        # DSI Host Video VFP Current Configuration Register,         Address offset: 0x15C
			('VVACCR'    , ctypes.c_uint32),        # DSI Host Video VA Current Configuration Register,          Address offset: 0x160
			('RESERVED7' , ctypes.c_uint32 * 11),   # Reserved, 0x164 - 0x18F
			('TDCCR'     , ctypes.c_uint32),        # DSI Host 3D Current Configuration Register,                Address offset: 0x190
			('RESERVED8' , ctypes.c_uint32 * 155),  # Reserved, 0x194 - 0x3FF
			('WCFGR'     , ctypes.c_uint32),        # DSI Wrapper Configuration Register,                       Address offset: 0x400
			('WCR'       , ctypes.c_uint32),        # DSI Wrapper Control Register,                             Address offset: 0x404
			('WIER'      , ctypes.c_uint32),        # DSI Wrapper Interrupt Enable Register,                    Address offset: 0x408
			('WISR'      , ctypes.c_uint32),        # DSI Wrapper Interrupt and Status Register,                Address offset: 0x40C
			('WIFCR'     , ctypes.c_uint32),        # DSI Wrapper Interrupt Flag Clear Register,                Address offset: 0x410
			('RESERVED9' , ctypes.c_uint32),        # Reserved, 0x414
			('WPCR'      , ctypes.c_uint32 * 5),    # DSI Wrapper PHY Configuration Register,                   Address offset: 0x418-0x42B
			('RESERVED10', ctypes.c_uint32),        # Reserved, 0x42C
			('WRPCR'     , ctypes.c_uint32),        # DSI Wrapper Regulator and PLL Control Register, Address offset: 0x430
		]

class STM32F4xxEth:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f469xx.h
		        stm32f427xx.h
		        stm32f479xx.h
		        stm32f429xx.h
		        stm32f439xx.h
		        stm32f407xx.h
		        stm32f417xx.h
		        stm32f437xx.h 
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
			('RESERVED1'  , ctypes.c_uint32),       
			('MACDBGR'    , ctypes.c_uint32),       
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
			('RESERVED8'  , ctypes.c_uint32),       
			('PTPTSSR'    , ctypes.c_uint32),       
			('RESERVED9'  , ctypes.c_uint32 * 565), 
			('DMABMR'     , ctypes.c_uint32),       
			('DMATPDR'    , ctypes.c_uint32),       
			('DMARPDR'    , ctypes.c_uint32),       
			('DMARDLAR'   , ctypes.c_uint32),       
			('DMATDLAR'   , ctypes.c_uint32),       
			('DMASR'      , ctypes.c_uint32),       
			('DMAOMR'     , ctypes.c_uint32),       
			('DMAIER'     , ctypes.c_uint32),       
			('DMAMFBOCR'  , ctypes.c_uint32),       
			('DMARSWTR'   , ctypes.c_uint32),       
			('RESERVED10' , ctypes.c_uint32 * 8),   
			('DMACHTDR'   , ctypes.c_uint32),       
			('DMACHRDR'   , ctypes.c_uint32),       
			('DMACHTBAR'  , ctypes.c_uint32),       
			('DMACHRBAR'  , ctypes.c_uint32),       
		]

class STM32F4xxFmc_bank1:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f469xx.h
		        stm32f427xx.h
		        stm32f479xx.h
		        stm32f429xx.h
		        stm32f439xx.h
		        stm32f446xx.h
		        stm32f437xx.h 
		"""

        _fields_ = [
			('BTCR', ctypes.c_uint32 * 8),  # NOR/PSRAM chip-select control register(BCR) and chip-select timing register(BTR), Address offset: 0x00-1C
		]

class STM32F4xxFmc_bank1e:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f469xx.h
		        stm32f427xx.h
		        stm32f479xx.h
		        stm32f429xx.h
		        stm32f439xx.h
		        stm32f446xx.h
		        stm32f437xx.h 
		"""

        _fields_ = [
			('BWTR', ctypes.c_uint32 * 7),  # NOR/PSRAM write timing registers, Address offset: 0x104-0x11C
		]

class STM32F4xxFmc_bank3:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f469xx.h
		        stm32f479xx.h
		        stm32f446xx.h 
		"""

        _fields_ = [
			('PCR'     , ctypes.c_uint32),  # NAND Flash control register,                       Address offset: 0x80
			('SR'      , ctypes.c_uint32),  # NAND Flash FIFO status and interrupt register,     Address offset: 0x84
			('PMEM'    , ctypes.c_uint32),  # NAND Flash Common memory space timing register,    Address offset: 0x88
			('PATT'    , ctypes.c_uint32),  # NAND Flash Attribute memory space timing register, Address offset: 0x8C
			('RESERVED', ctypes.c_uint32),  # Reserved, 0x90
			('ECCR'    , ctypes.c_uint32),  # NAND Flash ECC result registers,                   Address offset: 0x94
		]

class STM32F4xxFmc_bank5_6:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f469xx.h
		        stm32f427xx.h
		        stm32f479xx.h
		        stm32f429xx.h
		        stm32f439xx.h
		        stm32f446xx.h
		        stm32f437xx.h 
		"""

        _fields_ = [
			('SDCR' , ctypes.c_uint32 * 2),  # SDRAM Control registers ,      Address offset: 0x140-0x144
			('SDTR' , ctypes.c_uint32 * 2),  # SDRAM Timing registers ,       Address offset: 0x148-0x14C
			('SDCMR', ctypes.c_uint32),      # SDRAM Command Mode register,   Address offset: 0x150
			('SDRTR', ctypes.c_uint32),      # SDRAM Refresh Timer register,  Address offset: 0x154
			('SDSR' , ctypes.c_uint32),      # SDRAM Status register,         Address offset: 0x158
		]

class STM32F4xxLtdc:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f469xx.h
		        stm32f479xx.h
		        stm32f429xx.h
		        stm32f439xx.h 
		"""

        _fields_ = [
			('RESERVED0', ctypes.c_uint32 * 2),  # Reserved, 0x00-0x04
			('SSCR'     , ctypes.c_uint32),      # LTDC Synchronization Size Configuration Register,    Address offset: 0x08
			('BPCR'     , ctypes.c_uint32),      # LTDC Back Porch Configuration Register,              Address offset: 0x0C
			('AWCR'     , ctypes.c_uint32),      # LTDC Active Width Configuration Register,            Address offset: 0x10
			('TWCR'     , ctypes.c_uint32),      # LTDC Total Width Configuration Register,             Address offset: 0x14
			('GCR'      , ctypes.c_uint32),      # LTDC Global Control Register,                        Address offset: 0x18
			('RESERVED1', ctypes.c_uint32 * 2),  # Reserved, 0x1C-0x20
			('SRCR'     , ctypes.c_uint32),      # LTDC Shadow Reload Configuration Register,           Address offset: 0x24
			('RESERVED2', ctypes.c_uint32),      # Reserved, 0x28
			('BCCR'     , ctypes.c_uint32),      # LTDC Background Color Configuration Register,        Address offset: 0x2C
			('RESERVED3', ctypes.c_uint32),      # Reserved, 0x30
			('IER'      , ctypes.c_uint32),      # LTDC Interrupt Enable Register,                      Address offset: 0x34
			('ISR'      , ctypes.c_uint32),      # LTDC Interrupt Status Register,                      Address offset: 0x38
			('ICR'      , ctypes.c_uint32),      # LTDC Interrupt Clear Register,                       Address offset: 0x3C
			('LIPCR'    , ctypes.c_uint32),      # LTDC Line Interrupt Position Configuration Register, Address offset: 0x40
			('CPSR'     , ctypes.c_uint32),      # LTDC Current Position Status Register,               Address offset: 0x44
			('CDSR'     , ctypes.c_uint32),      # LTDC Current Display Status Register,                Address offset: 0x48
		]

class STM32F4xxLtdc_layer:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f469xx.h
		        stm32f479xx.h
		        stm32f429xx.h
		        stm32f439xx.h 
		"""

        _fields_ = [
			('CR'       , ctypes.c_uint32),      # LTDC Layerx Control Register                                  Address offset: 0x84
			('WHPCR'    , ctypes.c_uint32),      # LTDC Layerx Window Horizontal Position Configuration Register Address offset: 0x88
			('WVPCR'    , ctypes.c_uint32),      # LTDC Layerx Window Vertical Position Configuration Register   Address offset: 0x8C
			('CKCR'     , ctypes.c_uint32),      # LTDC Layerx Color Keying Configuration Register               Address offset: 0x90
			('PFCR'     , ctypes.c_uint32),      # LTDC Layerx Pixel Format Configuration Register               Address offset: 0x94
			('CACR'     , ctypes.c_uint32),      # LTDC Layerx Constant Alpha Configuration Register             Address offset: 0x98
			('DCCR'     , ctypes.c_uint32),      # LTDC Layerx Default Color Configuration Register              Address offset: 0x9C
			('BFCR'     , ctypes.c_uint32),      # LTDC Layerx Blending Factors Configuration Register           Address offset: 0xA0
			('RESERVED0', ctypes.c_uint32 * 2),  # Reserved
			('CFBAR'    , ctypes.c_uint32),      # LTDC Layerx Color Frame Buffer Address Register               Address offset: 0xAC
			('CFBLR'    , ctypes.c_uint32),      # LTDC Layerx Color Frame Buffer Length Register                Address offset: 0xB0
			('CFBLNR'   , ctypes.c_uint32),      # LTDC Layerx ColorFrame Buffer Line Number Register            Address offset: 0xB4
			('RESERVED1', ctypes.c_uint32 * 3),  # Reserved
			('CLUTWR'   , ctypes.c_uint32),      # LTDC Layerx CLUT Write Register                               Address offset: 0x144
		]

class STM32F4xxFmc_bank2_3:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f427xx.h
		        stm32f429xx.h
		        stm32f439xx.h
		        stm32f437xx.h 
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

class STM32F4xxFmc_bank4:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f427xx.h
		        stm32f429xx.h
		        stm32f439xx.h
		        stm32f437xx.h 
		"""

        _fields_ = [
			('PCR4' , ctypes.c_uint32),  # PC Card  control register 4,                       Address offset: 0xA0
			('SR4'  , ctypes.c_uint32),  # PC Card  FIFO status and interrupt register 4,     Address offset: 0xA4
			('PMEM4', ctypes.c_uint32),  # PC Card  Common memory space timing register 4,    Address offset: 0xA8
			('PATT4', ctypes.c_uint32),  # PC Card  Attribute memory space timing register 4, Address offset: 0xAC
			('PIO4' , ctypes.c_uint32),  # PC Card  I/O space timing register 4,              Address offset: 0xB0
		]

class STM32F4xxCryp:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f479xx.h
		        stm32f439xx.h
		        stm32f415xx.h
		        stm32f417xx.h
		        stm32f437xx.h 
		"""

        _fields_ = [
			('CR'        , ctypes.c_uint32),  # CRYP control register,                                    Address offset: 0x00
			('SR'        , ctypes.c_uint32),  # CRYP status register,                                     Address offset: 0x04
			('DIN'       , ctypes.c_uint32),  # CRYP data input register,                                 Address offset: 0x08
			('DOUT'      , ctypes.c_uint32),  # CRYP data output register,                                Address offset: 0x0C
			('DMACR'     , ctypes.c_uint32),  # CRYP DMA control register,                                Address offset: 0x10
			('IMSCR'     , ctypes.c_uint32),  # CRYP interrupt mask set/clear register,                   Address offset: 0x14
			('RISR'      , ctypes.c_uint32),  # CRYP raw interrupt status register,                       Address offset: 0x18
			('MISR'      , ctypes.c_uint32),  # CRYP masked interrupt status register,                    Address offset: 0x1C
			('K0LR'      , ctypes.c_uint32),  # CRYP key left  register 0,                                Address offset: 0x20
			('K0RR'      , ctypes.c_uint32),  # CRYP key right register 0,                                Address offset: 0x24
			('K1LR'      , ctypes.c_uint32),  # CRYP key left  register 1,                                Address offset: 0x28
			('K1RR'      , ctypes.c_uint32),  # CRYP key right register 1,                                Address offset: 0x2C
			('K2LR'      , ctypes.c_uint32),  # CRYP key left  register 2,                                Address offset: 0x30
			('K2RR'      , ctypes.c_uint32),  # CRYP key right register 2,                                Address offset: 0x34
			('K3LR'      , ctypes.c_uint32),  # CRYP key left  register 3,                                Address offset: 0x38
			('K3RR'      , ctypes.c_uint32),  # CRYP key right register 3,                                Address offset: 0x3C
			('IV0LR'     , ctypes.c_uint32),  # CRYP initialization vector left-word  register 0,         Address offset: 0x40
			('IV0RR'     , ctypes.c_uint32),  # CRYP initialization vector right-word register 0,         Address offset: 0x44
			('IV1LR'     , ctypes.c_uint32),  # CRYP initialization vector left-word  register 1,         Address offset: 0x48
			('IV1RR'     , ctypes.c_uint32),  # CRYP initialization vector right-word register 1,         Address offset: 0x4C
			('CSGCMCCM0R', ctypes.c_uint32),  # CRYP GCM/GMAC or CCM/CMAC context swap register 0,        Address offset: 0x50
			('CSGCMCCM1R', ctypes.c_uint32),  # CRYP GCM/GMAC or CCM/CMAC context swap register 1,        Address offset: 0x54
			('CSGCMCCM2R', ctypes.c_uint32),  # CRYP GCM/GMAC or CCM/CMAC context swap register 2,        Address offset: 0x58
			('CSGCMCCM3R', ctypes.c_uint32),  # CRYP GCM/GMAC or CCM/CMAC context swap register 3,        Address offset: 0x5C
			('CSGCMCCM4R', ctypes.c_uint32),  # CRYP GCM/GMAC or CCM/CMAC context swap register 4,        Address offset: 0x60
			('CSGCMCCM5R', ctypes.c_uint32),  # CRYP GCM/GMAC or CCM/CMAC context swap register 5,        Address offset: 0x64
			('CSGCMCCM6R', ctypes.c_uint32),  # CRYP GCM/GMAC or CCM/CMAC context swap register 6,        Address offset: 0x68
			('CSGCMCCM7R', ctypes.c_uint32),  # CRYP GCM/GMAC or CCM/CMAC context swap register 7,        Address offset: 0x6C
			('CSGCM0R'   , ctypes.c_uint32),  # CRYP GCM/GMAC context swap register 0,                    Address offset: 0x70
			('CSGCM1R'   , ctypes.c_uint32),  # CRYP GCM/GMAC context swap register 1,                    Address offset: 0x74
			('CSGCM2R'   , ctypes.c_uint32),  # CRYP GCM/GMAC context swap register 2,                    Address offset: 0x78
			('CSGCM3R'   , ctypes.c_uint32),  # CRYP GCM/GMAC context swap register 3,                    Address offset: 0x7C
			('CSGCM4R'   , ctypes.c_uint32),  # CRYP GCM/GMAC context swap register 4,                    Address offset: 0x80
			('CSGCM5R'   , ctypes.c_uint32),  # CRYP GCM/GMAC context swap register 5,                    Address offset: 0x84
			('CSGCM6R'   , ctypes.c_uint32),  # CRYP GCM/GMAC context swap register 6,                    Address offset: 0x88
			('CSGCM7R'   , ctypes.c_uint32),  # CRYP GCM/GMAC context swap register 7,                    Address offset: 0x8C
		]

class STM32F4xxHash:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f479xx.h
		        stm32f439xx.h
		        stm32f415xx.h
		        stm32f417xx.h
		        stm32f437xx.h 
		"""

        _fields_ = [
			('CR'      , ctypes.c_uint32),       # HASH control register,          Address offset: 0x00
			('DIN'     , ctypes.c_uint32),       # HASH data input register,       Address offset: 0x04
			('STR'     , ctypes.c_uint32),       # HASH start register,            Address offset: 0x08
			('HR'      , ctypes.c_uint32 * 5),   # HASH digest registers,          Address offset: 0x0C-0x1C
			('IMR'     , ctypes.c_uint32),       # HASH interrupt enable register, Address offset: 0x20
			('SR'      , ctypes.c_uint32),       # HASH status register,           Address offset: 0x24
			('RESERVED', ctypes.c_uint32 * 52),  # Reserved, 0x28-0xF4
			('CSR'     , ctypes.c_uint32 * 54),  # HASH context swap registers,    Address offset: 0x0F8-0x1CC
		]

class STM32F4xxHash_digestV1:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f479xx.h
		        stm32f439xx.h
		        stm32f437xx.h 
		"""

        _fields_ = [
			('HR', ctypes.c_uint32 * 8),  # HASH digest registers,          Address offset: 0x310-0x32C
		]

class STM32F4xxHash_digestV2:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f415xx.h
		        stm32f417xx.h 
		"""

        _fields_ = [
			('HR', ctypes.c_uint32 * 5),  # HASH digest registers,          Address offset: 0x310-0x32C
		]

class STM32F4xxFsmc_bank2_3:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f415xx.h
		        stm32f405xx.h
		        stm32f407xx.h
		        stm32f417xx.h 
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
		        stm32f415xx.h
		        stm32f405xx.h
		        stm32f407xx.h
		        stm32f417xx.h 
		"""

        _fields_ = [
			('PCR4' , ctypes.c_uint32),  # PC Card  control register 4,                       Address offset: 0xA0
			('SR4'  , ctypes.c_uint32),  # PC Card  FIFO status and interrupt register 4,     Address offset: 0xA4
			('PMEM4', ctypes.c_uint32),  # PC Card  Common memory space timing register 4,    Address offset: 0xA8
			('PATT4', ctypes.c_uint32),  # PC Card  Attribute memory space timing register 4, Address offset: 0xAC
			('PIO4' , ctypes.c_uint32),  # PC Card  I/O space timing register 4,              Address offset: 0xB0
		]

class STM32F446Cec:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f446xx.h 
		"""

        _fields_ = [
			('CR'  , ctypes.c_uint32),  # CEC control register,              Address offset:0x00
			('CFGR', ctypes.c_uint32),  # CEC configuration register,        Address offset:0x04
			('TXDR', ctypes.c_uint32),  # CEC Tx data register ,             Address offset:0x08
			('RXDR', ctypes.c_uint32),  # CEC Rx Data Register,              Address offset:0x0C
			('ISR' , ctypes.c_uint32),  # CEC Interrupt and Status Register, Address offset:0x10
			('IER' , ctypes.c_uint32),  # CEC interrupt enable register,     Address offset:0x14
		]

class STM32F446Spdifrx:
	class Type(ctypes.Structure):
		""" the structure is available in :
		        stm32f446xx.h 
		"""

        _fields_ = [
			('CR'       , ctypes.c_uint32),  # Control register,                   Address offset: 0x00
			('IMR'      , ctypes.c_uint8),   # Interrupt mask register,            Address offset: 0x04
			('RESERVED0', ctypes.c_uint8),   # Reserved,  0x06
			('SR'       , ctypes.c_uint32),  # Status register,                    Address offset: 0x08
			('IFCR'     , ctypes.c_uint8),   # Interrupt Flag Clear register,      Address offset: 0x0C
			('RESERVED1', ctypes.c_uint8),   # Reserved,  0x0E
			('DR'       , ctypes.c_uint32),  # Data input register,                Address offset: 0x10
			('CSR'      , ctypes.c_uint32),  # Channel Status register,            Address offset: 0x14
			('DIR'      , ctypes.c_uint32),  # Debug Information register,         Address offset: 0x18
			('RESERVED2', ctypes.c_uint8),   # Reserved,  0x1A
		]

