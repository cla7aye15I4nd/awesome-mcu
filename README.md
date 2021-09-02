# awesome-mcu

## Tools

- [OpenOCD](https://openocd.org/)  provides on-chip programming and debugging support, include breakpoints/watchpoints and flash chip drivers.
- [renode](https://renode.io/) can simulate physical hardware systems - including both the CPU, peripherals, sensors, environment and wired or wireless medium between nodes.
- [qemu](https://github.com/qemu/qemu) supports the simulation of some common devices in the `hw` module for guest linux.
- [qemu-arm-xpack](https://github.com/xpack-dev-tools/qemu-arm-xpack)  is a binary distribution of qemu arm, better support for bare metal Cortex-M based boards.
- [Keil](https://www2.keil.com/mdk5) is a software development solution for Arm®-based mcu, which can develop, debug and simulate the mcu.
- [rainbow](https://github.com/Ledger-Donjon/rainbow) provide interesting demo of unicorn-based mcu emulator framework and some side-channel attack examples.
- [Ghidra](https://github.com/NationalSecurityAgency/ghidra) support analysis intel hex format.
  - [Reverse Engineering Firmware with Ghidra](https://www.youtube.com/watch?v=4urMITJKQQs)
  - [Learn the basics of GHIDRA and analyze the firmware](https://www.cutawaysecurity.com/learning-ghidra-basics-analyzing-firmware/)
- [ARM-X](https://github.com/therealsaumil/armx) is a firmware emulation framework.
  - Slide: [ARM-X: The ARM IoT Firmware Emulation Framework](https://cyberweek.ae/materials/2019/D4%20TRACK%201%20-%20Introducing%20ARM-X%20%E2%80%93%20The%20ARM%20IoT%20Firmware%20Emulation%20Framework%20-%20Saumil%20Shah.pdf)
  - Youtube: [Introducing ARM-X: The ARM IoT Firmware Emulation Framework - Saumil Shah](https://www.youtube.com/watch?v=NVl6uJiEaoI)

## Projects

- [ArduPilot](https://github.com/ArduPilot/ardupilot) is the most advanced, full-featured and reliable open source autopilot software available.
- [RIOT](https://github.com/RIOT-OS/RIOT)  is a real-time multi-threading operating system that supports a range of devices that are typically found in the IoT.
- [Contiki](https://github.com/contiki-os/contiki)  is an open source operating system that runs on tiny low-power microcontrollers.
- [Contiki-NG](https://github.com/contiki-ng/contiki-ng)  is an open-source, cross-platform operating system for Next-Generation IoT devices.
- [IronOS](https://github.com/Ralim/IronOS)  Open Source Soldering Iron firmware for Miniware and Pinecil.
- [rusEFI](https://github.com/rusefi/rusefi) GPL internal combustion engine control unit
- [EmuFlight](https://github.com/emuflight/EmuFlight) is flight controller software (firmware) used to fly multi-rotor craft.
- [BetaFlight](https://github.com/betaflight/betaflight) Open Source Flight Controller Firmware
- [FreeRTOS](https://github.com/FreeRTOS/FreeRTOS-Kernel) Real-time operating system for microcontrollers.
- [RaceFlight](https://github.com/rs2k/raceflight)  Race prepared version of the cleanflight flight-controller

## Papers

- [Frankenstein: Advanced Wireless Fuzzing to Exploit New Bluetooth Escalation Targets](https://www.usenix.org/conference/usenixsecurity20/presentation/ruge)
- [Jetset: Targeted Firmware Rehosting for Embedded Systems](https://www.usenix.org/system/files/sec21fall-johnson.pdf)
- [DICE: Automatic Emulation of DMA Input Channels for Dynamic Firmware Analysis](https://arxiv.org/pdf/2007.01502.pdf)
- [PASAN: Detecting Peripheral Access Concurrency Bugs within Bare-Metal Embedded Applications](https://www.usenix.org/conference/usenixsecurity21/presentation/kim)

## Slides

- [Backdooring hardware devices by injecting malicious payloads on microcontrollers](https://media.defcon.org/DEF%20CON%2027/DEF%20CON%2027%20presentations/DEFCON-27-Sheila-A-Berta-Backdooring-hardware-devices-by-injecting-malicious-payloads-on-Microcontrollers.pdf)
- [Firmware Slap - Automating discovery of exploitable vulnerabilities in firmware](https://media.defcon.org/DEF%20CON%2027/DEF%20CON%2027%20presentations/DEFCON-27-Christopher-Roberts-Firmware-Slap.pdf)
- [The Art & Craft of writing ARM shellcode](https://cyberweek.ae/materials/2020/D1T3%20-%20Writing%20Bare-Metal%20ARM%20Shellcode.pdf)
- [Beyond Root Custom Firmware For Embedded Mobile Chip sets](https://media.defcon.org/DEF%20CON%2028/DEF%20CON%20Safe%20Mode%20presentations/DEF%20CON%20Safe%20Mode%20-%20Christopher%20Wade%20-%20Beyond%20Root%20Custom%20Firmware%20For%20Embedded%20Mobile%20Chipsets.pdf)
- [PicoDMA: DMA Attacks at Your Fingertips](http://i.blackhat.com/USA-19/Wednesday/us-19-Sandin-PicoDMA-DMA-Attacks-At-Your-Fingertips.pdf)
- [Broken Memory Allocators Led to Millions of Vulnerable IoT and Embedded Devices](http://i.blackhat.com/USA21/Wednesday-Handouts/us-21-Error-Badalloc-Broken-Memory-Allocators-Led-To-Millions-Of-Vulnerable-Iot-And-Embedded-Devices.pdf) - **FreeRTOS** malloc
- [Raiden Glitching Framework](http://i.blackhat.com/asia-20/Friday/asia-20-Wypych-Raiden-Glitching-Framework.pdf)

