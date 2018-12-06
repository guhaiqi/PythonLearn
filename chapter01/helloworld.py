# -*- coding: UTF-8 -*-
'''
Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

解决方法为只要在文件开头加入 # -*- coding: UTF-8 -*- 或者 #coding=utf-8 就行了
'''

# 输出
print "Hello World"

print("Hello World")

print "Hello", "World"

# + 是连接符
print "Hello" + " World"

print("Hello" + " World")

# print 默认输出是换行的，如果要实现不换行需要在变量末尾加上逗号 ,
x="a"
y="b"
# 换行输出
print x
print y

print '---------'
# 不换行输出
print x,
print y,

# 不换行输出
print x,y
