from enum import IntEnum


class CTL(IntEnum):
    CMD = 0xffff << 0   # Key value

class PSC(IntEnum):
    PSC = 0x7 << 0   # Free watchdog timer prescaler selection

class RLD(IntEnum):
    RLD = 0xfff << 0   # Free watchdog timer counter reload value

class STAT(IntEnum):
    PUD = 0x1 << 0   # Free watchdog timer prescaler value update
    RUD = 0x1 << 1   # Free watchdog timer counter reload value update

