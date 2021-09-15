#ifndef __LCD_H
#define __LCD_H

#include "stm32f4xx_hal.h"

void lcd_send_cmd(I2C_HandleTypeDef* hi2c, char cmd);
void lcd_send_data(I2C_HandleTypeDef* hi2c, char raw);
void lcd_init(I2C_HandleTypeDef* hi2c);
void lcd_send_string(I2C_HandleTypeDef* hi2c, char *ptr);
void lcd_put_cur(I2C_HandleTypeDef* hi2c, int row, int col);
void lcd_clear(I2C_HandleTypeDef* hi2c);

#endif
