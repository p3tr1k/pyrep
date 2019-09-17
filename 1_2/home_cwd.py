#!/usr/bin/env python

from pathlib import Path

# print(f"Current directory: {Path.cwd()}")
# print(f"Home directory: {Path.home()}")
#**************************************************

path = Path.home() / "novy"
path.mkdir()