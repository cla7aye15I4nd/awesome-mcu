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

if __name__ == '__main__':
    print('\n'.join(make_screen(['I guess you are ', 'watching me. ^_^'])))
