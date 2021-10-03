import pygame
import threading
        
class LCD:
    @classmethod
    def get_raw_pattern(cls, lo, up):
        with open('LCD1602A.txt') as f:
            lines = f.read().splitlines()[lo * 9 + 1: lo * 9 + 9]
            pattern = [line[up * 6 + 1: up * 6 + 6] for line in lines]

        return pattern

    @classmethod
    def get_char_pattern(cls, ch):
        lo = (ord(ch) >> 0) & 0xf
        up = (ord(ch) >> 4) & 0xf
        return LCD1602.get_raw_pattern(lo, up)

    @classmethod
    def make_single_line(cls, info):
        patterns = []
        for pack in info:
            if len(pack) == 1:
                patterns.append(LCD1602.get_char_pattern(pack))
            else:
                lo, up = pack
                patterns.append(LCD1602.get_raw_pattern(lo, up))

        screen = []    
        for row in range(8):
            line = ''
            for pattern in patterns:
                line += pattern[row]
            screen.append(line)
        
        return screen

    @classmethod
    def make_screen(cls, infos):
        screen = []
        for info in infos:
            screen += LCD1602.make_single_line(info)
        return screen

class LCD1602(LCD):    
    def __init__(self) -> None:
        super().__init__()

        self.rows, self.cols = 2, 16
        self.cheight, self.cwidth = 8, 5        
        
        self.data = LCD.make_screen([' ' * self.cols] * self.rows)

    def is_activate(self, i, j):
        return self.data[i][j] == '#'

    def render(self):
        size = 10
        margin, interval = size * 4, size // 2

        width  = margin * 2 + size * (self.cols * self.cwidth) + interval * (self.cols - 1)
        height = margin * 2 + size * (self.rows * self.cheight) + interval * (self.rows - 1)

        runable = True
        clock = pygame.time.Clock()
        win = pygame.display.set_mode((width, height))

        pygame.display.set_caption("LCD 1602A")

        while runable:            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    runable = False
            
            clock.tick(60)
            pygame.draw.rect(win, "#c9f6cd", ((size, size), (width - size*2, height - size*2)), border_radius=size)
            for i in range(self.rows * self.cheight):
                for j in range(self.cols * self.cwidth):
                    x = margin + size * j + interval * (j // self.cwidth)
                    y = margin + size * i + interval * (i // self.cheight)

                    color = "#446644" if self.is_activate(i, j) else "#bbeebb"
                    pygame.draw.rect(win, color, ((x, y), (size-1, size-1)))

            pygame.display.update()            

        print('LCD quit')
        pygame.quit()

    def run(self):
        threading.Thread(target=self.render).start()

if __name__ == '__main__':
    screen = LCD1602.make_screen(['I guess you are ', 'watching me. ^_^'])

    ## print in term
    print('\n'.join(screen))

    ## render html
    from jinja2 import Template    
    with open('templates/lcd1602.html') as f:
        t = Template(f.read())

    with open('examples/lcd1602.html', 'w') as f:
        f.write(t.render(info = ''.join(screen)))

    lcd = LCD1602()
    lcd.run()
    
    while True:
        info = input('Screen Info: ').ljust(32, ' ')
        lcd.data = LCD1602.make_screen([info[0: 16], info[16: 32]])
