# -*- coding: utf-8 -*-
# @Time : 2021/4/12 10:01
# @Author : Pactera
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

