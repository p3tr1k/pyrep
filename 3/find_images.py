#!/usr/bin/python3

from pathlib import Path
import os
from PIL import Image

home_dir = str(Path.home() / 'Documents')

directories = os.walk(home_dir)

for (root, dirs, files) in directories:
    for file in files:
        if file.endswith('jpg') or file.endswith('png'):
            # print(file)
            img = Image.open(os.path.join(root, file))
            print('Name: {} Format: {}\nSize: {}\nMode: {}'.format(file, img.format, img.size, img.mode))


# print(list(directories))

