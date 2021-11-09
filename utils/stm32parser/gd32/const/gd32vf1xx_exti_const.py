from enum import IntEnum


class INTEN(IntEnum):
    INTEN0  = 0x1 << 0    # Enable Interrupt on line 0
    INTEN1  = 0x1 << 1    # Enable Interrupt on line 1
    INTEN2  = 0x1 << 2    # Enable Interrupt on line 2
    INTEN3  = 0x1 << 3    # Enable Interrupt on line 3
    INTEN4  = 0x1 << 4    # Enable Interrupt on line 4
    INTEN5  = 0x1 << 5    # Enable Interrupt on line 5
    INTEN6  = 0x1 << 6    # Enable Interrupt on line 6
    INTEN7  = 0x1 << 7    # Enable Interrupt on line 7
    INTEN8  = 0x1 << 8    # Enable Interrupt on line 8
    INTEN9  = 0x1 << 9    # Enable Interrupt on line 9
    INTEN10 = 0x1 << 10   # Enable Interrupt on line 10
    INTEN11 = 0x1 << 11   # Enable Interrupt on line 11
    INTEN12 = 0x1 << 12   # Enable Interrupt on line 12
    INTEN13 = 0x1 << 13   # Enable Interrupt on line 13
    INTEN14 = 0x1 << 14   # Enable Interrupt on line 14
    INTEN15 = 0x1 << 15   # Enable Interrupt on line 15
    INTEN16 = 0x1 << 16   # Enable Interrupt on line 16
    INTEN17 = 0x1 << 17   # Enable Interrupt on line 17
    INTEN18 = 0x1 << 18   # Enable Interrupt on line 18

class EVEN(IntEnum):
    EVEN0  = 0x1 << 0    # Enable Event on line 0
    EVEN1  = 0x1 << 1    # Enable Event on line 1
    EVEN2  = 0x1 << 2    # Enable Event on line 2
    EVEN3  = 0x1 << 3    # Enable Event on line 3
    EVEN4  = 0x1 << 4    # Enable Event on line 4
    EVEN5  = 0x1 << 5    # Enable Event on line 5
    EVEN6  = 0x1 << 6    # Enable Event on line 6
    EVEN7  = 0x1 << 7    # Enable Event on line 7
    EVEN8  = 0x1 << 8    # Enable Event on line 8
    EVEN9  = 0x1 << 9    # Enable Event on line 9
    EVEN10 = 0x1 << 10   # Enable Event on line 10
    EVEN11 = 0x1 << 11   # Enable Event on line 11
    EVEN12 = 0x1 << 12   # Enable Event on line 12
    EVEN13 = 0x1 << 13   # Enable Event on line 13
    EVEN14 = 0x1 << 14   # Enable Event on line 14
    EVEN15 = 0x1 << 15   # Enable Event on line 15
    EVEN16 = 0x1 << 16   # Enable Event on line 16
    EVEN17 = 0x1 << 17   # Enable Event on line 17
    EVEN18 = 0x1 << 18   # Enable Event on line 18

class RTEN(IntEnum):
    RTEN0  = 0x1 << 0    # Rising edge trigger enable of line 0
    RTEN1  = 0x1 << 1    # Rising edge trigger enable of line 1
    RTEN2  = 0x1 << 2    # Rising edge trigger enable of line 2
    RTEN3  = 0x1 << 3    # Rising edge trigger enable of line 3
    RTEN4  = 0x1 << 4    # Rising edge trigger enable of line 4
    RTEN5  = 0x1 << 5    # Rising edge trigger enable of line 5
    RTEN6  = 0x1 << 6    # Rising edge trigger enable of line 6
    RTEN7  = 0x1 << 7    # Rising edge trigger enable of line 7
    RTEN8  = 0x1 << 8    # Rising edge trigger enable of line 8
    RTEN9  = 0x1 << 9    # Rising edge trigger enable of line 9
    RTEN10 = 0x1 << 10   # Rising edge trigger enable of line 10
    RTEN11 = 0x1 << 11   # Rising edge trigger enable of line 11
    RTEN12 = 0x1 << 12   # Rising edge trigger enable of line 12
    RTEN13 = 0x1 << 13   # Rising edge trigger enable of line 13
    RTEN14 = 0x1 << 14   # Rising edge trigger enable of line 14
    RTEN15 = 0x1 << 15   # Rising edge trigger enable of line 15
    RTEN16 = 0x1 << 16   # Rising edge trigger enable of line 16
    RTEN17 = 0x1 << 17   # Rising edge trigger enable of line 17
    RTEN18 = 0x1 << 18   # Rising edge trigger enable of line 18

class FTEN(IntEnum):
    FTEN0  = 0x1 << 0    # Falling edge trigger enable of line 0
    FTEN1  = 0x1 << 1    # Falling edge trigger enable of line 1
    FTEN2  = 0x1 << 2    # Falling edge trigger enable of line 2
    FTEN3  = 0x1 << 3    # Falling edge trigger enable of line 3
    FTEN4  = 0x1 << 4    # Falling edge trigger enable of line 4
    FTEN5  = 0x1 << 5    # Falling edge trigger enable of line 5
    FTEN6  = 0x1 << 6    # Falling edge trigger enable of line 6
    FTEN7  = 0x1 << 7    # Falling edge trigger enable of line 7
    FTEN8  = 0x1 << 8    # Falling edge trigger enable of line 8
    FTEN9  = 0x1 << 9    # Falling edge trigger enable of line 9
    FTEN10 = 0x1 << 10   # Falling edge trigger enable of line 10
    FTEN11 = 0x1 << 11   # Falling edge trigger enable of line 11
    FTEN12 = 0x1 << 12   # Falling edge trigger enable of line 12
    FTEN13 = 0x1 << 13   # Falling edge trigger enable of line 13
    FTEN14 = 0x1 << 14   # Falling edge trigger enable of line 14
    FTEN15 = 0x1 << 15   # Falling edge trigger enable of line 15
    FTEN16 = 0x1 << 16   # Falling edge trigger enable of line 16
    FTEN17 = 0x1 << 17   # Falling edge trigger enable of line 17
    FTEN18 = 0x1 << 18   # Falling edge trigger enable of line 18

class SWIEV(IntEnum):
    SWIEV0  = 0x1 << 0    # Interrupt/Event software trigger on line 0
    SWIEV1  = 0x1 << 1    # Interrupt/Event software trigger on line 1
    SWIEV2  = 0x1 << 2    # Interrupt/Event software trigger on line 2
    SWIEV3  = 0x1 << 3    # Interrupt/Event software trigger on line 3
    SWIEV4  = 0x1 << 4    # Interrupt/Event software trigger on line 4
    SWIEV5  = 0x1 << 5    # Interrupt/Event software trigger on line 5
    SWIEV6  = 0x1 << 6    # Interrupt/Event software trigger on line 6
    SWIEV7  = 0x1 << 7    # Interrupt/Event software trigger on line 7
    SWIEV8  = 0x1 << 8    # Interrupt/Event software trigger on line 8
    SWIEV9  = 0x1 << 9    # Interrupt/Event software trigger on line 9
    SWIEV10 = 0x1 << 10   # Interrupt/Event software trigger on line 10
    SWIEV11 = 0x1 << 11   # Interrupt/Event software trigger on line 11
    SWIEV12 = 0x1 << 12   # Interrupt/Event software trigger on line 12
    SWIEV13 = 0x1 << 13   # Interrupt/Event software trigger on line 13
    SWIEV14 = 0x1 << 14   # Interrupt/Event software trigger on line 14
    SWIEV15 = 0x1 << 15   # Interrupt/Event software trigger on line 15
    SWIEV16 = 0x1 << 16   # Interrupt/Event software trigger on line 16
    SWIEV17 = 0x1 << 17   # Interrupt/Event software trigger on line 17
    SWIEV18 = 0x1 << 18   # Interrupt/Event software trigger on line 18

class PD(IntEnum):
    PD0  = 0x1 << 0    # Interrupt pending status of line 0
    PD1  = 0x1 << 1    # Interrupt pending status of line 1
    PD2  = 0x1 << 2    # Interrupt pending status of line 2
    PD3  = 0x1 << 3    # Interrupt pending status of line 3
    PD4  = 0x1 << 4    # Interrupt pending status of line 4
    PD5  = 0x1 << 5    # Interrupt pending status of line 5
    PD6  = 0x1 << 6    # Interrupt pending status of line 6
    PD7  = 0x1 << 7    # Interrupt pending status of line 7
    PD8  = 0x1 << 8    # Interrupt pending status of line 8
    PD9  = 0x1 << 9    # Interrupt pending status of line 9
    PD10 = 0x1 << 10   # Interrupt pending status of line 10
    PD11 = 0x1 << 11   # Interrupt pending status of line 11
    PD12 = 0x1 << 12   # Interrupt pending status of line 12
    PD13 = 0x1 << 13   # Interrupt pending status of line 13
    PD14 = 0x1 << 14   # Interrupt pending status of line 14
    PD15 = 0x1 << 15   # Interrupt pending status of line 15
    PD16 = 0x1 << 16   # Interrupt pending status of line 16
    PD17 = 0x1 << 17   # Interrupt pending status of line 17
    PD18 = 0x1 << 18   # Interrupt pending status of line 18

