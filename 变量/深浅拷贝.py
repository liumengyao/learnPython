# -*- coding: utf-8 -*-
# @Time : 2021/4/19 16:03
# @Author : Pactera
# @Email : wayne_lau@aliyun.com
# @File : 深浅拷贝.py
# @time:2021/04/19
# @Project : learnPython
import  copy
'''
l1=l2 l1和l2指向同一块内存空间 不属于拷贝
浅拷贝：把原列表第一层的内内存地址完全拷贝一份，若列表中的值全部为不可变类型，则浅拷贝可以把两个列表完全区分开，若列表中存在容器(可变)类型，则两个列表会粘到一起
       list1=list2.copy()
       list1 和list2 的id不同，但是内部每个元素指向同一块内存地址
深拷贝：把列表中的值加以区分，深拷贝就是可变类型的拷贝和不可变类型的拷贝区分开
深拷贝总结：针对不可变类型，用原来的地址，针对容器类型，造一个新的瓶子，瓶子中的东西还是指向原来的

'''
print("=================浅拷贝=================")
list1 = ['anna', 'lmy', ['1', '2']]
# print(list1)
#浅拷贝：list1和list2指向的id虽然不同，但是列表中的每个元素还是指向了同一块内存地址，因此，一个列表改变，另一个列表不会变
list2 = list1.copy()
print(list1, list2)
print(id(list1), id(list2))
print(id(list1[0]), id(list1[1]), id(list1[2]))
print(id(list2[0]), id(list2[1]), id(list2[2]))

print("-----------改变列表中不可变类型元素，另一个不受影响-----------")
list1[0] = 'ANNA'
print(list1, list2)
print(id(list1), id(list2))
print(id(list1[0]), id(list1[1]), id(list1[2]))
print(id(list2[0]), id(list2[1]), id(list2[2]))

print("-----------改变列表中可变类型元素，另一个列表也会改变-----------")
list1[2][0] = '111'
list1[2][1] = '222'
print(list1, list2)
print(id(list1), id(list2))
print(id(list1[0]), id(list1[1]), id(list1[2]), id(list1[2]), id(list1[2][0]))
print(id(list2[0]), id(list2[1]), id(list2[2]), id(list2[2]), id(list2[2][0]))

print("=================深拷贝=================")
list3 = ['anna', 'lmy', ['1', '2']]
list4 = copy.deepcopy(list3)
print(list3, list4)
print(id(list3), id(list4))
print(id(list3[0]), id(list3[1]), id(list3[2]), id(list3[2][0]))
print(id(list4[0]), id(list4[1]), id(list4[2]), id(list4[2][0]))


'''
深浅拷贝总结：
          深拷贝：对可变类型加以区分，可变类型会拷贝一份，深拷贝会每层都拷贝，底层区别就是：深拷贝对可变类型加以区分了
          浅拷贝：对可变类型的不区分，浅拷贝只拷贝一层，
'''