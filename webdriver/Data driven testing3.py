from xml.dom import minidom

'''读取xml文件'''
#打开xml文档
dom = minidom.parse('info.xml') #parse用户打开XMl文件

#得到文档元素对象
root = dom.documentElement  #documentElement用于得到XML文件唯一的根元素


#获得标签信息
print(root.nodeName) #输出节点名称
print(root.nodeValue)   #输出节点的值，这个nodeName只对文本节点有效
print(root.nodeType)    #为节点的类型
print(root.ELEMENT_NODE)  #我也不知道是啥？？？

#获得任意标签名
tagname = root.getElementsByTagName('browser')
print(tagname)
print(tagname[0].tagName)

print("=========================")
tagname0 = root.getElementsByTagName('login') #获取login标签中第二个标签
print(tagname0[1])
print(tagname0[1].tagName)
print("=========================")

tagname1 = root.getElementsByTagName('province') #获取province标签中的第三个标签
print(tagname1[2])
print(tagname1[2].tagName)

#获得标签的属性值
print(tagname0[0].getAttribute('username'))  #getAttribute()方法用于获取元素的属性值
print(tagname0[1].getAttribute('password'))

#获得标签对之间的数据
provinces = root.getElementsByTagName('province')
citys = root.getElementsByTagName('city')

for p in provinces:
    print(p.firstChild.data)  #firstChild属性返回被选节点的第一个子节点 ，data表示获取该节点的数据

print("****************")

for c in citys:
    print(c.firstChild.data)



