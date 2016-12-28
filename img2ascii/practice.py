import ctypes

from PIL import Image


ASCII_CHARS = [' ', '.', ',', ':', ';', '+', '*', '?', '%', '#', '@']
IMAGE_FILE = 'image2ascii.jpg'
CONVERTED_WIDTH = 60

img = Image.open(IMAGE_FILE)
img = img.convert('L')

width, height = img.size
converted_height = height / width * CONVERTED_WIDTH * 0.5
img = img.resize((CONVERTED_WIDTH, int(converted_height)))

ascii_ord = [ord(val) for val in ASCII_CHARS]
ascii_offset = len(ascii_ord) - 1
render = ctypes.create_string_buffer(CONVERTED_WIDTH)
for i, pix in enumerate(img.getdata()):
    if not (i + 1) % CONVERTED_WIDTH:
        print(render.value.decode())
    ascii_pos = pix / 255 * ascii_offset
    render[i % CONVERTED_WIDTH] = ascii_ord[int(ascii_pos)]
