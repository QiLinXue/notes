#!/usr/bin/env python3

#
# Create symlinks of library .sty files in each subject's folder.
# Done with Python to ensure cross-platform compatibility
#

import os
from pathlib import Path

ignore_dirs = ['.git', 'lib', 'scripts']

files = next(os.walk('lib'))[2]
folders = next(os.walk('.'))[1]
[folders.remove(f) for f in ignore_dirs]
for folder in folders:
  # Remove old symlinks
  for p in Path(folder).glob('*.sty'):
    if p.is_symlink():
      print('Removing {}'.format(p))
      p.unlink()
  # Create new symlinks
  for f in files:
    print('Symlinking {} to {}'.format(f, folder))
    os.symlink('lib/{}'.format(f), '{}/{}'.format(folder, f))