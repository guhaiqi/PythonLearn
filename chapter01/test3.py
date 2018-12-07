# -*- coding: UTF-8 -*-
# 条件语句
print "条件语句"
var1 = True
if var1:
    print "var1 is true"
else:
    print "var1 is false"

var2 = 23
if var2 > 100:
    print "var2 > 100"
elif var2 > 20:
    print "var2 > 20"
else:
    print "var2 <= 20"
    

# 循环语句
# 1 while
# 1
count = 0
while count < 8:
    print "count is ", count
    count += 1

# 2
count = 0
while True:
    if count > 10:
        break
    count += 2
    print "count is ", count

# 3 使用else
count = 0
while(count < 5):
    print "count is less than 5", count
    count += 1
else:
    print "count is more than 4", count

# 2 for
# 1
for letter in "python":
    print letter
fruits = ["banana", "apple", "mango"]
for fruit in fruits:
    print fruit

# 2
fruits = ["banana", "apple", "mango"]
for index in range(len(fruits)):
    print index, fruits[index]

# 3
for num in range(10,20):  # 迭代 10 到 20 之间的数字
   for i in range(2,num): # 根据因子迭代
      if num%i == 0:      # 确定第一个因子
         j=num/i          # 计算第二个因子
         print num, "=", i, " * ", j
         break            # 跳出当前循环
   else:                  # 循环的 else 部分
      print num, '是一个质数'
    
