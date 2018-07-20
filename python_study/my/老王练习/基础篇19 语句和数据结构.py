# coding = utf-8
# 今天习题：

'''
1.用小于5行的代码解决周末习题中的1.6题。
1.6  a = "aAsmr3idd4bgs7Dlsf9eAF"
去除a字符串内的数字后，请将该字符串里的单词重新排序（a - z），并且重新输出一个排序后的字符
串。（保留大小写, a与A的顺序关系为：A在a前面。例：AaBb）
'''
print("++++++++++1")
import string

# import str
a = "aAsmr3idd4bgs7Dlsf9eAF"
a = ''.join([x for x in a if not x.isdigit()])
# print(sorted(a,key=string.ascii_uppercase))

'''
2. 已知字典：
ainfo = {'b':'python','a':'haha','c':'hehe','f':'xiaoming'}
2.1 迭代字典，输出结果：
('a', 'haha')
('c', 'hehe')
('b', 'python')
('f', 'xiaoming')
'''
ainfo = {'b': 'python', 'a': 'haha', 'c': 'hehe', 'f': 'xiaoming'}

for i in ainfo.keys():
    print(i)

list_a = []
for x, y in ainfo.items():
    list_a.append((x, y))
for x in sorted(list_a, key=lambda k: k[1]):
    print(x)
# print([(x,y) for  in ainfo.keys() ])


'''
2.2 用2种方法输出结果：ainfo = {'b':'python','a':'haha','c':'hehe','f':'xiaoming'}
a
c
b
f
'''
print("+++++++++++++++2.2.1")
ainfo = {'b': 'python', 'a': 'haha', 'c': 'hehe', 'f': 'xiaoming'}
for x in ainfo.keys():
    print(x)
print("++++++++++2.2.2")
a = sorted(ainfo.keys())
for x in a[::2]:
    print(x)

'''
2.3 写出查找字典里面值等于'haha'的key的代码

'''
print("++++++++2.3")
ainfo = {'b': 'python', 'a': 'haha', 'c': 'hehe', 'f': 'xiaoming'}
search_value = 'haha'
key_list = []
for x, y in ainfo.items():
    if y == search_value:
        key_list.append(x)
print(key_list)
