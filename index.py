from os import ctermid
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import glob


def signature(pic,your_name):
    photo = Image.open('./ins/'+pic)
   
    w,h = photo.size
    print(w,h)

    # making the image editable

    drawing = ImageDraw.Draw(photo)
    font = ImageFont.truetype('Nightcall.ttf',20)

    # get text width and height

    text = your_name
    text_w, text_h = drawing.textsize(text,font)

    pos = (w - text_w) - 20, (h - text_h) - 20

    # img2 = photo.resize((40,40))
    
    c_text = Image.new('RGBA', (text_w,text_h), (255, 255, 255, 0))
    drawing = ImageDraw.Draw(c_text)
    drawing.text((0, 0), text, fill="#ffffff", font=font)

    # Image.Image.paste(photo, img2, (50, 50))
    photo.paste(c_text,pos,c_text)
    photo.save('outs/'+ pic)


list = glob.glob('./ins/*.*')

for photo in list:
    signature(photo.split('/')[2],' Shafiq soweb ')
