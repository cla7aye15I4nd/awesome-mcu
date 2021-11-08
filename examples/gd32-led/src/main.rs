#![no_std]
#![no_main]

use panic_halt as _;

use riscv_rt::entry;
use gd32vf103xx_hal::{pac, prelude::*};

use embedded_hal::digital::v2::{OutputPin, StatefulOutputPin};
use gd32vf103xx_hal::gpio::gpioc::PC13;
use gd32vf103xx_hal::gpio::gpioa::{PA1, PA2};
use gd32vf103xx_hal::gpio::{Output, PushPull, Active};
use gd32vf103xx_hal::delay::McycleDelay;

/// Red LED
pub struct RED {
    port: PC13<Output<PushPull>>
}

impl RED {
    pub fn new<T: Active>(port: PC13<T>) -> Self {
        Self {
            port: port.into_push_pull_output()
        }
    }
}

/// Green LED
pub struct GREEN {
    port: PA1<Output<PushPull>>
}

impl GREEN {
    pub fn new<T: Active>(port: PA1<T>) -> Self {
        Self {
            port: port.into_push_pull_output()
        }
    }
}

/// Blue LED
pub struct BLUE {
    port: PA2<Output<PushPull>>
}

impl BLUE {
    pub fn new<T: Active>(port: PA2<T>) -> Self {
        Self {
            port: port.into_push_pull_output()
        }
    }
}

/// Returns RED, GREEN and BLUE LEDs.
pub fn rgb<X, Y, Z>(
    red: PC13<X>, green: PA1<Y>, blue: PA2<Z>
) -> (RED, GREEN, BLUE)
where X: Active, Y: Active, Z: Active
{
    let red: RED = RED::new(red);
    let green: GREEN = GREEN::new(green);
    let blue: BLUE = BLUE::new(blue);
    (red, green, blue)
}

/// Generic LED
pub trait Led {
    /// Turns the LED off
    fn off(&mut self);

    /// Turns the LED on
    fn on(&mut self);

    /// Checks the LED status
    fn is_on(&mut self) -> bool;
}

impl Led for RED {
    fn off(&mut self) {
        self.port.set_high().unwrap();
    }

    fn on(&mut self) {
        self.port.set_low().unwrap();
    }

    fn is_on(&mut self) -> bool {
        self.port.is_set_low().unwrap()
    }
}

impl Led for GREEN {
    fn off(&mut self) {
        self.port.set_high().unwrap();
    }

    fn on(&mut self) {
        self.port.set_low().unwrap();
    }

    fn is_on(&mut self) -> bool {
        self.port.is_set_low().unwrap()
    }
}

impl Led for BLUE {
    fn off(&mut self) {
        self.port.set_high().unwrap();
    }

    fn on(&mut self) {
        self.port.set_low().unwrap();
    }

    fn is_on(&mut self) -> bool {
        self.port.is_set_low().unwrap()
    }
}

#[entry]
fn main() -> ! {
    let dp = pac::Peripherals::take().unwrap();
    let mut rcu = dp.RCU.configure().freeze();

    let gpioa = dp.GPIOA.split(&mut rcu);
    let gpioc = dp.GPIOC.split(&mut rcu);

    let (mut red, mut green, mut blue) = rgb(gpioc.pc13, gpioa.pa1, gpioa.pa2);
    let leds: [&mut dyn Led; 3] = [&mut red, &mut green, &mut blue];

    let mut delay = McycleDelay::new(&rcu.clocks);

    let mut i = 0;

    loop {
        i = (i + 1) % 8;
        
        for bit in 0..3 {
            if (i >> bit) & 1 == 1 {
                leds[bit].on()
            } else {
                leds[bit].off()
            }
        }
        delay.delay_ms(500);
        
        for bit in 0..3 {
            if (i >> bit) & 1 == 0 {
                leds[bit].on()
            } else {
                leds[bit].off()
            }
        }
        delay.delay_ms(500);
    }
}
