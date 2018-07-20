# coding=utf-8
'''
今天习题：

一 元组；a = (1,2,3)

1 有2种方法输出实现下面的结果：

(5,2,3)
2 判断2是否在元组里
'''
print("1----------------")
a = (1, 2, 3)
print("方法一")
b = list(a)
b[0] = 5
print(tuple(b))

print("方法二")
c = set(a)
c.remove(1)
c.add(5)
print(tuple(c))

print("2----------------")
print(2 in set(a))

'''
二 集合a = set(['a','b','c'])做下面的操作：

1 添加字符串'jay'到集合a里。

2 集合b = set(['b','e','f','g']) 用2种方法求集合a 和集合b的并集。

'''
print("2.1----------")
a = set(['a', 'b', 'c'])
a.add('jay')
print(a)

print("2.2----------")
print("方法一")
b = set(['b', 'e', 'f', 'g'])
print(a | b)

print("方法二")
c = list(a) + list(b)
print(set(c))
