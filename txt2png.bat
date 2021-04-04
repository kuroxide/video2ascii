@ECHO OFF

CD ./output

SET WIDTH=%1
SET HEIGHT=%2
SET /A FRAMES=%3
SET /A count = 1

:X

CONVERT -size %WIDTH%x%HEIGHT% xc:white -font "C:\WINDOWS\FONTS\LUCON.TTF" -pointsize 12 -fill black -annotate +0+9 "@output%count%.txt" render\frame%count%.png
ECHO Rendered frame %count% to PNG

SET /A count = %count% + 1

IF %count% LEQ %FRAMES% goto X

TIMEOUT 15