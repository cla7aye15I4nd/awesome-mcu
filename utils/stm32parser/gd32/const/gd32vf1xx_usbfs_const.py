from enum import IntEnum


class GOTGCS(IntEnum):
    SRPS   = 0x1 << 0    # SRP success
    SRPREQ = 0x1 << 1    # SRP request
    HNPS   = 0x1 << 8    # Host success
    HNPREQ = 0x1 << 9    # HNP request
    HHNPEN = 0x1 << 10   # Host HNP enable
    DHNPEN = 0x1 << 11   # Device HNP enabled
    IDPS   = 0x1 << 16   # ID pin status
    DI     = 0x1 << 17   # Debounce interval
    ASV    = 0x1 << 18   # A-session valid
    BSV    = 0x1 << 19   # B-session valid

class GOTGINTF(IntEnum):
    SESEND = 0x1 << 2    # Session end
    SRPEND = 0x1 << 8    # Session request success status change
    HNPEND = 0x1 << 9    # HNP end
    HNPDET = 0x1 << 17   # Host negotiation request detected
    ADTO   = 0x1 << 18   # A-device timeout
    DF     = 0x1 << 19   # Debounce finish

class GAHBCS(IntEnum):
    GINTEN = 0x1 << 0   # Global interrupt enable
    TXFTH  = 0x1 << 7   # Tx FIFO threshold
    PTXFTH = 0x1 << 8   # Periodic Tx FIFO threshold

class GUSBCS(IntEnum):
    TOC    = 0x7 << 0    # Timeout calibration
    SRPCEN = 0x1 << 8    # SRP capability enable
    HNPCEN = 0x1 << 9    # HNP capability enable
    UTT    = 0xf << 10   # USB turnaround time
    FHM    = 0x1 << 29   # Force host mode
    FDM    = 0x1 << 30   # Force device mode

class GRSTCTL(IntEnum):
    CSRST  = 0x1 << 0    # Core soft reset
    HCSRST = 0x1 << 1    # HCLK soft reset
    HFCRST = 0x1 << 2    # Host frame counter reset
    RXFF   = 0x1 << 4    # RxFIFO flush
    TXFF   = 0x1 << 5    # TxFIFO flush
    TXFNUM = 0x1f << 6   # TxFIFO number

class GINTF(IntEnum):
    COPM            = 0x1 << 0    # Current operation mode
    MFIF            = 0x1 << 1    # Mode fault interrupt flag
    OTGIF           = 0x1 << 2    # OTG interrupt flag
    SOF             = 0x1 << 3    # Start of frame
    RXFNEIF         = 0x1 << 4    # RxFIFO non-empty interrupt flag
    NPTXFEIF        = 0x1 << 5    # Non-periodic TxFIFO empty interrupt flag
    GNPINAK         = 0x1 << 6    # Global Non-Periodic IN NAK effective
    GONAK           = 0x1 << 7    # Global OUT NAK effective
    ESP             = 0x1 << 10   # Early suspend
    SP              = 0x1 << 11   # USB suspend
    RST             = 0x1 << 12   # USB reset
    ENUMF           = 0x1 << 13   # Enumeration finished
    ISOOPDIF        = 0x1 << 14   # Isochronous OUT packet dropped interrupt
    EOPFIF          = 0x1 << 15   # End of periodic frame interrupt flag
    IEPIF           = 0x1 << 18   # IN endpoint interrupt flag
    OEPIF           = 0x1 << 19   # OUT endpoint interrupt flag
    ISOINCIF        = 0x1 << 20   # Isochronous IN transfer Not Complete Interrupt Flag
    PXNCIF_ISOONCIF = 0x1 << 21   # periodic transfer not complete interrupt flag(Host mode)/isochronous OUT transfer not complete interrupt flag(Device mode)
    HPIF            = 0x1 << 24   # Host port interrupt flag
    HCIF            = 0x1 << 25   # Host channels interrupt flag
    PTXFEIF         = 0x1 << 26   # Periodic TxFIFO empty interrupt flag
    IDPSC           = 0x1 << 28   # ID pin status change
    DISCIF          = 0x1 << 29   # Disconnect interrupt flag
    SESIF           = 0x1 << 30   # Session interrupt flag
    WKUPIF          = 0x1 << 31   # Wakeup interrupt flag

class GINTEN(IntEnum):
    MFIE            = 0x1 << 1    # Mode fault interrupt enable
    OTGIE           = 0x1 << 2    # OTG interrupt enable
    SOFIE           = 0x1 << 3    # Start of frame interrupt enable
    RXFNEIE         = 0x1 << 4    # Receive FIFO non-empty interrupt enable
    NPTXFEIE        = 0x1 << 5    # Non-periodic TxFIFO empty interrupt enable
    GNPINAKIE       = 0x1 << 6    # Global non-periodic IN NAK effective interrupt enable
    GONAKIE         = 0x1 << 7    # Global OUT NAK effective interrupt enable
    ESPIE           = 0x1 << 10   # Early suspend interrupt enable
    SPIE            = 0x1 << 11   # USB suspend interrupt enable
    RSTIE           = 0x1 << 12   # USB reset interrupt enable
    ENUMFIE         = 0x1 << 13   # Enumeration finish interrupt enable
    ISOOPDIE        = 0x1 << 14   # Isochronous OUT packet dropped interrupt enable
    EOPFIE          = 0x1 << 15   # End of periodic frame interrupt enable
    IEPIE           = 0x1 << 18   # IN endpoints interrupt enable
    OEPIE           = 0x1 << 19   # OUT endpoints interrupt enable
    ISOINCIE        = 0x1 << 20   # isochronous IN transfer not complete interrupt enable
    PXNCIE_ISOONCIE = 0x1 << 21   # periodic transfer not compelete Interrupt enable(Host mode)/isochronous OUT transfer not complete interrupt enable(Device mode)
    HPIE            = 0x1 << 24   # Host port interrupt enable
    HCIE            = 0x1 << 25   # Host channels interrupt enable
    PTXFEIE         = 0x1 << 26   # Periodic TxFIFO empty interrupt enable
    IDPSCIE         = 0x1 << 28   # ID pin status change interrupt enable
    DISCIE          = 0x1 << 29   # Disconnect interrupt enable
    SESIE           = 0x1 << 30   # Session interrupt enable
    WKUPIE          = 0x1 << 31   # Wakeup interrupt enable

class GRSTATR_Device(IntEnum):
    EPNUM  = 0xf << 0     # Endpoint number
    BCOUNT = 0x7ff << 4   # Byte count
    DPID   = 0x3 << 15    # Data PID
    RPCKST = 0xf << 17    # Recieve packet status

class GRSTATR_Host(IntEnum):
    CNUM   = 0xf << 0     # Channel number
    BCOUNT = 0x7ff << 4   # Byte count
    DPID   = 0x3 << 15    # Data PID
    RPCKST = 0xf << 17    # Reivece packet status

class GRSTATP_Device(IntEnum):
    EPNUM  = 0xf << 0     # Endpoint number
    BCOUNT = 0x7ff << 4   # Byte count
    DPID   = 0x3 << 15    # Data PID
    RPCKST = 0xf << 17    # Recieve packet status

class GRSTATP_Host(IntEnum):
    CNUM   = 0xf << 0     # Channel number
    BCOUNT = 0x7ff << 4   # Byte count
    DPID   = 0x3 << 15    # Data PID
    RPCKST = 0xf << 17    # Reivece packet status

class GRFLEN(IntEnum):
    RXFD = 0xffff << 0   # Rx FIFO depth

class HNPTFLEN(IntEnum):
    HNPTXRSAR = 0xffff << 0    # host non-periodic transmit Tx RAM start address
    HNPTXFD   = 0xffff << 16   # host non-periodic TxFIFO depth

class DIEP0TFLEN(IntEnum):
    IEP0TXFD   = 0xffff << 16   # in endpoint 0 Tx FIFO depth
    IEP0TXRSAR = 0xffff << 0    # in endpoint 0 Tx RAM start address

class HNPTFQSTAT(IntEnum):
    NPTXFS    = 0xffff << 0   # Non-periodic TxFIFO space
    NPTXRQS   = 0xff << 16    # Non-periodic transmit request queue space
    NPTXRQTOP = 0x7f << 24    # Top of the non-periodic transmit request queue

class GCCFG(IntEnum):
    PWRON    = 0x1 << 16   # Power on
    VBUSACEN = 0x1 << 18   # The VBUS A-device Comparer enable
    VBUSBCEN = 0x1 << 19   # The VBUS B-device Comparer enable
    SOFOEN   = 0x1 << 20   # SOF output enable
    VBUSIG   = 0x1 << 21   # VBUS ignored

class CID(IntEnum):
    CID = 0xffffffff << 0   # Core ID

class HPTFLEN(IntEnum):
    HPTXFSAR = 0xffff << 0    # Host periodic TxFIFO start address
    HPTXFD   = 0xffff << 16   # Host periodic TxFIFO depth

class DIEP1TFLEN(IntEnum):
    IEPTXRSAR = 0xffff << 0    # IN endpoint FIFO transmit RAM start address
    IEPTXFD   = 0xffff << 16   # IN endpoint TxFIFO depth

class DIEP2TFLEN(IntEnum):
    IEPTXRSAR = 0xffff << 0    # IN endpoint FIFO transmit RAM start address
    IEPTXFD   = 0xffff << 16   # IN endpoint TxFIFO depth

class DIEP3TFLEN(IntEnum):
    IEPTXRSAR = 0xffff << 0    # IN endpoint FIFO4 transmit RAM start address
    IEPTXFD   = 0xffff << 16   # IN endpoint TxFIFO depth

