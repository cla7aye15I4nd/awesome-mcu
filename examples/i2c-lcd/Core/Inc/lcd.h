#ifndef __LCD_H
#define __LCD_H

#include "stm32f4xx_hal.h"

void lcd_send_cmd(char cmd);
void lcd_send_data(char raw);
void lcd_init(void);
void lcd_send_string(char *ptr);
void lcd_put_cur(int row, int col);
void lcd_clear(void);

#endif
