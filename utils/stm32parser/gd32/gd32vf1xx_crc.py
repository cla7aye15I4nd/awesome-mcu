import ctypes


class GD32VF1xxCrc:
    class Type(ctypes.Structure):
        """ cyclic redundancy check calculation unit 
        """

        _fields_ = [
            ("DATA" , ctypes.c_uint32), # Address offset: 0x0, Data register
            ("FDATA", ctypes.c_uint32), # Address offset: 0x04, Free data register
            ("CTL"  , ctypes.c_uint32), # Address offset: 0x08, Control register
        ]

    def __init__(self, ql, label):
        super().__init__(ql, label)

        self.crc = self.struct(
            DATA  =  0xffffffff,
            FDATA =  0x00000000,
            CTL   =  0x00000000,
        )

