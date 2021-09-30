#ifndef __UTILS_H
#define __UTILS_H

#include "stm32f4xx_hal.h"

void lcd_send_cmd(char cmd);
void lcd_send_data(char raw);
void lcd_init(void);
void lcd_send_string(char *ptr);
void lcd_put_cur(int row, int col);
void lcd_clear(void);

void print(const char *format, ...);

#endif
