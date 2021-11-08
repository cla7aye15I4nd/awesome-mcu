TARGET = gd32-blinky

all:
	cargo build --release

	cargo objcopy --release -- target/$(TARGET).elf
	cargo objcopy --release -- -O ihex target/$(TARGET).bin
	cargo objcopy --release -- -O binary target/$(TARGET).bin

	sudo dfu-util -a 0 -s 0x8000000:leave -D target/$(TARGET).bin


clean:
	cargo clean
