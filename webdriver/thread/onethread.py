from time import sleep,ctime

#听音乐任务
def music(func,loop):
    for i in range(loop):
        print('i was listening to %s! %s' %(func,ctime()))
        sleep(2)

#看电影任务
def movie(func,loop):
    for i in range(loop):
        print('i was at the %s! %s' %(func,ctime()))
        sleep(5)

if __name__ == '__main__':
    music('因为爱情',2)
    movie('阿凡达',2)
    print("all end! %s " %ctime())