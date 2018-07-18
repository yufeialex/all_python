# coding=utf-8

# 一.已经字符串 s = "i,am,lilei",请用两种办法取出之间的“am”字符。
print("第一题--------------")
s = "i,am,lilei"
print(s.split(",")[1])
print(s[2:4])
print(s.format("am"))

print("第二题--------------")
# 二.在python中，如何修改字符串？
# 使用字符串的replace方法
a = "i love php"
c = a.replace("php", "python")
print(c)

# 三.bool("2012" == 2012) 的结果是什么。
print("第三题------------------")
print(bool("2012" == 2012))

'''
四.已知一个文件 test.txt，内容如下：
____________
2012来了。
2012不是世界末日。
2012欢乐多。
___________
1.请输出其内容。
2.请计算该文本的原始长度。
3.请去除该文本的换行。
4.请替换其中的字符"2012"为"2013"。
5.请取出最中间的长度为5的子串。
6.请取出最后2个字符。
7.请从字符串的最初开始，截断该字符串，使其长度为11.
8.请将{4}中的字符串保存为test1.py文本.
'''
print("4.1--------------")
b = open("test.txt", "r",encoding="utf-8")
f = b.read()
print(f)

print("4.2--------------")
print(len(f))

print("4.3--------------")
print(f.replace("\n",""))

print("4.4--------------")
print(f.replace("2012","2013"))

print("4.5--------------")
print (f[len(f)//2:len(f)//2+5])

print("4.6--------------")
print(f[len(f)-2:])
print(f[-2:])

print("4.7--------------")
print(f[:11])

print("4.8--------------")
f2 = f.replace("2012","2013")
test1 = open("test1.py","w")
test1.write(f2)
test1.close()

'''
五.请用代码的形式描述python的引用机制。
'''
import sys
print("``````五`````````````")
aa = "love1"
print(id(aa))
print(sys.getrefcount("love1"))         #python 引用计数是从3开始 3+1

bb = "love1"
print(id(bb))
print(sys.getrefcount("love1"))       #3 + 1 + 1


'''
六.已知如下代码
________
a = "中文编程"
b = a
c = a
a = "python编程"
b = u'%s' %a
d = "中文编程"
e = a
c = b
b2 = a.replace("中","中")
________
1.请给出str对象"中文编程"的引用计数
2.请给出str对象"python编程"的引用计数
'''
print("````````````````六```````````````")
china = "中文编程"
print(sys.getrefcount("中文编程"))


'''

七.已知如下变量
_______
a = "字符串拼接1"
b = "字符串拼接2"
________
1.请用四种以上的方式将a与b拼接成字符串c。并指出每一种方法的优劣。
2.请将a与b拼接成字符串c，并用逗号分隔。
3.请计算出新拼接出来的字符串长度，并取出其中的第七个字符。
'''
print("7.1-------------------")
a = "字符串拼接1"
b = "字符串拼接2"
#方法1      (劣势：当有多个字符串拼接时会产生多个中间变量)
c = a + b
print(c)

#方法二     （劣势：变量顺序有关系）
c = "%s%s" % (a,b)
print(c)

#方法三
c = ("{a}{b}" .format(a=a,b=b))
print(c)

#方法四    (优点：只需申请一次内存空间)
c = "" .join([a,b])
print(c)

print("7.2-------------------")
#方法一
c = "%s,%s" % (a,b)
print(c)

#方法二
c = "," .join([a,b])
print(c)

print("7.3--------------")
lennum = len(c)
print(lennum)
print(c[6])

'''
八.请阅读string模块，并且，根据string模块的内置方法输出如下几题的答案。
1.包含0-9的数字。
2.所有小写字母。
3.所有标点符号。
4.所有大写字母和小写字母。
5.请使用你认为最好的办法将{1}-{4}点中的字符串拼接成一个字符串。
'''
print("8.1--------------")
import string
#help(string)
print(string.digits)

print("8.2--------------")
print(string.ascii_lowercase)

print("8.3--------------")
print(string.punctuation)

print("8.4--------------")
print(string.ascii_uppercase)

print("8.5--------------")
strinfo = []
strinfo.append(string.digits)
strinfo.append(string.ascii_lowercase)
strinfo.append(string.punctuation)
strinfo.append(string.ascii_uppercase)
print("" .join(strinfo))

'''
九.已知字符串
________
a = "i,am,a,boy,in,china"
_______
1.假设boy和china是随时可能变换的，例boy可能改成girl或者gay，而china可能会改成别的国家，你会如何将上面的字符串，变为可配置的。
2.请使用2种办法取出其间的字符"boy"和"china"。
3.请找出第一个"i"出现的位置。
4.请找出"china"中的"i"字符在字符串a中的位置。
5.请计算该字符串一共有几个逗号。
'''
print("9.1--------------")
a = "i,am,a,boy,in,china"
aa = "i,am,a,%(sex)s, in, %(country)s" %{'sex':'girl','country':'china'}
print(aa)

print("9.2--------------")
#1
print(aa.split(',')[3])
print(aa[7:11])

print("9.3--------------")
print(a.find('i'))      #当‘i’ 不存在返回-1
print(a.index('i'))     #当‘i'不存在是报异常

print("9.4--------------")
print(a.find('i',a.find('china')))
print(a.rfind('i'))

print("9.4--------------")
print(a.count(','))

'''
十.请将模块string的帮助文档保存为一个文件。
'''
import string
f = open('string_help.txt','w')
sys.stdout = f
help(string)
f.close()