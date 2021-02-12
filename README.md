# ASCII/Unicode Art Converter
A Python script that takes a sequence of images and turns them into ASCII art. \

## Requirements
ImageMagick 7.0.1.0 with legacy tools \
ffmpeg \
Python 3.9 \
All of these should be added to $PATH.


# Converting a video to ASCII art
## Step 1: Splitting MP4 video to PNG frames
Rename your video to input.mp4 and put it in /input. \
`cd` to /input and run:

`ffmpeg -i input.mp4 -vf fps=30 %d.png`

`fps` should be the fps of the source video. \
After this, move the source video out of the input folder.

## Step 2: Run the Python script
Run the Python script using `python img2ascii.py` in this directory. Alternative, open your IDE or text editor and run the script.

## Step 3: Rendering .txt to PNG images

Right-click on txt2png.bat and click 'Edit' in the context menu that shows up. \
On the line that says `if %count% LEQ frames goto x`, change `frames` to the number of frames the source video has. \
Also, change `WIDTH` to the width of the frames * 10 and `HEIGHT` to the height of the frames*16. \
Move txt2png.bat to /output and then run it and wait for it to finish executing.

## Step 4: Rendering PNG frames to MP4 video

`cd` to /output/render and run: \
`ffmpeg -r framerate -f image2 -s widthxheight -i frame%0d.png -vcodec libx264 -crf 25  -pix_fmt yuv420p output.mp4`

Replace `framerate` with the framerate of the source video. \
Replace `width` and `height` with the dimensions of the frames.

This should result in a video named output.mp4 in the output folder.

## Step 5 (optional): De-stretching the output video
If you don't want you video to be vertically stretched, you can use the transform effect in your preferred video editing software to resize the video.