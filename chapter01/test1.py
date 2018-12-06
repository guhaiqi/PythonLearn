# -*- coding: UTF-8 -*-
# -*- coding: UTF-8 -*-

# 变量类型
counter = 100   # 整型
miles = 1000.5  # 浮点型
name = "Tom"    # 字符串

print counter
print miles
print name

# 列表
"""
列表可以完成大多数集合类的数据结构实现。它支持字符，数字，字符串甚至可以包含列表（即嵌套）。
列表用 [ ] 标识，是 python 最通用的复合数据类型。
列表中值的切割也可以用到变量 [头下标:尾下标] ，就可以截取相应的列表，从左到右索引默认 0 开始，从右到左索引默认 -1 开始，下标可以为空表示取到头或尾。
加号 + 是列表连接运算符，星号 * 是重复操作
"""
list1 = [2.34, 50, "Tom", 10001]
list2 = [100, 101, 102]
print "LIST"
print list1             # 输出完整列表
print list1[0]          # 输出列表的第一个元素
print list1[-1]         # 输出列表的最后一个元素
print list1[1:3]        # 输出第二个至第三个元素
print list1[2:]         # 输出从第三个开始至列表末尾的所有元素
print list1[-3:]        # 输出从倒数第三个开始至列表末尾的所有元素
print list1 * 2         # 输出列表两次
print list1 + list2     # 打印组合的列表

# 元组
'''
元组是另一个数据类型，类似于List（列表）
元组用"()"标识。内部元素用逗号隔开,但是元组不能二次赋值，相当于只读列表
'''
tuple1 = (1, "Tom", 2, "Hello", 20.2)
tuple2 = ("ONE", "TWO", "THREE")
print "TUPLE"
print tuple1
print tuple1[0]
print tuple1[1:3]
print tuple1[2:]
print tuple1 * 2
print tuple1 + tuple2
# 下面的操作是不允许的
#tuple1[0] = 53


# 字典
'''
列表是有序的对象集合，字典是无序的对象集合
两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取
字典用"{ }"标识。字典由索引(key)和它对应的值value组成
'''
dict1 = {"name":"Tom", "sex":1, 'age':22}
dict2 = {}
dict2['pos'] = 200
print "DICTIONARY"
print dict1             # 输出完整的字典
print dict1['name']     # 输出键为'one' 的值
print dict1.keys()      # 输出所有键
print dict1.values()    # 输出所有值
print dict2['pos']

# 数据类型转换
'''
int(x)
float(x)
str(x)
'''
var1 = "123"
var2 = 23.9
print int(var1)
print int(var2)
print float(var1)
print str(var2)


