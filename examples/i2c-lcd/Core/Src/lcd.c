#include "lcd.h"

#define LCD_SLAVE_ADDR (0x3f << 1)
#define ASSERT(x) if ((x) != HAL_OK) for(;;);

void lcd_send_cmd(I2C_HandleTypeDef* hi2c, char cmd) 
{
    uint8_t data[4];

    char upper = (cmd << 0) & 0xf0;
    char lower = (cmd << 4) & 0xf0;

    data[0] = upper | 0x0c;
    data[1] = upper | 0x08;
    data[2] = lower | 0x0c;
    data[3] = lower | 0x08;

    ASSERT(HAL_I2C_Master_Transmit(hi2c, LCD_SLAVE_ADDR, data, 4, 100));
    HAL_Delay(1);
}

void lcd_send_data(I2C_HandleTypeDef* hi2c, char raw) 
{
    uint8_t data[4];

    char upper = (raw << 0) & 0xf0;
    char lower = (raw << 4) & 0xf0;

    data[0] = upper | 0x0d;
    data[1] = upper | 0x09;
    data[2] = lower | 0x0d;
    data[3] = lower | 0x09;

    ASSERT(HAL_I2C_Master_Transmit(hi2c, LCD_SLAVE_ADDR, data, 4, 100));
    HAL_Delay(1);
}

void lcd_init(I2C_HandleTypeDef* hi2c)
{
    HAL_Delay(50);
    lcd_send_cmd(hi2c, 0x30);
    HAL_Delay(5);
    lcd_send_cmd(hi2c, 0x30);
    HAL_Delay(1);
    lcd_send_cmd(hi2c, 0x30);
    HAL_Delay(10);
    lcd_send_cmd(hi2c, 0x20);
    HAL_Delay(10);

    lcd_send_cmd(hi2c, 0x28);
    HAL_Delay(1);
    lcd_send_cmd(hi2c, 0x08);
    HAL_Delay(1);
    lcd_send_cmd(hi2c, 0x01);
    HAL_Delay(1);
    lcd_send_cmd(hi2c, 0x06);
    HAL_Delay(1);
    lcd_send_cmd(hi2c, 0x0e);
    HAL_Delay(1);
}

void lcd_send_string(I2C_HandleTypeDef* hi2c, char *ptr)
{
	while (*ptr) 
        lcd_send_data (hi2c, *ptr++);
}

void lcd_put_cur(I2C_HandleTypeDef* hi2c, int row, int col){
	switch(row){
	case 0:
		col |= 0x80;
		break;
	case 1:
		col |= 0xC0;
		break;
	}

	lcd_send_cmd(hi2c, col);
}

void lcd_clear(I2C_HandleTypeDef* hi2c){
	lcd_send_cmd(hi2c, 0x01);
}