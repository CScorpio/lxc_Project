'''
功能：五角星的绘制
版本：1.0

'''

import turtle

def main():
    #主函数

    distance = 300

    for i in range(10):

        for i in range(5):
            turtle.forward(distance)
            turtle.right(144)

        distance = distance + 50


    turtle.exitonclick()

if __name__ == '__main__':
    main()
