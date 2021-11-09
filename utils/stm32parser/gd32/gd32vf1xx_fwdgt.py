import ctypes


class GD32VF1xxFwdgt:
    class Type(ctypes.Structure):
        """ free watchdog timer 
        """

        _fields_ = [
            ("CTL" , ctypes.c_uint32), # Address offset: 0x00, Control register
            ("PSC" , ctypes.c_uint32), # Address offset: 0x04, Prescaler register
            ("RLD" , ctypes.c_uint32), # Address offset: 0x08, Reload register
            ("STAT", ctypes.c_uint32), # Address offset: 0x0C, Status register
        ]

    def __init__(self, ql, label):
        super().__init__(ql, label)

        self.fwdgt = self.struct(
            CTL  =  0x00000000,
            PSC  =  0x00000000,
            RLD  =  0x00000fff,
            STAT =  0x00000000,
        )

