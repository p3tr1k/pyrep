#!/usr/bin/python3

from PIL import Image, ImageFilter
import sys

try:
    img = Image.open("sid.jpg")
    
except IOError:
    print("Unable to load image")    
    sys.exit(1)

blurred = img.filter(ImageFilter.BLUR)

blurred.save("blurred_sid.png")