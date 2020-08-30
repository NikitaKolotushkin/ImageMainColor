#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Counter
from PIL import Image


img = Image.open("input_image.jpg")

colors = []

for i in range(img.size[0]):
    for j in range(img.size[1]):
        #print(img.getpixel((i, j)))
        colors.append(img.getpixel((i, j)))
        j += 1
    c = Counter(colors)
    print(c)
    break
    i += 1
