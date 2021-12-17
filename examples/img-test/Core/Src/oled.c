#include "oled.h"
#include "main.h"
#include "font.h"
#include "spi.h"


void oled_write_byte(uint8_t byte, uint8_t flag) {
  if (flag)
    OLED_DC_SET();
  else
    OLED_DC_RESET();

  OLED_CS_RESET();

  HAL_SPI_Transmit(&hspi1, &byte, 1, HAL_MAX_DELAY);
  OLED_CS_SET();
  OLED_DC_SET();
}

void oled_set_position(uint32_t x, uint32_t y) {

  oled_write_byte(0xb0 | y, OLED_CMD);
  oled_write_byte(((x & 0xf0) >> 4) | 0x10, OLED_CMD);
  oled_write_byte((x & 0x0f), OLED_CMD);
}

void oled_clear(void) {
  for (int i = 0; i < 8; i++) {
    oled_set_position(0, i);
    for (int j = 0; j < 128; j++)
      oled_write_byte(0, OLED_DATA);
  }
}

void oled_putchar(uint32_t x, uint32_t y, char c) {
  c = c - ' ';
  
  oled_set_position(x, y);
  for (int i = 0; i < 8; i++)
    oled_write_byte(oled_charmap[c * 16 + i], OLED_DATA);

  oled_set_position(x, y + 1);
  for (int i = 0; i < 8; i++)
    oled_write_byte(oled_charmap[c * 16 + i + 8], OLED_DATA);
}

void oled_print(uint32_t x, uint32_t y, char *ptr) {
  while (*ptr) {
    if (x + 8 > MAX_COL) {
      x = 0;
      y += 2;
    }
    oled_putchar(x, y, *ptr);
    x += 8;
    ptr++;
  }

  while (x + 8 <= MAX_COL) {
    oled_putchar(x, y, ' ');
    x += 8;
  }
}

void oled_init(void) {

  OLED_RST_RESET();
  HAL_Delay(200);

  OLED_RST_SET();
  oled_write_byte(0xAE, OLED_CMD);
  oled_write_byte(0xD5, OLED_CMD);
  oled_write_byte(0x80, OLED_CMD);
  oled_write_byte(0x40, OLED_CMD);
  oled_write_byte(0x81, OLED_CMD);
  oled_write_byte(0xCF, OLED_CMD);
  oled_write_byte(0xA1, OLED_CMD);
  oled_write_byte(0xC8, OLED_CMD);
  oled_write_byte(0xA6, OLED_CMD);
  oled_write_byte(0xA8, OLED_CMD);
  oled_write_byte(0x3f, OLED_CMD);
  oled_write_byte(0xD3, OLED_CMD);
  oled_write_byte(0x00, OLED_CMD);
  oled_write_byte(0xd5, OLED_CMD);
  oled_write_byte(0x80, OLED_CMD);
  oled_write_byte(0xD9, OLED_CMD);
  oled_write_byte(0xF1, OLED_CMD);
  oled_write_byte(0xDA, OLED_CMD);
  oled_write_byte(0x12, OLED_CMD);
  oled_write_byte(0xDB, OLED_CMD);
  oled_write_byte(0x40, OLED_CMD);
  oled_write_byte(0x20, OLED_CMD);
  oled_write_byte(0x02, OLED_CMD);
  oled_write_byte(0x8D, OLED_CMD);
  oled_write_byte(0x14, OLED_CMD);
  oled_write_byte(0xA4, OLED_CMD);
  oled_write_byte(0xA6, OLED_CMD);
  oled_write_byte(0xAF, OLED_CMD);
  oled_write_byte(0xAF, OLED_CMD);

  oled_clear();
}
