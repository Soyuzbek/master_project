# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import numpy as np
from PIL import Image
# file_path = filedialog.askopenfilename()


def cut(F, r=2, power=1):
    width, height = F.shape
    for i in range(len(F)):
        for j in range(len(F[i])):
            if ((i-width/2)**2/(width/r)**2+(j-height/2)**2 /
                    (height/r)**2)*power < power:
                F[i, j] = 0

    # Build and apply a Gaussian filter.
#    sigmax, sigmay = 100, 100
#    cy, cx = height/2, width/2
#    x = np.linspace(0, height, height)
#    y = np.linspace(0, width, width)
#    X, Y = np.meshgrid(x, y)
#    gmask = np.exp(-(((X-cx)/sigmax)**2 + ((Y-cy)/sigmay)**2))
#    F = F * gmask

    return F


def blur(image, r=0.5):
    f = np.fft.fft2(image)
    fs = cut(f)
    return np.fft.ifft2(fs).real


#def sharp(image, r=50):
#    z = np.fft.rfft2(image)
#    l = z[0, 0]
#    zshtrih = cut(z)
#    zshtrih[0, 0] = l
#    new_img = np.fft.irfft2(zshtrih)
#
#    return new_img.astype(np.uint8)


if __name__ == '__main__':
    cwd = 'C:\\Users\\soyuz\\Desktop\\'
    file = 'fruitsL.png'
    image = Image.open(cwd + file).convert('L')
    new_img = blur(image).astype(np.uint8)
    new_image = Image.fromarray(new_img)
