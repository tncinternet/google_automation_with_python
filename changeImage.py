#!/usr/bin/env python3

from PIL import Image
import os
import sys


def conv_image(path):
    if path.endswith('.tiff'):
        im = Image.open(path).convert('RGB')
        file = os.path.basename(path)
        filename, ext = file.split('.')
        print(filename)
        im = im.resize((600, 400))
        im.save('/home/student-01-2bb814477945/supplier-data/images/' + filename + '.jpeg', 'JPEG')


directory = sys.argv[1]
for root, dirs, files in os.walk(directory):
    for name in files:
        full_path = os.path.join(root, name)
        print(os.path.join(root, name))
        conv_image(full_path)
