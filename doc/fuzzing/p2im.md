# Approximate MCU Emulation for Fuzzing

**P2IM: Scalable and Hardware-independent Firmware Testing via Automatic Peripheral Interface Modeling**

## Emulator types

- Emulate peripheral hardware by software components in the emulator - *Incomplete support for peripherals, significant manual efforts*
- Use real peripheral hardware to handle peripheral access in the emulator - *Rely on real hardware, slow, unscalable*
- Replace peripheral-dependent firmware code with software stubs that have the same functionalities - *Unable to test peripheral-dependent code, significant manual efforts*

## Methods

The interface of peripheral include register and interrupt, the paper mentioned that peripheral is complex but interface not. So they choose to find the common place among all peripheral.

For **register**, they divide registers into four categories `CR`,`DR`,`SR`,`C&SR`. Each category are recognized by the access-pattern. For example ,a read-modify-write access pattern are usually be observed on `CR`. After finish the category, we use corresponding hander to handle the read/write.

For **interrupt**, they just send interrupts round-robin and do not consider the trigger condition in real world.

## Evaluation

The accuracy of register identification and categorization 76% ~ 92%.

The unit test result is that 79% of the tests passed while 21% failed. 

For a test to qualify as pass, the firmware under test needs to properly boot, configure the peripherals, and conduct the functionality, without any crash, stall, or operation skipping.

## Discussion

- Why approximate emulation works? Is the MCU are still run in correct workflow with high probability?

  - Note most firmware are build base on some reliable library, the interrupt handler in these lib usually check if the interrupt be sent correctly.
  - Most register can just been seen memory, we even not need to do any categories.

- How to detect error in this paper?

  - **stall**: stay in infinite loop
  - **crash**: access memory with wrong perm. 
  - For a accurate simulation, stall are not usually happened, stall usually used in handle peripheral error.

- Where is bound of peripheral emulation? Which part of peripheral are not needed to emulate?

  ![](../img/MCU.png)







