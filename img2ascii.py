from PIL import Image
import os
import subprocess
import time


FPS = int(input("FPS of the source video: "))
subprocess.run(f"ffmpeg -i ./input/input.mp4 -vf fps={FPS} input/%d.png")

frameCount = 0
for file in os.listdir("input"):
    if file.endswith(".png"):
        frameCount += 1


PALETTE = "█▓▒░|:. "

t = time.perf_counter()
for i in range(1, frameCount):
    t2 = time.perf_counter()

    image = Image.open("input/" + str(i) + ".png").convert("L")
    frameWidth, frameHeight = image.size
    with open('output/output' + str(i) + '.txt', 'w') as f:
        lines = ''
        for y in range(frameHeight):
            for x in range(frameWidth):
                lines += PALETTE[int(image.getpixel((x, y))/32)]
            lines += '\n'
        f.write(lines)

    print(f"Converted frame {i} to text in {time.perf_counter() - t2} seconds")
print(f"Converted {frameCount} frames to text in {time.perf_counter() - t} seconds")


frameWidth = frameWidth*7
frameHeight = frameHeight*13

if frameWidth % 2 == 1:
    frameWidth += 1
if frameHeight % 2 == 1:
    frameHeight += 1

subprocess.run(f"txt2png.bat {str(frameWidth)} {str(frameHeight)} {str(frameCount)}")

subprocess.run(f"ffmpeg -r {FPS} -f image2 -s {frameWidth}x{frameHeight} -i output/render/frame%0d.png -vcodec libx264 -crf 25  -pix_fmt yuv420p output/output.mp4")