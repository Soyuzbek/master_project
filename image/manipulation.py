# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 01:22:02 2019

@author: RK
"""
import numpy as np
from PIL import Image


def rectangle(img, a=60, b=-60, n=230, p=15):
    width, height = img.shape

    x0 = width // 2
    y0 = height // 2
    dx = p * width // 200
    dy = p * height // 200

    new_img = np.zeros((width, height), np.uint8)

    for x in range(width):
        for y in range(height):
            if abs(x-x0) > dx or abs(y-y0) > dy:
                new_img[x, y] = a + ((b-a)/n) * x + img[x, y]
    return new_img


def circle(img, a=60, b=-60, n=230, r=15):
    width, height = img.shape

    x0 = width // 2
    y0 = height // 2

    new_img = np.zeros((width, height), np.uint8)

    for x in range(width):
        for y in range(height):
            if (x-x0)**2 + (y-y0)**2 > r * r + 4:
                new_img[x, y] = a + ((b-a)/n) * x + img[x, y]
    return new_img


def ellipse(img, a=60, b=-60, n=230, r=15):
    width, height = img.shape

    x0 = width // 2
    y0 = height // 2

    new_img = np.zeros((width, height), np.uint8)

    for x in range(width):
        for y in range(height):
            if ((x-x0)*(x-x0)) / (a * a) + ((y-y0) * (y-y0)) / (b * b) >= 1:
                new_img[x, y] = a + ((b-a)/n) * x + img[x, y]
    return new_img


if __name__ == '__main__':
    cwd = 'C:\\users\\soyuz\\Desktop\\'
    file_name = 'fruits.png'
    image = Image.open(cwd + file_name).convert('L')
    new_image = Image.fromarray(rectangle(np.asarray(image)))
