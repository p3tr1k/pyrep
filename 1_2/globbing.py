#!/usr/bin/env python

from pathlib import Path

path = Path('C:/Users/admin/Documents/pyprg')

for e in path.rglob('*.py'):
    print(e)
    
# for e in path.glob('**/*.py'):
#     print(e)