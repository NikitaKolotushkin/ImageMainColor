#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from PIL import Image
from main import *


new_image_resolution = 512, 512
im = Image.new("RGB", new_image_resolution, color=c).save("output_image.jpg")  # Creating a new image
