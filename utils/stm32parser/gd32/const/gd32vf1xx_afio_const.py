from enum import IntEnum


class EC(IntEnum):
    EOE  = 0x1 << 7   # Event output enable
    PORT = 0x7 << 4   # Event output port selection
    PIN  = 0xf << 0   # Event output pin selection

class PCF0(IntEnum):
    TIMER1ITI1_REMAP = 0x1 << 29   # TIMER1 internal trigger 1 remapping
    SPI2_REMAP       = 0x1 << 28   # SPI2/I2S2 remapping
    SWJ_CFG          = 0x7 << 24   # Serial wire JTAG configuration
    CAN1_REMAP       = 0x1 << 22   # CAN1 I/O remapping
    TIMER4CH3_IREMAP = 0x1 << 16   # TIMER4 channel3 internal remapping
    PD01_REMAP       = 0x1 << 15   # Port D0/Port D1 mapping on OSC_IN/OSC_OUT
    CAN0_REMAP       = 0x3 << 13   # CAN0 alternate interface remapping
    TIMER3_REMAP     = 0x1 << 12   # TIMER3 remapping
    TIMER2_REMAP     = 0x3 << 10   # TIMER2 remapping
    TIMER1_REMAP     = 0x3 << 8    # TIMER1 remapping
    TIMER0_REMAP     = 0x3 << 6    # TIMER0 remapping
    USART2_REMAP     = 0x3 << 4    # USART2 remapping
    USART1_REMAP     = 0x1 << 3    # USART1 remapping
    USART0_REMAP     = 0x1 << 2    # USART0 remapping
    I2C0_REMAP       = 0x1 << 1    # I2C0 remapping
    SPI0_REMAP       = 0x1 << 0    # SPI0 remapping

class EXTISS0(IntEnum):
    EXTI3_SS = 0xf << 12   # EXTI 3 sources selection
    EXTI2_SS = 0xf << 8    # EXTI 2 sources selection
    EXTI1_SS = 0xf << 4    # EXTI 1 sources selection
    EXTI0_SS = 0xf << 0    # EXTI 0 sources selection

class EXTISS1(IntEnum):
    EXTI7_SS = 0xf << 12   # EXTI 7 sources selection
    EXTI6_SS = 0xf << 8    # EXTI 6 sources selection
    EXTI5_SS = 0xf << 4    # EXTI 5 sources selection
    EXTI4_SS = 0xf << 0    # EXTI 4 sources selection

class EXTISS2(IntEnum):
    EXTI11_SS = 0xf << 12   # EXTI 11 sources selection
    EXTI10_SS = 0xf << 8    # EXTI 10 sources selection
    EXTI9_SS  = 0xf << 4    # EXTI 9 sources selection
    EXTI8_SS  = 0xf << 0    # EXTI 8 sources selection

class EXTISS3(IntEnum):
    EXTI15_SS = 0xf << 12   # EXTI 15 sources selection
    EXTI14_SS = 0xf << 8    # EXTI 14 sources selection
    EXTI13_SS = 0xf << 4    # EXTI 13 sources selection
    EXTI12_SS = 0xf << 0    # EXTI 12 sources selection

class PCF1(IntEnum):
    EXMC_NADV = 0x1 << 10   # EXMC_NADV connect/disconnect

