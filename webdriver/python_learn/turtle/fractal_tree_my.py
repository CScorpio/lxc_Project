import turtle



def draw_branch(branch_length):
    '''
    绘制分形树
    '''
    if branch_length > 5:
        #绘制右侧树枝
        turtle.forward(branch_length)
        print('向前长度:',branch_length)
        turtle.right(20)
        print('向右转20度')
        aaa = branch_length - 15
        if aaa <= 20:
            turtle.pencolor('green')
        else:
            turtle.pencolor('brown')
        draw_branch(aaa)


        #绘制左侧树枝
        turtle.left(40)
        print('向左转40度')
        if aaa <= 20:
            turtle.pencolor('green')
        else:
            turtle.pencolor('brown')
        draw_branch(aaa) #这样会怎么样呢


        #返回之前的树枝
        turtle.right(20)  #此时向右转20度
        print('向右转20度')
        turtle.penup()
        turtle.backward(branch_length)
        turtle.pendown()




def main():
    turtle.left(90)
    turtle.penup()
    turtle.backward(150)
    turtle.pendown()
    #turtle.pencolor('green')
    draw_branch(60)
    turtle.exitonclick()

if __name__ == '__main__':
    main()

