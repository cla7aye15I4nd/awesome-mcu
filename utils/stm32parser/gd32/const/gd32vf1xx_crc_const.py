from enum import IntEnum


class DATA(IntEnum):
    DATA = 0xffffffff << 0   # CRC calculation result bits

class FDATA(IntEnum):
    FDATA = 0xff << 0   # Free Data Register bits

class CTL(IntEnum):
    RST = 0x1 << 0   # reset bit

