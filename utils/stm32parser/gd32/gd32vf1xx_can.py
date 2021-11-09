import ctypes


class GD32VF1xxCan:
    class Type(ctypes.Structure):
        """ Controller area network 
        """

        _fields_ = [
            ("CTL"         , ctypes.c_uint32), # Address offset: 0x0, Control register
            ("STAT"        , ctypes.c_uint32), # Address offset: 0x04, Status register
            ("TSTAT"       , ctypes.c_uint32), # Address offset: 0x8, Transmit status register
            ("RFIFO0"      , ctypes.c_uint32), # Address offset: 0x0C, Receive message FIFO0 register
            ("RFIFO1"      , ctypes.c_uint32), # Address offset: 0x10, Receive message FIFO1 register
            ("INTEN"       , ctypes.c_uint32), # Address offset: 0x14, Interrupt enable register
            ("ERR"         , ctypes.c_uint32), # Address offset: 0x18, Error register
            ("BT"          , ctypes.c_uint32), # Address offset: 0x1C, Bit timing register
            ("TMI0"        , ctypes.c_uint32), # Address offset: 0x180, Transmit mailbox identifier register 0
            ("TMP0"        , ctypes.c_uint32), # Address offset: 0x184, Transmit mailbox property register 0
            ("TMDATA00"    , ctypes.c_uint32), # Address offset: 0x188, Transmit mailbox data0 register
            ("TMDATA10"    , ctypes.c_uint32), # Address offset: 0x18C, Transmit mailbox data1 register
            ("TMI1"        , ctypes.c_uint32), # Address offset: 0x190, Transmit mailbox identifier register 1
            ("TMP1"        , ctypes.c_uint32), # Address offset: 0x194, Transmit mailbox property register 1
            ("TMDATA01"    , ctypes.c_uint32), # Address offset: 0x198, Transmit mailbox data0 register
            ("TMDATA11"    , ctypes.c_uint32), # Address offset: 0x19C, Transmit mailbox data1 register
            ("TMI2"        , ctypes.c_uint32), # Address offset: 0x1A0, Transmit mailbox identifier register 2
            ("TMP2"        , ctypes.c_uint32), # Address offset: 0x1A4, Transmit mailbox property register 2
            ("TMDATA02"    , ctypes.c_uint32), # Address offset: 0x1A8, Transmit mailbox data0 register
            ("TMDATA12"    , ctypes.c_uint32), # Address offset: 0x1AC, Transmit mailbox data1 register
            ("RFIFOMI0"    , ctypes.c_uint32), # Address offset: 0x1B0, Receive FIFO mailbox identifier register
            ("RFIFOMP0"    , ctypes.c_uint32), # Address offset: 0x1B4, Receive FIFO0 mailbox property register
            ("RFIFOMDATA00", ctypes.c_uint32), # Address offset: 0x1B8, Receive FIFO0 mailbox data0 register
            ("RFIFOMDATA10", ctypes.c_uint32), # Address offset: 0x1BC, Receive FIFO0 mailbox data1 register
            ("RFIFOMI1"    , ctypes.c_uint32), # Address offset: 0x1C0, Receive FIFO1 mailbox identifier register
            ("RFIFOMP1"    , ctypes.c_uint32), # Address offset: 0x1C4, Receive FIFO1 mailbox property register
            ("RFIFOMDATA01", ctypes.c_uint32), # Address offset: 0x1C8, Receive FIFO1 mailbox data0 register
            ("RFIFOMDATA11", ctypes.c_uint32), # Address offset: 0x1CC, Receive FIFO1 mailbox data1 register
            ("FCTL"        , ctypes.c_uint32), # Address offset: 0x200, Filter control register
            ("FMCFG"       , ctypes.c_uint32), # Address offset: 0x204, Filter mode configuration register
            ("FSCFG"       , ctypes.c_uint32), # Address offset: 0x20C, Filter scale configuration register
            ("FAFIFO"      , ctypes.c_uint32), # Address offset: 0x214, Filter associated FIFO register
            ("FW"          , ctypes.c_uint32), # Address offset: 0x21C, Filter working register
            ("F0DATA0"     , ctypes.c_uint32), # Address offset: 0x240, Filter 0 data 0 register
            ("F0DATA1"     , ctypes.c_uint32), # Address offset: 0x244, Filter 0 data 1 register
            ("F1DATA0"     , ctypes.c_uint32), # Address offset: 0x248, Filter 1 data 0 register
            ("F1DATA1"     , ctypes.c_uint32), # Address offset: 0x24C, Filter 1 data 1 register
            ("F2DATA0"     , ctypes.c_uint32), # Address offset: 0x250, Filter 2 data 0 register
            ("F2DATA1"     , ctypes.c_uint32), # Address offset: 0x254, Filter 2 data 1 register
            ("F3DATA0"     , ctypes.c_uint32), # Address offset: 0x258, Filter 3 data 0 register
            ("F3DATA1"     , ctypes.c_uint32), # Address offset: 0x25C, Filter 3 data 1 register
            ("F4DATA0"     , ctypes.c_uint32), # Address offset: 0x260, Filter 4 data 0 register
            ("F4DATA1"     , ctypes.c_uint32), # Address offset: 0x264, Filter 4 data 1 register
            ("F5DATA0"     , ctypes.c_uint32), # Address offset: 0x268, Filter 5 data 0 register
            ("F5DATA1"     , ctypes.c_uint32), # Address offset: 0x26C, Filter 5 data 1 register
            ("F6DATA0"     , ctypes.c_uint32), # Address offset: 0x270, Filter 6 data 0 register
            ("F6DATA1"     , ctypes.c_uint32), # Address offset: 0x274, Filter 6 data 1 register
            ("F7DATA0"     , ctypes.c_uint32), # Address offset: 0x278, Filter 7 data 0 register
            ("F7DATA1"     , ctypes.c_uint32), # Address offset: 0x27C, Filter 7 data 1 register
            ("F8DATA0"     , ctypes.c_uint32), # Address offset: 0x280, Filter 8 data 0 register
            ("F8DATA1"     , ctypes.c_uint32), # Address offset: 0x284, Filter 8 data 1 register
            ("F9DATA0"     , ctypes.c_uint32), # Address offset: 0x288, Filter 9 data 0 register
            ("F9DATA1"     , ctypes.c_uint32), # Address offset: 0x28C, Filter 9 data 1 register
            ("F10DATA0"    , ctypes.c_uint32), # Address offset: 0x290, Filter 10 data 0 register
            ("F10DATA1"    , ctypes.c_uint32), # Address offset: 0x294, Filter 10 data 1 register
            ("F11DATA0"    , ctypes.c_uint32), # Address offset: 0x298, Filter 11 data 0 register
            ("F11DATA1"    , ctypes.c_uint32), # Address offset: 0x29C, Filter 11 data 1 register
            ("F12DATA0"    , ctypes.c_uint32), # Address offset: 0x2A0, Filter 12 data 0 register
            ("F12DATA1"    , ctypes.c_uint32), # Address offset: 0x2A4, Filter 12 data 1 register
            ("F13DATA0"    , ctypes.c_uint32), # Address offset: 0x2A8, Filter 13 data 0 register
            ("F13DATA1"    , ctypes.c_uint32), # Address offset: 0x2AC, Filter 13 data 1 register
            ("F14DATA0"    , ctypes.c_uint32), # Address offset: 0x2B0, Filter 14 data 0 register
            ("F14DATA1"    , ctypes.c_uint32), # Address offset: 0x2B4, Filter 14 data 1 register
            ("F15DATA0"    , ctypes.c_uint32), # Address offset: 0x2B8, Filter 15 data 0 register
            ("F15DATA1"    , ctypes.c_uint32), # Address offset: 0x2BC, Filter 15 data 1 register
            ("F16DATA0"    , ctypes.c_uint32), # Address offset: 0x2C0, Filter 16 data 0 register
            ("F16DATA1"    , ctypes.c_uint32), # Address offset: 0x2C4, Filter 16 data 1 register
            ("F17DATA0"    , ctypes.c_uint32), # Address offset: 0x2C8, Filter 17 data 0 register
            ("F17DATA1"    , ctypes.c_uint32), # Address offset: 0x2CC, Filter 17 data 1 register
            ("F18DATA0"    , ctypes.c_uint32), # Address offset: 0x2D0, Filter 18 data 0 register
            ("F18DATA1"    , ctypes.c_uint32), # Address offset: 0x2D4, Filter 18 data 1 register
            ("F19DATA0"    , ctypes.c_uint32), # Address offset: 0x2D8, Filter 19 data 0 register
            ("F19DATA1"    , ctypes.c_uint32), # Address offset: 0x2DC, Filter 19 data 1 register
            ("F20DATA0"    , ctypes.c_uint32), # Address offset: 0x2E0, Filter 20 data 0 register
            ("F20DATA1"    , ctypes.c_uint32), # Address offset: 0x2E4, Filter 20 data 1 register
            ("F21DATA0"    , ctypes.c_uint32), # Address offset: 0x2E8, Filter 21 data 0 register
            ("F21DATA1"    , ctypes.c_uint32), # Address offset: 0x2EC, Filter 21 data 1 register
            ("F22DATA0"    , ctypes.c_uint32), # Address offset: 0x2F0, Filter 22 data 0 register
            ("F22DATA1"    , ctypes.c_uint32), # Address offset: 0x2F4, Filter 22 data 1 register
            ("F23DATA0"    , ctypes.c_uint32), # Address offset: 0x2F8, Filter 23 data 0 register
            ("F23DATA1"    , ctypes.c_uint32), # Address offset: 0x2FC, Filter 23 data 1 register
            ("F24DATA0"    , ctypes.c_uint32), # Address offset: 0x300, Filter 24 data 0 register
            ("F24DATA1"    , ctypes.c_uint32), # Address offset: 0x304, Filter 24 data 1 register
            ("F25DATA0"    , ctypes.c_uint32), # Address offset: 0x308, Filter 25 data 0 register
            ("F25DATA1"    , ctypes.c_uint32), # Address offset: 0x30C, Filter 25 data 1 register
            ("F26DATA0"    , ctypes.c_uint32), # Address offset: 0x310, Filter 26 data 0 register
            ("F26DATA1"    , ctypes.c_uint32), # Address offset: 0x314, Filter 26 data 1 register
            ("F27DATA0"    , ctypes.c_uint32), # Address offset: 0x318, Filter 27 data 0 register
            ("F27DATA1"    , ctypes.c_uint32), # Address offset: 0x31C, Filter 27 data 1 register
        ]

    def __init__(self, ql, label):
        super().__init__(ql, label)

        self.can = self.struct(
            CTL          =  0x00010002,
            STAT         =  0x00000c02,
            TSTAT        =  0x1c000000,
            RFIFO0       =  0x00000000,
            RFIFO1       =  0x00000000,
            INTEN        =  0x00000000,
            ERR          =  0x00000000,
            BT           =  0x01230000,
            TMI0         =  0x00000000,
            TMP0         =  0x00000000,
            TMDATA00     =  0x00000000,
            TMDATA10     =  0x00000000,
            TMI1         =  0x00000000,
            TMP1         =  0x00000000,
            TMDATA01     =  0x00000000,
            TMDATA11     =  0x00000000,
            TMI2         =  0x00000000,
            TMP2         =  0x00000000,
            TMDATA02     =  0x00000000,
            TMDATA12     =  0x00000000,
            RFIFOMI0     =  0x00000000,
            RFIFOMP0     =  0x00000000,
            RFIFOMDATA00 =  0x00000000,
            RFIFOMDATA10 =  0x00000000,
            RFIFOMI1     =  0x00000000,
            RFIFOMP1     =  0x00000000,
            RFIFOMDATA01 =  0x00000000,
            RFIFOMDATA11 =  0x00000000,
            FCTL         =  0x2a1c0e01,
            FMCFG        =  0x00000000,
            FSCFG        =  0x00000000,
            FAFIFO       =  0x00000000,
            FW           =  0x00000000,
            F0DATA0      =  0x00000000,
            F0DATA1      =  0x00000000,
            F1DATA0      =  0x00000000,
            F1DATA1      =  0x00000000,
            F2DATA0      =  0x00000000,
            F2DATA1      =  0x00000000,
            F3DATA0      =  0x00000000,
            F3DATA1      =  0x00000000,
            F4DATA0      =  0x00000000,
            F4DATA1      =  0x00000000,
            F5DATA0      =  0x00000000,
            F5DATA1      =  0x00000000,
            F6DATA0      =  0x00000000,
            F6DATA1      =  0x00000000,
            F7DATA0      =  0x00000000,
            F7DATA1      =  0x00000000,
            F8DATA0      =  0x00000000,
            F8DATA1      =  0x00000000,
            F9DATA0      =  0x00000000,
            F9DATA1      =  0x00000000,
            F10DATA0     =  0x00000000,
            F10DATA1     =  0x00000000,
            F11DATA0     =  0x00000000,
            F11DATA1     =  0x00000000,
            F12DATA0     =  0x00000000,
            F12DATA1     =  0x00000000,
            F13DATA0     =  0x00000000,
            F13DATA1     =  0x00000000,
            F14DATA0     =  0x00000000,
            F14DATA1     =  0x00000000,
            F15DATA0     =  0x00000000,
            F15DATA1     =  0x00000000,
            F16DATA0     =  0x00000000,
            F16DATA1     =  0x00000000,
            F17DATA0     =  0x00000000,
            F17DATA1     =  0x00000000,
            F18DATA0     =  0x00000000,
            F18DATA1     =  0x00000000,
            F19DATA0     =  0x00000000,
            F19DATA1     =  0x00000000,
            F20DATA0     =  0x00000000,
            F20DATA1     =  0x00000000,
            F21DATA0     =  0x00000000,
            F21DATA1     =  0x00000000,
            F22DATA0     =  0x00000000,
            F22DATA1     =  0x00000000,
            F23DATA0     =  0x00000000,
            F23DATA1     =  0x00000000,
            F24DATA0     =  0x00000000,
            F24DATA1     =  0x00000000,
            F25DATA0     =  0x00000000,
            F25DATA1     =  0x00000000,
            F26DATA0     =  0x00000000,
            F26DATA1     =  0x00000000,
            F27DATA0     =  0x00000000,
            F27DATA1     =  0x00000000,
        )

