from PIL import Image, ImageChops
import PIL.ImageOps  
import cv2
import numpy as np
import random


point_table = ([0] + ([255] * 255))


f = Image.new('RGB',(119,83),(0,0,0))


def black_or_b(a, b):
    diff = ImageChops.difference(a, b)
    diff = diff.convert('L')
    diff = diff.point(point_table)
    new = diff.convert('RGB')
    new.paste(b, mask=diff)
    return new
    


#for i in range(41):
    a = Image.open('image1.png')
    b = Image.open('image%d.png'%(i*11+1))
    e = black_or_b(a, b)
    final_img = Image.blend(f,e,0.9)
    f =final_img


a = Image.open('image1.png')
b = Image.open('image12.png')
e = black_or_b(a, b)
e.s