# -*- coding: UTF-8 -*-

# 算术运算符
print "算术运算符"
a = 23
b = 8
c = 0

c = a + b
print "1 result c is ", c

c = a - b
print "2 result c is ", c

c = a * b
print "3 result c is ", c

#注意：Python2.x 里，整数除整数，只能得出整数。如果要得到小数部分，把其中一个数改成浮点数即可
c = a / b
print "4 result c is ", c

c = a % b
print "5 result c is ", c

# x**y 幂 - 返回x的y次幂
c = a ** b
print "6 result c is ", c

# x//b 取整除 - 返回商的整数部分（向下取整）
c = a // b
print "7 result c is ", c

# 此外还有 “+=”，“-=”，“*=”，“/=”


# 比较运算符
print "比较运算符"

a = 23
b = 8
c = 0

print "a == b ", a == b
print "a != b ", a != b
print "a > b ", a > b
print "a < b ", a < b
print "a >= b ", a >= b
print "a <= b ", a <= b
# <> 不等于 - 比较两个对象是否不相等
print "a <> b ", a <> b


# 赋值运算符
print "赋值运算符"
'''
=	简单的赋值运算符	c = a + b 将 a + b 的运算结果赋值为 c
+=	加法赋值运算符	        c += a 等效于 c = c + a
-=	减法赋值运算符	        c -= a 等效于 c = c - a
*=	乘法赋值运算符	        c *= a 等效于 c = c * a
/=	除法赋值运算符	        c /= a 等效于 c = c / a
%=	取模赋值运算符	        c %= a 等效于 c = c % a
**=	幂赋值运算符	        c **= a 等效于 c = c ** a
//=	取整除赋值运算符	c //= a 等效于 c = c // a
'''

# 位运算符
print "位运算符"
a = 60            # 60 = 0011 1100
b = 13            # 13 = 0000 1101
c = 0
 
c = a & b;        # 12 = 0000 1100
print "1 - c 的值为：", c
 
c = a | b;        # 61 = 0011 1101
print "2 - c 的值为：", c
 
c = a ^ b;        # 49 = 0011 0001
print "3 - c 的值为：", c
 
c = ~a;           # -61 = 1100 0011
print "4 - c 的值为：", c
 
c = a << 2;       # 240 = 1111 0000
print "5 - c 的值为：", c
 
c = a >> 2;       # 15 = 0000 1111
print "6 - c 的值为：", c


# 逻辑运算符
print "逻辑运算符"

a = 23
b = 8
print "a and b is ", a and b
print "a or b is ", a or b
print "not a is ", not a


# 成员运算符
print "成员运算符"
a = 23
b = 8
list1 = [2, 4, 6, 8]
print "a in list1 ", a in list1
print "b in list1 ", b in list1
print "a not in list1 ", a not in list1
print "b not in list1 ", b not in list1


# 身份运算符
print "身份运算符"
a = 23
b = 23
print "a is b ", a is b
print "a is not b ", a is not b
a = [1, 2]
b = [1, 2]
c = a
print "a is b ", a is b
print "c is a ", c is a
# is 与 == 区别：is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等



