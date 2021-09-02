# Peripheral Access Concurrency Bugs
The internal struct of peripheral is a finite state machine, an **operator** of peripheral such as read/write a byte from UART may need multi-access to peripheral, single access will change the state (transition on FSM) of the peripheral once. The access sequence of a specific operator be defined a **transaction**. Usually, two transactions cannot be execute concurrently. In other words, a transaction should be atomic operator. So the peripheral can be seen as a resource in multithreading, peripheral access from the different tasks may lead to an error access sequence of peripheral.

## Examples

**USART struct:**

```c
typedef struct
{
  uint32_t SR;         /*!< USART Status register,                   Address offset: 0x00 */
  uint32_t DR;         /*!< USART Data register,                     Address offset: 0x04 */
  uint32_t BRR;        /*!< USART Baud rate register,                Address offset: 0x08 */
  uint32_t CR1;        /*!< USART Control register 1,                Address offset: 0x0C */
  uint32_t CR2;        /*!< USART Control register 2,                Address offset: 0x10 */
  uint32_t CR3;        /*!< USART Control register 3,                Address offset: 0x14 */
  uint32_t GTPR;       /*!< USART Guard time and prescaler register, Address offset: 0x18 */
} USART_TypeDef;
```

**Write Byte Sequence**: Read `SR` (TXE), Write `DR`, Read `SR`(TC).

**Concurrency Bugs demo**: 

| Task A   | Task B                                |
| -------- | ------------------------------------- |
| Read SR  |                                       |
|          | Read SR                               |
| Write DR |                                       |
|          | Write DR (cover Task A content !!!!!) |
| Read TC  |                                       |
|          | Read TC                               |

After write the DR, the UART will move the DR to UART buffer (shift register), but in the process task B cover the DR, the data from Task A are lost. The byte of Task A is not delivered.

## Real World Case

**SPI Thread Safe**: [Implement thread safety for all SPI devices](https://github.com/RIOT-OS/RIOT/pull/2317)

    To communicate with any device, the bus needs to: 
    (i) select the slave device and 
    (ii) read/write data from/to the device.
    These two steps represent the internal state machines of this bus. Now imagine step (i) is done by thread A, which is going to send a command to the LIS3DH sensor. Simultaneously, thread B makes the SPI bus choose another slave device, i.e., the SD
    card controller. In this case, thread A’s command will then be redirected to another slave device due to the transaction corruption of SPI caused by concurrent bus accesses.

