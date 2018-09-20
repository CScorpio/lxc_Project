'''
功能：五角星的绘制
版本：1.0

'''

import turtle

def draw_pentagram(size):
    for i in range(5):
        turtle.forward(size)
        turtle.right(144)
    if size <= 500:
        size += 50
        print(size)
        draw_pentagram(size)

def main():
    #主函数

    turtle.penup()
    turtle.backward(200)
    turtle.pendown()
    turtle.pensize(2)
    turtle.pencolor('green')

    distance = 300
    draw_pentagram(distance)



    turtle.exitonclick()

if __name__ == '__main__':
    main()
