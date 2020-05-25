# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 01:22:02 2019

@author: RK
"""
import numpy as np
from PIL import Image, ImageDraw


def salt_pepper(image):
    draw = ImageDraw.Draw(image)

    for k in range(100):
        i = int(np.random.uniform(0, image.size[0], 1))
        j = int(np.random.uniform(0, image.size[1], 1))
        draw.point((i, j), 255)  # salting

        i = int(np.random.uniform(0, image.size[0], 1))
        j = int(np.random.uniform(0, image.size[1], 1))
        draw.point((i, j), 0)  # peppering

    return image


if __name__ == '__main__':
    cwd = 'C:\\users\\soyuz\\Desktop\\'
    file_name = 'fruits.png'
    image = Image.open(cwd + file_name).convert('L')  # Сүрөттү жүктөйбүз
    new_image = salt_pepper(image)
    new_image.save(cwd + 'salted_fruits.png')