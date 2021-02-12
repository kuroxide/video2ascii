@echo off

set /A count = 1

:x

convert -size WIDTHxHEIGHT xc:white -font "C:\WINDOWS\FONTS\LUCON.TTF" -pointsize 12 -fill black -annotate +0+0 "@output%count%.txt" render\frame%count%.png
echo Rendered frame %count%

set /A count = %count% + 1

if %count% LEQ frames goto x

timeout 60