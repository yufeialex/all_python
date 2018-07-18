#coding=utf-8
'''
今天习题：

1 字符串:
a = 'abcd'

用2个方法取出字母d

2：
a = 'jay'
b = 'python'
用字符串拼接的方法输出：
my name is jay,i love python.
'''

#1
a = "abcd"

print(a[len(a)-1])
print(a[-1])

#2

aa = "jay"
bb = "python"

print ("my name is %s, i love %s" % ('aa','bb'))
print ("my name is {name}, i love {love}" .format(name=aa,love=bb))   #推荐使用

