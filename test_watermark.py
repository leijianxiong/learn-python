from itertools import product
from PIL import Image
import os

pic = '/Users/leijianxiong/Downloads/5eec7193-df54-526b-b58e-9d4d6c3d2c9f.jpg'
newpic = '/Users/leijianxiong/Downloads/removed_1.png'
print('pic ', pic)
print('newpic ', newpic)

img = Image.open(pic)
width, height = img.size
for pos in product(range(width), range(height)):
    if sum(img.getpixel(pos)[:3]) >= 600:
        img.putpixel(pos, (255,255,255))
img.save(newpic)

print('handle done')