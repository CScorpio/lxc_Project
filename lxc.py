# -*- coding: UTF-8 -*-
print "hello world!"


# 汉字输出 以及代码缩进
if True:
	print '答案正确'.decode('utf-8').encode('gbk');
else:
	print 'false';
#代码缩进	
if True:
	print 'anser';
	print 'true';
else:
	print 'anser';
	print 'false';
	
'''	
#多行语句:一行语句多行显示
total=item_one+\
	item_two+\
	item_three
print total;
#多行语句:多行连接符的使用
'''
	
days=['monday','tuesday',
'wednesday',
'thursday','Friday']
print days;
# 引号用法
word='word'; #以及注释用法
sentence="这是一个sentence";
paragragh="""这是一个paragragh，
包含了多条语句""";
print word.decode('utf-8').encode('gbk');
print sentence.decode('utf-8').encode('gbk');
print paragragh.decode('utf-8').encode('gbk');
'''
#用户输入测试

因为显示的值依旧是乱码，这个方法并不能让他变成中文。

'''
#raw_input("按下enter键退出，其他任意键显示".decode('utf-8').encode('gbk'));

# 同一行显示多条语句
import sys;x='runoob';sys.stdout.write(x+'\n');
import sys;x='runoob';print(x+'\n');

#print 输出默认换行

x='a'
y='b'
#换行输出
print x;
print y;

print '-------------------'
x='a'
y='b'
#不换行输出
print x,
print y

#不换行输出
print x,y;

import sys;
print '参数个数为'.decode('utf-8').encode('gbk') ,len(sys.argv),'个参数。'.decode('utf-8').encode('gbk')
print '参数列表：'.decode('utf-8').encode('gbk'),str(sys.argv)

#变量赋值
counter = 100 #赋值整形变量
miles = 1000.0 #浮点型
name = "john" #字符串

print counter;
print miles;
print name;

#多个变量赋值

a=b=c=100
print a,b,c;

a,b,c = 1,2,"john" 
print a,b,c;

#字符串赋值以及显示
var=1;
s='123abc_';
str1='helloworld';
print str1;      #打印出整个字符串
print str1[0];	#打印出第一个字符 h
print str1[2:5];	#发引出第三个至第五个之间的字符串llo，不包含第五个  
print str1[2:];	#打印出从第三个字符串开始的字符串lloworld
print str1 * 2;	#输出字符串两次 hello worldhello world
print str1+"myself";	#打印出连接的字符串hello worldmyself


#列表赋值以及显示
list1=['python','786','2.23','2.23L',['haha','kkkk'],70.2];
tinylist=[123,'lxc'];

print list1; #打印出整个列表['python','786','2.23','2.23L',['haha','kkkk'],70.2]
print list1[0];	#打印列表中的第一个元素python
print list1[1:5];#打印出列表中的第二个和第五个之间的元素，不包括第五个['786','2.23','2.23L',['haha','kkkk']]
print list1[2:];	#打印出列表中第三个之后的所有元素['2.23','2.23L',['haha','kkkk'],70.2]
print tinylist *2;	#打印两次列表[123,'lxc',123,'lxc']
print list1+tinylist;	#打印出组合的列表['python','786','2.23','2.23L',['haha','kkkk'],70.2,123,'lxc']

print "------------------------------------------------------"
#元祖赋值以及显示 元祖不可以进行二次赋值，相当于只读列表

tuple1=('python','786','2.23','2.23L',('haha','kkkk'),70.2);
tinytuple=(123,'lxc');

print tuple1;		#输出整个元祖('python','786','2.23','2.23L',('haha','kkkk'),70.2)
print tuple1[0];		#输出元祖中第一个元素python
print tuple1[1:5];	#输出元祖中第二个至第五个之间的元素，不包含第五个('786','2.23','2.23L',('haha','kkkk'))
print tuple1[2:];	#输出元祖中第三个开始至列表末尾的所有元素('2.23','2.23L',('haha','kkkk'),70.2)
print tinytuple*2;	#输出元祖两次(123,'lxc',123,'lxc')
print tuple1+tinytuple;#输出连接的元祖('python','786','2.23','2.23L',('haha','kkkk'),70.2,123,'lxc')

list2=['python','786','2.23','2.23L',['haha','kkkk'],70.2];
tuple2=('python','786','2.23','2.23L',('haha','kkkk'),70.2);
list2[2]=1000;
print list2;
# tuple[2]=1000;  在元祖中时非法的，因为元祖不可以进行二次赋值，运行时会提示 tuple object does not support item assignment

print "------------------------------------------------------"
print "------------*****************************-------------"
# 字典赋值以及显示 字典通过索引（key）和它对应的value组成
dict3={};
dict3['one']="this is the one";
dict3[0]="this is two";
dict3['two']="['hello','hello']";
dict3[1]="11"
dict3[2]="22"
dict3[3]="33"
dict3[4]="44"
dict3[5]="55"
dict3[6]="66"
dict3[7]="77"
dict3[8]="88"

tinydict={'1':'11','2':'22','3':'33','4':'44','5':'55','6':'66','7':'77','8':'88','9':'99','10':'1010'}

print dict3;
print dict3['one'];		#输出键值为one的值
print dict3[0];			#输出键值为2的值
print tinydict;			#输出完整的字典
print tinydict.keys(); #输出所有键
print tinydict.values();#输出所有值


print type(counter);
print isinstance(counter,int);
print type(miles);
print isinstance(miles,float);
print type(name);
print isinstance(name,str);

print type(list1);
print isinstance(list1,list);#
print type(tuple1);
print isinstance(tuple1,tuple);
print type(dict3);
print isinstance(dict3,tuple);

print "==================================="

strange=[1,2,3,4,5];
strange[0]=100;
print strange;
strange={};
strange[0]="this is 100";
print strange;


#python 运算符--算数运算符
a=21
b=10
c=0

c=a+b;  print "1:c ",c  #两个对象值相加 31
c=a-b;	print "2:c ",c	#两个对象值相减 11
c=a*b;	print "3:c ",c	#两个对象值相乘 210
c=a/b;	print "4:c ",c	#两个对象值相除 2
c=a%b;	print "5:c ",c	#两个对象取模，即返回除法的余数 1

a,b=2,3;
c=a**b; print "6:c ",c	#返回a的b次方 2的3次方8

a,b=10,5;
c=a//b; print "7:c ",c	#取整数，返回商的整数部分

a,b=10.0,3
c=a/b;	print "8:c ",c
c=a//b;	print "9:c ",c

#python 运算符--比较运算符
a=21
b=10
c=0

if(a==b): print "1:a=b"
else: print "1:a!=b";

if(a!=b): print "2:a!=b"
else:print "2:a=b"

if(a<>b):print "3:a<>b"
else:print "3:a=b"

if(a<b):print "4:a<b"
else: print "4:a>=b"

if(a>b):print"5:a>b"
else:print "5:a<=b"

a,b=5,20
if(a<=b):print"6:a<=b"
else:print"6:a>b"

if(b>=a):print"7:b>=a"
else:print"7:b<a"

#python 运算符--赋值运算符

a=21
b=10
c=0
c=a+b; print "1:c:",c;   #c=31
c+=a; print "2:c:",c;    #c=31+21=52
c*=a; print "3:c:",c;	#c=c*a=52*21=1092
c/=a; print "4:c:",c;	#c=1092/a=1092/21=52
c-=a; print "5:c:",c;	#c=52-21=31


c=2
c%=a; print "6:c:",c;   #c=c%a=2%21=2
c**=a;print "7:c:",c;	#c=c的a次方=2的21次方2097152
c//=a;print "8:c:",c;	#c=c除以a并且取商的整数 = 99864

#python 运算符--逻辑运算符
a=10
b=20
c=a and b; #如果a和b都为true，那么返回b的值
if(c): print c;      #输出20
else:print "hello"; 
c=not(a and b) 
print c;

c=a or b;	#如果a是非0，那么返回a，否则返回b
if(c): print c;      #输出10
else:print "hello";
c=not (a or b);
print c; 
if not(c): print "true";      
else:print "false";

a=0
b=20
c=a and b; #
if(c): print c;      #
else:print "hello"; 
c=not(a and b) 
print c;

c=a or b;	#
if(c): print c;      #
else:print "hello";
c=not (a or b);
print c; 
if not(c): print "true";      
else:print "false";



a=1288;
b=1288;

print id(a);
print id(b);
print(a is b);

a=b=1288;
print(a is b);


flag = False
name =  'java'
if name == 'python':
	flag = 'c++'
	print flag;
else:
	print name;
	
num = 5
if num ==3:
	print "num=3";
elif num==2:
	print "num=2";
elif num==1:
	print "num=1";
elif num <= 0:
	print "num<=0";
else:
	print num;
	
	
num = 9;
if num>=0 and num<=10:
	print 'hello';

num = 10;
if num<0 or num>10:
	print 'hello'
else:
	print "hello1"
	
num = 8
if (num>=0 and num<=5) or (num>=10 and num<=15):
	print "hello"
else:
	print "hello1"
	
	
num = 8
if num>=0 and num<=5 or num>=10 and num<=15:
	print "hello"
else:
	print "hello1"
	
a=100
if(a==100):print "a=100"

print "good bye"


a=0
b=1
if ( a > 0 ) and ( b / a > 2 ):
    print "yes"
else :
    print "no"
	
'''
a=0
b=1
if ( a > 0 ) or ( b / a > 2 ):
    print "yes"
else :
    print "no"
'''
	

count=0
while (count<9):
	print 'The count is:',count
	count +=1;
print "good bye"
	
i=1
while i < 10:
	i += 1
	if i%2 > 0:
		continue
	print i

print '======================'
i=1
while 1: #当判断条件为常值时，循环必定成立
	print i
	i +=1
	if i>10:
		break

		
print '======================'
"""	
var = 1
while var==1:
	num = raw_input("Enter a number:")
	print "you entered:",num	
print "good bye" #无限循环可以用CTRL+C终端循环


print '======================'"""	

count= 0
while count<5:
	print count,"is less than 5"
	count +=1
else:
	print count,"is not less than 5"
	
print '======================'
'''
flag = 1
while(flag):print"hello"
print"good bye"
'''
'''
print '==========big or small==========='
import random
s = int(random.uniform(1,10))
print(s)
m = int(input('input:'))
while m != s:
    if m > s:
        print('big')
        m = int(input('input:'))
    if m < s:
        print('small')
        m = int(input('input:'))
    if m == s:
        print('OK')
        break;

print '======================'
print"======shitou jiandao bu======="


import random
while 1:
	computer = int(random.randint(0,2))
	#print computer
	if computer==0:computer1='st'
	elif computer==1:computer1='jd'
	elif computer==2:computer1='bu'

	personal = raw_input("Enter a string:")

	if (personal!='st' and personal!='jd' and personal!='bu' and personal!='end'):
		print "Input error, please reenter"
	elif (personal=='jd' and computer1=='st') or (personal=='st' and computer1=='bu') or (personal=='bu' and computer1=='jd'):
		print "you lose!"
	elif (personal=='st' and computer1=='jd') or (personal=='bu' and computer1=='st') or (personal=='jd' and computer1=='bu'):
		print "you win!"
	elif personal==computer1:
		print "a draw"
	elif personal=='end':
		print "The game over"
		break
		
'''
print '======================'
print"======9*9======="

i=0
while(i<9):
	i=i+1
	j=0
	while (j<9):
		j=j+1;  
		sum=i*j
		print i,"*",j,"=",sum
		

for letter in "python":
	print 'The letter:',letter

fruits = ['banana','apple','mango']
for fruit in  fruits:
	print "fruit:",fruit



print"======index for======="	
fruits = ['banana','apple','mango']
for index in range(len(fruits)):
	print len(fruits)	#输出3
	print range(len(fruits))	#输出【0,1,2】
	print 'fruit:',fruits[index]



for num in range(10,20):
	for i in range(2,num):
		if num%i == 0:
			j=num/i
			print '%d = %d*%d' % (num,i,j)
			break	#跳出当前循环
	else:
		print num,'is zhishu'
		
	
print "====output 0-100 zhishu=========="

for num in range(2,100):
	for i in range(2,num):
		if num%i == 0:
			break
	else:
		print num

'''			
print "====***========"
num = int(raw_input('input a num:'))
for i in range (1,num):
	for k in range(1,i):
		print '*',
	print '\n'
	
	
	

print "====####========"
num = int(raw_input('input a num:'))
for i in range(2,num):
	for k in range(1,i):
		print k,
	print '\n'
'''


s = 'qazxswedcvfr'
for i in range(0,len(s),2):
    print s[i]
	
for (index,char) in enumerate(s):
    print "index=%s ,char=%s" % (index,char)
	

print "************break and continue************"	

for letter in 'python':
	if letter == 'h':
		break	#跳出整个循环，不继续往下执行循环
	print letter,   #输出pyt

print '\n'
	
for letter in 'python':
	if letter == 'h':
		continue	#跳出本次循环，即跳过本次循环的剩余语句，继续执行下一次循环
	print letter,  #输出pyton



print "\n************break and continue1************"	

var = 10
while var  > 0 :
	print var,
	var = var -1
	if var == 5 :
		break	#当var=5时，跳出整个循环，输出goodbye
print "good bye!"  #输出结果为109876goodbye!

print '\n'

var = 10
while var >0:
	print var,
	var = var -1
	if var ==5:
		continue	#当var=5时，跳出本次循环的剩余语句，继续执行下一次循环
print "good bye!"	#输出结果为 10987654321good bye!

var = 10                    
while var > 0:              
   var = var -1
   if var == 5:
      continue 	#当var=5时，跳出本次循环的剩余语句，继续执行下一次循环     
   print var, #输出结果为 987643210good bye!
print "Good bye!"


print "\n************pass************"	

for letter in 'Python':
   if letter == 'h':
      pass
      print 'pass'
   print letter,

print "Good bye!"


print "my name is %s and weight is %s kg" %('zara',21)
print "my name is %s and weight is %d kg" %('zara',21)


print "~~~~~~~~~~list test~~~~~~~~~~~"

list = []
list.append('lxc')
list.append('zj')
list.append('xyy')

print list 
del list[1]
print list
print list[-2]  #读取列表中倒数第二个元素


a=[1,2,3,4,5,6]
b=[7,8,9,10,0]
print cmp(a,b)
print len(a)
print max(a)
print min(a)
list.append('gk')
print list

a.extend(a)
print a
print a.count(1)  #统计1在a列表中出现了几次
print a.index(6)  #输出6这个元素在列表中的索引位置
a.insert(1,"lxc") #将lxc这个元素插入索引为1的位置
print a 
print a.pop(0)     #将索引位置为1的元素移除（不写索引时，默认删除最后一个元素），并且返回该元素的值
print a

a.remove(6)  #将括号中某个值得第一个匹配项移除
print a 
a.reverse()  #反向列表中元素
print a 
a.sort()	#对原列表进行排序
print a

c=[123,['aaa','bbb','ccc'],234,567]
print 'a' in c
print 'aaa' in c[1]
print c[1][2]
print c[:-2]  #表示从第一个元素遍历到倒数第3个元素


for i in c:
	if isinstance(i,type(c)):
		for j in i:
			print j
	else:
		print i

num_list = [[1,2,3],[4,5,6]]
for i in num_list:
	for j in i:
		print j,

print "~~~~~~~~~tuple test~~~~~~~~~~~"
#修改删除元组中的元素都是非法的
#tup1[0]=22
#del tup[0]

tup0=()
print tup0
tup00=(888,)	#当元组中只有一个元素的时候，需要在这个元素后面添加逗号
print tup00
tup1=(11,23.45)
tup2=('abc','eee','ddd')
print tup1+tup2
print len(tup1+tup2)
print tup00*4
print tup0 in tup2
print tup2[2]
print tup2[-2]
print tup2[-1:]

del tup2
#print tup2

h='aaa','bbb','ccc','eee'
g=(1,'ggg',15.03,('2',3.58))
print g

print len(h)

print("=========dictionary===========")

a={'name':'lxc','age':18,99:1314}
print a;
print a['age'];

#print a['hah']

a['age']=16
print a;
a[9.09]=99.99
print a;

del a[9.09]
print a;

a.clear()
print a;

#del a
print a;

b={'a':15,'b':30,'b':60,'b':90} #不允许同一个键被赋值两次，创建时，如果同一个键被赋值多次，最后一个值会被记住
print b;

#c={[1,2]:3,'a':15}
#print c;


dict = {'a':3,3:'a',(3,3):'lalala'}
#dict = {'a':3,3:'a',['a',3]:'lalala'}
print dict;
print len(dict);  #输出字典的长度
print str(dict);
print type(dict);
dict.clear();
print len(dict);



print '看不懂cmp()函数  ????????????'
dict1 = {'Name': 'Zara', 'Age': 7};
dict2 = {'Name': 'Mahnaz', 'Age': 27};
dict3 = {'Name': 'Abid', 'Age': 27};
dict4 = {'Name': 'Zara', 'Age': 7};
print "Return Value : %d" %  cmp (dict1, dict2)
print "Return Value : %d" %  cmp (dict2, dict3)
print "Return Value : %d" %  cmp (dict1, dict4)


print '============time==============';
import time;

a=time.time();
print a;

b=time.localtime(time.time());
print b;
print '**',time.localtime();

c=time.asctime(time.localtime(time.time()));
print c;

print time.strftime("%Y-%m-%d %H:%M:%S",time.localtime());
print time.strftime('%a %b %d %H:%M:%S %Y',time.localtime());
a='Thu Jun 07 14:10:33 2018'
print time.mktime(time.localtime());
print time.mktime(time.strptime(a,'%a %b %d %H:%M:%S %Y'));

print '==========calendar=========='

import calendar;

a = calendar.month(2018,6);
print a;

#print time.timezone;
#print time.tzname;

#a=calendar.calendar(year,w=2,l=1,c=6)
#print calendar.month(year,month,w=2,l=1);

print '=======函数========='
#定义函数
def printme(str):
	'打印任何传入的字符串'
	print str;
	return;
#调用函数
printme('hello');
#再次调用函数
printme('lalalla')
printme(str='hahahahah')

#不可变对象实例：整数、字符串、元祖
#实例中有int对象2，指向它的变量是b，
#在传递给changeint函数时，按传值的方式复制了变量b，
#a和b都指向了同一个int对象，在a=10时，则新生成一个int值对象10，并且让a指向它
def changeint(a):
	a=10

b=2
changeint(b)
print b

#可变对象实例：列表
#实例中传入函数的和在末尾添加新内容的对象时同一个引用
def changeme(mylist):
	"修改传入的列表"
	mylist.append([1,2,3,4])
	print "函数内取值",mylist
	return

#调用changeme函数
mylist = [10,20,30];
changeme(mylist)
print "函数外取值",mylist

#关键字参数：参数顺序不重要
def printinfo(name,age,color):
	print "name:",name
	print "age:",age
	print "color:",color
	return

printinfo(color='black',name='nike',age=15)
print  '**************'
#缺省参数：缺省参数的值如果没有传入，被认为是默认值

def printinfo(name,age,color='blue'):
	print "name:",name
	print "age:",age
	print "color:",color
	return

printinfo(color='black',name='nike',age=15)
printinfo(name='nike',age=15)

#不定长参数
def printinfo1(arg1,*andsoon):
	"打印任何传入的参数"
	print "输出："
	print  arg1
	for var in andsoon:
		print var
	return ;

printinfo1(10);
printinfo1(50,60,70,40);

#匿名参数
sum = lambda arg1,arg2:arg1+arg2;

print "相加后的值为 : ", sum( 10, 20 )
print "相加后的值为 : ", sum( 20, 20 )

def sum(arg1,arg2):
#返回两个参数的和
	total=arg2+arg1
	print "函数内：",total
	return total;

#调用sum函数
total = sum(10,20);

def sum(arg1,arg2):
#返回两个参数的和
	total=arg2+arg1
	print "函数内：",total
	return

#调用sum函数
total = sum(10,20);


total = 1;
def sum(arg1,arg2):
	total = arg1+arg2;
	print "函数内局部变量：",total;
	return

sum(10,20);
print "函数外全局变量：",total;

money = 2000
def addmoney():
	global  money;
	money = money + 1;

print money
addmoney();
print money;

import math;
content = dir(math)
print content;

#导入模块
import math;
#现在可以调用模块里包含的函数了
print math.acos(1);


from math import acos;
print acos(1)

#raw_input 和input 的区别
#input([prompt]) 函数和 raw_input([prompt]) 函数基本类似，
#但是 input 可以接收一个Python表达式作为输入，并将运算结果返回。
#str = raw_input("请输入：");
#print "输出结果是：",str;

#str1 = input("请输入：");
#print "输出结果是：",str1;
'''
请输入：[x*5 for x in range(2,10,2)]
输出结果是： [x*5 for x in range(2,10,2)]
请输入：[x*5 for x in range(2,10,2)]
输出结果是： [10, 20, 30, 40]
'''

print '+++++++++++文件+++++++++++++'

r = open("999.txt","r")
print  r.name
print  r.closed
print  r.mode
print  r.softspace
str = r.read()
print str

r = open("999.txt","w")
r.write("hello,world\nwww.runoob.com!\nVery good site!\n");
str = r.read()
print str
r.closed


r = open("999.txt","r+")
t = r.read();
print t;
r.closed









































