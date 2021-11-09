import ctypes


class GD32VF1xxBkp:
    class Type(ctypes.Structure):
        """ Backup registers 
        """

        _fields_ = [
            ("DATA0" , ctypes.c_uint16), # Address offset: 0x4, Backup data register 0
            ("DATA1" , ctypes.c_uint16), # Address offset: 0x8, Backup data register 1
            ("DATA2" , ctypes.c_uint16), # Address offset: 0xC, Backup data register 2
            ("DATA3" , ctypes.c_uint16), # Address offset: 0x10, Backup data register 3
            ("DATA4" , ctypes.c_uint16), # Address offset: 0x14, Backup data register 4
            ("DATA5" , ctypes.c_uint16), # Address offset: 0x18, Backup data register 5
            ("DATA6" , ctypes.c_uint16), # Address offset: 0x1C, Backup data register 6
            ("DATA7" , ctypes.c_uint16), # Address offset: 0x20, Backup data register 7
            ("DATA8" , ctypes.c_uint16), # Address offset: 0x24, Backup data register 8
            ("DATA9" , ctypes.c_uint16), # Address offset: 0x28, Backup data register 9
            ("DATA10", ctypes.c_uint16), # Address offset: 0x40, Backup data register 10
            ("DATA11", ctypes.c_uint16), # Address offset: 0x44, Backup data register 11
            ("DATA12", ctypes.c_uint16), # Address offset: 0x48, Backup data register 12
            ("DATA13", ctypes.c_uint16), # Address offset: 0x4C, Backup data register 13
            ("DATA14", ctypes.c_uint16), # Address offset: 0x50, Backup data register 14
            ("DATA15", ctypes.c_uint16), # Address offset: 0x54, Backup data register 15
            ("DATA16", ctypes.c_uint16), # Address offset: 0x58, Backup data register 16
            ("DATA17", ctypes.c_uint16), # Address offset: 0x5C, Backup data register 17
            ("DATA18", ctypes.c_uint16), # Address offset: 0x60, Backup data register 18
            ("DATA19", ctypes.c_uint16), # Address offset: 0x64, Backup data register 19
            ("DATA20", ctypes.c_uint16), # Address offset: 0x68, Backup data register 20
            ("DATA21", ctypes.c_uint16), # Address offset: 0x6C, Backup data register 21
            ("DATA22", ctypes.c_uint16), # Address offset: 0x70, Backup data register 22
            ("DATA23", ctypes.c_uint16), # Address offset: 0x74, Backup data register 23
            ("DATA24", ctypes.c_uint16), # Address offset: 0x78, Backup data register 24
            ("DATA25", ctypes.c_uint16), # Address offset: 0x7C, Backup data register 25
            ("DATA26", ctypes.c_uint16), # Address offset: 0x80, Backup data register 26
            ("DATA27", ctypes.c_uint16), # Address offset: 0x84, Backup data register 27
            ("DATA28", ctypes.c_uint16), # Address offset: 0x88, Backup data register 28
            ("DATA29", ctypes.c_uint16), # Address offset: 0x8C, Backup data register 29
            ("DATA30", ctypes.c_uint16), # Address offset: 0x90, Backup data register 30
            ("DATA31", ctypes.c_uint16), # Address offset: 0x94, Backup data register 31
            ("DATA32", ctypes.c_uint16), # Address offset: 0x98, Backup data register 32
            ("DATA33", ctypes.c_uint16), # Address offset: 0x9C, Backup data register 33
            ("DATA34", ctypes.c_uint16), # Address offset: 0xA0, Backup data register 34
            ("DATA35", ctypes.c_uint16), # Address offset: 0xA4, Backup data register 35
            ("DATA36", ctypes.c_uint16), # Address offset: 0xA8, Backup data register 36
            ("DATA37", ctypes.c_uint16), # Address offset: 0xAC, Backup data register 37
            ("DATA38", ctypes.c_uint16), # Address offset: 0xB0, Backup data register 38
            ("DATA39", ctypes.c_uint16), # Address offset: 0xB4, Backup data register 39
            ("DATA40", ctypes.c_uint16), # Address offset: 0xB8, Backup data register 40
            ("DATA41", ctypes.c_uint16), # Address offset: 0xBC, Backup data register 41
            ("OCTL"  , ctypes.c_uint16), # Address offset: 0x2C, RTC signal output control register
            ("TPCTL" , ctypes.c_uint16), # Address offset: 0x30, Tamper pin control register
            ("TPCS"  , ctypes.c_uint16), # Address offset: 0x34, Tamper control and status register
        ]

    def __init__(self, ql, label):
        super().__init__(ql, label)

        self.bkp = self.struct(
            DATA0  =  0x00000000,
            DATA1  =  0x00000000,
            DATA2  =  0x00000000,
            DATA3  =  0x00000000,
            DATA4  =  0x00000000,
            DATA5  =  0x00000000,
            DATA6  =  0x00000000,
            DATA7  =  0x00000000,
            DATA8  =  0x00000000,
            DATA9  =  0x00000000,
            DATA10 =  0x00000000,
            DATA11 =  0x00000000,
            DATA12 =  0x00000000,
            DATA13 =  0x00000000,
            DATA14 =  0x00000000,
            DATA15 =  0x00000000,
            DATA16 =  0x00000000,
            DATA17 =  0x00000000,
            DATA18 =  0x00000000,
            DATA19 =  0x00000000,
            DATA20 =  0x00000000,
            DATA21 =  0x00000000,
            DATA22 =  0x00000000,
            DATA23 =  0x00000000,
            DATA24 =  0x00000000,
            DATA25 =  0x00000000,
            DATA26 =  0x00000000,
            DATA27 =  0x00000000,
            DATA28 =  0x00000000,
            DATA29 =  0x00000000,
            DATA30 =  0x00000000,
            DATA31 =  0x00000000,
            DATA32 =  0x00000000,
            DATA33 =  0x00000000,
            DATA34 =  0x00000000,
            DATA35 =  0x00000000,
            DATA36 =  0x00000000,
            DATA37 =  0x00000000,
            DATA38 =  0x00000000,
            DATA39 =  0x00000000,
            DATA40 =  0x00000000,
            DATA41 =  0x00000000,
            OCTL   =  0x00000000,
            TPCTL  =  0x00000000,
            TPCS   =  0x00000000,
        )

