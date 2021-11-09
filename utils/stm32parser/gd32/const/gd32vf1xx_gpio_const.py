from enum import IntEnum


class CTL0(IntEnum):
    CTL7 = 0x3 << 30   # Port x configuration bits (x = 7)
    MD7  = 0x3 << 28   # Port x mode bits (x = 7)
    CTL6 = 0x3 << 26   # Port x configuration bits (x = 6)
    MD6  = 0x3 << 24   # Port x mode bits (x = 6)
    CTL5 = 0x3 << 22   # Port x configuration bits (x = 5)
    MD5  = 0x3 << 20   # Port x mode bits (x = 5)
    CTL4 = 0x3 << 18   # Port x configuration bits (x = 4)
    MD4  = 0x3 << 16   # Port x mode bits (x = 4)
    CTL3 = 0x3 << 14   # Port x configuration bits (x = 3)
    MD3  = 0x3 << 12   # Port x mode bits (x = 3 )
    CTL2 = 0x3 << 10   # Port x configuration bits (x = 2)
    MD2  = 0x3 << 8    # Port x mode bits (x = 2 )
    CTL1 = 0x3 << 6    # Port x configuration bits (x = 1)
    MD1  = 0x3 << 4    # Port x mode bits (x = 1)
    CTL0 = 0x3 << 2    # Port x configuration bits (x = 0)
    MD0  = 0x3 << 0    # Port x mode bits (x = 0)

class CTL1(IntEnum):
    CTL15 = 0x3 << 30   # Port x configuration bits (x = 15)
    MD15  = 0x3 << 28   # Port x mode bits (x = 15)
    CTL14 = 0x3 << 26   # Port x configuration bits (x = 14)
    MD14  = 0x3 << 24   # Port x mode bits (x = 14)
    CTL13 = 0x3 << 22   # Port x configuration bits (x = 13)
    MD13  = 0x3 << 20   # Port x mode bits (x = 13)
    CTL12 = 0x3 << 18   # Port x configuration bits (x = 12)
    MD12  = 0x3 << 16   # Port x mode bits (x = 12)
    CTL11 = 0x3 << 14   # Port x configuration bits (x = 11)
    MD11  = 0x3 << 12   # Port x mode bits (x = 11 )
    CTL10 = 0x3 << 10   # Port x configuration bits (x = 10)
    MD10  = 0x3 << 8    # Port x mode bits (x = 10 )
    CTL9  = 0x3 << 6    # Port x configuration bits (x = 9)
    MD9   = 0x3 << 4    # Port x mode bits (x = 9)
    CTL8  = 0x3 << 2    # Port x configuration bits (x = 8)
    MD8   = 0x3 << 0    # Port x mode bits (x = 8)

class ISTAT(IntEnum):
    ISTAT15 = 0x1 << 15   # Port input status
    ISTAT14 = 0x1 << 14   # Port input status
    ISTAT13 = 0x1 << 13   # Port input status
    ISTAT12 = 0x1 << 12   # Port input status
    ISTAT11 = 0x1 << 11   # Port input status
    ISTAT10 = 0x1 << 10   # Port input status
    ISTAT9  = 0x1 << 9    # Port input status
    ISTAT8  = 0x1 << 8    # Port input status
    ISTAT7  = 0x1 << 7    # Port input status
    ISTAT6  = 0x1 << 6    # Port input status
    ISTAT5  = 0x1 << 5    # Port input status
    ISTAT4  = 0x1 << 4    # Port input status
    ISTAT3  = 0x1 << 3    # Port input status
    ISTAT2  = 0x1 << 2    # Port input status
    ISTAT1  = 0x1 << 1    # Port input status
    ISTAT0  = 0x1 << 0    # Port input status

class OCTL(IntEnum):
    OCTL15 = 0x1 << 15   # Port output control
    OCTL14 = 0x1 << 14   # Port output control
    OCTL13 = 0x1 << 13   # Port output control
    OCTL12 = 0x1 << 12   # Port output control
    OCTL11 = 0x1 << 11   # Port output control
    OCTL10 = 0x1 << 10   # Port output control
    OCTL9  = 0x1 << 9    # Port output control
    OCTL8  = 0x1 << 8    # Port output control
    OCTL7  = 0x1 << 7    # Port output control
    OCTL6  = 0x1 << 6    # Port output control
    OCTL5  = 0x1 << 5    # Port output control
    OCTL4  = 0x1 << 4    # Port output control
    OCTL3  = 0x1 << 3    # Port output control
    OCTL2  = 0x1 << 2    # Port output control
    OCTL1  = 0x1 << 1    # Port output control
    OCTL0  = 0x1 << 0    # Port output control

class BOP(IntEnum):
    CR15  = 0x1 << 31   # Port 15 Clear bit
    CR14  = 0x1 << 30   # Port 14 Clear bit
    CR13  = 0x1 << 29   # Port 13 Clear bit
    CR12  = 0x1 << 28   # Port 12 Clear bit
    CR11  = 0x1 << 27   # Port 11 Clear bit
    CR10  = 0x1 << 26   # Port 10 Clear bit
    CR9   = 0x1 << 25   # Port 9 Clear bit
    CR8   = 0x1 << 24   # Port 8 Clear bit
    CR7   = 0x1 << 23   # Port 7 Clear bit
    CR6   = 0x1 << 22   # Port 6 Clear bit
    CR5   = 0x1 << 21   # Port 5 Clear bit
    CR4   = 0x1 << 20   # Port 4 Clear bit
    CR3   = 0x1 << 19   # Port 3 Clear bit
    CR2   = 0x1 << 18   # Port 2 Clear bit
    CR1   = 0x1 << 17   # Port 1 Clear bit
    CR0   = 0x1 << 16   # Port 0 Clear bit
    BOP15 = 0x1 << 15   # Port 15 Set bit
    BOP14 = 0x1 << 14   # Port 14 Set bit
    BOP13 = 0x1 << 13   # Port 13 Set bit
    BOP12 = 0x1 << 12   # Port 12 Set bit
    BOP11 = 0x1 << 11   # Port 11 Set bit
    BOP10 = 0x1 << 10   # Port 10 Set bit
    BOP9  = 0x1 << 9    # Port 9 Set bit
    BOP8  = 0x1 << 8    # Port 8 Set bit
    BOP7  = 0x1 << 7    # Port 7 Set bit
    BOP6  = 0x1 << 6    # Port 6 Set bit
    BOP5  = 0x1 << 5    # Port 5 Set bit
    BOP4  = 0x1 << 4    # Port 4 Set bit
    BOP3  = 0x1 << 3    # Port 3 Set bit
    BOP2  = 0x1 << 2    # Port 2 Set bit
    BOP1  = 0x1 << 1    # Port 1 Set bit
    BOP0  = 0x1 << 0    # Port 0 Set bit

class BC(IntEnum):
    CR15 = 0x1 << 15   # Port 15 Clear bit
    CR14 = 0x1 << 14   # Port 14 Clear bit
    CR13 = 0x1 << 13   # Port 13 Clear bit
    CR12 = 0x1 << 12   # Port 12 Clear bit
    CR11 = 0x1 << 11   # Port 11 Clear bit
    CR10 = 0x1 << 10   # Port 10 Clear bit
    CR9  = 0x1 << 9    # Port 9 Clear bit
    CR8  = 0x1 << 8    # Port 8 Clear bit
    CR7  = 0x1 << 7    # Port 7 Clear bit
    CR6  = 0x1 << 6    # Port 6 Clear bit
    CR5  = 0x1 << 5    # Port 5 Clear bit
    CR4  = 0x1 << 4    # Port 4 Clear bit
    CR3  = 0x1 << 3    # Port 3 Clear bit
    CR2  = 0x1 << 2    # Port 2 Clear bit
    CR1  = 0x1 << 1    # Port 1 Clear bit
    CR0  = 0x1 << 0    # Port 0 Clear bit

class LOCK(IntEnum):
    LKK  = 0x1 << 16   # Lock sequence key
    LK15 = 0x1 << 15   # Port Lock bit 15
    LK14 = 0x1 << 14   # Port Lock bit 14
    LK13 = 0x1 << 13   # Port Lock bit 13
    LK12 = 0x1 << 12   # Port Lock bit 12
    LK11 = 0x1 << 11   # Port Lock bit 11
    LK10 = 0x1 << 10   # Port Lock bit 10
    LK9  = 0x1 << 9    # Port Lock bit 9
    LK8  = 0x1 << 8    # Port Lock bit 8
    LK7  = 0x1 << 7    # Port Lock bit 7
    LK6  = 0x1 << 6    # Port Lock bit 6
    LK5  = 0x1 << 5    # Port Lock bit 5
    LK4  = 0x1 << 4    # Port Lock bit 4
    LK3  = 0x1 << 3    # Port Lock bit 3
    LK2  = 0x1 << 2    # Port Lock bit 2
    LK1  = 0x1 << 1    # Port Lock bit 1
    LK0  = 0x1 << 0    # Port Lock bit 0

