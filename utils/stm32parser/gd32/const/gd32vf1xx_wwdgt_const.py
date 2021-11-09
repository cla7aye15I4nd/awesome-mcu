from enum import IntEnum


class CTL(IntEnum):
    WDGTEN = 0x1 << 7    # Activation bit
    CNT    = 0x7f << 0   # 7-bit counter

class CFG(IntEnum):
    EWIE = 0x1 << 9    # Early wakeup interrupt
    PSC  = 0x3 << 7    # Prescaler
    WIN  = 0x7f << 0   # 7-bit window value

class STAT(IntEnum):
    EWIF = 0x1 << 0   # Early wakeup interrupt flag

