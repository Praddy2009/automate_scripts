#Import required Image library
from PIL import Image, ImageDraw, ImageFont
import os

#Create an Image Object from an Image
directory = r'.'
b=1
for filename in os.listdir(directory):
    if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".PNG") or filename.endswith(".jpeg"):
        a=os.path.join(directory, filename)
        im = Image.open(a)
        b=filename.split(".")[0]
        im.save('test/'+b+".webp","webp")
    else:
        continue