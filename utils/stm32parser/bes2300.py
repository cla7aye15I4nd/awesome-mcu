import ctypes

class BES2300Spi:
    class Type(ctypes.Structure):
        _fields_ = [
            ("SSPCR0"  , ctypes.c_uint32),        # 0x00000000
            ("SSPCR1"  , ctypes.c_uint32),        # 0x00000004
            ("SSPDR"   , ctypes.c_uint32),        # 0x00000008
            ("SSPSR"   , ctypes.c_uint32),        # 0x0000000C
            ("SSPCPSR" , ctypes.c_uint32),        # 0x00000010
            ("SSPIMSC" , ctypes.c_uint32),        # 0x00000014
            ("SSPRIS"  , ctypes.c_uint32),        # 0x00000018
            ("SSPMIS"  , ctypes.c_uint32),        # 0x0000001C
            ("SSPICR"  , ctypes.c_uint32),        # 0x00000020
            ("SSPDMACR", ctypes.c_uint32),        # 0x00000024
            ("reserved", ctypes.c_uint32 * 0x18), # 0x00000028
            ("SSPRXCR" , ctypes.c_uint32),        # 0x00000088
        ]

class BES2300Dma:
    class Type(ctypes.Structure):
        _fields_ = [
            ("SRCADDR"  , ctypes.c_uint32),     #  0x100+N*0x20 DMA Channel Source Address Register
            ("DSTADDR"  , ctypes.c_uint32),     #  0x104+N*0x20 DMA Channel Destination Address Register
            ("LLI"      , ctypes.c_uint32),     #  0x108+N*0x20 DMA Channel Linked List Item Register
            ("CONTROL"  , ctypes.c_uint32),     #  0x10C+N*0x20 DMA Channel Control Register
            ("CONFIG"   , ctypes.c_uint32),     #  0x110+N*0x20 DMA Channel Configuration Register
            ("RESERVED1", ctypes.c_uint32 * 3), #  0x114+N*0x20
        ]

class BES2300Transq:
    class Type(ctypes.Structure):
        _fields_ = [
            ("CTRL"         , ctypes.c_uint32), #  0x000
            ("RMT_INTMASK"  , ctypes.c_uint32), #  0x004
            ("RMT_INTSET"   , ctypes.c_uint32), #  0x008
            ("LDONE_INTMASK", ctypes.c_uint32), #  0x00C
        ]

class BES2300Rtc:
    class Type(ctypes.Structure):
        _fields_ = [
            ("RTCDR"  , ctypes.c_uint32), #  0x000
            ("RTCMR"  , ctypes.c_uint32), #  0x004
            ("RTCLR"  , ctypes.c_uint32), #  0x008
            ("RTCCR"  , ctypes.c_uint32), #  0x00C
            ("RTCIMSC", ctypes.c_uint32), #  0x010
            ("RTCRIS" , ctypes.c_uint32), #  0x014
            ("RTCMIS" , ctypes.c_uint32), #  0x018
            ("RTCICR" , ctypes.c_uint32), #  0x01C
        ]

class BES2300Norflash:
    class Type(ctypes.Structure):
        _fields_ = [
            ("REG_000", ctypes.c_uint32), # 
            ("REG_004", ctypes.c_uint32), # 
        ]

class BES2300Pwm:
    class Type(ctypes.Structure):
        _fields_ = [
            ("ID"      , ctypes.c_uint32), #  0x000
            ("EN"      , ctypes.c_uint32), #  0x004
            ("INV"     , ctypes.c_uint32), #  0x008
            ("PHASE01" , ctypes.c_uint32), #  0x00C
            ("PHASE23" , ctypes.c_uint32), #  0x010
            ("LOAD01"  , ctypes.c_uint32), #  0x014
            ("LOAD23"  , ctypes.c_uint32), #  0x018
            ("TOGGLE01", ctypes.c_uint32), #  0x01C
            ("TOGGLE23", ctypes.c_uint32), #  0x020
            ("PHASEMOD", ctypes.c_uint32), #  0x024
        ]

class BES2300Uart:
    class Type(ctypes.Structure):
        _fields_ = [
            ("UARTDR", ctypes.c_uint32), #  0x000
        ]

class BES2300Aoncmu:
    class Type(ctypes.Structure):
        _fields_ = [
            ("CHIP_ID"        , ctypes.c_uint32),        #  0x00
            ("TOP_CLK_ENABLE" , ctypes.c_uint32),        #  0x04
            ("TOP_CLK_DISABLE", ctypes.c_uint32),        #  0x08
            ("RESET_PULSE"    , ctypes.c_uint32),        #  0x0C
            ("RESET_SET"      , ctypes.c_uint32),        #  0x10
            ("RESET_CLR"      , ctypes.c_uint32),        #  0x14
            ("CLK_SELECT"     , ctypes.c_uint32),        #  0x18
            ("CLK_OUT"        , ctypes.c_uint32),        #  0x1C
            ("WRITE_UNLOCK"   , ctypes.c_uint32),        #  0x20
            ("MEMSC"          , ctypes.c_uint32 * 4),    #  0x24
            ("MEMSC_STATUS"   , ctypes.c_uint32),        #  0x34
            ("BOOTMODE"       , ctypes.c_uint32),        #  0x38
            ("RESERVED_03C"   , ctypes.c_uint32),        #  0x3C
            ("MOD_CLK_ENABLE" , ctypes.c_uint32),        #  0x40
            ("MOD_CLK_DISABLE", ctypes.c_uint32),        #  0x44
            ("MOD_CLK_MODE"   , ctypes.c_uint32),        #  0x48
            ("CODEC_DIV"      , ctypes.c_uint32),        #  0x4C
            ("TIMER_CLK"      , ctypes.c_uint32),        #  0x50
            ("PWM01_CLK"      , ctypes.c_uint32),        #  0x54
            ("PWM23_CLK"      , ctypes.c_uint32),        #  0x58
            ("RAM_CFG"        , ctypes.c_uint32),        #  0x5C
            ("RESERVED_060"   , ctypes.c_uint32),        #  0x60
            ("PCM_I2S_CLK"    , ctypes.c_uint32),        #  0x64
            ("SPDIF_CLK"      , ctypes.c_uint32),        #  0x68
            ("SLEEP_TIMER_OSC", ctypes.c_uint32),        #  0x6C
            ("SLEEP_TIMER_32K", ctypes.c_uint32),        #  0x70
            ("STORE_GPIO_MASK", ctypes.c_uint32),        #  0x74
            ("CODEC_IIR"      , ctypes.c_uint32),        #  0x78
            ("RESERVED_07C"   , ctypes.c_uint32 * 0x1D), #  0x7C
            ("WAKEUP_PC"      , ctypes.c_uint32),        #  0xF0
            ("DEBUG_RES"      , ctypes.c_uint32 * 2),    #  0xF4
            ("CHIP_FEATURE"   , ctypes.c_uint32),        #  0xFC
        ]

class BES2300Codec:
    class Type(ctypes.Structure):
        _fields_ = [
            ("REG_000", ctypes.c_uint32), # 
            ("REG_004", ctypes.c_uint32), # 
            ("REG_008", ctypes.c_uint32), # 
            ("REG_00C", ctypes.c_uint32), # 
            ("REG_010", ctypes.c_uint32), # 
            ("REG_014", ctypes.c_uint32), # 
            ("REG_018", ctypes.c_uint32), # 
            ("REG_01C", ctypes.c_uint32), # 
            ("REG_020", ctypes.c_uint32), # 
            ("REG_024", ctypes.c_uint32), # 
            ("REG_028", ctypes.c_uint32), # 
            ("REG_02C", ctypes.c_uint32), # 
            ("REG_030", ctypes.c_uint32), # 
            ("REG_034", ctypes.c_uint32), # 
            ("REG_038", ctypes.c_uint32), # 
            ("REG_03C", ctypes.c_uint32), # 
            ("REG_040", ctypes.c_uint32), # 
            ("REG_044", ctypes.c_uint32), # 
            ("REG_048", ctypes.c_uint32), # 
            ("REG_04C", ctypes.c_uint32), # 
            ("REG_050", ctypes.c_uint32), # 
            ("REG_054", ctypes.c_uint32), # 
            ("REG_058", ctypes.c_uint32), # 
            ("REG_05C", ctypes.c_uint32), # 
            ("REG_060", ctypes.c_uint32), # 
            ("REG_064", ctypes.c_uint32), # 
            ("REG_068", ctypes.c_uint32), # 
            ("REG_06C", ctypes.c_uint32), # 
            ("REG_070", ctypes.c_uint32), # 
            ("REG_074", ctypes.c_uint32), # 
            ("REG_078", ctypes.c_uint32), # 
            ("REG_07C", ctypes.c_uint32), # 
            ("REG_080", ctypes.c_uint32), # 
            ("REG_084", ctypes.c_uint32), # 
            ("REG_088", ctypes.c_uint32), # 
            ("REG_08C", ctypes.c_uint32), # 
            ("REG_090", ctypes.c_uint32), # 
            ("REG_094", ctypes.c_uint32), # 
            ("REG_098", ctypes.c_uint32), # 
            ("REG_09C", ctypes.c_uint32), # 
            ("REG_0A0", ctypes.c_uint32), # 
            ("REG_0A4", ctypes.c_uint32), # 
            ("REG_0A8", ctypes.c_uint32), # 
            ("REG_0AC", ctypes.c_uint32), # 
            ("REG_0B0", ctypes.c_uint32), # 
            ("REG_0B4", ctypes.c_uint32), # 
            ("REG_0B8", ctypes.c_uint32), # 
            ("REG_0BC", ctypes.c_uint32), # 
            ("REG_0C0", ctypes.c_uint32), # 
            ("REG_0C4", ctypes.c_uint32), # 
            ("REG_0C8", ctypes.c_uint32), # 
            ("REG_0CC", ctypes.c_uint32), # 
            ("REG_0D0", ctypes.c_uint32), # 
            ("REG_0D4", ctypes.c_uint32), # 
            ("REG_0D8", ctypes.c_uint32), # 
            ("REG_0DC", ctypes.c_uint32), # 
            ("REG_0E0", ctypes.c_uint32), # 
            ("REG_0E4", ctypes.c_uint32), # 
            ("REG_0E8", ctypes.c_uint32), # 
            ("REG_0EC", ctypes.c_uint32), # 
            ("REG_0F0", ctypes.c_uint32), # 
            ("REG_0F4", ctypes.c_uint32), # 
            ("REG_0F8", ctypes.c_uint32), # 
            ("REG_0FC", ctypes.c_uint32), # 
            ("REG_100", ctypes.c_uint32), # 
            ("REG_104", ctypes.c_uint32), # 
            ("REG_108", ctypes.c_uint32), # 
            ("REG_10C", ctypes.c_uint32), # 
            ("REG_110", ctypes.c_uint32), # 
            ("REG_114", ctypes.c_uint32), # 
            ("REG_118", ctypes.c_uint32), # 
            ("REG_11C", ctypes.c_uint32), # 
            ("REG_120", ctypes.c_uint32), # 
            ("REG_124", ctypes.c_uint32), # 
            ("REG_128", ctypes.c_uint32), # 
            ("REG_12C", ctypes.c_uint32), # 
            ("REG_130", ctypes.c_uint32), # 
            ("REG_134", ctypes.c_uint32), # 
            ("REG_138", ctypes.c_uint32), # 
            ("REG_13C", ctypes.c_uint32), # 
            ("REG_140", ctypes.c_uint32), # 
            ("REG_144", ctypes.c_uint32), # 
            ("REG_148", ctypes.c_uint32), # 
            ("REG_14C", ctypes.c_uint32), # 
            ("REG_150", ctypes.c_uint32), # 
            ("REG_154", ctypes.c_uint32), # 
            ("REG_158", ctypes.c_uint32), # 
            ("REG_15C", ctypes.c_uint32), # 
            ("REG_160", ctypes.c_uint32), # 
            ("REG_164", ctypes.c_uint32), # 
            ("REG_168", ctypes.c_uint32), # 
            ("REG_16C", ctypes.c_uint32), # 
            ("REG_170", ctypes.c_uint32), # 
            ("REG_174", ctypes.c_uint32), # 
            ("REG_178", ctypes.c_uint32), # 
            ("REG_17C", ctypes.c_uint32), # 
            ("REG_180", ctypes.c_uint32), # 
            ("REG_184", ctypes.c_uint32), # 
            ("REG_188", ctypes.c_uint32), # 
            ("REG_18C", ctypes.c_uint32), # 
            ("REG_190", ctypes.c_uint32), # 
            ("REG_194", ctypes.c_uint32), # 
            ("REG_198", ctypes.c_uint32), # 
            ("REG_19C", ctypes.c_uint32), # 
            ("REG_1A0", ctypes.c_uint32), # 
            ("REG_1A4", ctypes.c_uint32), # 
            ("REG_1A8", ctypes.c_uint32), # 
            ("REG_1AC", ctypes.c_uint32), # 
            ("REG_1B0", ctypes.c_uint32), # 
            ("REG_1B4", ctypes.c_uint32), # 
            ("REG_1B8", ctypes.c_uint32), # 
            ("REG_1BC", ctypes.c_uint32), # 
            ("REG_1C0", ctypes.c_uint32), # 
            ("REG_1C4", ctypes.c_uint32), # 
            ("REG_1C8", ctypes.c_uint32), # 
            ("REG_1CC", ctypes.c_uint32), # 
            ("REG_1D0", ctypes.c_uint32), # 
            ("REG_1D4", ctypes.c_uint32), # 
            ("REG_1D8", ctypes.c_uint32), # 
            ("REG_1DC", ctypes.c_uint32), # 
            ("REG_1E0", ctypes.c_uint32), # 
            ("REG_1E4", ctypes.c_uint32), # 
            ("REG_1E8", ctypes.c_uint32), # 
            ("REG_1EC", ctypes.c_uint32), # 
            ("REG_1F0", ctypes.c_uint32), # 
            ("REG_1F4", ctypes.c_uint32), # 
            ("REG_1F8", ctypes.c_uint32), # 
            ("REG_1FC", ctypes.c_uint32), # 
            ("REG_200", ctypes.c_uint32), # 
            ("REG_204", ctypes.c_uint32), # 
            ("REG_208", ctypes.c_uint32), # 
            ("REG_20C", ctypes.c_uint32), # 
            ("REG_210", ctypes.c_uint32), # 
            ("REG_214", ctypes.c_uint32), # 
            ("REG_218", ctypes.c_uint32), # 
            ("REG_21C", ctypes.c_uint32), # 
            ("REG_220", ctypes.c_uint32), # 
            ("REG_224", ctypes.c_uint32), # 
        ]

class BES2300Btcmu:
    class Type(ctypes.Structure):
        _fields_ = [
            ("CLK_ENABLE"  , ctypes.c_uint32),        #  0x00
            ("CLK_DISABLE" , ctypes.c_uint32),        #  0x04
            ("CLK_MODE"    , ctypes.c_uint32),        #  0x08
            ("DIV_TIMER"   , ctypes.c_uint32),        #  0x0C
            ("RESET_SET"   , ctypes.c_uint32),        #  0x10
            ("RESET_CLR"   , ctypes.c_uint32),        #  0x14
            ("DIV_WDT"     , ctypes.c_uint32),        #  0x18
            ("RESET_PULSE" , ctypes.c_uint32),        #  0x1C
            ("RESERVED_020", ctypes.c_uint32 * 0x24), #  0x20
            ("CLK_OUT"     , ctypes.c_uint32),        #  0x44
            ("RESERVED_048", ctypes.c_uint32 * 2),    #  0x48
            ("ISIRQ_SET"   , ctypes.c_uint32),        #  0x50
            ("ISIRQ_CLR"   , ctypes.c_uint32),        #  0x54
        ]

class BES2300Iomux:
    class Type(ctypes.Structure):
        _fields_ = [
            ("REG_000", ctypes.c_uint32), # 
            ("REG_004", ctypes.c_uint32), # 
            ("REG_008", ctypes.c_uint32), # 
            ("REG_00C", ctypes.c_uint32), # 
            ("REG_010", ctypes.c_uint32), # 
            ("REG_014", ctypes.c_uint32), # 
            ("REG_018", ctypes.c_uint32), # 
            ("REG_01C", ctypes.c_uint32), # 
            ("REG_020", ctypes.c_uint32), # 
            ("REG_024", ctypes.c_uint32), # 
            ("REG_028", ctypes.c_uint32), # 
            ("REG_02C", ctypes.c_uint32), # 
            ("REG_030", ctypes.c_uint32), # 
            ("REG_034", ctypes.c_uint32), # 
            ("REG_038", ctypes.c_uint32), # 
            ("REG_03C", ctypes.c_uint32), # 
            ("REG_040", ctypes.c_uint32), # 
            ("REG_044", ctypes.c_uint32), # 
            ("REG_048", ctypes.c_uint32), # 
            ("REG_04C", ctypes.c_uint32), # 
            ("REG_050", ctypes.c_uint32), # 
            ("REG_054", ctypes.c_uint32), # 
            ("REG_058", ctypes.c_uint32), # 
            ("REG_05C", ctypes.c_uint32), # 
            ("REG_060", ctypes.c_uint32), # 
            ("REG_064", ctypes.c_uint32), # 
            ("REG_068", ctypes.c_uint32), # 
            ("REG_06C", ctypes.c_uint32), # 
            ("REG_070", ctypes.c_uint32), # 
            ("REG_074", ctypes.c_uint32), # 
            ("REG_078", ctypes.c_uint32), # 
        ]

class BES2300Psc:
    class Type(ctypes.Structure):
        _fields_ = [
            ("REG_000", ctypes.c_uint32), # 
            ("REG_004", ctypes.c_uint32), # 
            ("REG_008", ctypes.c_uint32), # 
            ("REG_00C", ctypes.c_uint32), # 
            ("REG_010", ctypes.c_uint32), # 
            ("REG_014", ctypes.c_uint32), # 
            ("REG_018", ctypes.c_uint32), # 
            ("REG_01C", ctypes.c_uint32), # 
            ("REG_020", ctypes.c_uint32), # 
            ("REG_024", ctypes.c_uint32), # 
            ("REG_028", ctypes.c_uint32), # 
            ("REG_02C", ctypes.c_uint32), # 
            ("REG_030", ctypes.c_uint32), # 
            ("REG_034", ctypes.c_uint32), # 
            ("REG_038", ctypes.c_uint32), # 
            ("REG_03C", ctypes.c_uint32), # 
            ("REG_040", ctypes.c_uint32), # 
            ("REG_044", ctypes.c_uint32), # 
            ("REG_048", ctypes.c_uint32), # 
            ("REG_04C", ctypes.c_uint32), # 
            ("REG_050", ctypes.c_uint32), # 
            ("REG_054", ctypes.c_uint32), # 
            ("REG_058", ctypes.c_uint32), # 
            ("REG_05C", ctypes.c_uint32), # 
            ("REG_060", ctypes.c_uint32), # 
            ("REG_064", ctypes.c_uint32), # 
            ("REG_068", ctypes.c_uint32), # 
            ("REG_06C", ctypes.c_uint32), # 
            ("REG_070", ctypes.c_uint32), # 
            ("REG_074", ctypes.c_uint32), # 
            ("REG_078", ctypes.c_uint32), # 
            ("REG_07C", ctypes.c_uint32), # 
            ("REG_080", ctypes.c_uint32), # 
            ("REG_084", ctypes.c_uint32), # 
            ("REG_088", ctypes.c_uint32), # 
            ("REG_08C", ctypes.c_uint32), # 
            ("REG_090", ctypes.c_uint32), # 
            ("REG_094", ctypes.c_uint32), # 
            ("REG_098", ctypes.c_uint32), # 
            ("REG_09C", ctypes.c_uint32), # 
            ("REG_0A0", ctypes.c_uint32), # 
            ("REG_0A4", ctypes.c_uint32), # 
            ("REG_0A8", ctypes.c_uint32), # 
            ("REG_0AC", ctypes.c_uint32), # 
            ("REG_0B0", ctypes.c_uint32), # 
            ("REG_0B4", ctypes.c_uint32), # 
        ]

class BES2300Cmu:
    class Type(ctypes.Structure):
        _fields_ = [
            ("HCLK_ENABLE"    , ctypes.c_uint32),     #  0x00
            ("HCLK_DISABLE"   , ctypes.c_uint32),     #  0x04
            ("PCLK_ENABLE"    , ctypes.c_uint32),     #  0x08
            ("PCLK_DISABLE"   , ctypes.c_uint32),     #  0x0C
            ("OCLK_ENABLE"    , ctypes.c_uint32),     #  0x10
            ("OCLK_DISABLE"   , ctypes.c_uint32),     #  0x14
            ("HCLK_MODE"      , ctypes.c_uint32),     #  0x18
            ("PCLK_MODE"      , ctypes.c_uint32),     #  0x1C
            ("OCLK_MODE"      , ctypes.c_uint32),     #  0x20
            ("RESERVED_024"   , ctypes.c_uint32),     #  0x24
            ("HRESET_PULSE"   , ctypes.c_uint32),     #  0x28
            ("PRESET_PULSE"   , ctypes.c_uint32),     #  0x2C
            ("ORESET_PULSE"   , ctypes.c_uint32),     #  0x30
            ("HRESET_SET"     , ctypes.c_uint32),     #  0x34
            ("HRESET_CLR"     , ctypes.c_uint32),     #  0x38
            ("PRESET_SET"     , ctypes.c_uint32),     #  0x3C
            ("PRESET_CLR"     , ctypes.c_uint32),     #  0x40
            ("ORESET_SET"     , ctypes.c_uint32),     #  0x44
            ("ORESET_CLR"     , ctypes.c_uint32),     #  0x48
            ("TIMER0_CLK"     , ctypes.c_uint32),     #  0x4C
            ("BOOTMODE"       , ctypes.c_uint32),     #  0x50
            ("MCU_TIMER"      , ctypes.c_uint32),     #  0x54
            ("SLEEP"          , ctypes.c_uint32),     #  0x58
            ("PERIPH_CLK"     , ctypes.c_uint32),     #  0x5C
            ("SYS_CLK_ENABLE" , ctypes.c_uint32),     #  0x60
            ("SYS_CLK_DISABLE", ctypes.c_uint32),     #  0x64
            ("RESERVED_068"   , ctypes.c_uint32),     #  0x68
            ("BOOT_DVS"       , ctypes.c_uint32),     #  0x6C
            ("UART_CLK"       , ctypes.c_uint32),     #  0x70
            ("I2C_CLK"        , ctypes.c_uint32),     #  0x74
            ("RAM_CFG0"       , ctypes.c_uint32),     #  0x78
            ("RAM_CFG1"       , ctypes.c_uint32),     #  0x7C
            ("WRITE_UNLOCK"   , ctypes.c_uint32),     #  0x80
            ("WAKEUP_MASK0"   , ctypes.c_uint32),     #  0x84
            ("WAKEUP_MASK1"   , ctypes.c_uint32),     #  0x88
            ("WAKEUP_CLK_CFG" , ctypes.c_uint32),     #  0x8C
            ("TIMER1_CLK"     , ctypes.c_uint32),     #  0x90
            ("TIMER2_CLK"     , ctypes.c_uint32),     #  0x94
            ("RESERVED_098"   , ctypes.c_uint32),     #  0x98
            ("RESERVED_09C"   , ctypes.c_uint32),     #  0x9C
            ("ISIRQ_SET"      , ctypes.c_uint32),     #  0xA0
            ("ISIRQ_CLR"      , ctypes.c_uint32),     #  0xA4
            ("SYS_DIV"        , ctypes.c_uint32),     #  0xA8
            ("DMA_CFG"        , ctypes.c_uint32),     #  0xAC
            ("MCU2BT_INTMASK0", ctypes.c_uint32),     #  0xB0
            ("MCU2BT_INTMASK1", ctypes.c_uint32),     #  0xB4
            ("RESERVED_0B8"   , ctypes.c_uint32),     #  0xB8
            ("RESERVED_0BC"   , ctypes.c_uint32),     #  0xBC
            ("MEMSC"          , ctypes.c_uint32 * 4), #  0xC0
            ("MEMSC_STATUS"   , ctypes.c_uint32),     #  0xD0
            ("RESERVED2"      , ctypes.c_uint32 * 7), #  0xD4
            ("MISC"           , ctypes.c_uint32),     #  0xF0
            ("SIMU_RES"       , ctypes.c_uint32),     #  0xF4
        ]

bes2300 = {
    "ROM": {
        "base":0x0,
        "size":0xc000,
        "type": "memory"
    },
    "RAM": {
        "base":0x200a0000,
        "size":0x20000,
        "type": "memory"
    },
    "CMU": {
        "struct": "BES2300Cmu",
        "base":0x40000000,
        "type": "peripheral"
    },
    "I2C0": {
        "struct": "BES2300I2c",
        "base":0x40005000,
        "type": "peripheral"
    },
    "I2C1": {
        "struct": "BES2300I2c",
        "base":0x40006000,
        "type": "peripheral"
    },
    "SPI": {
        "struct": "BES2300Spi",
        "base":0x40007000,
        "type": "peripheral"
    },
    "SPILCD": {
        "struct": "BES2300Spi",
        "base":0x40008000,
        "type": "peripheral"
    },
    "SPIPHY": {
        "struct": "BES2300Spi",
        "base":0x4000a000,
        "type": "peripheral"
    },
    "UART0": {
        "struct": "BES2300Uart",
        "base":0x4000b000,
        "type": "peripheral"
    },
    "UART1": {
        "struct": "BES2300Uart",
        "base":0x4000c000,
        "type": "peripheral"
    },
    "UART2": {
        "struct": "BES2300Uart",
        "base":0x4000d000,
        "type": "peripheral"
    },
    "BTPCM": {
        "struct": "BES2300Btpcm",
        "base":0x4000e000,
        "type": "peripheral"
    },
    "I2S0": {
        "struct": "BES2300I2s",
        "base":0x4000f000,
        "type": "peripheral"
    },
    "SPDIF0": {
        "struct": "BES2300Spdif",
        "base":0x40010000,
        "type": "peripheral"
    },
    "SDMMC": {
        "struct": "BES2300Sdmmc",
        "base":0x40110000,
        "type": "peripheral"
    },
    "I2C_SLAVE": {
        "struct": "BES2300I2c",
        "base":0x40160000,
        "type": "peripheral"
    },
    "USB": {
        "struct": "BES2300Usb",
        "base":0x40180000,
        "type": "peripheral"
    },
    "CODEC": {
        "struct": "BES2300Codec",
        "base":0x40300000,
        "type": "peripheral"
    },
    "IOMUX": {
        "struct": "BES2300Iomux",
        "base":0x40086000,
        "type": "peripheral"
    },
    "GPIO": {
        "struct": "BES2300Gpio",
        "base":0x40081000,
        "type": "peripheral"
    },
    "PWM": {
        "struct": "BES2300Pwm",
        "base":0x40083000,
        "type": "peripheral"
    },
    "TIMER0": {
        "struct": "BES2300Timer",
        "base":0x40002000,
        "type": "peripheral"
    },
    "TIMER1": {
        "struct": "BES2300Timer",
        "base":0x40003000,
        "type": "peripheral"
    }
}