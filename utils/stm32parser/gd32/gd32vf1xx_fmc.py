import ctypes


class GD32VF1xxFmc:
    class Type(ctypes.Structure):
        """ FMC 
        """

        _fields_ = [
            ("WS"    , ctypes.c_uint32), # Address offset: 0x0, wait state counter register
            ("KEY0"  , ctypes.c_uint32), # Address offset: 0x04, Unlock key register 0
            ("OBKEY" , ctypes.c_uint32), # Address offset: 0x08, Option byte unlock key register
            ("STAT0" , ctypes.c_uint32), # Address offset: 0x0C, Status register 0
            ("CTL0"  , ctypes.c_uint32), # Address offset: 0x10, Control register 0
            ("ADDR0" , ctypes.c_uint32), # Address offset: 0x14, Address register 0
            ("OBSTAT", ctypes.c_uint32), # Address offset: 0x1C, Option byte status register
            ("WP"    , ctypes.c_uint32), # Address offset: 0x20, Erase/Program Protection register
            ("PID"   , ctypes.c_uint32), # Address offset: 0x100, Product ID register
        ]

    def __init__(self, ql, label):
        super().__init__(ql, label)

        self.fmc = self.struct(
            WS     =  0x00000000,
            KEY0   =  0x00000000,
            OBKEY  =  0x00000000,
            STAT0  =  0x00000000,
            CTL0   =  0x00000080,
            ADDR0  =  0x00000000,
            OBSTAT =  0x00000000,
            WP     =  0x00000000,
            PID    =  0x00000000,
        )

