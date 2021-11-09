import ctypes


class GD32VF1xxAfio:
    class Type(ctypes.Structure):
        """ Alternate-function I/Os 
        """

        _fields_ = [
            ("EC"     , ctypes.c_uint32), # Address offset: 0x0, Event control register
            ("PCF0"   , ctypes.c_uint32), # Address offset: 0x04, AFIO port configuration register 0
            ("EXTISS0", ctypes.c_uint32), # Address offset: 0x08, EXTI sources selection register 0
            ("EXTISS1", ctypes.c_uint32), # Address offset: 0x0C, EXTI sources selection register 1
            ("EXTISS2", ctypes.c_uint32), # Address offset: 0x10, EXTI sources selection register 2
            ("EXTISS3", ctypes.c_uint32), # Address offset: 0x14, EXTI sources selection register 3
            ("PCF1"   , ctypes.c_uint32), # Address offset: 0x1C, AFIO port configuration register 1
        ]

    def __init__(self, ql, label):
        super().__init__(ql, label)

        self.afio = self.struct(
            EC      =  0x00000000,
            PCF0    =  0x00000000,
            EXTISS0 =  0x00000000,
            EXTISS1 =  0x00000000,
            EXTISS2 =  0x00000000,
            EXTISS3 =  0x00000000,
            PCF1    =  0x00000000,
        )

