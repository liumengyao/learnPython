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
# #1、标记
# 通俗地讲就是：
# 栈区相当于“根”，凡是从根出发可以访达（直接或间接引用）的，都称之为“有根之人”，有根之人当活，无根之人当死。
# 具体地：标记的过程其实就是，遍历所有的GC Roots对象(栈区中的所有内容或者线程都可以作为GC Roots对象），然后将所有GC Roots的对象可以直接或间接访问到的对象标记为存活的对象，其余的均为非存活对象，应该被清除。
#
# #2、清除
# 清除的过程将遍历堆中所有的对象，将没有标记的对象全部清除掉。

# 3.分代回收
# 分代回收的核心思想是：在历经多次扫描的情况下，都没有被回收的变量，gc机制就会认为，该变量是常用变量，gc对其扫描的频率会降低，具体实现原理如下：
# 分代指的是根据存活时间来为变量划分不同等级（也就是不同的代）

# 新定义的变量，放到新生代这个等级中，假设每隔1分钟扫描新生代一次，如果发现变量依然被引用，那么该对象的权重（权重本质就是个整数）加一，
# 当变量的权重大于某个设定得值（假设为3），会将它移动到更高一级的青春代，青春代的gc扫描的频率低于新生代（扫描时间间隔更长），
# 假设5分钟扫描青春代一次，这样每次gc需要扫描的变量的总个数就变少了，节省了扫描的总时间，接下来，青春代中的对象，也会以同样的方式被移动到老年代中。
# 也就是等级（代）越高，被垃圾回收机制扫描的频率越低