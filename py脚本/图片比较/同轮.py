from typing import Counter
from PIL import Image
from PIL import ImageFile
import collections


ImageFile.LOAD_TRUNCATED_IMAGES = True
Image.MAX_IMAGE_PIXELS = None


f = Image.new('RGB',(119,83),(0,0,0))


for i in range(11):
    img=Image.open(str(i)+'.png')
    img1=Image.new('RGB',(119,83),(255,255,255))
    for h in range(40):
        im=Image.open(str((h+1)*11+i)+'.png')
        width,height=img.size
        for j in range(0,width):
            for k in range(0,height):
                tmp = img.getpixel((j,k))
                tmp1 = im.getpixel((j,k))
                if tmp != tmp1:
                    img1.putpixel((j,k),(0,0,0))


    img1.save('test'+str(i+1)+'.png')


f.s