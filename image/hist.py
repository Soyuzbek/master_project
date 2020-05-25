# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 01:22:02 2019

@author: RK
"""
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt


def hist(img):
    img = np.asarray(img)
    width, height = img.shape
    H = np.zeros(256)
    a = 0
    b = 255
    c = 150
    d = 250

    for x in range(width):
        for y in range(height):
            t = int(((d - c)/(b - a))*(x - a) + c)
            A = img[t, y]
            H[A] += 1

    return H


if __name__ == '__main__':
    cwd = 'C:\\users\\soyuz\\Desktop\\'
    file_name = 'salted_fruits.png'
    image = Image.open(cwd + file_name).convert('L')  # Сүрөттү жүктөйбүз

    H = hist(image)
    plt.axis([0, 255, 0, H.max()])
    plt.plot(H)
    plt.xlabel('scales')
    plt.ylabel('number of scales')
