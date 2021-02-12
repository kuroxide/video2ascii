from PIL import Image
import os
import math
import time

PALETTE = "█▓▒░|:. "
inputsize = len(os.listdir("input"))

def convertUnicode():
    image = Image.open("input/" + str(i) + ".png").convert("L")
    width, height = image.size
    with open('output/output' + str(i) + '.txt', 'w') as f:
        lines = ''
        for y in range(height):
            for x in range(width):
                lines += PALETTE[int(image.getpixel((x, y))/32)]
            lines += '\n'
        f.write(lines)

t = time.perf_counter()

for i in range(1, inputsize):
    tframe = time.perf_counter()
    convertUnicode()
    print("Rendered frame", i, "in", time.perf_counter() - tframe, "seconds")

print("Rendered", inputsize, "frames in", time.perf_counter() - t, "seconds")