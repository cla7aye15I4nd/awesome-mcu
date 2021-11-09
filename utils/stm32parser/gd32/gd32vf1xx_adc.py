import ctypes


class GD32VF1xxAdc:
    class Type(ctypes.Structure):
        """ Analog to digital converter 
        """

        _fields_ = [
            ("STAT"     , ctypes.c_uint32), # Address offset: 0x0, status register
            ("CTL0"     , ctypes.c_uint32), # Address offset: 0x04, control register 0
            ("CTL1"     , ctypes.c_uint32), # Address offset: 0x08, control register 1
            ("SAMPT0"   , ctypes.c_uint32), # Address offset: 0x0C, Sample time register 0
            ("SAMPT1"   , ctypes.c_uint32), # Address offset: 0x10, Sample time register 1
            ("IOFF0"    , ctypes.c_uint32), # Address offset: 0x14, Inserted channel data offset register 0
            ("IOFF1"    , ctypes.c_uint32), # Address offset: 0x18, Inserted channel data offset register 1
            ("IOFF2"    , ctypes.c_uint32), # Address offset: 0x1C, Inserted channel data offset register 2
            ("IOFF3"    , ctypes.c_uint32), # Address offset: 0x20, Inserted channel data offset register 3
            ("WDHT"     , ctypes.c_uint32), # Address offset: 0x24, watchdog higher threshold register
            ("WDLT"     , ctypes.c_uint32), # Address offset: 0x28, watchdog lower threshold register
            ("RSQ0"     , ctypes.c_uint32), # Address offset: 0x2C, regular sequence register 0
            ("RSQ1"     , ctypes.c_uint32), # Address offset: 0x30, regular sequence register 1
            ("RSQ2"     , ctypes.c_uint32), # Address offset: 0x34, regular sequence register 2
            ("ISQ"      , ctypes.c_uint32), # Address offset: 0x38, Inserted sequence register
            ("IDATA0"   , ctypes.c_uint32), # Address offset: 0x3C, Inserted data register 0
            ("IDATA1"   , ctypes.c_uint32), # Address offset: 0x40, Inserted data register 1
            ("IDATA2"   , ctypes.c_uint32), # Address offset: 0x44, Inserted data register 2
            ("IDATA3"   , ctypes.c_uint32), # Address offset: 0x48, Inserted data register 3
            ("RDATA"    , ctypes.c_uint32), # Address offset: 0x4C, regular data register
            ("OVSAMPCTL", ctypes.c_uint32), # Address offset: 0x80, Oversample control register
        ]

    def __init__(self, ql, label):
        super().__init__(ql, label)

        self.adc = self.struct(
            STAT      =  0x00000000,
            CTL0      =  0x00000000,
            CTL1      =  0x00000000,
            SAMPT0    =  0x00000000,
            SAMPT1    =  0x00000000,
            IOFF0     =  0x00000000,
            IOFF1     =  0x00000000,
            IOFF2     =  0x00000000,
            IOFF3     =  0x00000000,
            WDHT      =  0x00000fff,
            WDLT      =  0x00000000,
            RSQ0      =  0x00000000,
            RSQ1      =  0x00000000,
            RSQ2      =  0x00000000,
            ISQ       =  0x00000000,
            IDATA0    =  0x00000000,
            IDATA1    =  0x00000000,
            IDATA2    =  0x00000000,
            IDATA3    =  0x00000000,
            RDATA     =  0x00000000,
            OVSAMPCTL =  0x00000000,
        )

