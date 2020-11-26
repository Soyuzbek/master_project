import cv2
import pytesseract
import sys
from pdf2image import convert_from_path
import os

pages = convert_from_path(r'pdf\albo_vicenza.pdf', 256)

image_counter = 1
for page in pages:
    filename = f'images/page_{image_counter}.jpg'
    page.save(filename, 'JPEG')
    image_counter += 1

file_limit = image_counter - 1
outfile = "out_text.txt"
f = open(outfile, 'a')
for i in range(1, file_limit+1):
    filename = f'images/page_{i}.jpg'
    text = str((pytesseract.image_to_string(cv2.imread(filename))))
    text = text.replace('-\n', '')
    f.write(text)

f.close()


