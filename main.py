#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Counter
from PIL import Image, ImageDraw, ImageFont
from save import *


img = Image.open("input_image.jpg")  # Opening the original image

colors = []  # An empty list to which the colors of each pixel will be added

for i in range(img.size[0]):  # Go through pixels of width
    for j in range(img.size[1]):  # Go through pixels of height
        colors.append(img.getpixel((i, j)))  # Adding pixel colors to a list
        j += 1  # Move to the next pixel in height
    i += 1  # Move to the next pixel in width

c = list(Counter(colors).most_common(1))[0][0]  # Determining the most common color
