import pygame
import threading

def get_raw_pattern(lo, up):
    with open('LCD1602A.txt') as f:
        lines = f.read().splitlines()[lo * 9 + 1: lo * 9 + 9]
        pattern = [line[up * 6 + 1: up * 6 + 6] for line in lines]

    return pattern

def get_char_pattern(ch):
    lo = (ord(ch) >> 0) & 0xf
    up = (ord(ch) >> 4) & 0xf
    return get_raw_pattern(lo, up)

def make_single_line(info):
    patterns = []
    for pack in info:
        if len(pack) == 1:
            patterns.append(get_char_pattern(pack))
        else:
            lo, up = pack
            patterns.append(get_raw_pattern(lo, up))

    screen = []    
    for row in range(8):
        line = ''
        for pattern in patterns:
            line += pattern[row]
        screen.append(line)
    
    return screen

def make_screen(infos):
    screen = []
    for info in infos:
        screen += make_single_line(info)
    return screen

def render(is_activate):
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
    screen = make_screen(['I guess you are ', 'watching me. ^_^'])

    ## print in term
    print('\n'.join(screen))

    ## render html
    from jinja2 import Template    
    with open('templates/lcd1602.html') as f:
        t = Template(f.read())

    with open('examples/lcd1602.html', 'w') as f:
        f.write(t.render(info = ''.join(screen)))

    screen = make_screen([' ' * 16] * 2)

    def is_activate(i, j):    
        return screen[i][j] == '#'

    threading.Thread(target=render, args=(is_activate, )).start()
    
    while True:
        info = input('Screen Info: ').ljust(32, ' ')
        screen = make_screen([info[0: 16], info[16: 32]])
