# -*- coding: utf-8 -*-
# @Time : 2021/4/13 15:53
# @Author : Anna
# @Email : 734666093@qq.com
# @File : 用户交互.py
# @time:2021/04/13
# @Project : learnPython
#
# # input(),input()会将用户输入的所有类型都保存为字符串类型
# name = input("please input your name:")
# print(name)
# age = input("please input your age:")
# print(type(age))
# age = int(age) #int只能将纯数字的字符串转换为整型
# # pyhon2 中raw_input()与python3的input()用法一模一样
# # python2中的input()要求用户必须输入一个明确的数据类型，输入的是什么类型就存成什么类型


# 格式化输出
# 按照位置传值，一一对应，%d只能接收int，%s能接收任何类型
print("My name is:%s,age is:%s"%('anna',18))
# 传输字典
print("My name is:%(name)s,age is:%(age)s"%{'name':'anna', 'age' : 18})

# 2.2 str.fotmat()
res = "My name is:{},age is:{}".format('anna',18)
print(res)
res = "My name is:{0}{0},age is:{1}{1}".format('anna',18)
print(res)

# 打破位置的限制：使用key=value的方式传值
res = "My name is:{name},age is:{age}".format(name='anna',age=18)
print(res)

# 2.3 f:python3.5以后退出  速度：f>format>%s
name = input("your name:")
age = int(input("your age:"))
res = f"My name is:{name},age is:{age}"
print(res)
