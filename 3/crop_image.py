#!/usr/bin/python3

from PIL import Image
import sys

try:
    tatras = Image.open("sid.jpg")

except IOError:
    print("Unable to load image")
    sys.exit(1)
    
cropped = tatras.crop((200, 10, 900, 300))
cropped.save('tatras_cropped.png')