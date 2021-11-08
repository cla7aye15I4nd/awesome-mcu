all:
	cargo build --release

	
	riscv32-unknown-elf-objcopy -O binary target/riscv32imac-unknown-none-elf/release/gd32-blinky target/gd32-blinky.bin
	sudo dfu-util -a 0 -s 0x08000000:leave -D target/gd32-blinky.bin
clean:
	cargo clean
