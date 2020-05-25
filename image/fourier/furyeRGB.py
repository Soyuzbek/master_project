# -*- coding: utf-8 -*-
import numpy as np
from PIL import Image, ImageDraw
from matplotlib import pyplot as plt
# file_path = filedialog.askopenfilename()
file_path = 'C:\\Users\\soyuz\Desktop\\'
file_name = 'president.png'
image = Image.open(file_path + file_name)  # Сүрөттү жүктөйбүз
width, height = image.size  # Өлчөмдөрүн аныктайбыз
new_image = Image.new('RGB', image.size, (0, 0, 0))
draw = ImageDraw.Draw(new_image)


def zeroing(F, a, b, r):
#    indexes = np.arange(len(F))
    for i in range(len(F)):
        for j in range(len(F[i])):
            if (i-a)**2+(j-b)**2 < r**2:
                F[i, j, :] = 0
    return F


# =============================================================================
# management
fold = np.asarray(image) # Фурьенин түз өзгөртүүсүн эсептөө үчүн массив алабыз

px = np.sum(fold)
px0 = np.average(fold[:, :, 0])
px1 = np.average(fold[:, :, 1])
px2 = np.average(fold[:, :, 2])

F = np.fft.rfft2(fold, axes=(0, 1)) # Фурьенин түз өзгөртүүсү
F = zeroing(F, F.shape[0]/2, F.shape[1]/2, 200)

fnew = np.fft.irfft2(F, axes=(0, 1)).astype(np.uint8)
py = np.sum(fnew)
py0 = np.average(fnew[:, :, 0])
py1 = np.average(fnew[:, :, 1])
py2 = np.average(fnew[:, :, 2])
fnew = fnew*(px/py)
#fnew = fnew[:, :, 0]*(px0/py0)
#fnew = fnew[:, :, 1]*(px1/py1)
#fnew = fnew[:, :, 2]*(px2/py2)
# массивден сүрөт алабыз
new_image = Image.fromarray(fnew, 'RGB')