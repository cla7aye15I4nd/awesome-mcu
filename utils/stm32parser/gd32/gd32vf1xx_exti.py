import ctypes


class GD32VF1xxExti:
    class Type(ctypes.Structure):
        """ External interrupt/event
      controller 
        """

        _fields_ = [
            ("INTEN", ctypes.c_uint32), # Address offset: 0x0, Interrupt enable register (EXTI_INTEN)
            ("EVEN" , ctypes.c_uint32), # Address offset: 0x04, Event enable register (EXTI_EVEN)
            ("RTEN" , ctypes.c_uint32), # Address offset: 0x08, Rising Edge Trigger Enable register (EXTI_RTEN)
            ("FTEN" , ctypes.c_uint32), # Address offset: 0x0C, Falling Egde Trigger Enable register (EXTI_FTEN)
            ("SWIEV", ctypes.c_uint32), # Address offset: 0x10, Software interrupt event register (EXTI_SWIEV)
            ("PD"   , ctypes.c_uint32), # Address offset: 0x14, Pending register (EXTI_PD)
        ]

    def __init__(self, ql, label):
        super().__init__(ql, label)

        self.exti = self.struct(
            INTEN =  0x00000000,
            EVEN  =  0x00000000,
            RTEN  =  0x00000000,
            FTEN  =  0x00000000,
            SWIEV =  0x00000000,
            PD    =  0x00000000,
        )

