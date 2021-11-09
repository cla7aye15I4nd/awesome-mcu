import ctypes


class GD32VF1xxDac:
    class Type(ctypes.Structure):
        """ Digital-to-analog converter 
        """

        _fields_ = [
            ("CTL"       , ctypes.c_uint32), # Address offset: 0x0, control register
            ("SWT"       , ctypes.c_uint32), # Address offset: 0x04, software trigger register
            ("DAC0_R12DH", ctypes.c_uint32), # Address offset: 0x08, DAC0 12-bit right-aligned data holding register
            ("DAC0_L12DH", ctypes.c_uint32), # Address offset: 0x0C, DAC0 12-bit left-aligned data holding register
            ("DAC0_R8DH" , ctypes.c_uint32), # Address offset: 0x10, DAC0 8-bit right aligned data holding register
            ("DAC1_R12DH", ctypes.c_uint32), # Address offset: 0x14, DAC1 12-bit right-aligned data holding register
            ("DAC1_L12DH", ctypes.c_uint32), # Address offset: 0x18, DAC1 12-bit left aligned data holding register
            ("DAC1_R8DH" , ctypes.c_uint32), # Address offset: 0x1C, DAC1 8-bit right aligned data holding register
            ("DACC_R12DH", ctypes.c_uint32), # Address offset: 0x20, DAC concurrent mode 12-bit right-aligned data holding register
            ("DACC_L12DH", ctypes.c_uint32), # Address offset: 0x24, DAC concurrent mode 12-bit left aligned data holding register
            ("DACC_R8DH" , ctypes.c_uint32), # Address offset: 0x28, DAC concurrent mode 8-bit right aligned data holding register
            ("DAC0_DO"   , ctypes.c_uint32), # Address offset: 0x2C, DAC0 data output register
            ("DAC1_DO"   , ctypes.c_uint32), # Address offset: 0x30, DAC1 data output register
        ]

    def __init__(self, ql, label):
        super().__init__(ql, label)

        self.dac = self.struct(
            CTL        =  0x00000000,
            SWT        =  0x00000000,
            DAC0_R12DH =  0x00000000,
            DAC0_L12DH =  0x00000000,
            DAC0_R8DH  =  0x00000000,
            DAC1_R12DH =  0x00000000,
            DAC1_L12DH =  0x00000000,
            DAC1_R8DH  =  0x00000000,
            DACC_R12DH =  0x00000000,
            DACC_L12DH =  0x00000000,
            DACC_R8DH  =  0x00000000,
            DAC0_DO    =  0x00000000,
            DAC1_DO    =  0x00000000,
        )

