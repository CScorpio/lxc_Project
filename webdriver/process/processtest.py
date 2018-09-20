from time import sleep,ctime
import multiprocessing

def super_player(file_,time):
    for i in range(2):
        print('start playing: %s! %s' %(file_,ctime()))
        sleep(time)


lists = {'因为爱情.mp3':2,'阿凡达.mp4':3,'浮夸.mp3':4}
files = range(len(lists))
process = []

for file_,time in lists.items():
    t = multiprocessing.Process(target=super_player,args=(file_,time))
    process.append(t)

if __name__ == '__main__':
    #启动进程
    for t in files:
        process[t].start()
    for t in files:
        process[t].join()
    print("end:%s " %ctime())