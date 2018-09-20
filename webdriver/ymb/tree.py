import turtle
count = 0
def draw_branch(branch_length):
    global count
    count+=1
    print("Begin... 当前是第", 5-branch_length//15,"层树，| >5 = ",branch_length>5)
    #
    color = "brown"
    if branch_length - 15 <= 20:
        # 变颜色
        color = "green"

    turtle.pencolor(color)

    if branch_length > 5:
        #绘制右侧树枝
        turtle.forward(branch_length)
        #print('向前长度:',branch_length)
        turtle.right(20)
        print('向右转20度，画右分叉')
        draw_branch(branch_length - 15)

        #绘制左侧树枝
        turtle.left(40)
        print('向左转20度，画左分岔')
        draw_branch(branch_length - 15)

        #返回之前的树枝
        turtle.right(20)
        print("返回")
        turtle.pencolor(color)
        turtle.backward(branch_length)
    else:
        print("END: 由于已经是末端，所以结束绘制")

if __name__ == '__main__':
    turtle.lt(90)
    draw_branch(100)
    print("总共执行了",count,"次draw_branch方法")
    turtle.done()