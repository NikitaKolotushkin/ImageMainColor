#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Counter
from PIL import Image, ImageDraw, ImageFont
from save import *


img = Image.open("input_image.jpg")

colors = []

for i in range(img.size[0]):
    for j in range(img.size[1]):
        colors.append(img.getpixel((i, j)))
        j += 1
    c = list(Counter(colors).most_common(1))[0][0]
    i += 1
print(c)

new_image_resolution = 512, 512
# new_img = Image.new("RGB", new_image_resolution, c).show()
