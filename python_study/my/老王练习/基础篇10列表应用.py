# coding=utf-8

'''
今天习题：

一: 已知：元组 a = (1,2,3) 利用list方法，输出下面的结果：

(1,2,4)

'''
a = (1, 2, 3)
b = list(a)
b[-1] = 4
print(tuple(b))

'''
二: 利用列表推导完成下面习题：

1 输出结果：[1 love python,2 love python,3 love python,.... 10 love python]

2 输出结果：[(0,0),(0,2),(2,0),(2,2)]

'''
print(["%s love python" % i for i in range(1, 10)])
print([(x, y) for x in range(0, 3, 2) for y in range(0, 3, 2)])

'''
三：

a = [1,2,3]

b = a[:]

del a

b的值是什么。为什么呢？
'''
a = [1, 2, 3]
b = a[:]
del a
print(b)
