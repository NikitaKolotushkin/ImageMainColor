#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image


img = Image.open("input_image.jpg")
print(img.size)

for i in range(img.size[0]):
    for j in range(img.size[1]):
        print(img.getpixel((i, j)))
        j += 1
    i += 1
