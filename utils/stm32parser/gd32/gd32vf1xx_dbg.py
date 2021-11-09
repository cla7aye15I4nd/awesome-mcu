import ctypes


class GD32VF1xxDbg:
    class Type(ctypes.Structure):
        """ Debug support 
        """

        _fields_ = [
            ("ID" , ctypes.c_uint32), # Address offset: 0x0, ID code register
            ("CTL", ctypes.c_uint32), # Address offset: 0x4, Control register 0
        ]

    def __init__(self, ql, label):
        super().__init__(ql, label)

        self.dbg = self.struct(
            ID  =  0x00000000,
            CTL =  0x00000000,
        )

