# -*- coding: utf-8 -*-
# @Time : 2021/4/12 10:01
# @Author : Anna
# @Email : wayne_lau@aliyun.com
# @File : 变量.py
# @time:2021/04/12
# @Project : basePython
'''
变量：先定义后引用
'''
name = 'anna' #定义
print(name) #引用
# 内存管理
# 垃圾：当一个变量值被绑定的变量名的个数为0时，该变量无法被访问到，称为垃圾
# 引用计数增加
x = 10
y = x #y也指向x的内存地址
z = x
# 引用计数的减少
del x #解除x与10的绑定关系  10的引用计数变为2
del y #10的引用计数变为1
z = 12345 #z指向12345在的内存地址，10此时变成了垃圾

# 变量值的三个重要特征：id type value
# id：反应的是变量值的内存地址（根据内存地址计算的一串号码），变量值的内存地址不同id则不同
print(id(name))
# type：不同类型的值用来表示记录不同的状态
print(type(name))
# value：变量的值
print(name)

#is ==
# is：比较左右两个变量值身份id是否相同
# ==：比较左右两个变量的值是否相同
# x is y 成立则 x == y一定成立
x = 'anne'
y = 'anne'
print(x is y) #false

# 小整数池概念


# 基本数据类型：int float str bool list dict
#list



