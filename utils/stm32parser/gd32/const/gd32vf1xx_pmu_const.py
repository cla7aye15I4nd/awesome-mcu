from enum import IntEnum


class CTL(IntEnum):
    BKPWEN = 0x1 << 8   # Backup Domain Write Enable
    LVDT   = 0x7 << 5   # Low Voltage Detector Threshold
    LVDEN  = 0x1 << 4   # Low Voltage Detector Enable
    STBRST = 0x1 << 3   # Standby Flag Reset
    WURST  = 0x1 << 2   # Wakeup Flag Reset
    STBMOD = 0x1 << 1   # Standby Mode
    LDOLP  = 0x1 << 0   # LDO Low Power Mode

class CS(IntEnum):
    WUPEN = 0x1 << 8   # Enable WKUP pin
    LVDF  = 0x1 << 2   # Low Voltage Detector Status Flag
    STBF  = 0x1 << 1   # Standby flag
    WUF   = 0x1 << 0   # Wakeup flag

