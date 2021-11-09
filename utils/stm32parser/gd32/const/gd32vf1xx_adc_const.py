from enum import IntEnum


class STAT(IntEnum):
    STRC = 0x1 << 4   # Start flag of regular channel group
    STIC = 0x1 << 3   # Start flag of inserted channel group
    EOIC = 0x1 << 2   # End of inserted group conversion flag
    EOC  = 0x1 << 1   # End of group conversion flag
    WDE  = 0x1 << 0   # Analog watchdog event flag

class CTL0(IntEnum):
    RWDEN   = 0x1 << 23   # Regular channel analog watchdog enable
    IWDEN   = 0x1 << 22   # Inserted channel analog watchdog enable
    SYNCM   = 0xf << 16   # sync mode selection
    DISNUM  = 0x7 << 13   # Number of conversions in discontinuous mode
    DISIC   = 0x1 << 12   # Discontinuous mode on inserted channels
    DISRC   = 0x1 << 11   # Discontinuous mode on regular channels
    ICA     = 0x1 << 10   # Inserted channel group convert automatically
    WDSC    = 0x1 << 9    # When in scan mode, analog watchdog is effective on a single channel
    SM      = 0x1 << 8    # Scan mode
    EOICIE  = 0x1 << 7    # Interrupt enable for EOIC
    WDEIE   = 0x1 << 6    # Interrupt enable for WDE
    EOCIE   = 0x1 << 5    # Interrupt enable for EOC
    WDCHSEL = 0x1f << 0   # Analog watchdog channel select

class CTL1(IntEnum):
    TSVREN = 0x1 << 23   # Channel 16 and 17 enable of ADC0
    SWRCST = 0x1 << 22   # Start on regular channel
    SWICST = 0x1 << 21   # Start on inserted channel
    ETERC  = 0x1 << 20   # External trigger enable for regular channel
    ETSRC  = 0x7 << 17   # External trigger select for regular channel
    ETEIC  = 0x1 << 15   # External trigger select for inserted channel
    ETSIC  = 0x7 << 12   # External trigger select for inserted channel
    DAL    = 0x1 << 11   # Data alignment
    DMA    = 0x1 << 8    # DMA request enable
    RSTCLB = 0x1 << 3    # Reset calibration
    CLB    = 0x1 << 2    # ADC calibration
    CTN    = 0x1 << 1    # Continuous mode
    ADCON  = 0x1 << 0    # ADC on

class SAMPT0(IntEnum):
    SPT10 = 0x7 << 0    # Channel 10 sample time selection
    SPT11 = 0x7 << 3    # Channel 11 sample time selection
    SPT12 = 0x7 << 6    # Channel 12 sample time selection
    SPT13 = 0x7 << 9    # Channel 13 sample time selection
    SPT14 = 0x7 << 12   # Channel 14 sample time selection
    SPT15 = 0x7 << 15   # Channel 15 sample time selection
    SPT16 = 0x7 << 18   # Channel 16 sample time selection
    SPT17 = 0x7 << 21   # Channel 17 sample time selection

class SAMPT1(IntEnum):
    SPT0 = 0x7 << 0    # Channel 0 sample time selection
    SPT1 = 0x7 << 3    # Channel 1 sample time selection
    SPT2 = 0x7 << 6    # Channel 2 sample time selection
    SPT3 = 0x7 << 9    # Channel 3 sample time selection
    SPT4 = 0x7 << 12   # Channel 4 sample time selection
    SPT5 = 0x7 << 15   # Channel 5 sample time selection
    SPT6 = 0x7 << 18   # Channel 6 sample time selection
    SPT7 = 0x7 << 21   # Channel 7 sample time selection
    SPT8 = 0x7 << 24   # Channel 8 sample time selection
    SPT9 = 0x7 << 27   # Channel 9 sample time selection

class IOFF0(IntEnum):
    IOFF = 0xfff << 0   # Data offset for inserted channel 0

class IOFF1(IntEnum):
    IOFF = 0xfff << 0   # Data offset for inserted channel 1

class IOFF2(IntEnum):
    IOFF = 0xfff << 0   # Data offset for inserted channel 2

class IOFF3(IntEnum):
    IOFF = 0xfff << 0   # Data offset for inserted channel 3

class WDHT(IntEnum):
    WDHT = 0xfff << 0   # Analog watchdog higher threshold

class WDLT(IntEnum):
    WDLT = 0xfff << 0   # Analog watchdog lower threshold

class RSQ0(IntEnum):
    RL    = 0xf << 20    # Regular channel group length
    RSQ15 = 0x1f << 15   # 16th conversion in regular sequence
    RSQ14 = 0x1f << 10   # 15th conversion in regular sequence
    RSQ13 = 0x1f << 5    # 14th conversion in regular sequence
    RSQ12 = 0x1f << 0    # 13th conversion in regular sequence

class RSQ1(IntEnum):
    RSQ11 = 0x1f << 25   # 12th conversion in regular sequence
    RSQ10 = 0x1f << 20   # 11th conversion in regular sequence
    RSQ9  = 0x1f << 15   # 10th conversion in regular sequence
    RSQ8  = 0x1f << 10   # 9th conversion in regular sequence
    RSQ7  = 0x1f << 5    # 8th conversion in regular sequence
    RSQ6  = 0x1f << 0    # 7th conversion in regular sequence

class RSQ2(IntEnum):
    RSQ5 = 0x1f << 25   # 6th conversion in regular sequence
    RSQ4 = 0x1f << 20   # 5th conversion in regular sequence
    RSQ3 = 0x1f << 15   # 4th conversion in regular sequence
    RSQ2 = 0x1f << 10   # 3rd conversion in regular sequence
    RSQ1 = 0x1f << 5    # 2nd conversion in regular sequence
    RSQ0 = 0x1f << 0    # 1st conversion in regular sequence

class ISQ(IntEnum):
    IL   = 0x3 << 20    # Inserted channel group length
    ISQ3 = 0x1f << 15   # 4th conversion in inserted sequence
    ISQ2 = 0x1f << 10   # 3rd conversion in inserted sequence
    ISQ1 = 0x1f << 5    # 2nd conversion in inserted sequence
    ISQ0 = 0x1f << 0    # 1st conversion in inserted sequence

class IDATA0(IntEnum):
    IDATAn = 0xffff << 0   # Inserted number n conversion data

class IDATA1(IntEnum):
    IDATAn = 0xffff << 0   # Inserted number n conversion data

class IDATA2(IntEnum):
    IDATAn = 0xffff << 0   # Inserted number n conversion data

class IDATA3(IntEnum):
    IDATAn = 0xffff << 0   # Inserted number n conversion data

class RDATA(IntEnum):
    ADC1RDTR = 0xffff << 16   # ADC regular channel data
    RDATA    = 0xffff << 0    # Regular channel data

class OVSAMPCTL(IntEnum):
    DRES  = 0x3 << 12   # ADC resolution
    TOVS  = 0x1 << 9    # Triggered Oversampling
    OVSS  = 0xf << 5    # Oversampling shift
    OVSR  = 0x7 << 2    # Oversampling ratio
    OVSEN = 0x1 << 0    # Oversampler Enable

