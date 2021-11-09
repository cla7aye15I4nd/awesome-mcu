from enum import IntEnum


class DATA0(IntEnum):
    DATA = 0xffff << 0   # Backup data

class DATA1(IntEnum):
    DATA = 0xffff << 0   # Backup data

class DATA2(IntEnum):
    DATA = 0xffff << 0   # Backup data

class DATA3(IntEnum):
    DATA = 0xffff << 0   # Backup data

class DATA4(IntEnum):
    DATA = 0xffff << 0   # Backup data

class DATA5(IntEnum):
    DATA = 0xffff << 0   # Backup data

class DATA6(IntEnum):
    DATA = 0xffff << 0   # Backup data

class DATA7(IntEnum):
    DATA = 0xffff << 0   # Backup data

class DATA8(IntEnum):
    DATA = 0xffff << 0   # Backup data

class DATA9(IntEnum):
    DATA = 0xffff << 0   # Backup data

class DATA10(IntEnum):
    DATA = 0xffff << 0   # Backup data

class DATA11(IntEnum):
    DATA = 0xffff << 0   # Backup data

class DATA12(IntEnum):
    DATA = 0xffff << 0   # Backup data

class DATA13(IntEnum):
    DATA = 0xffff << 0   # Backup data

class DATA14(IntEnum):
    DATA = 0xffff << 0   # Backup data

class DATA15(IntEnum):
    DATA = 0xffff << 0   # Backup data

class DATA16(IntEnum):
    DATA = 0xffff << 0   # Backup data

class DATA17(IntEnum):
    DATA = 0xffff << 0   # Backup data

class DATA18(IntEnum):
    DATA = 0xffff << 0   # Backup data

class DATA19(IntEnum):
    DATA = 0xffff << 0   # Backup data

class DATA20(IntEnum):
    DATA = 0xffff << 0   # Backup data

class DATA21(IntEnum):
    DATA = 0xffff << 0   # Backup data

class DATA22(IntEnum):
    DATA = 0xffff << 0   # Backup data

class DATA23(IntEnum):
    DATA = 0xffff << 0   # Backup data

class DATA24(IntEnum):
    DATA = 0xffff << 0   # Backup data

class DATA25(IntEnum):
    DATA = 0xffff << 0   # Backup data

class DATA26(IntEnum):
    DATA = 0xffff << 0   # Backup data

class DATA27(IntEnum):
    DATA = 0xffff << 0   # Backup data

class DATA28(IntEnum):
    DATA = 0xffff << 0   # Backup data

class DATA29(IntEnum):
    DATA = 0xffff << 0   # Backup data

class DATA30(IntEnum):
    DATA = 0xffff << 0   # Backup data

class DATA31(IntEnum):
    DATA = 0xffff << 0   # Backup data

class DATA32(IntEnum):
    DATA = 0xffff << 0   # Backup data

class DATA33(IntEnum):
    DATA = 0xffff << 0   # Backup data

class DATA34(IntEnum):
    DATA = 0xffff << 0   # Backup data

class DATA35(IntEnum):
    DATA = 0xffff << 0   # Backup data

class DATA36(IntEnum):
    DATA = 0xffff << 0   # Backup data

class DATA37(IntEnum):
    DATA = 0xffff << 0   # Backup data

class DATA38(IntEnum):
    DATA = 0xffff << 0   # Backup data

class DATA39(IntEnum):
    DATA = 0xffff << 0   # Backup data

class DATA40(IntEnum):
    DATA = 0xffff << 0   # Backup data

class DATA41(IntEnum):
    DATA = 0xffff << 0   # Backup data

class OCTL(IntEnum):
    ROSEL = 0x1 << 9    # RTC output selection
    ASOEN = 0x1 << 8    # RTC alarm or second signal output enable
    COEN  = 0x1 << 7    # RTC clock calibration output enable
    RCCV  = 0x7f << 0   # RTC clock calibration value

class TPCTL(IntEnum):
    TPAL = 0x1 << 1   # TAMPER pin active level
    TPEN = 0x1 << 0   # TAMPER detection enable

class TPCS(IntEnum):
    TIF  = 0x1 << 9   # Tamper interrupt flag
    TEF  = 0x1 << 8   # Tamper event flag
    TPIE = 0x1 << 2   # Tamper interrupt enable
    TIR  = 0x1 << 1   # Tamper interrupt reset
    TER  = 0x1 << 0   # Tamper event reset

