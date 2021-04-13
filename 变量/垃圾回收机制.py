# -*- coding: utf-8 -*-
# @Time : 2021/4/12 14:35
# @Author : Anna
# @Email : wayne_lau@aliyun.com
# @File : 垃圾回收机制.py
# @time:2021/04/12
# @Project : learnPython
# 理解GC需要储备的知识
# 堆区与栈区：
#           变量名和变量值内存地址的关联关系存放于栈区
#           变量值存放于堆区，内存管理回收的则是堆区的内容

# 1.引用计数
# 直接引用和间接引用，间接引用主要针对容器类型的变量
# 列表在内存中的存储方式:为间接引用
# 循环引用导致内存泄漏
x = 10
l = [x,5]
print(id(x))
print(id(l[0]))

m = 18
del m #接触m和18的绑定关系
l1 = [111]
l2 = [222]
l1.append(l2) #l1=[111的内存地址,l2的内存地址]
l2.append(l1) #l2=[222的内存地址,l2的内存地址]

print(id(l1[1])) #l1[1]、l2的id相同
print(id(l2))
print(id(l2[1])) #l2[1]、l1的id相同
print(id(l1))
# 获取l1、l2的方式有两种：l1或者l2[1]都可以获取到l1的地址
# del l1
# del l2后，l1，l2无法被使用，但是l1，l2中的引用计数不为0，造成了内存泄漏

# 2.标记清除

# 3.分代回收
