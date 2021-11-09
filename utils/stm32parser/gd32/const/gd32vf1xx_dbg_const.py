from enum import IntEnum


class ID(IntEnum):
    ID_CODE = 0xffffffff << 0   # DBG ID code register

class CTL(IntEnum):
    SLP_HOLD    = 0x1 << 0    # Sleep mode hold register
    DSLP_HOLD   = 0x1 << 1    # Deep-sleep mode hold register
    STB_HOLD    = 0x1 << 2    # Standby mode hold register
    FWDGT_HOLD  = 0x1 << 8    # FWDGT hold bit
    WWDGT_HOLD  = 0x1 << 9    # WWDGT hold bit
    TIMER0_HOLD = 0x1 << 10   # TIMER 0 hold bit
    TIMER1_HOLD = 0x1 << 11   # TIMER 1 hold bit
    TIMER2_HOLD = 0x1 << 12   # TIMER 2 hold bit
    TIMER3_HOLD = 0x1 << 13   # TIMER 23 hold bit
    CAN0_HOLD   = 0x1 << 14   # CAN0 hold bit
    I2C0_HOLD   = 0x1 << 15   # I2C0 hold bit
    I2C1_HOLD   = 0x1 << 16   # I2C1 hold bit
    TIMER4_HOLD = 0x1 << 18   # TIMER4_HOLD
    TIMER5_HOLD = 0x1 << 19   # TIMER 5 hold bit
    TIMER6_HOLD = 0x1 << 20   # TIMER 6 hold bit
    CAN1_HOLD   = 0x1 << 21   # CAN1 hold bit

