import ctypes


class GD32VF1xxExmc:
    class Type(ctypes.Structure):
        """ External memory controller 
        """

        _fields_ = [
            ("SNCTL0" , ctypes.c_uint32), # Address offset: 0x0, SRAM/NOR flash control register 0
            ("SNTCFG0", ctypes.c_uint32), # Address offset: 0x4, SRAM/NOR flash timing configuration register 0
            ("SNCTL1" , ctypes.c_uint32), # Address offset: 0x8, SRAM/NOR flash control register 1
        ]

    def __init__(self, ql, label):
        super().__init__(ql, label)

        self.exmc = self.struct(
            SNCTL0  =  0x000030da,
            SNTCFG0 =  0x0fffffff,
            SNCTL1  =  0x000030da,
        )

