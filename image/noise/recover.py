# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 01:22:02 2020

@author: Soyuzbek Orozbek uulu
"""
import numpy as np
from PIL import Image


class Recover:
    def __init__(self, image):
        self.img = np.asarray(image)
        self.width, self.height = self.img.shape

    def median(self):
        new_img = np.zeros(self.img.shape, np.uint8)
        w_width, w_height = 3, 3
        window = np.zeros(w_height*w_width, np.uint8)
        edgex = int(w_width/2)
        edgey = int(w_height/2)

        for x in range(edgex, self.width-edgex):
            for y in range(edgey, self.height-edgey):
                i = 0
                for fx in range(0, w_width):
                    for fy in range(0, w_height):
                        window[i] = self.img[x+fx-edgex, y+fy-edgey]
                        i += 1
                window.sort()
                new_img[x, y] = window[w_width*w_height//2]

        return new_img

    def square_mean(self):
        new_img = np.zeros(self.img.shape, np.uint8)

        for x in range(1, self.width-1):
            for y in range(1, self.height-1):
                new_img[x, y] = np.sqrt((int(self.img[x+1, y]) -
                                         int(self.img[x-1, y]))**2 +
                                        (int(self.img[x, y+1]) -
                                         int(self.img[x, y-1]))**2)

        return new_img

    def average(self):
        fnew = np.zeros(self.width, self.height, np.uint8)

        weight = [1, 1, 1, 1]

        for x in range(1, self.width-1):
            for y in range(1, self.height-1):
                fnew[x, y] = (weight[0]*self.img[x-1, y] +
                              weight[1]*self.img[x+1, y] +
                              weight[2]*self.img[x, y-1] +
                              weight[3]*self.img[x, y+1]) / sum(weight)
        return fnew


def gradient(image):
    img = np.asarray(image, np.float)
    width, height = img.shape
    new_img = np.zeros((width, height), np.uint8)
    for x in range(1, width):
        for y in range(1, height):
            new_img[x, y] = np.sqrt((img[x-1, y]-img[x, y])**2 +
                                    (img[x, y-1]-img[x, y])**2)
    return new_img


if __name__ == '__main__':
    cwd = 'C:\\users\\soyuz\\Desktop\\'
    file_name = 'salted_fruits.png'
    image = Image.open(cwd + file_name).convert('L')  # Сүрөттү жүктөйбүз

    new_image = Image.fromarray(gradient(image))
