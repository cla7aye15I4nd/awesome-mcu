import pygame
import threading

from lcd1602 import *

screen = make_screen([' ' * 16] * 2)

def is_activate(i, j):    
    return screen[i][j] == '#'

def main():
    FPS = 60
    runable = True

    size = 10
    offset = 12
    
    row_n, col_n = 8, 5
    row_c, col_c = 2, 16
    
    margin, interval = size * 4, size // 2

    width  = margin * 2 + size * (col_c * col_n) + interval * (col_c - 1)
    height = margin * 2 + size * (row_c * row_n) + interval * (row_c - 1)

    win = pygame.display.set_mode((width, height))

    clock = pygame.time.Clock()

    pygame.display.set_caption("LCD 1602A")

    while runable:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runable = False
        
        pygame.draw.rect(win, "#c9f6cd", ((offset, offset), (width - offset*2, height - offset*2)), border_radius=offset)
        for i in range(row_c * row_n):
            for j in range(col_c * col_n):
                x = margin + size * j + interval * (j // col_n)
                y = margin + size * i + interval * (i // row_n)

                color = "#446644" if is_activate(i, j) else "#bbeebb"
                pygame.draw.rect(win, color, ((x, y), (size-1, size-1)))

        pygame.display.update()

    print('LCD quit')
    pygame.quit()

if __name__ == '__main__':
    threading.Thread(target=main).start()
    
    while True:
        info = input('Screen Info: ').ljust(32, ' ')
        screen = make_screen([info[0: 16], info[16: 32]])