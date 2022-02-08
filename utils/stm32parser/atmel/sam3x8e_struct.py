import ctypes

class SAM3xaGpbr:
    class Type(ctypes.Structure):
        _fields_ = [
            ("SYS_GPBR", ctypes.c_uint32 * 8), # (Gpbr Offset: 0x0) General Purpose Backup Register
        ]

class SAM3xaHsmci:
    class Type(ctypes.Structure):
        _fields_ = [
            ("CR"       , ctypes.c_uint32),       # (Hsmci Offset: 0x00) Control Register
            ("MR"       , ctypes.c_uint32),       # (Hsmci Offset: 0x04) Mode Register
            ("DTOR"     , ctypes.c_uint32),       # (Hsmci Offset: 0x08) Data Timeout Register
            ("SDCR"     , ctypes.c_uint32),       # (Hsmci Offset: 0x0C) SD/SDIO Card Register
            ("ARGR"     , ctypes.c_uint32),       # (Hsmci Offset: 0x10) Argument Register
            ("CMDR"     , ctypes.c_uint32),       # (Hsmci Offset: 0x14) Command Register
            ("BLKR"     , ctypes.c_uint32),       # (Hsmci Offset: 0x18) Block Register
            ("CSTOR"    , ctypes.c_uint32),       # (Hsmci Offset: 0x1C) Completion Signal Timeout Register
            ("RSPR"     , ctypes.c_uint32 * 4),   # (Hsmci Offset: 0x20) Response Register
            ("RDR"      , ctypes.c_uint32),       # (Hsmci Offset: 0x30) Receive Data Register
            ("TDR"      , ctypes.c_uint32),       # (Hsmci Offset: 0x34) Transmit Data Register
            ("Reserved1", ctypes.c_uint32 * 2),   # 
            ("SR"       , ctypes.c_uint32),       # (Hsmci Offset: 0x40) Status Register
            ("IER"      , ctypes.c_uint32),       # (Hsmci Offset: 0x44) Interrupt Enable Register
            ("IDR"      , ctypes.c_uint32),       # (Hsmci Offset: 0x48) Interrupt Disable Register
            ("IMR"      , ctypes.c_uint32),       # (Hsmci Offset: 0x4C) Interrupt Mask Register
            ("DMA"      , ctypes.c_uint32),       # (Hsmci Offset: 0x50) DMA Configuration Register
            ("CFG"      , ctypes.c_uint32),       # (Hsmci Offset: 0x54) Configuration Register
            ("Reserved2", ctypes.c_uint32 * 35),  # 
            ("WPMR"     , ctypes.c_uint32),       # (Hsmci Offset: 0xE4) Write Protection Mode Register
            ("WPSR"     , ctypes.c_uint32),       # (Hsmci Offset: 0xE8) Write Protection Status Register
            ("Reserved3", ctypes.c_uint32 * 69),  # 
            ("FIFO"     , ctypes.c_uint32 * 256), # (Hsmci Offset: 0x200) FIFO Memory Aperture0
        ]

class SAM3xaMatrix:
    class Type(ctypes.Structure):
        _fields_ = [
            ("MCFG"      , ctypes.c_uint32 * 6),  # (Matrix Offset: 0x0000) Master Configuration Register
            ("Reserved1" , ctypes.c_uint32 * 10), # 
            ("SCFG"      , ctypes.c_uint32 * 9),  # (Matrix Offset: 0x0040) Slave Configuration Register
            ("Reserved2" , ctypes.c_uint32 * 7),  # 
            ("PRAS0"     , ctypes.c_uint32),      # (Matrix Offset: 0x0080) Priority Register A for Slave 0
            ("Reserved3" , ctypes.c_uint32),      # 
            ("PRAS1"     , ctypes.c_uint32),      # (Matrix Offset: 0x0088) Priority Register A for Slave 1
            ("Reserved4" , ctypes.c_uint32),      # 
            ("PRAS2"     , ctypes.c_uint32),      # (Matrix Offset: 0x0090) Priority Register A for Slave 2
            ("Reserved5" , ctypes.c_uint32),      # 
            ("PRAS3"     , ctypes.c_uint32),      # (Matrix Offset: 0x0098) Priority Register A for Slave 3
            ("Reserved6" , ctypes.c_uint32),      # 
            ("PRAS4"     , ctypes.c_uint32),      # (Matrix Offset: 0x00A0) Priority Register A for Slave 4
            ("Reserved7" , ctypes.c_uint32),      # 
            ("PRAS5"     , ctypes.c_uint32),      # (Matrix Offset: 0x00A8) Priority Register A for Slave 5
            ("Reserved8" , ctypes.c_uint32),      # 
            ("PRAS6"     , ctypes.c_uint32),      # (Matrix Offset: 0x00B0) Priority Register A for Slave 6
            ("Reserved9" , ctypes.c_uint32),      # 
            ("PRAS7"     , ctypes.c_uint32),      # (Matrix Offset: 0x00B8) Priority Register A for Slave 7
            ("Reserved10", ctypes.c_uint32),      # 
            ("PRAS8"     , ctypes.c_uint32),      # (Matrix Offset: 0x00C0) Priority Register A for Slave 8
            ("Reserved11", ctypes.c_uint32),      # 
            ("Reserved12", ctypes.c_uint32 * 14), # 
            ("MRCR"      , ctypes.c_uint32),      # (Matrix Offset: 0x0100) Master Remap Control Register
            ("Reserved13", ctypes.c_uint32 * 4),  # 
            ("CCFG_SYSIO", ctypes.c_uint32),      # (Matrix Offset: 0x0114) System I/O Configuration register
            ("Reserved14", ctypes.c_uint32 * 51), # 
            ("WPMR"      , ctypes.c_uint32),      # (Matrix Offset: 0x1E4) Write Protect Mode Register
            ("WPSR"      , ctypes.c_uint32),      # (Matrix Offset: 0x1E8) Write Protect Status Register
        ]

class SAM3xaSpi:
    class Type(ctypes.Structure):
        _fields_ = [
            ("CR"       , ctypes.c_uint32),      # (Spi Offset: 0x00) Control Register
            ("MR"       , ctypes.c_uint32),      # (Spi Offset: 0x04) Mode Register
            ("RDR"      , ctypes.c_uint32),      # (Spi Offset: 0x08) Receive Data Register
            ("TDR"      , ctypes.c_uint32),      # (Spi Offset: 0x0C) Transmit Data Register
            ("SR"       , ctypes.c_uint32),      # (Spi Offset: 0x10) Status Register
            ("IER"      , ctypes.c_uint32),      # (Spi Offset: 0x14) Interrupt Enable Register
            ("IDR"      , ctypes.c_uint32),      # (Spi Offset: 0x18) Interrupt Disable Register
            ("IMR"      , ctypes.c_uint32),      # (Spi Offset: 0x1C) Interrupt Mask Register
            ("Reserved1", ctypes.c_uint32 * 4),  # 
            ("CSR"      , ctypes.c_uint32 * 4),  # (Spi Offset: 0x30) Chip Select Register
            ("Reserved2", ctypes.c_uint32 * 41), # 
            ("WPMR"     , ctypes.c_uint32),      # (Spi Offset: 0xE4) Write Protection Control Register
            ("WPSR"     , ctypes.c_uint32),      # (Spi Offset: 0xE8) Write Protection Status Register
        ]

class SAM3xaDmac:
    class Type(ctypes.Structure):
        _fields_ = [
            ("GCFG"     , ctypes.c_uint32),                # (Dmac Offset: 0x000) DMAC Global Configuration Register
            ("EN"       , ctypes.c_uint32),                # (Dmac Offset: 0x004) DMAC Enable Register
            ("SREQ"     , ctypes.c_uint32),                # (Dmac Offset: 0x008) DMAC Software Single Request Register
            ("CREQ"     , ctypes.c_uint32),                # (Dmac Offset: 0x00C) DMAC Software Chunk Transfer Request Register
            ("LAST"     , ctypes.c_uint32),                # (Dmac Offset: 0x010) DMAC Software Last Transfer Flag Register
            ("Reserved1", ctypes.c_uint32),                # 
            ("EBCIER"   , ctypes.c_uint32),                # (Dmac Offset: 0x018) DMAC Error, Chained Buffer Transfer Completed Interrupt and Buffer Transfer Completed Interrupt Enable register.
            ("EBCIDR"   , ctypes.c_uint32),                # (Dmac Offset: 0x01C) DMAC Error, Chained Buffer Transfer Completed Interrupt and Buffer Transfer Completed Interrupt Disable register.
            ("EBCIMR"   , ctypes.c_uint32),                # (Dmac Offset: 0x020) DMAC Error, Chained Buffer Transfer Completed Interrupt and Buffer transfer completed Mask Register.
            ("EBCISR"   , ctypes.c_uint32),                # (Dmac Offset: 0x024) DMAC Error, Chained Buffer Transfer Completed Interrupt and Buffer transfer completed Status Register.
            ("CHER"     , ctypes.c_uint32),                # (Dmac Offset: 0x028) DMAC Channel Handler Enable Register
            ("CHDR"     , ctypes.c_uint32),                # (Dmac Offset: 0x02C) DMAC Channel Handler Disable Register
            ("CHSR"     , ctypes.c_uint32),                # (Dmac Offset: 0x030) DMAC Channel Handler Status Register
            ("Reserved2", ctypes.c_uint32 * 2),            # 
            ("CH_NUM"   , DmacCh_num * DMACCH_NUM_NUMBER), # (Dmac Offset: 0x3C) ch_num = 0 .. 5
            ("Reserved3", ctypes.c_uint32 * 46),           # 
            ("WPMR"     , ctypes.c_uint32),                # (Dmac Offset: 0x1E4) DMAC Write Protect Mode Register
            ("WPSR"     , ctypes.c_uint32),                # (Dmac Offset: 0x1E8) DMAC Write Protect Status Register
        ]

class SAM3xaEfc:
    class Type(ctypes.Structure):
        _fields_ = [
            ("EEFC_FMR", ctypes.c_uint32), # (Efc Offset: 0x00) EEFC Flash Mode Register
            ("EEFC_FCR", ctypes.c_uint32), # (Efc Offset: 0x04) EEFC Flash Command Register
            ("EEFC_FSR", ctypes.c_uint32), # (Efc Offset: 0x08) EEFC Flash Status Register
            ("EEFC_FRR", ctypes.c_uint32), # (Efc Offset: 0x0C) EEFC Flash Result Register
        ]

class SAM3xaPwm:
    class Type(ctypes.Structure):
        _fields_ = [
            ("CLK"      , ctypes.c_uint32),              # (Pwm Offset: 0x00) PWM Clock Register
            ("ENA"      , ctypes.c_uint32),              # (Pwm Offset: 0x04) PWM Enable Register
            ("DIS"      , ctypes.c_uint32),              # (Pwm Offset: 0x08) PWM Disable Register
            ("SR"       , ctypes.c_uint32),              # (Pwm Offset: 0x0C) PWM Status Register
            ("IER1"     , ctypes.c_uint32),              # (Pwm Offset: 0x10) PWM Interrupt Enable Register 1
            ("IDR1"     , ctypes.c_uint32),              # (Pwm Offset: 0x14) PWM Interrupt Disable Register 1
            ("IMR1"     , ctypes.c_uint32),              # (Pwm Offset: 0x18) PWM Interrupt Mask Register 1
            ("ISR1"     , ctypes.c_uint32),              # (Pwm Offset: 0x1C) PWM Interrupt Status Register 1
            ("SCM"      , ctypes.c_uint32),              # (Pwm Offset: 0x20) PWM Sync Channels Mode Register
            ("Reserved1", ctypes.c_uint32),              # 
            ("SCUC"     , ctypes.c_uint32),              # (Pwm Offset: 0x28) PWM Sync Channels Update Control Register
            ("SCUP"     , ctypes.c_uint32),              # (Pwm Offset: 0x2C) PWM Sync Channels Update Period Register
            ("SCUPUPD"  , ctypes.c_uint32),              # (Pwm Offset: 0x30) PWM Sync Channels Update Period Update Register
            ("IER2"     , ctypes.c_uint32),              # (Pwm Offset: 0x34) PWM Interrupt Enable Register 2
            ("IDR2"     , ctypes.c_uint32),              # (Pwm Offset: 0x38) PWM Interrupt Disable Register 2
            ("IMR2"     , ctypes.c_uint32),              # (Pwm Offset: 0x3C) PWM Interrupt Mask Register 2
            ("ISR2"     , ctypes.c_uint32),              # (Pwm Offset: 0x40) PWM Interrupt Status Register 2
            ("OOV"      , ctypes.c_uint32),              # (Pwm Offset: 0x44) PWM Output Override Value Register
            ("OS"       , ctypes.c_uint32),              # (Pwm Offset: 0x48) PWM Output Selection Register
            ("OSS"      , ctypes.c_uint32),              # (Pwm Offset: 0x4C) PWM Output Selection Set Register
            ("OSC"      , ctypes.c_uint32),              # (Pwm Offset: 0x50) PWM Output Selection Clear Register
            ("OSSUPD"   , ctypes.c_uint32),              # (Pwm Offset: 0x54) PWM Output Selection Set Update Register
            ("OSCUPD"   , ctypes.c_uint32),              # (Pwm Offset: 0x58) PWM Output Selection Clear Update Register
            ("FMR"      , ctypes.c_uint32),              # (Pwm Offset: 0x5C) PWM Fault Mode Register
            ("FSR"      , ctypes.c_uint32),              # (Pwm Offset: 0x60) PWM Fault Status Register
            ("FCR"      , ctypes.c_uint32),              # (Pwm Offset: 0x64) PWM Fault Clear Register
            ("FPV"      , ctypes.c_uint32),              # (Pwm Offset: 0x68) PWM Fault Protection Value Register
            ("FPE1"     , ctypes.c_uint32),              # (Pwm Offset: 0x6C) PWM Fault Protection Enable Register 1
            ("FPE2"     , ctypes.c_uint32),              # (Pwm Offset: 0x70) PWM Fault Protection Enable Register 2
            ("Reserved2", ctypes.c_uint32 * 2),          # 
            ("ELMR"     , ctypes.c_uint32 * 2),          # (Pwm Offset: 0x7C) PWM Event Line 0 Mode Register
            ("Reserved3", ctypes.c_uint32 * 11),         # 
            ("SMMR"     , ctypes.c_uint32),              # (Pwm Offset: 0xB0) PWM Stepper Motor Mode Register
            ("Reserved4", ctypes.c_uint32 * 12),         # 
            ("WPCR"     , ctypes.c_uint32),              # (Pwm Offset: 0xE4) PWM Write Protect Control Register
            ("WPSR"     , ctypes.c_uint32),              # (Pwm Offset: 0xE8) PWM Write Protect Status Register
            ("Reserved5", ctypes.c_uint32 * 7),          # 
            ("TPR"      , ctypes.c_uint32),              # (Pwm Offset: 0x108) Transmit Pointer Register
            ("TCR"      , ctypes.c_uint32),              # (Pwm Offset: 0x10C) Transmit Counter Register
            ("Reserved6", ctypes.c_uint32 * 2),          # 
            ("TNPR"     , ctypes.c_uint32),              # (Pwm Offset: 0x118) Transmit Next Pointer Register
            ("TNCR"     , ctypes.c_uint32),              # (Pwm Offset: 0x11C) Transmit Next Counter Register
            ("PTCR"     , ctypes.c_uint32),              # (Pwm Offset: 0x120) Transfer Control Register
            ("PTSR"     , ctypes.c_uint32),              # (Pwm Offset: 0x124) Transfer Status Register
            ("Reserved7", ctypes.c_uint32 * 2),          # 
            ("CMP"      , PwmCmp * PWMCMP_NUMBER),       # (Pwm Offset: 0x130) 0 .. 7
            ("Reserved8", ctypes.c_uint32 * 20),         # 
            ("CH_NUM"   , PwmCh_num * PWMCH_NUM_NUMBER), # (Pwm Offset: 0x200) ch_num = 0 .. 7
        ]

class SAM3xaSmc:
    class Type(ctypes.Structure):
        _fields_ = [
            ("CFG"      , ctypes.c_uint32),                    # (Smc Offset: 0x000) SMC NFC Configuration Register
            ("CTRL"     , ctypes.c_uint32),                    # (Smc Offset: 0x004) SMC NFC Control Register
            ("SR"       , ctypes.c_uint32),                    # (Smc Offset: 0x008) SMC NFC Status Register
            ("IER"      , ctypes.c_uint32),                    # (Smc Offset: 0x00C) SMC NFC Interrupt Enable Register
            ("IDR"      , ctypes.c_uint32),                    # (Smc Offset: 0x010) SMC NFC Interrupt Disable Register
            ("IMR"      , ctypes.c_uint32),                    # (Smc Offset: 0x014) SMC NFC Interrupt Mask Register
            ("ADDR"     , ctypes.c_uint32),                    # (Smc Offset: 0x018) SMC NFC Address Cycle Zero Register
            ("BANK"     , ctypes.c_uint32),                    # (Smc Offset: 0x01C) SMC Bank Address Register
            ("ECC_CTRL" , ctypes.c_uint32),                    # (Smc Offset: 0x020) SMC ECC Control Register
            ("ECC_MD"   , ctypes.c_uint32),                    # (Smc Offset: 0x024) SMC ECC Mode Register
            ("ECC_SR1"  , ctypes.c_uint32),                    # (Smc Offset: 0x028) SMC ECC Status 1 Register
            ("ECC_PR0"  , ctypes.c_uint32),                    # (Smc Offset: 0x02C) SMC ECC Parity 0 Register
            ("ECC_PR1"  , ctypes.c_uint32),                    # (Smc Offset: 0x030) SMC ECC parity 1 Register
            ("ECC_SR2"  , ctypes.c_uint32),                    # (Smc Offset: 0x034) SMC ECC status 2 Register
            ("ECC_PR2"  , ctypes.c_uint32),                    # (Smc Offset: 0x038) SMC ECC parity 2 Register
            ("ECC_PR3"  , ctypes.c_uint32),                    # (Smc Offset: 0x03C) SMC ECC parity 3 Register
            ("ECC_PR4"  , ctypes.c_uint32),                    # (Smc Offset: 0x040) SMC ECC parity 4 Register
            ("ECC_PR5"  , ctypes.c_uint32),                    # (Smc Offset: 0x044) SMC ECC parity 5 Register
            ("ECC_PR6"  , ctypes.c_uint32),                    # (Smc Offset: 0x048) SMC ECC parity 6 Register
            ("ECC_PR7"  , ctypes.c_uint32),                    # (Smc Offset: 0x04C) SMC ECC parity 7 Register
            ("ECC_PR8"  , ctypes.c_uint32),                    # (Smc Offset: 0x050) SMC ECC parity 8 Register
            ("ECC_PR9"  , ctypes.c_uint32),                    # (Smc Offset: 0x054) SMC ECC parity 9 Register
            ("ECC_PR10" , ctypes.c_uint32),                    # (Smc Offset: 0x058) SMC ECC parity 10 Register
            ("ECC_PR11" , ctypes.c_uint32),                    # (Smc Offset: 0x05C) SMC ECC parity 11 Register
            ("ECC_PR12" , ctypes.c_uint32),                    # (Smc Offset: 0x060) SMC ECC parity 12 Register
            ("ECC_PR13" , ctypes.c_uint32),                    # (Smc Offset: 0x064) SMC ECC parity 13 Register
            ("ECC_PR14" , ctypes.c_uint32),                    # (Smc Offset: 0x068) SMC ECC parity 14 Register
            ("ECC_PR15" , ctypes.c_uint32),                    # (Smc Offset: 0x06C) SMC ECC parity 15 Register
            ("CS_NUMBER", SmcCs_number * SMCCS_NUMBER_NUMBER), # (Smc Offset: 0x70) CS_number = 0 .. 7
            ("OCMS"     , ctypes.c_uint32),                    # (Smc Offset: 0x110) SMC OCMS Register
            ("KEY1"     , ctypes.c_uint32),                    # (Smc Offset: 0x114) SMC OCMS KEY1 Register
            ("KEY2"     , ctypes.c_uint32),                    # (Smc Offset: 0x118) SMC OCMS KEY2 Register
            ("Reserved1", ctypes.c_uint32 * 50),               # 
            ("WPCR"     , ctypes.c_uint32),                    # (Smc Offset: 0x1E4) Write Protection Control Register
            ("WPSR"     , ctypes.c_uint32),                    # (Smc Offset: 0x1E8) Write Protection Status Register
        ]

class SAM3xaUotghs:
    class Type(ctypes.Structure):
        _fields_ = [
            ("DEVCTRL"   , ctypes.c_uint32),                    # (Uotghs Offset: 0x0000) Device General Control Register
            ("DEVISR"    , ctypes.c_uint32),                    # (Uotghs Offset: 0x0004) Device Global Interrupt Status Register
            ("DEVICR"    , ctypes.c_uint32),                    # (Uotghs Offset: 0x0008) Device Global Interrupt Clear Register
            ("DEVIFR"    , ctypes.c_uint32),                    # (Uotghs Offset: 0x000C) Device Global Interrupt Set Register
            ("DEVIMR"    , ctypes.c_uint32),                    # (Uotghs Offset: 0x0010) Device Global Interrupt Mask Register
            ("DEVIDR"    , ctypes.c_uint32),                    # (Uotghs Offset: 0x0014) Device Global Interrupt Disable Register
            ("DEVIER"    , ctypes.c_uint32),                    # (Uotghs Offset: 0x0018) Device Global Interrupt Enable Register
            ("DEVEPT"    , ctypes.c_uint32),                    # (Uotghs Offset: 0x001C) Device Endpoint Register
            ("DEVFNUM"   , ctypes.c_uint32),                    # (Uotghs Offset: 0x0020) Device Frame Number Register
            ("Reserved1" , ctypes.c_uint32 * 55),               # 
            ("DEVEPTCFG" , ctypes.c_uint32 * 10),               # (Uotghs Offset: 0x100) Device Endpoint Configuration Register (n = 0)
            ("Reserved2" , ctypes.c_uint32 * 2),                # 
            ("DEVEPTISR" , ctypes.c_uint32 * 10),               # (Uotghs Offset: 0x130) Device Endpoint Status Register (n = 0)
            ("Reserved3" , ctypes.c_uint32 * 2),                # 
            ("DEVEPTICR" , ctypes.c_uint32 * 10),               # (Uotghs Offset: 0x160) Device Endpoint Clear Register (n = 0)
            ("Reserved4" , ctypes.c_uint32 * 2),                # 
            ("DEVEPTIFR" , ctypes.c_uint32 * 10),               # (Uotghs Offset: 0x190) Device Endpoint Set Register (n = 0)
            ("Reserved5" , ctypes.c_uint32 * 2),                # 
            ("DEVEPTIMR" , ctypes.c_uint32 * 10),               # (Uotghs Offset: 0x1C0) Device Endpoint Mask Register (n = 0)
            ("Reserved6" , ctypes.c_uint32 * 2),                # 
            ("DEVEPTIER" , ctypes.c_uint32 * 10),               # (Uotghs Offset: 0x1F0) Device Endpoint Enable Register (n = 0)
            ("Reserved7" , ctypes.c_uint32 * 2),                # 
            ("DEVEPTIDR" , ctypes.c_uint32 * 10),               # (Uotghs Offset: 0x220) Device Endpoint Disable Register (n = 0)
            ("Reserved8" , ctypes.c_uint32 * 50),               # 
            ("DEVDMA"    , UotghsDevdma * UOTGHSDEVDMA_NUMBER), # (Uotghs Offset: 0x310) n = 1 .. 7
            ("Reserved9" , ctypes.c_uint32 * 32),               # 
            ("HSTCTRL"   , ctypes.c_uint32),                    # (Uotghs Offset: 0x0400) Host General Control Register
            ("HSTISR"    , ctypes.c_uint32),                    # (Uotghs Offset: 0x0404) Host Global Interrupt Status Register
            ("HSTICR"    , ctypes.c_uint32),                    # (Uotghs Offset: 0x0408) Host Global Interrupt Clear Register
            ("HSTIFR"    , ctypes.c_uint32),                    # (Uotghs Offset: 0x040C) Host Global Interrupt Set Register
            ("HSTIMR"    , ctypes.c_uint32),                    # (Uotghs Offset: 0x0410) Host Global Interrupt Mask Register
            ("HSTIDR"    , ctypes.c_uint32),                    # (Uotghs Offset: 0x0414) Host Global Interrupt Disable Register
            ("HSTIER"    , ctypes.c_uint32),                    # (Uotghs Offset: 0x0418) Host Global Interrupt Enable Register
            ("HSTPIP"    , ctypes.c_uint32),                    # (Uotghs Offset: 0x0041C) Host Pipe Register
            ("HSTFNUM"   , ctypes.c_uint32),                    # (Uotghs Offset: 0x0420) Host Frame Number Register
            ("HSTADDR1"  , ctypes.c_uint32),                    # (Uotghs Offset: 0x0424) Host Address 1 Register
            ("HSTADDR2"  , ctypes.c_uint32),                    # (Uotghs Offset: 0x0428) Host Address 2 Register
            ("HSTADDR3"  , ctypes.c_uint32),                    # (Uotghs Offset: 0x042C) Host Address 3 Register
            ("Reserved10", ctypes.c_uint32 * 52),               # 
            ("HSTPIPCFG" , ctypes.c_uint32 * 10),               # (Uotghs Offset: 0x500) Host Pipe Configuration Register (n = 0)
            ("Reserved11", ctypes.c_uint32 * 2),                # 
            ("HSTPIPISR" , ctypes.c_uint32 * 10),               # (Uotghs Offset: 0x530) Host Pipe Status Register (n = 0)
            ("Reserved12", ctypes.c_uint32 * 2),                # 
            ("HSTPIPICR" , ctypes.c_uint32 * 10),               # (Uotghs Offset: 0x560) Host Pipe Clear Register (n = 0)
            ("Reserved13", ctypes.c_uint32 * 2),                # 
            ("HSTPIPIFR" , ctypes.c_uint32 * 10),               # (Uotghs Offset: 0x590) Host Pipe Set Register (n = 0)
            ("Reserved14", ctypes.c_uint32 * 2),                # 
            ("HSTPIPIMR" , ctypes.c_uint32 * 10),               # (Uotghs Offset: 0x5C0) Host Pipe Mask Register (n = 0)
            ("Reserved15", ctypes.c_uint32 * 2),                # 
            ("HSTPIPIER" , ctypes.c_uint32 * 10),               # (Uotghs Offset: 0x5F0) Host Pipe Enable Register (n = 0)
            ("Reserved16", ctypes.c_uint32 * 2),                # 
            ("HSTPIPIDR" , ctypes.c_uint32 * 10),               # (Uotghs Offset: 0x620) Host Pipe Disable Register (n = 0)
            ("Reserved17", ctypes.c_uint32 * 2),                # 
            ("HSTPIPINRQ", ctypes.c_uint32 * 10),               # (Uotghs Offset: 0x650) Host Pipe IN Request Register (n = 0)
            ("Reserved18", ctypes.c_uint32 * 2),                # 
            ("HSTPIPERR" , ctypes.c_uint32 * 10),               # (Uotghs Offset: 0x680) Host Pipe Error Register (n = 0)
            ("Reserved19", ctypes.c_uint32 * 26),               # 
            ("HSTDMA"    , UotghsHstdma * UOTGHSHSTDMA_NUMBER), # (Uotghs Offset: 0x710) n = 1 .. 7
            ("Reserved20", ctypes.c_uint32 * 32),               # 
            ("CTRL"      , ctypes.c_uint32),                    # (Uotghs Offset: 0x0800) General Control Register
            ("SR"        , ctypes.c_uint32),                    # (Uotghs Offset: 0x0804) General Status Register
            ("SCR"       , ctypes.c_uint32),                    # (Uotghs Offset: 0x0808) General Status Clear Register
            ("SFR"       , ctypes.c_uint32),                    # (Uotghs Offset: 0x080C) General Status Set Register
            ("Reserved21", ctypes.c_uint32 * 7),                # 
            ("FSM"       , ctypes.c_uint32),                    # (Uotghs Offset: 0x082C) General Finite State Machine Register
        ]

class SAM3xaSupc:
    class Type(ctypes.Structure):
        _fields_ = [
            ("CR"  , ctypes.c_uint32), # (Supc Offset: 0x00) Supply Controller Control Register
            ("SMMR", ctypes.c_uint32), # (Supc Offset: 0x04) Supply Controller Supply Monitor Mode Register
            ("MR"  , ctypes.c_uint32), # (Supc Offset: 0x08) Supply Controller Mode Register
            ("WUMR", ctypes.c_uint32), # (Supc Offset: 0x0C) Supply Controller Wake Up Mode Register
            ("WUIR", ctypes.c_uint32), # (Supc Offset: 0x10) Supply Controller Wake Up Inputs Register
            ("SR"  , ctypes.c_uint32), # (Supc Offset: 0x14) Supply Controller Status Register
        ]

class SAM3xaSdramc:
    class Type(ctypes.Structure):
        _fields_ = [
            ("MR"       , ctypes.c_uint32), # (Sdramc Offset: 0x00) SDRAMC Mode Register
            ("TR"       , ctypes.c_uint32), # (Sdramc Offset: 0x04) SDRAMC Refresh Timer Register
            ("CR"       , ctypes.c_uint32), # (Sdramc Offset: 0x08) SDRAMC Configuration Register
            ("Reserved1", ctypes.c_uint32), # 
            ("LPR"      , ctypes.c_uint32), # (Sdramc Offset: 0x10) SDRAMC Low Power Register
            ("IER"      , ctypes.c_uint32), # (Sdramc Offset: 0x14) SDRAMC Interrupt Enable Register
            ("IDR"      , ctypes.c_uint32), # (Sdramc Offset: 0x18) SDRAMC Interrupt Disable Register
            ("IMR"      , ctypes.c_uint32), # (Sdramc Offset: 0x1C) SDRAMC Interrupt Mask Register
            ("ISR"      , ctypes.c_uint32), # (Sdramc Offset: 0x20) SDRAMC Interrupt Status Register
            ("MDR"      , ctypes.c_uint32), # (Sdramc Offset: 0x24) SDRAMC Memory Device Register
            ("CR1"      , ctypes.c_uint32), # (Sdramc Offset: 0x28) SDRAMC Configuration Register 1
            ("OCMS"     , ctypes.c_uint32), # (Sdramc Offset: 0x2C) SDRAMC OCMS Register 1
        ]

class SAM3xaPio:
    class Type(ctypes.Structure):
        _fields_ = [
            ("PER"       , ctypes.c_uint32),     # (Pio Offset: 0x0000) PIO Enable Register
            ("PDR"       , ctypes.c_uint32),     # (Pio Offset: 0x0004) PIO Disable Register
            ("PSR"       , ctypes.c_uint32),     # (Pio Offset: 0x0008) PIO Status Register
            ("Reserved1" , ctypes.c_uint32),     # 
            ("OER"       , ctypes.c_uint32),     # (Pio Offset: 0x0010) Output Enable Register
            ("ODR"       , ctypes.c_uint32),     # (Pio Offset: 0x0014) Output Disable Register
            ("OSR"       , ctypes.c_uint32),     # (Pio Offset: 0x0018) Output Status Register
            ("Reserved2" , ctypes.c_uint32),     # 
            ("IFER"      , ctypes.c_uint32),     # (Pio Offset: 0x0020) Glitch Input Filter Enable Register
            ("IFDR"      , ctypes.c_uint32),     # (Pio Offset: 0x0024) Glitch Input Filter Disable Register
            ("IFSR"      , ctypes.c_uint32),     # (Pio Offset: 0x0028) Glitch Input Filter Status Register
            ("Reserved3" , ctypes.c_uint32),     # 
            ("SODR"      , ctypes.c_uint32),     # (Pio Offset: 0x0030) Set Output Data Register
            ("CODR"      , ctypes.c_uint32),     # (Pio Offset: 0x0034) Clear Output Data Register
            ("ODSR"      , ctypes.c_uint32),     # (Pio Offset: 0x0038) Output Data Status Register
            ("PDSR"      , ctypes.c_uint32),     # (Pio Offset: 0x003C) Pin Data Status Register
            ("IER"       , ctypes.c_uint32),     # (Pio Offset: 0x0040) Interrupt Enable Register
            ("IDR"       , ctypes.c_uint32),     # (Pio Offset: 0x0044) Interrupt Disable Register
            ("IMR"       , ctypes.c_uint32),     # (Pio Offset: 0x0048) Interrupt Mask Register
            ("ISR"       , ctypes.c_uint32),     # (Pio Offset: 0x004C) Interrupt Status Register
            ("MDER"      , ctypes.c_uint32),     # (Pio Offset: 0x0050) Multi-driver Enable Register
            ("MDDR"      , ctypes.c_uint32),     # (Pio Offset: 0x0054) Multi-driver Disable Register
            ("MDSR"      , ctypes.c_uint32),     # (Pio Offset: 0x0058) Multi-driver Status Register
            ("Reserved4" , ctypes.c_uint32),     # 
            ("PUDR"      , ctypes.c_uint32),     # (Pio Offset: 0x0060) Pull-up Disable Register
            ("PUER"      , ctypes.c_uint32),     # (Pio Offset: 0x0064) Pull-up Enable Register
            ("PUSR"      , ctypes.c_uint32),     # (Pio Offset: 0x0068) Pad Pull-up Status Register
            ("Reserved5" , ctypes.c_uint32),     # 
            ("ABSR"      , ctypes.c_uint32),     # (Pio Offset: 0x0070) Peripheral AB Select Register
            ("Reserved6" , ctypes.c_uint32 * 3), # 
            ("SCIFSR"    , ctypes.c_uint32),     # (Pio Offset: 0x0080) System Clock Glitch Input Filter Select Register
            ("DIFSR"     , ctypes.c_uint32),     # (Pio Offset: 0x0084) Debouncing Input Filter Select Register
            ("IFDGSR"    , ctypes.c_uint32),     # (Pio Offset: 0x0088) Glitch or Debouncing Input Filter Clock Selection Status Register
            ("SCDR"      , ctypes.c_uint32),     # (Pio Offset: 0x008C) Slow Clock Divider Debouncing Register
            ("Reserved7" , ctypes.c_uint32 * 4), # 
            ("OWER"      , ctypes.c_uint32),     # (Pio Offset: 0x00A0) Output Write Enable
            ("OWDR"      , ctypes.c_uint32),     # (Pio Offset: 0x00A4) Output Write Disable
            ("OWSR"      , ctypes.c_uint32),     # (Pio Offset: 0x00A8) Output Write Status Register
            ("Reserved8" , ctypes.c_uint32),     # 
            ("AIMER"     , ctypes.c_uint32),     # (Pio Offset: 0x00B0) Additional Interrupt Modes Enable Register
            ("AIMDR"     , ctypes.c_uint32),     # (Pio Offset: 0x00B4) Additional Interrupt Modes Disables Register
            ("AIMMR"     , ctypes.c_uint32),     # (Pio Offset: 0x00B8) Additional Interrupt Modes Mask Register
            ("Reserved9" , ctypes.c_uint32),     # 
            ("ESR"       , ctypes.c_uint32),     # (Pio Offset: 0x00C0) Edge Select Register
            ("LSR"       , ctypes.c_uint32),     # (Pio Offset: 0x00C4) Level Select Register
            ("ELSR"      , ctypes.c_uint32),     # (Pio Offset: 0x00C8) Edge/Level Status Register
            ("Reserved10", ctypes.c_uint32),     # 
            ("FELLSR"    , ctypes.c_uint32),     # (Pio Offset: 0x00D0) Falling Edge/Low Level Select Register
            ("REHLSR"    , ctypes.c_uint32),     # (Pio Offset: 0x00D4) Rising Edge/ High Level Select Register
            ("FRLHSR"    , ctypes.c_uint32),     # (Pio Offset: 0x00D8) Fall/Rise - Low/High Status Register
            ("Reserved11", ctypes.c_uint32),     # 
            ("LOCKSR"    , ctypes.c_uint32),     # (Pio Offset: 0x00E0) Lock Status
            ("WPMR"      , ctypes.c_uint32),     # (Pio Offset: 0x00E4) Write Protect Mode Register
            ("WPSR"      , ctypes.c_uint32),     # (Pio Offset: 0x00E8) Write Protect Status Register
        ]

class SAM3xaTrng:
    class Type(ctypes.Structure):
        _fields_ = [
            ("CR"       , ctypes.c_uint32),      # (Trng Offset: 0x00) Control Register
            ("Reserved1", ctypes.c_uint32 * 3),  # 
            ("IER"      , ctypes.c_uint32),      # (Trng Offset: 0x10) Interrupt Enable Register
            ("IDR"      , ctypes.c_uint32),      # (Trng Offset: 0x14) Interrupt Disable Register
            ("IMR"      , ctypes.c_uint32),      # (Trng Offset: 0x18) Interrupt Mask Register
            ("ISR"      , ctypes.c_uint32),      # (Trng Offset: 0x1C) Interrupt Status Register
            ("Reserved2", ctypes.c_uint32 * 12), # 
            ("ODATA"    , ctypes.c_uint32),      # (Trng Offset: 0x50) Output Data Register
        ]

class SAM3xaAdc:
    class Type(ctypes.Structure):
        _fields_ = [
            ("CR"       , ctypes.c_uint32),      # (Adc Offset: 0x00) Control Register
            ("MR"       , ctypes.c_uint32),      # (Adc Offset: 0x04) Mode Register
            ("SEQR1"    , ctypes.c_uint32),      # (Adc Offset: 0x08) Channel Sequence Register 1
            ("SEQR2"    , ctypes.c_uint32),      # (Adc Offset: 0x0C) Channel Sequence Register 2
            ("CHER"     , ctypes.c_uint32),      # (Adc Offset: 0x10) Channel Enable Register
            ("CHDR"     , ctypes.c_uint32),      # (Adc Offset: 0x14) Channel Disable Register
            ("CHSR"     , ctypes.c_uint32),      # (Adc Offset: 0x18) Channel Status Register
            ("Reserved1", ctypes.c_uint32),      # 
            ("LCDR"     , ctypes.c_uint32),      # (Adc Offset: 0x20) Last Converted Data Register
            ("IER"      , ctypes.c_uint32),      # (Adc Offset: 0x24) Interrupt Enable Register
            ("IDR"      , ctypes.c_uint32),      # (Adc Offset: 0x28) Interrupt Disable Register
            ("IMR"      , ctypes.c_uint32),      # (Adc Offset: 0x2C) Interrupt Mask Register
            ("ISR"      , ctypes.c_uint32),      # (Adc Offset: 0x30) Interrupt Status Register
            ("Reserved2", ctypes.c_uint32 * 2),  # 
            ("OVER"     , ctypes.c_uint32),      # (Adc Offset: 0x3C) Overrun Status Register
            ("EMR"      , ctypes.c_uint32),      # (Adc Offset: 0x40) Extended Mode Register
            ("CWR"      , ctypes.c_uint32),      # (Adc Offset: 0x44) Compare Window Register
            ("CGR"      , ctypes.c_uint32),      # (Adc Offset: 0x48) Channel Gain Register
            ("COR"      , ctypes.c_uint32),      # (Adc Offset: 0x4C) Channel Offset Register
            ("CDR"      , ctypes.c_uint32 * 16), # (Adc Offset: 0x50) Channel Data Register
            ("Reserved3", ctypes.c_uint32),      # 
            ("ACR"      , ctypes.c_uint32),      # (Adc Offset: 0x94) Analog Control Register
            ("Reserved4", ctypes.c_uint32 * 19), # 
            ("WPMR"     , ctypes.c_uint32),      # (Adc Offset: 0xE4) Write Protect Mode Register
            ("WPSR"     , ctypes.c_uint32),      # (Adc Offset: 0xE8) Write Protect Status Register
            ("Reserved5", ctypes.c_uint32 * 5),  # 
            ("RPR"      , ctypes.c_uint32),      # (Adc Offset: 0x100) Receive Pointer Register
            ("RCR"      , ctypes.c_uint32),      # (Adc Offset: 0x104) Receive Counter Register
            ("Reserved6", ctypes.c_uint32 * 2),  # 
            ("RNPR"     , ctypes.c_uint32),      # (Adc Offset: 0x110) Receive Next Pointer Register
            ("RNCR"     , ctypes.c_uint32),      # (Adc Offset: 0x114) Receive Next Counter Register
            ("Reserved7", ctypes.c_uint32 * 2),  # 
            ("PTCR"     , ctypes.c_uint32),      # (Adc Offset: 0x120) Transfer Control Register
            ("PTSR"     , ctypes.c_uint32),      # (Adc Offset: 0x124) Transfer Status Register
        ]

class SAM3xaSsc:
    class Type(ctypes.Structure):
        _fields_ = [
            ("CR"       , ctypes.c_uint32),      # (Ssc Offset: 0x0) Control Register
            ("CMR"      , ctypes.c_uint32),      # (Ssc Offset: 0x4) Clock Mode Register
            ("Reserved1", ctypes.c_uint32 * 2),  # 
            ("RCMR"     , ctypes.c_uint32),      # (Ssc Offset: 0x10) Receive Clock Mode Register
            ("RFMR"     , ctypes.c_uint32),      # (Ssc Offset: 0x14) Receive Frame Mode Register
            ("TCMR"     , ctypes.c_uint32),      # (Ssc Offset: 0x18) Transmit Clock Mode Register
            ("TFMR"     , ctypes.c_uint32),      # (Ssc Offset: 0x1C) Transmit Frame Mode Register
            ("RHR"      , ctypes.c_uint32),      # (Ssc Offset: 0x20) Receive Holding Register
            ("THR"      , ctypes.c_uint32),      # (Ssc Offset: 0x24) Transmit Holding Register
            ("Reserved2", ctypes.c_uint32 * 2),  # 
            ("RSHR"     , ctypes.c_uint32),      # (Ssc Offset: 0x30) Receive Sync. Holding Register
            ("TSHR"     , ctypes.c_uint32),      # (Ssc Offset: 0x34) Transmit Sync. Holding Register
            ("RC0R"     , ctypes.c_uint32),      # (Ssc Offset: 0x38) Receive Compare 0 Register
            ("RC1R"     , ctypes.c_uint32),      # (Ssc Offset: 0x3C) Receive Compare 1 Register
            ("SR"       , ctypes.c_uint32),      # (Ssc Offset: 0x40) Status Register
            ("IER"      , ctypes.c_uint32),      # (Ssc Offset: 0x44) Interrupt Enable Register
            ("IDR"      , ctypes.c_uint32),      # (Ssc Offset: 0x48) Interrupt Disable Register
            ("IMR"      , ctypes.c_uint32),      # (Ssc Offset: 0x4C) Interrupt Mask Register
            ("Reserved3", ctypes.c_uint32 * 37), # 
            ("WPMR"     , ctypes.c_uint32),      # (Ssc Offset: 0xE4) Write Protect Mode Register
            ("WPSR"     , ctypes.c_uint32),      # (Ssc Offset: 0xE8) Write Protect Status Register
        ]

class SAM3xaTwi:
    class Type(ctypes.Structure):
        _fields_ = [
            ("CR"       , ctypes.c_uint32),      # (Twi Offset: 0x00) Control Register
            ("MMR"      , ctypes.c_uint32),      # (Twi Offset: 0x04) Master Mode Register
            ("SMR"      , ctypes.c_uint32),      # (Twi Offset: 0x08) Slave Mode Register
            ("IADR"     , ctypes.c_uint32),      # (Twi Offset: 0x0C) Internal Address Register
            ("CWGR"     , ctypes.c_uint32),      # (Twi Offset: 0x10) Clock Waveform Generator Register
            ("Reserved1", ctypes.c_uint32 * 3),  # 
            ("SR"       , ctypes.c_uint32),      # (Twi Offset: 0x20) Status Register
            ("IER"      , ctypes.c_uint32),      # (Twi Offset: 0x24) Interrupt Enable Register
            ("IDR"      , ctypes.c_uint32),      # (Twi Offset: 0x28) Interrupt Disable Register
            ("IMR"      , ctypes.c_uint32),      # (Twi Offset: 0x2C) Interrupt Mask Register
            ("RHR"      , ctypes.c_uint32),      # (Twi Offset: 0x30) Receive Holding Register
            ("THR"      , ctypes.c_uint32),      # (Twi Offset: 0x34) Transmit Holding Register
            ("Reserved2", ctypes.c_uint32 * 50), # 
            ("RPR"      , ctypes.c_uint32),      # (Twi Offset: 0x100) Receive Pointer Register
            ("RCR"      , ctypes.c_uint32),      # (Twi Offset: 0x104) Receive Counter Register
            ("TPR"      , ctypes.c_uint32),      # (Twi Offset: 0x108) Transmit Pointer Register
            ("TCR"      , ctypes.c_uint32),      # (Twi Offset: 0x10C) Transmit Counter Register
            ("RNPR"     , ctypes.c_uint32),      # (Twi Offset: 0x110) Receive Next Pointer Register
            ("RNCR"     , ctypes.c_uint32),      # (Twi Offset: 0x114) Receive Next Counter Register
            ("TNPR"     , ctypes.c_uint32),      # (Twi Offset: 0x118) Transmit Next Pointer Register
            ("TNCR"     , ctypes.c_uint32),      # (Twi Offset: 0x11C) Transmit Next Counter Register
            ("PTCR"     , ctypes.c_uint32),      # (Twi Offset: 0x120) Transfer Control Register
            ("PTSR"     , ctypes.c_uint32),      # (Twi Offset: 0x124) Transfer Status Register
        ]

class SAM3xaPmc:
    class Type(ctypes.Structure):
        _fields_ = [
            ("SCER"      , ctypes.c_uint32),      # (Pmc Offset: 0x0000) System Clock Enable Register
            ("SCDR"      , ctypes.c_uint32),      # (Pmc Offset: 0x0004) System Clock Disable Register
            ("SCSR"      , ctypes.c_uint32),      # (Pmc Offset: 0x0008) System Clock Status Register
            ("Reserved1" , ctypes.c_uint32),      # 
            ("PCER0"     , ctypes.c_uint32),      # (Pmc Offset: 0x0010) Peripheral Clock Enable Register 0
            ("PCDR0"     , ctypes.c_uint32),      # (Pmc Offset: 0x0014) Peripheral Clock Disable Register 0
            ("PCSR0"     , ctypes.c_uint32),      # (Pmc Offset: 0x0018) Peripheral Clock Status Register 0
            ("CKGR_UCKR" , ctypes.c_uint32),      # (Pmc Offset: 0x001C) UTMI Clock Register
            ("CKGR_MOR"  , ctypes.c_uint32),      # (Pmc Offset: 0x0020) Main Oscillator Register
            ("CKGR_MCFR" , ctypes.c_uint32),      # (Pmc Offset: 0x0024) Main Clock Frequency Register
            ("CKGR_PLLAR", ctypes.c_uint32),      # (Pmc Offset: 0x0028) PLLA Register
            ("Reserved2" , ctypes.c_uint32),      # 
            ("MCKR"      , ctypes.c_uint32),      # (Pmc Offset: 0x0030) Master Clock Register
            ("Reserved3" , ctypes.c_uint32),      # 
            ("USB"       , ctypes.c_uint32),      # (Pmc Offset: 0x0038) USB Clock Register
            ("Reserved4" , ctypes.c_uint32),      # 
            ("PCK"       , ctypes.c_uint32 * 3),  # (Pmc Offset: 0x0040) Programmable Clock 0 Register
            ("Reserved5" , ctypes.c_uint32 * 5),  # 
            ("IER"       , ctypes.c_uint32),      # (Pmc Offset: 0x0060) Interrupt Enable Register
            ("IDR"       , ctypes.c_uint32),      # (Pmc Offset: 0x0064) Interrupt Disable Register
            ("SR"        , ctypes.c_uint32),      # (Pmc Offset: 0x0068) Status Register
            ("IMR"       , ctypes.c_uint32),      # (Pmc Offset: 0x006C) Interrupt Mask Register
            ("FSMR"      , ctypes.c_uint32),      # (Pmc Offset: 0x0070) Fast Startup Mode Register
            ("FSPR"      , ctypes.c_uint32),      # (Pmc Offset: 0x0074) Fast Startup Polarity Register
            ("FOCR"      , ctypes.c_uint32),      # (Pmc Offset: 0x0078) Fault Output Clear Register
            ("Reserved6" , ctypes.c_uint32 * 26), # 
            ("WPMR"      , ctypes.c_uint32),      # (Pmc Offset: 0x00E4) Write Protect Mode Register
            ("WPSR"      , ctypes.c_uint32),      # (Pmc Offset: 0x00E8) Write Protect Status Register
            ("Reserved7" , ctypes.c_uint32 * 5),  # 
            ("PCER1"     , ctypes.c_uint32),      # (Pmc Offset: 0x0100) Peripheral Clock Enable Register 1
            ("PCDR1"     , ctypes.c_uint32),      # (Pmc Offset: 0x0104) Peripheral Clock Disable Register 1
            ("PCSR1"     , ctypes.c_uint32),      # (Pmc Offset: 0x0108) Peripheral Clock Status Register 1
            ("PCR"       , ctypes.c_uint32),      # (Pmc Offset: 0x010C) Peripheral Control Register
        ]

class SAM3xaRtt:
    class Type(ctypes.Structure):
        _fields_ = [
            ("MR", ctypes.c_uint32), # (Rtt Offset: 0x00) Mode Register
            ("AR", ctypes.c_uint32), # (Rtt Offset: 0x04) Alarm Register
            ("VR", ctypes.c_uint32), # (Rtt Offset: 0x08) Value Register
            ("SR", ctypes.c_uint32), # (Rtt Offset: 0x0C) Status Register
        ]

class SAM3xaEmac:
    class Type(ctypes.Structure):
        _fields_ = [
            ("NCR"      , ctypes.c_uint32),        # (Emac Offset: 0x00) Network Control Register
            ("NCFGR"    , ctypes.c_uint32),        # (Emac Offset: 0x04) Network Configuration Register
            ("NSR"      , ctypes.c_uint32),        # (Emac Offset: 0x08) Network Status Register
            ("Reserved1", ctypes.c_uint32 * 2),    # 
            ("TSR"      , ctypes.c_uint32),        # (Emac Offset: 0x14) Transmit Status Register
            ("RBQP"     , ctypes.c_uint32),        # (Emac Offset: 0x18) Receive Buffer Queue Pointer Register
            ("TBQP"     , ctypes.c_uint32),        # (Emac Offset: 0x1C) Transmit Buffer Queue Pointer Register
            ("RSR"      , ctypes.c_uint32),        # (Emac Offset: 0x20) Receive Status Register
            ("ISR"      , ctypes.c_uint32),        # (Emac Offset: 0x24) Interrupt Status Register
            ("IER"      , ctypes.c_uint32),        # (Emac Offset: 0x28) Interrupt Enable Register
            ("IDR"      , ctypes.c_uint32),        # (Emac Offset: 0x2C) Interrupt Disable Register
            ("IMR"      , ctypes.c_uint32),        # (Emac Offset: 0x30) Interrupt Mask Register
            ("MAN"      , ctypes.c_uint32),        # (Emac Offset: 0x34) Phy Maintenance Register
            ("PTR"      , ctypes.c_uint32),        # (Emac Offset: 0x38) Pause Time Register
            ("PFR"      , ctypes.c_uint32),        # (Emac Offset: 0x3C) Pause Frames Received Register
            ("FTO"      , ctypes.c_uint32),        # (Emac Offset: 0x40) Frames Transmitted Ok Register
            ("SCF"      , ctypes.c_uint32),        # (Emac Offset: 0x44) Single Collision Frames Register
            ("MCF"      , ctypes.c_uint32),        # (Emac Offset: 0x48) Multiple Collision Frames Register
            ("FRO"      , ctypes.c_uint32),        # (Emac Offset: 0x4C) Frames Received Ok Register
            ("FCSE"     , ctypes.c_uint32),        # (Emac Offset: 0x50) Frame Check Sequence Errors Register
            ("ALE"      , ctypes.c_uint32),        # (Emac Offset: 0x54) Alignment Errors Register
            ("DTF"      , ctypes.c_uint32),        # (Emac Offset: 0x58) Deferred Transmission Frames Register
            ("LCOL"     , ctypes.c_uint32),        # (Emac Offset: 0x5C) Late Collisions Register
            ("ECOL"     , ctypes.c_uint32),        # (Emac Offset: 0x60) Excessive Collisions Register
            ("TUND"     , ctypes.c_uint32),        # (Emac Offset: 0x64) Transmit Underrun Errors Register
            ("CSE"      , ctypes.c_uint32),        # (Emac Offset: 0x68) Carrier Sense Errors Register
            ("RRE"      , ctypes.c_uint32),        # (Emac Offset: 0x6C) Receive Resource Errors Register
            ("ROV"      , ctypes.c_uint32),        # (Emac Offset: 0x70) Receive Overrun Errors Register
            ("RSE"      , ctypes.c_uint32),        # (Emac Offset: 0x74) Receive Symbol Errors Register
            ("ELE"      , ctypes.c_uint32),        # (Emac Offset: 0x78) Excessive Length Errors Register
            ("RJA"      , ctypes.c_uint32),        # (Emac Offset: 0x7C) Receive Jabbers Register
            ("USF"      , ctypes.c_uint32),        # (Emac Offset: 0x80) Undersize Frames Register
            ("STE"      , ctypes.c_uint32),        # (Emac Offset: 0x84) SQE Test Errors Register
            ("RLE"      , ctypes.c_uint32),        # (Emac Offset: 0x88) Received Length Field Mismatch Register
            ("Reserved2", ctypes.c_uint32),        # 
            ("HRB"      , ctypes.c_uint32),        # (Emac Offset: 0x90) Hash Register Bottom [31:0] Register
            ("HRT"      , ctypes.c_uint32),        # (Emac Offset: 0x94) Hash Register Top [63:32] Register
            ("SA"       , EmacSa * EMACSA_NUMBER), # (Emac Offset: 0x98) sa = 1 .. 4
            ("TID"      , ctypes.c_uint32),        # (Emac Offset: 0xB8) Type ID Checking Register
            ("Reserved3", ctypes.c_uint32),        # 
            ("USRIO"    , ctypes.c_uint32),        # (Emac Offset: 0xC0) User Input/Output Register
        ]

class SAM3xaTc:
    class Type(ctypes.Structure):
        _fields_ = [
            ("CHANNEL"  , TcChannel * TCCHANNEL_NUMBER), # (Tc Offset: 0x0) channel = 0 .. 2
            ("BCR"      , ctypes.c_uint32),              # (Tc Offset: 0xC0) Block Control Register
            ("BMR"      , ctypes.c_uint32),              # (Tc Offset: 0xC4) Block Mode Register
            ("QIER"     , ctypes.c_uint32),              # (Tc Offset: 0xC8) QDEC Interrupt Enable Register
            ("QIDR"     , ctypes.c_uint32),              # (Tc Offset: 0xCC) QDEC Interrupt Disable Register
            ("QIMR"     , ctypes.c_uint32),              # (Tc Offset: 0xD0) QDEC Interrupt Mask Register
            ("QISR"     , ctypes.c_uint32),              # (Tc Offset: 0xD4) QDEC Interrupt Status Register
            ("FMR"      , ctypes.c_uint32),              # (Tc Offset: 0xD8) Fault Mode Register
            ("Reserved1", ctypes.c_uint32 * 2),          # 
            ("WPMR"     , ctypes.c_uint32),              # (Tc Offset: 0xE4) Write Protect Mode Register
        ]

class SAM3xaPdc:
    class Type(ctypes.Structure):
        _fields_ = [
            ("PERIPH_RPR" , ctypes.c_uint32), # (Pdc Offset: 0x0) Receive Pointer Register
            ("PERIPH_RCR" , ctypes.c_uint32), # (Pdc Offset: 0x4) Receive Counter Register
            ("PERIPH_TPR" , ctypes.c_uint32), # (Pdc Offset: 0x8) Transmit Pointer Register
            ("PERIPH_TCR" , ctypes.c_uint32), # (Pdc Offset: 0xC) Transmit Counter Register
            ("PERIPH_RNPR", ctypes.c_uint32), # (Pdc Offset: 0x10) Receive Next Pointer Register
            ("PERIPH_RNCR", ctypes.c_uint32), # (Pdc Offset: 0x14) Receive Next Counter Register
            ("PERIPH_TNPR", ctypes.c_uint32), # (Pdc Offset: 0x18) Transmit Next Pointer Register
            ("PERIPH_TNCR", ctypes.c_uint32), # (Pdc Offset: 0x1C) Transmit Next Counter Register
            ("PERIPH_PTCR", ctypes.c_uint32), # (Pdc Offset: 0x20) Transfer Control Register
            ("PERIPH_PTSR", ctypes.c_uint32), # (Pdc Offset: 0x24) Transfer Status Register
        ]

class SAM3xaUart:
    class Type(ctypes.Structure):
        _fields_ = [
            ("CR"       , ctypes.c_uint32),      # (Uart Offset: 0x0000) Control Register
            ("MR"       , ctypes.c_uint32),      # (Uart Offset: 0x0004) Mode Register
            ("IER"      , ctypes.c_uint32),      # (Uart Offset: 0x0008) Interrupt Enable Register
            ("IDR"      , ctypes.c_uint32),      # (Uart Offset: 0x000C) Interrupt Disable Register
            ("IMR"      , ctypes.c_uint32),      # (Uart Offset: 0x0010) Interrupt Mask Register
            ("SR"       , ctypes.c_uint32),      # (Uart Offset: 0x0014) Status Register
            ("RHR"      , ctypes.c_uint32),      # (Uart Offset: 0x0018) Receive Holding Register
            ("THR"      , ctypes.c_uint32),      # (Uart Offset: 0x001C) Transmit Holding Register
            ("BRGR"     , ctypes.c_uint32),      # (Uart Offset: 0x0020) Baud Rate Generator Register
            ("Reserved1", ctypes.c_uint32 * 55), # 
            ("RPR"      , ctypes.c_uint32),      # (Uart Offset: 0x100) Receive Pointer Register
            ("RCR"      , ctypes.c_uint32),      # (Uart Offset: 0x104) Receive Counter Register
            ("TPR"      , ctypes.c_uint32),      # (Uart Offset: 0x108) Transmit Pointer Register
            ("TCR"      , ctypes.c_uint32),      # (Uart Offset: 0x10C) Transmit Counter Register
            ("RNPR"     , ctypes.c_uint32),      # (Uart Offset: 0x110) Receive Next Pointer Register
            ("RNCR"     , ctypes.c_uint32),      # (Uart Offset: 0x114) Receive Next Counter Register
            ("TNPR"     , ctypes.c_uint32),      # (Uart Offset: 0x118) Transmit Next Pointer Register
            ("TNCR"     , ctypes.c_uint32),      # (Uart Offset: 0x11C) Transmit Next Counter Register
            ("PTCR"     , ctypes.c_uint32),      # (Uart Offset: 0x120) Transfer Control Register
            ("PTSR"     , ctypes.c_uint32),      # (Uart Offset: 0x124) Transfer Status Register
        ]

class SAM3xaRtc:
    class Type(ctypes.Structure):
        _fields_ = [
            ("CR"       , ctypes.c_uint32),      # (Rtc Offset: 0x00) Control Register
            ("MR"       , ctypes.c_uint32),      # (Rtc Offset: 0x04) Mode Register
            ("TIMR"     , ctypes.c_uint32),      # (Rtc Offset: 0x08) Time Register
            ("CALR"     , ctypes.c_uint32),      # (Rtc Offset: 0x0C) Calendar Register
            ("TIMALR"   , ctypes.c_uint32),      # (Rtc Offset: 0x10) Time Alarm Register
            ("CALALR"   , ctypes.c_uint32),      # (Rtc Offset: 0x14) Calendar Alarm Register
            ("SR"       , ctypes.c_uint32),      # (Rtc Offset: 0x18) Status Register
            ("SCCR"     , ctypes.c_uint32),      # (Rtc Offset: 0x1C) Status Clear Command Register
            ("IER"      , ctypes.c_uint32),      # (Rtc Offset: 0x20) Interrupt Enable Register
            ("IDR"      , ctypes.c_uint32),      # (Rtc Offset: 0x24) Interrupt Disable Register
            ("IMR"      , ctypes.c_uint32),      # (Rtc Offset: 0x28) Interrupt Mask Register
            ("VER"      , ctypes.c_uint32),      # (Rtc Offset: 0x2C) Valid Entry Register
            ("Reserved1", ctypes.c_uint32 * 45), # 
            ("WPMR"     , ctypes.c_uint32),      # (Rtc Offset: 0xE4) Write Protect Mode Register
        ]

class SAM3xaCan:
    class Type(ctypes.Structure):
        _fields_ = [
            ("MR"       , ctypes.c_uint32),      # (Can Offset: 0x0000) Mode Register
            ("IER"      , ctypes.c_uint32),      # (Can Offset: 0x0004) Interrupt Enable Register
            ("IDR"      , ctypes.c_uint32),      # (Can Offset: 0x0008) Interrupt Disable Register
            ("IMR"      , ctypes.c_uint32),      # (Can Offset: 0x000C) Interrupt Mask Register
            ("SR"       , ctypes.c_uint32),      # (Can Offset: 0x0010) Status Register
            ("BR"       , ctypes.c_uint32),      # (Can Offset: 0x0014) Baudrate Register
            ("TIM"      , ctypes.c_uint32),      # (Can Offset: 0x0018) Timer Register
            ("TIMESTP"  , ctypes.c_uint32),      # (Can Offset: 0x001C) Timestamp Register
            ("ECR"      , ctypes.c_uint32),      # (Can Offset: 0x0020) Error Counter Register
            ("TCR"      , ctypes.c_uint32),      # (Can Offset: 0x0024) Transfer Command Register
            ("ACR"      , ctypes.c_uint32),      # (Can Offset: 0x0028) Abort Command Register
            ("Reserved1", ctypes.c_uint32 * 46), # 
            ("WPMR"     , ctypes.c_uint32),      # (Can Offset: 0x00E4) Write Protect Mode Register
            ("WPSR"     , ctypes.c_uint32),      # (Can Offset: 0x00E8) Write Protect Status Register
            ("Reserved2", ctypes.c_uint32 * 69), # 
            ("MB"       , CanMb * CANMB_NUMBER), # (Can Offset: 0x200) MB = 0 .. 7
        ]

class SAM3xaDacc:
    class Type(ctypes.Structure):
        _fields_ = [
            ("CR"       , ctypes.c_uint32),      # (Dacc Offset: 0x00) Control Register
            ("MR"       , ctypes.c_uint32),      # (Dacc Offset: 0x04) Mode Register
            ("Reserved1", ctypes.c_uint32 * 2),  # 
            ("CHER"     , ctypes.c_uint32),      # (Dacc Offset: 0x10) Channel Enable Register
            ("CHDR"     , ctypes.c_uint32),      # (Dacc Offset: 0x14) Channel Disable Register
            ("CHSR"     , ctypes.c_uint32),      # (Dacc Offset: 0x18) Channel Status Register
            ("Reserved2", ctypes.c_uint32),      # 
            ("CDR"      , ctypes.c_uint32),      # (Dacc Offset: 0x20) Conversion Data Register
            ("IER"      , ctypes.c_uint32),      # (Dacc Offset: 0x24) Interrupt Enable Register
            ("IDR"      , ctypes.c_uint32),      # (Dacc Offset: 0x28) Interrupt Disable Register
            ("IMR"      , ctypes.c_uint32),      # (Dacc Offset: 0x2C) Interrupt Mask Register
            ("ISR"      , ctypes.c_uint32),      # (Dacc Offset: 0x30) Interrupt Status Register
            ("Reserved3", ctypes.c_uint32 * 24), # 
            ("ACR"      , ctypes.c_uint32),      # (Dacc Offset: 0x94) Analog Current Register
            ("Reserved4", ctypes.c_uint32 * 19), # 
            ("WPMR"     , ctypes.c_uint32),      # (Dacc Offset: 0xE4) Write Protect Mode register
            ("WPSR"     , ctypes.c_uint32),      # (Dacc Offset: 0xE8) Write Protect Status register
            ("Reserved5", ctypes.c_uint32 * 7),  # 
            ("TPR"      , ctypes.c_uint32),      # (Dacc Offset: 0x108) Transmit Pointer Register
            ("TCR"      , ctypes.c_uint32),      # (Dacc Offset: 0x10C) Transmit Counter Register
            ("Reserved6", ctypes.c_uint32 * 2),  # 
            ("TNPR"     , ctypes.c_uint32),      # (Dacc Offset: 0x118) Transmit Next Pointer Register
            ("TNCR"     , ctypes.c_uint32),      # (Dacc Offset: 0x11C) Transmit Next Counter Register
            ("PTCR"     , ctypes.c_uint32),      # (Dacc Offset: 0x120) Transfer Control Register
            ("PTSR"     , ctypes.c_uint32),      # (Dacc Offset: 0x124) Transfer Status Register
        ]

class SAM3xaChipid:
    class Type(ctypes.Structure):
        _fields_ = [
            ("CIDR", ctypes.c_uint32), # (Chipid Offset: 0x0) Chip ID Register
            ("EXID", ctypes.c_uint32), # (Chipid Offset: 0x4) Chip ID Extension Register
        ]

class SAM3xaRstc:
    class Type(ctypes.Structure):
        _fields_ = [
            ("CR", ctypes.c_uint32), # (Rstc Offset: 0x00) Control Register
            ("SR", ctypes.c_uint32), # (Rstc Offset: 0x04) Status Register
            ("MR", ctypes.c_uint32), # (Rstc Offset: 0x08) Mode Register
        ]

class SAM3xaWdt:
    class Type(ctypes.Structure):
        _fields_ = [
            ("CR", ctypes.c_uint32), # (Wdt Offset: 0x00) Control Register
            ("MR", ctypes.c_uint32), # (Wdt Offset: 0x04) Mode Register
            ("SR", ctypes.c_uint32), # (Wdt Offset: 0x08) Status Register
        ]

class SAM3xaUsart:
    class Type(ctypes.Structure):
        _fields_ = [
            ("US_CR"    , ctypes.c_uint32),      # (Usart Offset: 0x0000) Control Register
            ("US_MR"    , ctypes.c_uint32),      # (Usart Offset: 0x0004) Mode Register
            ("US_IER"   , ctypes.c_uint32),      # (Usart Offset: 0x0008) Interrupt Enable Register
            ("US_IDR"   , ctypes.c_uint32),      # (Usart Offset: 0x000C) Interrupt Disable Register
            ("US_IMR"   , ctypes.c_uint32),      # (Usart Offset: 0x0010) Interrupt Mask Register
            ("US_CSR"   , ctypes.c_uint32),      # (Usart Offset: 0x0014) Channel Status Register
            ("US_RHR"   , ctypes.c_uint32),      # (Usart Offset: 0x0018) Receiver Holding Register
            ("US_THR"   , ctypes.c_uint32),      # (Usart Offset: 0x001C) Transmitter Holding Register
            ("US_BRGR"  , ctypes.c_uint32),      # (Usart Offset: 0x0020) Baud Rate Generator Register
            ("US_RTOR"  , ctypes.c_uint32),      # (Usart Offset: 0x0024) Receiver Time-out Register
            ("US_TTGR"  , ctypes.c_uint32),      # (Usart Offset: 0x0028) Transmitter Timeguard Register
            ("Reserved1", ctypes.c_uint32 * 5),  # 
            ("US_FIDI"  , ctypes.c_uint32),      # (Usart Offset: 0x0040) FI DI Ratio Register
            ("US_NER"   , ctypes.c_uint32),      # (Usart Offset: 0x0044) Number of Errors Register
            ("Reserved2", ctypes.c_uint32),      # 
            ("US_IF"    , ctypes.c_uint32),      # (Usart Offset: 0x004C) IrDA Filter Register
            ("US_MAN"   , ctypes.c_uint32),      # (Usart Offset: 0x0050) Manchester Encoder Decoder Register
            ("US_LINMR" , ctypes.c_uint32),      # (Usart Offset: 0x0054) LIN Mode Register
            ("US_LINIR" , ctypes.c_uint32),      # (Usart Offset: 0x0058) LIN Identifier Register
            ("Reserved3", ctypes.c_uint32 * 34), # 
            ("US_WPMR"  , ctypes.c_uint32),      # (Usart Offset: 0xE4) Write Protect Mode Register
            ("US_WPSR"  , ctypes.c_uint32),      # (Usart Offset: 0xE8) Write Protect Status Register
            ("Reserved4", ctypes.c_uint32 * 5),  # 
            ("US_RPR"   , ctypes.c_uint32),      # (Usart Offset: 0x100) Receive Pointer Register
            ("US_RCR"   , ctypes.c_uint32),      # (Usart Offset: 0x104) Receive Counter Register
            ("US_TPR"   , ctypes.c_uint32),      # (Usart Offset: 0x108) Transmit Pointer Register
            ("US_TCR"   , ctypes.c_uint32),      # (Usart Offset: 0x10C) Transmit Counter Register
            ("US_RNPR"  , ctypes.c_uint32),      # (Usart Offset: 0x110) Receive Next Pointer Register
            ("US_RNCR"  , ctypes.c_uint32),      # (Usart Offset: 0x114) Receive Next Counter Register
            ("US_TNPR"  , ctypes.c_uint32),      # (Usart Offset: 0x118) Transmit Next Pointer Register
            ("US_TNCR"  , ctypes.c_uint32),      # (Usart Offset: 0x11C) Transmit Next Counter Register
            ("US_PTCR"  , ctypes.c_uint32),      # (Usart Offset: 0x120) Transfer Control Register
            ("US_PTSR"  , ctypes.c_uint32),      # (Usart Offset: 0x124) Transfer Status Register
        ]

