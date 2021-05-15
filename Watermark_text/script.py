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
        width, height = im.size

        draw = ImageDraw.Draw(im)
        text = "@its_praddy"

        font = ImageFont.truetype('arial.ttf', 36)
        textwidth, textheight = draw.textsize(text, font)

        # calculate the x,y coordinates of the text
        margin = 10
        x = width - textwidth - margin
        y = height - textheight - margin

        # draw watermark in the bottom right corner
        draw.text((x, y), text, font=font)

        #Save watermarked image
        im.save('test/'+str(b)+".webp","webp")
        b=b+1
    else:
        continue