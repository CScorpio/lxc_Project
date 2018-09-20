import turtle





def draw_fractal_tree(size,angle):

        turtle.left(angle)
        turtle.forward(size)
        left_coordinate = turtle.pos()
        print('左侧树枝节点：',left_coordinate)


        turtle.backward(size)
        turtle.right(angle*2)
        turtle.forward(size)
        right_coordinate = turtle.pos()
        print('右侧树枝节点：', right_coordinate)

def clear_pen(x,y,angle):
    turtle.penup()
    turtle.goto(x,y)
    turtle.home()
    turtle.left(angle*2)
    turtle.pendown()



def main():
    turtle.penup()
    turtle.left(90)
    turtle.backward(200)
    turtle.pendown()


    size = 150
    angle = 20

    turtle.forward(150)
    times = 7
    for i in range(times):
        draw_fractal_tree(size,angle)
        size = size - 20
        #angle = angle - 2
        print('长度：', size, '角度：', angle)

    #去第五个节点,画一个V
    clear_pen(436.94,257.70,20*2)
    draw_fractal_tree(30,20)

    #去第四个节点，画个V
    clear_pen(379.38,296.17, 20*2)
    draw_fractal_tree(50,20)

    #去第三个节点，画个V
    clear_pen(287.98,314.48,20*2)
    draw_fractal_tree(70,20)

    #去第二个节点，画个V
    clear_pen(172.49,293.91,20*2)
    draw_fractal_tree(90, 20)

    #去第一个节点，画个V
    clear_pen(51.30,220.95,20*2)
    draw_fractal_tree(110,20)

    #去第0个节点，画个V
    clear_pen(-51.30,90.95,20*2)
    draw_fractal_tree(130,20)





    turtle.exitonclick()

if __name__ == '__main__':
    main()

