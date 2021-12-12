#ifndef __OLED_H
#define __OLED_H

#include "main.h"

#define MAX_COL	128

#define OLED_CMD  0
#define OLED_DATA 1

#define OLED_SCLK_SET()   HAL_GPIO_WritePin(OLED_SCLK_GPIO_Port, OLED_SCLK_Pin, GPIO_PIN_SET)
#define OLED_SCLK_RESET() HAL_GPIO_WritePin(OLED_SCLK_GPIO_Port, OLED_SCLK_Pin, GPIO_PIN_RESET)

#define OLED_SDIN_SET()   HAL_GPIO_WritePin(OLED_SDIN_GPIO_Port, OLED_SDIN_Pin, GPIO_PIN_SET)
#define OLED_SDIN_RESET() HAL_GPIO_WritePin(OLED_SDIN_GPIO_Port, OLED_SDIN_Pin, GPIO_PIN_RESET)

#define OLED_RST_SET()    HAL_GPIO_WritePin(OLED_RST_GPIO_Port, OLED_RST_Pin, GPIO_PIN_SET)
#define OLED_RST_RESET()  HAL_GPIO_WritePin(OLED_RST_GPIO_Port, OLED_RST_Pin, GPIO_PIN_RESET)

#define OLED_DC_SET()     HAL_GPIO_WritePin(OLED_DC_GPIO_Port, OLED_DC_Pin, GPIO_PIN_SET)
#define OLED_DC_RESET()   HAL_GPIO_WritePin(OLED_DC_GPIO_Port, OLED_DC_Pin, GPIO_PIN_RESET)

#define OLED_CS_SET()     HAL_GPIO_WritePin(OLED_CS_GPIO_Port, OLED_CS_Pin, GPIO_PIN_SET)
#define OLED_CS_RESET()   HAL_GPIO_WritePin(OLED_CS_GPIO_Port, OLED_CS_Pin, GPIO_PIN_RESET)

void oled_write_byte(uint8_t, uint8_t);
void oled_init(void);
void oled_clear(void);
void oled_putchar(uint32_t, uint32_t, char);
void oled_print(uint32_t, uint32_t, char *);	 
void oled_set_position(uint32_t, uint32_t);

#endif // __OLED_H
