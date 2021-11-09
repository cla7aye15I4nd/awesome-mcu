import ctypes


class GD32VF1xxWwdgt:
    class Type(ctypes.Structure):
        """ Window watchdog timer 
        """

        _fields_ = [
            ("CTL" , ctypes.c_uint32), # Address offset: 0x0, Control register
            ("CFG" , ctypes.c_uint32), # Address offset: 0x04, Configuration register
            ("STAT", ctypes.c_uint32), # Address offset: 0x08, Status register
        ]

    def __init__(self, ql, label):
        super().__init__(ql, label)

        self.wwdgt = self.struct(
            CTL  =  0x0000007f,
            CFG  =  0x0000007f,
            STAT =  0x00000000,
        )

