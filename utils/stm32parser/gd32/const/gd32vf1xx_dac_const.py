from enum import IntEnum


class CTL(IntEnum):
    DEN0    = 0x1 << 0    # DAC0 enable
    DBOFF0  = 0x1 << 1    # DAC0 output buffer turn off
    DTEN0   = 0x1 << 2    # DAC0 trigger enable
    DTSEL0  = 0x7 << 3    # DAC0 trigger selection
    DWM0    = 0x3 << 6    # DAC0 noise wave mode
    DWBW0   = 0xf << 8    # DAC0 noise wave bit width
    DDMAEN0 = 0x1 << 12   # DAC0 DMA enable
    DEN1    = 0x1 << 16   # DAC1 enable
    DBOFF1  = 0x1 << 17   # DAC1 output buffer turn off
    DTEN1   = 0x1 << 18   # DAC1 trigger enable
    DTSEL1  = 0x7 << 19   # DAC1 trigger selection
    DWM1    = 0x3 << 22   # DAC1 noise wave mode
    DWBW1   = 0xf << 24   # DAC1 noise wave bit width
    DDMAEN1 = 0x1 << 28   # DAC1 DMA enable

class SWT(IntEnum):
    SWTR0 = 0x1 << 0   # DAC0 software trigger
    SWTR1 = 0x1 << 1   # DAC1 software trigger

class DAC0_R12DH(IntEnum):
    DAC0_DH = 0xfff << 0   # DAC0 12-bit right-aligned data

class DAC0_L12DH(IntEnum):
    DAC0_DH = 0xfff << 4   # DAC0 12-bit left-aligned data

class DAC0_R8DH(IntEnum):
    DAC0_DH = 0xff << 0   # DAC0 8-bit right-aligned data

class DAC1_R12DH(IntEnum):
    DAC1_DH = 0xfff << 0   # DAC1 12-bit right-aligned data

class DAC1_L12DH(IntEnum):
    DAC1_DH = 0xfff << 4   # DAC1 12-bit left-aligned data

class DAC1_R8DH(IntEnum):
    DAC1_DH = 0xff << 0   # DAC1 8-bit right-aligned data

class DACC_R12DH(IntEnum):
    DAC0_DH = 0xfff << 0    # DAC0 12-bit right-aligned data
    DAC1_DH = 0xfff << 16   # DAC1 12-bit right-aligned data

class DACC_L12DH(IntEnum):
    DAC0_DH = 0xfff << 4    # DAC0 12-bit left-aligned data
    DAC1_DH = 0xfff << 20   # DAC1 12-bit left-aligned data

class DACC_R8DH(IntEnum):
    DAC0_DH = 0xff << 0   # DAC0 8-bit right-aligned data
    DAC1_DH = 0xff << 8   # DAC1 8-bit right-aligned data

class DAC0_DO(IntEnum):
    DAC0_DO = 0xfff << 0   # DAC0 data output

class DAC1_DO(IntEnum):
    DAC1_DO = 0xfff << 0   # DAC1 data output

