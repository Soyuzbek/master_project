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
#image = ImageOps.mirror(image)
#image = ImageOps.flip(image)
#image = image.rotate(-180)
img = np.asarray(image)


def hough_line(image):
    width, height = image.shape
    max_r = int(np.round(np.sqrt(width**2+height**2)))
    thetas = np.deg2rad(np.arange(-90, 90))
    rhos = np.linspace(-max_r, max_r, 2*max_r)
    accumulator = np.zeros((2*max_r, len(thetas)))
    for y in range(width):
        for x in range(height):
            if image[y, x] < 10:
                for k in range(len(thetas)):
                    r = x * np.cos(thetas[k]) + y * np.sin(thetas[k])  # line
#                    r = np.sqrt(x**2+y**2)  # circle
                    accumulator[int(r)+max_r, k] += 1
    return accumulator, thetas, rhos


accumulator, thetas, rhos = hough_line(img)

#plt.figure('Original Image')
#plt.imshow(img)
#plt.set_cmap('gray')
#plt.figure('Hough Space')
#plt.imshow(accumulator)
#plt.set_cmap('gray')
#plt.show()
#plt.close()
idx = np.argmax(accumulator)
rho = int(rhos[int(idx / accumulator.shape[1])])
theta = thetas[int(idx % accumulator.shape[1])]
degree = theta #np.rad2deg(theta)
a = rho*np.cos(degree)
b = rho*np.sin(degree)
print(f"Сүрөттөгү сызыктын теңдемеси: y = {a}x + {b}")  # line
#print(f"Сүрөттөгү айлананы теңдемеси: (y-({a}))^2 + (x-({b}))^2 = {rho}^2")

xs = np.linspace(0, 50, 50)
ys = a*xs+b
plt.plot(xs, ys)
#c = plt.Circle((a, b), rho, fill=False)
#plt.gca().add_artist(c)
plt.show()

image.close()