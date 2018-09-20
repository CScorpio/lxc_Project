import turtle




#绘制五角星

spiral = turtle.Turtle()

for i in range(500):
    spiral.forward(i *  10)
    spiral.right(144)

turtle.done()
'''

#绘制两个奇怪的圈
painter = turtle.Turtle()

painter.pencolor("blue")
for i in range(50):
    painter.forward(100)
    painter.left(123)

painter.pencolor("red")
for i in range(50):
    painter.forward(200)
    painter.left(123)

turtle.done()
'''
'''
#绘制一个奇怪的圈
ninjia=turtle.Turtle()
ninjia.pencolor("green")
for i in range(180):
    ninjia.forward(100)
    ninjia.right(30)
    ninjia.forward(20)
    ninjia.left(60)
    ninjia.forward(50)
    ninjia.right(30)

    ninjia.penup()
    ninjia.setposition(0,0)
    ninjia.pendown()

    ninjia.right(2)

turtle.done()
'''
'''
from PIL import Image

ascii_char = list(r"$@&%B#=1. ")

def select_ascii_char(r,g,b):
	gary = int((19595*r+38469*g+7472*b) >> 16)
	unit = 256.0/len(ascii_char)
	return ascii_char[int(gary/unit)]

def output(imgpath,width=100,height=100):
	im = Image.open(imgpath)
	im = im.resize((width,height),Image.NEAREST)
	txt = ""

	for h in xrange(height):
		for w in xrange(width):
			txt += select_ascii_char(*im.getpixel((w,h))[:3])
		txt+='\n'
	return txt
'''
