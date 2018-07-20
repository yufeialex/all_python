# coding=utf-8

'''
今天习题：
习题一：
1 用while语句的2种方法输出数字：1到10
2 用for语句和continue 输出结果：1 3 5 7 9
'''
# 方法一
x = 0
while True:
    x += 1
    if x > 10:
        break
    else:
        print(x)

# 方法二
y = 0
while y < 11:
    y += 1
    print(y),

else:
    print("end")

x = 0
for x in range(1, 10):
    if x % 2 == 1:
        print(x),
    else:
        continue

'''
习题二：假设有列表
a = [1,2,3,4,5,6]
1 用for if else 的方法查找数字8是否在列表a里，如果在的话，输出字符串'find'，如果不存在的话，
输出字符串'not find'
2 用while语句操作上面的列表a，输出下面结果：
[2,3,4,5,6,7]
'''
a = [1, 2, 3, 4, 5, 6]
for i in a:
    if i == 8:
        print("find"),

else:
    print("not find")

i = 0
while i < a.__len__():
    a[i] += 1
    #    print(a[i])
    i += 1
print(a)
