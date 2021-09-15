#include "lcd.h"

extern I2C_HandleTypeDef hi2c1;

#define PIN_RS    (1 << 0)
#define PIN_EN    (1 << 2)
#define BACKLIGHT (1 << 3)

#define LCD_ADDR (0x3f << 1)
#define ASSERT(x) if ((x) != HAL_OK) for(;;);

void lcd_send_hook(uint8_t raw, uint8_t flags) 
{
    uint8_t data[4];

    char up = (raw << 0) & 0xf0;
    char lo = (raw << 4) & 0xf0;

    data[0] = up|flags|BACKLIGHT|PIN_EN;
    data[1] = up|flags|BACKLIGHT;
    data[2] = lo|flags|BACKLIGHT|PIN_EN;
    data[3] = lo|flags|BACKLIGHT;

    ASSERT(HAL_I2C_Master_Transmit(&hi2c1, LCD_ADDR, data, 4, HAL_MAX_DELAY));    
}

void lcd_send_cmd(char cmd) 
{
    lcd_send_hook(cmd, 0);
}

void lcd_send_byte(char byte) 
{
    lcd_send_hook(byte, PIN_RS);
}

void lcd_init(void)
{
    lcd_send_cmd(0b00110000);
    lcd_send_cmd(0b00000010);
    lcd_send_cmd(0b00001100);
    lcd_clear();
}

void lcd_send_string(char *ptr)
{
	while (*ptr) lcd_send_byte (*ptr++);
}

void lcd_put_cur(int row, int col){
	col |= row ? 0xC0: 0x80;
	lcd_send_cmd(col);
}

void lcd_clear(void)
{
	lcd_send_cmd(0x01);
    HAL_Delay(5);
}
