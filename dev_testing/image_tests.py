from PIL import Image, ImageDraw
import sys

size = (3,3)

im = Image.new('RGB',(
    (size[0]+2)*20,
    (size[1]+2)*20))

draw = ImageDraw.Draw(im)

origin = {'x': 20, 'y': 20}

draw.rectangle([(origin['x'],origin['y']),
    (origin['x']+(size[0]*20),
    origin['y']+(size[1]*20))], outline='teal', fill='white')

creature = Image.open('flame.jpeg', 'r')
trap = Image.open('trap.gif', 'r')

im.paste(creature,(20,20))
im.paste(trap,(40,40))

for x in xrange(0,size[0]):
    x0 = origin['x']+(x*20)
    x1 = x0 + 20
    for y in xrange(0,size[1]):
        y0 = origin['y']+(y*20)
        y1 = y0 + 20
        draw.rectangle([(x0,y0),(x1,y1)], outline='teal')


del draw
        

im.save("test.png")
