TARGET = led-rust

all:
	cargo build --release	

flash:
	cargo objcopy --release -- -O ihex $(TARGET).hex
	st-flash --format=ihex write $(TARGET).hex

clean:
	cargo clean