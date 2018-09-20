from ram

try:
    open("abc.txt",'r')
except FileNotFoundError:
    print('异常！')


try:
	print (aa);
except BaseException as msg:
	print(msg);
else:
	print("???");

try:
	print(a);
except BaseException as msg:
	print(msg);
finally:
	print('haha');

try:
      a='lalal'
      print(a);
except BaseException as msg:
	print(msg);
finally:
	print('haha');

	
