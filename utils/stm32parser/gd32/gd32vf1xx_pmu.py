import ctypes


class GD32VF1xxPmu:
    class Type(ctypes.Structure):
        """ Power management unit 
        """

        _fields_ = [
            ("CTL", ctypes.c_uint32), # Address offset: 0x00, power control register
            ("CS" , ctypes.c_uint32), # Address offset: 0x04, power control/status register
        ]

    def __init__(self, ql, label):
        super().__init__(ql, label)

        self.pmu = self.struct(
            CTL =  0x00000000,
            CS  =  0x00000000,
        )

