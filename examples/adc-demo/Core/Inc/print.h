#ifndef __PRINT_H
#define __PRINT_H

#include <stdio.h>

#define print(...) do {                                     \
uint8_t buff[0x100];                                        \
    int size = sprintf((char*) buff, __VA_ARGS__);          \
    HAL_UART_Transmit(&huart2, buff, size, HAL_MAX_DELAY);  \
} while(0)

#endif //__PRINT_H
