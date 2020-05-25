# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 01:22:02 2019

@author: RK
"""
import numpy as np
from PIL import Image


def linear(img, minm=0, maxm=255):
    act_max = np.max(img)
    act_min = np.min(img)
    img = ((maxm - minm) / (act_max-act_min)) * (img - minm) + minm

    return img.astype(np.uint8)


if __name__ == '__main__':
    cwd = 'C:\\users\\soyuz\\Desktop\\'
    image = np.asarray(Image.open(cwd + 'fruitsL.png'))
    new_image = Image.fromarray(linear(image))
