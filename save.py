#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from PIL import Image
from main import *


im = Image.new("RGB", new_image_resolution, color=c).save("output_image.jpg")