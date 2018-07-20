# coding=utf-8
'''
今天习题
1：
a = 'pyer'
b = 'apple'

用字典和format方法实现：
my name is pyer, i love apple.

2:打开文件info.txt,并且写入500这个数字。

'''
a = "pyer"
b = "apple"

print("my name is {name},i love {love}".format(name=a, love=b))
print("my,name is %(name)s, i love %(love)s" % {"name": a, "love": b})

# 2
file = open("info.txt", "w")
file.write("500\n")
file.close()
