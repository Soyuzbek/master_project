# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 17:34:39 2020

@author: soyuz
"""

import numpy as np
from PIL import Image
from matplotlib import pyplot as plt


def pixels(image_file, a=1, b=1):
    img = np.asarray(image_file)
    width, height = img.shape
    R = np.zeros((width, height), np.float)+1
    W = [[-2, -2], [-1, -2], [0, -2], [1, -2], [2, -2],
         [-2, -1], [-1, -1], [0, -1], [1, -1], [2, -1],
         [-2, 0], [-1, 0], [1, 0], [2, 0],
         [-2, 1], [-1, 1], [0, 1], [1, 1], [2, 1],
         [-2, 2], [-1, 2], [0, 2], [1, 2], [2, 2],
         ]
    for x in range(5, width-5):
        for y in range(5, height-5):
            counter = 0
            for i, j in W:
                if img[x, y]-5 < img[x+i, y+j] < img[x, y]+5:
                    counter += 1
            R[x, y] = counter/24
    max_value = R.max()
    for x in range(width):
        for y in range(height):
            if R[x, y] > max_value*0.35:
                R[x, y] = 0
            else:
                R[x, y] = img[x, y]
    return R.astype(np.uint8)


if __name__ == '__main__':
    cwd = 'C:\\Users\\stat01\\Desktop\\'
    image = Image.open(cwd + 'sign.png').convert('L')
    result = pixels(image, 1, 1)

    new_image = Image.fromarray(result)
    plt.imshow(result)
    plt.show()
