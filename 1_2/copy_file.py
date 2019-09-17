#!/usr/bin/env python

from pathlib import Path
from shutil import copyfile

# source = Path('words.txt')
# destination = Path.home() / Path('words_bck.txt')

# copyfile(source, destination)
#****************************************************

# Path("empty.txt").touch()
#*****************************************************

path = Path("empty.txt")
path.rename("prazdny.txt")


