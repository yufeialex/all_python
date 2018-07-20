# coding = utf-8
'''
今天习题：
1 写一个函数代码，返回这3个数字中最大的一个。
a = 123
b = 345
c = 444
'''


def MAX(a, b, c):
    list_l = [a, b, c]
    max_num = max(list_l)
    return max_num


print(MAX(123, 345, 444))

'''
2 分别写2个函数，完成下面的功能：

提示一下用到函数的：**和*，猩猩是字典，星是元组

2.1 调用函数：ainfo(x=88,y=22,z=44) 你定义ainfo函数体里面的内容并且返回结果： 

[22, 44, 88]

2.2 调用函数：cinfo(x=88,y=22,z=44) 你定义cinfo函数体里面的内容并且返回结果：

('xaay','yaay','zaay')

'''


def ainfo(**kr):
    return sorted(list(kr.values()))


print(ainfo(x=88, y=22, z=44))


def cinfo(**kr):
    a = tuple(['%saay' % x for x in kr.keys()])
    return a


print(cinfo(x=88, y=22, z=44))
