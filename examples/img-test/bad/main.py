import os
import ffmpy
import shutil

from PIL import Image

TMP_DIR = 'tmp'
width, height = 86, 64

def create_workspace():
    if os.path.exists(TMP_DIR):
        shutil.rmtree(TMP_DIR)
    os.mkdir(TMP_DIR)

def split_video(video_dir):  
    gif_dir = os.path.join(TMP_DIR, 'bad.gif')

    ffmpy.FFmpeg(
        inputs  = {video_dir : None},
        outputs = {gif_dir   : None}
    ).run()

    im = Image.open(gif_dir)
    image_id = 0
    screen = [[0 for _ in range(width)] for _ in range(height // 8)]
    filesize = 0

    with open('badapple.h', 'w') as f:
        f.write('uint8_t video[] = {\n')
        while True:
            try:
                frame = im.tell()
                png_dir = os.path.join(TMP_DIR, f'bad{image_id}.png')

                image_id += 1 
                im.save(png_dir)
                im.seek(frame + 1)
                
                img = compress_image(png_dir)
                diff = []
                f.write('    0xff, ')
                for i in range(height // 8):
                    for j in range(width):
                        if screen[i][j] != img[i][j]:
                            screen[i][j] = img[i][j]
                            diff.append((i, j, img[i][j]))   
                            f.write(f'{i}, {j}, {img[i][j]}, ')

                f.write('\n')
                filesize += len(diff) * 2 + 1
                
            except EOFError:
                break
        
        f.write('};')
    print(f'{filesize / 1024.} KB')

def compress_image(png_dir):
    png = Image.open(png_dir).resize((width, height), Image.ANTIALIAS)

    img = [[0 for _ in range(width)] for _ in range(height // 8)]
    for i in range(height):
        for j in range(width):
            pixel = png.getpixel((j, i))
            if pixel > 127:
                img[i // 8][j] |= 1 << (i % 8)

    return img

def transfer(video_dir):
    create_workspace()
    split_video(video_dir)

if __name__ == '__main__':
    transfer('video/bad.mp4')