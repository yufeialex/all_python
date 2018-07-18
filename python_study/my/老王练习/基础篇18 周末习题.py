#coding=utf-8
'''
1.
已知字符串
a = "aAsmr3idd4bgs7Dlsf9eAF", 要求如下
1.1
请将a字符串的大写改为小写，小写改为大写。
'''
a = "aAsmr3idd4bgs7Dlsf9eAF"
print(a.swapcase())

'''
1.2
请将a字符串的数字取出，并输出成一个新的字符串。
'''
b = [s for s in a if s.isdigit()]
print(''.join(b))

'''
1.3
请统计a字符串出现的每个字母的出现次数（忽略大小写，a与A是同一个字母），并输出成一个字典。 例
{'a': 4, 'b': 2}
'''
a = a.lower()
print(dict([(x,a.count(x)) for x in set(a)]))
#
#[(x,a.count(x)) for x in set(a)]

'''
1.4
请去除a字符串多次出现的字母，仅留最先出现的一个。例
'abcabb'，经过去除后，输出'abc'
'''
print("=========1.4")
a = "aAsmr3idd4bgs7Dlsf9eAF"
a_list = list(a)
set_list = list(set(a_list))
set_list.sort(key=a_list.index)
print(''.join(set_list))
#print(a_list)

'''
1.5
请将a字符串反转并输出。例：'abc'
的反转是
'cba'
'''
print("++++++++++++++1.5")
a = "aAsmr3idd4bgs7Dlsf9eAF"
list_a = list(a)
#set_a = list(set(list_a))
list_a.reverse()
print(''.join(list_a))

a = "aAsmr3idd4bgs7Dlsf9eAF"
print(a[::-1])

'''
1.6
去除a字符串内的数字后，请将该字符串里的单词重新排序（a - z），并且重新输出一个排序后的字符
串。（保留大小写, a与A的顺序关系为：A在a前面。例：AaBb）
'''
print("+++++++++++1.6")
a = "aAsmr3idd4bgs7Dlsf9eAFHH"
#b = [s for s in a if s.islower()]
#c = [s for s in a if s.isupper()]
b = sorted(a)
upper_list = []
lower_list = []
for x in b:
    if x.isupper():
        upper_list.append(x)
    elif x.islower():
        lower_list.append(x)
    else:
        pass

for y in upper_list:
    y_lower = y.lower()
    if y_lower in lower_list:
        lower_list.insert(lower_list.index(y_lower),y)
        print(lower_list.index(y_lower))

print(upper_list)
print(''.join(lower_list))

'''
1.7
请判断
'boy'里出现的每一个字母，是否都出现在a字符串里。如果出现，则输出True，否则，则输出False.
'''
print("++++++++++1.7")
a = "aAsmr3idd4bgs7Dlsf9eAFoyHH"

for i in "boari34bgsy":
    if i in a:
        continue
    else:
        break
else:
    print("Ture")
'''
1.8
要求如1.7，此时的单词判断，由'boy'改为四个，分别是'boy', 'girl', 'bird', 'dirty'，请判断如上这4个字符串里的每个字母，是否都出现在a字符串里。
'''
print("+++++++++++++++1.8")
a = "aAsmr3idd4bgs7Dlsf9eAFoyHH"
find = ['boy','girl','bird','dirty']
find_set = set(''.join(find))
b = set(a)
u = len(b)

for i in find_set:
    b.update(i)

if u == len(b):
    print("Ture")
else:
    print("none")

#print(find_set)

'''
1.9
输出a字符串出现频率最高的字母

'''
print("++++++++++1.9")
a = "aAsmr3idd4bgs7Dlsf9eAFoyHH"
b = [(x,a.count(x))for x in a]
b.sort(key=lambda k:k[1],reverse=True)
print(b[0][0])

'''
2.
在python命令行里，输入import this以后出现的文档，统计该文档中，"be" "is" "than"的出现次数。
'''
print("+++++++++++2.0")
import os
m = os.popen('python -m this').read()
m = m.replace('\n','')
m = m.split(' ')
print([(x,m.count(x)) for x in ['be','is','than']])


'''
3.
一文件的字节数为
102324123499123，请计算该文件按照kb与mb计算得到的大小。

'''
print("+++++++++3.0")
b = 102324123499123
print("%s kb" % (b >> 10))
print("%s mb" % (b >> 20))

'''
4.
已知
a = [1, 2, 3, 6, 8, 9, 10, 14, 17], 请将该list转换为字符串，例如
'123689101417'.
'''
print("++++++++++++++4.0")
a = [1, 2, 3, 6, 8, 9, 10, 14, 17]

print(str(a)[1:-1].replace(', ',''))