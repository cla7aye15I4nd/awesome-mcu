//! Demonstrate the use of a blocking `Delay` using the SYST (sysclock) timer.

#![allow(clippy::empty_loop)]
#![no_main]
#![no_std]

// Halt on panic
use panic_halt as _; // panic handler

use core::cell::RefCell;
use cortex_m::{interrupt::Mutex};
use cortex_m_rt::entry;
use stm32f4xx_hal as hal;

use crate::hal::{pac, prelude::*, stm32, interrupt, serial};
use hal::gpio::{gpioa, Alternate};

type STM32F4Serial 
    = serial::Serial<
        stm32::USART2,
        (
            gpioa::PA2<Alternate<hal::gpio::AF7>>,
            gpioa::PA3<Alternate<hal::gpio::AF7>>,
        ),
    >;

static HUSART2: Mutex<RefCell<Option<STM32F4Serial>>> = Mutex::new(RefCell::new(None));

#[entry]
fn main() -> ! {
    if let (Some(dp), Some(cp)) = (
        pac::Peripherals::take(),
        cortex_m::peripheral::Peripherals::take(),
    ) {
        let gpioa = dp.GPIOA.split();
        let mut led = gpioa.pa5.into_push_pull_output();
        
        let rcc = dp.RCC.constrain();
        let clocks = rcc.cfgr.sysclk(48.mhz()).freeze();

        let tx_pin = gpioa.pa2.into_alternate_af7();
        let rx_pin = gpioa.pa3.into_alternate_af7();
        
        dp.USART2.cr1.modify(|_,w|{
            w.rxneie().set_bit()
        });
        
        let mut ser = serial::Serial::new(
            dp.USART2,
            (tx_pin, rx_pin),
            serial::config::Config::default().baudrate(9600.bps()),
            clocks,
        )
        .unwrap();

        ser.listen(serial::Event::Rxne); 
        cortex_m::interrupt::free(|cs| *HUSART2.borrow(cs).borrow_mut() = Some(ser));

        unsafe {
            stm32::NVIC::unmask(hal::interrupt::USART2);            
        }

        let mut delay = hal::delay::Delay::new(cp.SYST, clocks);

        loop {
            delay.delay_ms(500_u32);
            led.set_high().unwrap();
            delay.delay_ms(500_u32);
            led.set_low().unwrap();
        }
    }

    loop {}
}

#[interrupt]
fn USART2() {
    static mut SER: Option<STM32F4Serial> = None;
    
    let ser = SER.get_or_insert_with(|| {
        cortex_m::interrupt::free(|cs| {        
            HUSART2.borrow(cs).replace(None).unwrap()            
        })
    });
        
    if ser.is_rxne() {
        let data = ser.read().unwrap();
        ser.write(data).unwrap();
    }    
}
