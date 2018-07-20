# __*__coding:utf-8__*__
#  Author:   benson

# coding=utf-8
'''
习题：
定义一个列表的操作类：Listinfo
包括的方法: 
1 列表元素添加: add_key(keyname)  [keyname:字符串或者整数类型]
2 列表元素取值：get_key(num) [num:整数类型]
3 列表合并：update_list(list)	  [list:列表类型]
4 删除并且返回最后一个元素：del_key() 

list_info = Listinfo([44,222,111,333,454,'sss','333'])
'''


class Listinfo(object):
    def __init__(self, arg1):
        self.arg1 = arg1

    def add_key(self, keyname):
        if not isinstance(keyname, int) and not isinstance(keyname, str):
            return "plz a str or num"
        self.arg1 = self.arg1.append(keyname)
        return self.arg1

    def get_key(self, Num):
        if not isinstance(Num, int):
            return "plz a num"
        if Num > len(self.arg1):
            return "num is out line"
        else:
            return self.arg1[Num]


list_info = Listinfo([44, 222, 111, 333, 454, 'sss', '333'])
print(list_info.add_key('safas'))

'''
定义一个集合的操作类：Setinfo

包括的方法: 

1 集合元素添加: add_setinfo(keyname)  [keyname:字符串或者整数类型]
2 集合的交集：get_intersection(unioninfo) [unioninfo :集合类型]
3 集合的并集： get_union(unioninfo)[unioninfo :集合类型]
4 集合的差集：del_difference(unioninfo) [unioninfo :集合类型]

set_info =  Setinfo(你要操作的集合)
'''

"""
进阶课 面向对象


1 习题讲解

2.class的基本定义

3.构造，析构函数

"""


class test(object):
    a = 1

    def func_1(self):
        return self.arg1, self.arg2

    def __init__(self, arg1, arg2):  ##构造函数
        self.arg1 = arg1
        self.arg2 = arg2

    def __del__(self):  ##析构函数
        del self.arg1
        del self.arg2

# a 被称为 test的 属性
# func_1  被称为 test的 方法
# 我们所有的class都是object的派生类

# t = test(1, 4)
# print(t.a)
# print
# t.func_1()
