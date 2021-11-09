from enum import IntEnum


class WS(IntEnum):
    WSCNT = 0x7 << 0   # wait state counter register

class KEY0(IntEnum):
    KEY = 0xffffffff << 0   # FMC_CTL0 unlock key

class OBKEY(IntEnum):
    OBKEY = 0xffffffff << 0   # FMC_ CTL0 option byte operation unlock register

class STAT0(IntEnum):
    ENDF  = 0x1 << 5   # End of operation flag bit
    WPERR = 0x1 << 4   # Erase/Program protection error flag bit
    PGERR = 0x1 << 2   # Program error flag bit
    BUSY  = 0x1 << 0   # The flash is busy bit

class CTL0(IntEnum):
    ENDIE = 0x1 << 12   # End of operation interrupt enable bit
    ERRIE = 0x1 << 10   # Error interrupt enable bit
    OBWEN = 0x1 << 9    # Option byte erase/program enable bit
    LK    = 0x1 << 7    # FMC_CTL0 lock bit
    START = 0x1 << 6    # Send erase command to FMC bit
    OBER  = 0x1 << 5    # Option bytes erase command bit
    OBPG  = 0x1 << 4    # Option bytes program command bit
    MER   = 0x1 << 2    # Main flash mass erase for bank0 command bit
    PER   = 0x1 << 1    # Main flash page erase for bank0 command bit
    PG    = 0x1 << 0    # Main flash program for bank0 command bit

class ADDR0(IntEnum):
    ADDR = 0xffffffff << 0   # Flash erase/program command address bits

class OBSTAT(IntEnum):
    OBERR = 0x1 << 0       # Option bytes read error bit
    SPC   = 0x1 << 1       # Option bytes security protection code
    USER  = 0xff << 2      # Store USER of option bytes block after system reset
    DATA  = 0xffff << 10   # Store DATA[15:0] of option bytes block after system reset

class WP(IntEnum):
    WP = 0xffffffff << 0   # Store WP[31:0] of option bytes block after system reset

class PID(IntEnum):
    PID = 0xffffffff << 0   # Product reserved ID code register

