import time
import string

# print(time.time())
# print("hello wold")
#
# a="adf sd    "
# b="iiiii"
# c=1
# print(str.__add__(a,b))
# #print(str.__rmod__(a,b))
# print(str.__sizeof__(a))
#
# d="    python是动态语言   "
# e=" "
# f="ADADSF"
# g="aadfDA"
# print(str.capitalize(a))
# print(str.casefold(a))
# print(str.encode(a))
# #print(str.find("a"))
# print(a.islower())
# print(b.isnumeric())
# print(e.isspace())
# print(d.ljust(0))
# print(f.lower())
# print(g.rstrip(d))
# print(b.upper())
# print(d.replace("p","pp"))
#
# print(str.__len__(d))
# h=u"哈哈哈"
# print (h)
# print(str.__len__(h))
# print(a[2])
# print (f[len(f)-1])
# print(f[-1])
# print ("my name is %s,and i am %d old" %("wqb",24))
# print(str.join(",",[f,g,h]))
#
# FILE=open("test.txt","w")
# FILE.write("ni hao\nmy name is")
# FILE.close()

#格式化
a="my name is %s and i am %d year old" % ("wqb",24)

b="my name is {1} and i am {0} year old" .format("wqb","24")

c="my name is {name} and i am {age} year old" .format(name="wqb",age=24)    #推荐使用

d="my name is %(name)s and i am %(age)d year old" % {"name":"wqb","age":24}  #字典

print(a)
print(b)
print(c)
print(d)

import string
help(string)

