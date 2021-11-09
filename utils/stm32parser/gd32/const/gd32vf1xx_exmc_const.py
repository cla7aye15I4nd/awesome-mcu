from enum import IntEnum


class SNCTL0(IntEnum):
    ASYNCWAIT = 0x1 << 15   # Asynchronous wait
    NRWTEN    = 0x1 << 13   # NWAIT signal enable
    WREN      = 0x1 << 12   # Write enable
    NRWTPOL   = 0x1 << 9    # NWAIT signal polarity
    NREN      = 0x1 << 6    # NOR Flash access enable
    NRW       = 0x3 << 4    # NOR bank memory data bus width
    NRTP      = 0x3 << 2    # NOR bank memory type
    NRMUX     = 0x1 << 1    # NOR bank memory address/data multiplexing
    NRBKEN    = 0x1 << 0    # NOR bank enable

class SNTCFG0(IntEnum):
    BUSLAT = 0xf << 16   # Bus latency
    DSET   = 0xff << 8   # Data setup time
    AHLD   = 0xf << 4    # Address hold time
    ASET   = 0xf << 0    # Address setup time

class SNCTL1(IntEnum):
    ASYNCWAIT = 0x1 << 15   # Asynchronous wait
    NRWTEN    = 0x1 << 13   # NWAIT signal enable
    WREN      = 0x1 << 12   # Write enable
    NRWTPOL   = 0x1 << 9    # NWAIT signal polarity
    NREN      = 0x1 << 6    # NOR Flash access enable
    NRW       = 0x3 << 4    # NOR bank memory data bus width
    NRTP      = 0x3 << 2    # NOR bank memory type
    NRMUX     = 0x1 << 1    # NOR bank memory address/data multiplexing
    NRBKEN    = 0x1 << 0    # NOR bank enable

