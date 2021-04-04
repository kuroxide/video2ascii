# ASCII/Unicode Art Converter
A Python script that takes a MPEG-4 video and turns it into ASCII art. 

# Requirements
- Python 3.9
- ImageMagick 7.0.1.0 with legacy tools (Added to $PATH)
- ffmpeg 4.2.3 (Added to $PATH)

# Using the script
Find out the FPS of the video you wish to convert. \
Rename the video to input.mp4 and copy it to ./input.

Run the Python script using `python img2ascii.py` in this directory. Alternatively, open the script in your IDE and run the script. (Make sure to be in this directory.)

Running this script may take a very long time, especially if you have a slow computer. Multithreading or something similar is planned for implementation at some point.


## Post-processing
If you don't want your video to be vertically stretched, you can use the transform effect in your preferred video editing software to resize the video. \
You can also add effects to make it look older/more retro.