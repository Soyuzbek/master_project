# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 09:05:22 2020

@author: soyuz
"""

from matplotlib import pyplot as plt
from PIL import Image, ImageDraw, ImageOps
import numpy as np

image = Image.open('C:\\Users\\soyuz\Desktop\\' + 'line.png')
image = image.convert('L')
image = ImageOps.flip(image)
width, height = image.size
img = np.asarray(image)

teta = np.arange(0, 181, 1)
len_teta = len(teta)
new_img = np.zeros((180, 10), np.int8) + 255
kaldik = 250/max(180, 10)
epsilon = 1.01

for x in range(width):
    for y in range(height):
        if img[y, x] < 10:
            temp = []
            for i in range(len_teta):
                temp.append(x*np.cos(teta[i]) + y*np.sin(teta[i]))
#                ro = x*np.cos(teta[i]) + y * np.sin(teta[i])
#                new_img[]
#                if abs(b[j]-y+a[i]*x) < epsilon:
#                    new_img[j, i] -= 2*kaldik
            plt.plot(teta, temp)

#new_image = Image.fromarray(new_img)
#ind = np.unravel_index(np.argmin(new_img), new_img.shape)

#print("Сызыктын издоо интервалдары:")
#print("a интервалы [",a[0],";",a[-1],"]")
#print("b интервалы [",b[0],";",b[-1],"]")
#print(f"Сүрөттөгү сызыктын теңдемеси: y = {a[ind[1]]}x + {b[ind[0]]}")

plt.show()
image.close()# -*- coding: utf-8 -*-

