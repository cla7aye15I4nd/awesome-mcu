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
    screen = [[0 for _ in range(width)] for _ in range(height)]
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
                
                skip = 1
                if image_id % skip == 0:
                    img = compress_image(png_dir)
                    size = 0
                    for w in range(image_id // skip % 2, width, 2):
                        ch = 0
                        for h in range(0, height, 8):
                            for hc in range(8):
                                if img[h + hc][w] != screen[h + hc][w]:
                                    ch |= 1 << (h // 8)
                        assert (ch < 256)
                        f.write(f'{ch}, ')
                        size += 1
                        for h in range(0, height, 8):
                            if (ch >> (h // 8)) & 1:
                                ret = 0
                                for hc in range(7, -1, -1):
                                    ret = ret * 2 + (img[h + hc][w])
                                    assert img[h + hc][w] < 2
                                assert ret < 256
                                f.write(f'{ret}, ')
                                size += 1
                        for h in range(height):
                            screen[h][w] = img[h][w]
                    f.write('\n')
                    filesize += size
                
            except EOFError:
                break
        
        f.write('};')
    print(f'{filesize / 1024.} KB')

def compress_image(png_dir):
    png = Image.open(png_dir).resize((width, height), Image.ANTIALIAS)

    img = [[0 for _ in range(width)] for _ in range(height)]
    for i in range(height):
        for j in range(width):
            pixel = png.getpixel((j, i))
            img[i][j] = 1 if pixel > 127 else 0

    return img

def transfer(video_dir):
    create_workspace()
    split_video(video_dir)

if __name__ == '__main__':
    transfer('video/bad.mp4')