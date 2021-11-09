import ctypes


class GD32VF1xxUsbfs:
    class Type(ctypes.Structure):
        """ USB full speed global registers 
        """

        _fields_ = [
            ("GOTGCS"        , ctypes.c_uint32), # Address offset: 0x0, Global OTG control and status register (USBFS_GOTGCS)
            ("GOTGINTF"      , ctypes.c_uint32), # Address offset: 0x04, Global OTG interrupt flag register (USBFS_GOTGINTF)
            ("GAHBCS"        , ctypes.c_uint32), # Address offset: 0x08, Global AHB control and status register (USBFS_GAHBCS)
            ("GUSBCS"        , ctypes.c_uint32), # Address offset: 0x0C, Global USB control and status register (USBFS_GUSBCSR)
            ("GRSTCTL"       , ctypes.c_uint32), # Address offset: 0x10, Global reset control register (USBFS_GRSTCTL)
            ("GINTF"         , ctypes.c_uint32), # Address offset: 0x14, Global interrupt flag register (USBFS_GINTF)
            ("GINTEN"        , ctypes.c_uint32), # Address offset: 0x18, Global interrupt enable register (USBFS_GINTEN)
            ("GRSTATR_Device", ctypes.c_uint32), # Address offset: 0x1C, Global Receive status read(Device mode)
            ("GRSTATR_Host"  , ctypes.c_uint32), # Address offset: 0x1C, Global Receive status read(Host mode)
            ("GRSTATP_Device", ctypes.c_uint32), # Address offset: 0x20, Global Receive status pop(Device mode)
            ("GRSTATP_Host"  , ctypes.c_uint32), # Address offset: 0x20, Global Receive status pop(Host mode)
            ("GRFLEN"        , ctypes.c_uint32), # Address offset: 0x24, Global Receive FIFO size register (USBFS_GRFLEN)
            ("HNPTFLEN"      , ctypes.c_uint32), # Address offset: 0x28, Host non-periodic transmit FIFO length register (Host mode)
            ("DIEP0TFLEN"    , ctypes.c_uint32), # Address offset: 0x28, Device IN endpoint 0 transmit FIFO length (Device mode)
            ("HNPTFQSTAT"    , ctypes.c_uint32), # Address offset: 0x2C, Host non-periodic transmit FIFO/queue status register (HNPTFQSTAT)
            ("GCCFG"         , ctypes.c_uint32), # Address offset: 0x38, Global core configuration register (USBFS_GCCFG)
            ("CID"           , ctypes.c_uint32), # Address offset: 0x3C, core ID register
            ("HPTFLEN"       , ctypes.c_uint32), # Address offset: 0x100, Host periodic transmit FIFO length register (HPTFLEN)
            ("DIEP1TFLEN"    , ctypes.c_uint32), # Address offset: 0x104, device IN endpoint transmit FIFO size register (DIEP1TFLEN)
            ("DIEP2TFLEN"    , ctypes.c_uint32), # Address offset: 0x108, device IN endpoint transmit FIFO size register (DIEP2TFLEN)
            ("DIEP3TFLEN"    , ctypes.c_uint32), # Address offset: 0x10C, device IN endpoint transmit FIFO size register (FS_DIEP3TXFLEN)
        ]

    def __init__(self, ql, label):
        super().__init__(ql, label)

        self.usbfs = self.struct(
            GOTGCS         =  0x00000800,
            GOTGINTF       =  0x00000000,
            GAHBCS         =  0x00000000,
            GUSBCS         =  0x00000a80,
            GRSTCTL        =  0x80000000,
            GINTF          =  0x04000021,
            GINTEN         =  0x00000000,
            GRSTATR_Device =  0x00000000,
            GRSTATR_Host   =  0x00000000,
            GRSTATP_Device =  0x00000000,
            GRSTATP_Host   =  0x00000000,
            GRFLEN         =  0x00000200,
            HNPTFLEN       =  0x02000200,
            DIEP0TFLEN     =  0x02000200,
            HNPTFQSTAT     =  0x00080200,
            GCCFG          =  0x00000000,
            CID            =  0x00001000,
            HPTFLEN        =  0x02000600,
            DIEP1TFLEN     =  0x02000400,
            DIEP2TFLEN     =  0x02000400,
            DIEP3TFLEN     =  0x02000400,
        )

