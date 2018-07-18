# __*__coding:utf-8__*__
#  Author:   benson

#coding=utf-8

'''
1.定义一个func(name)，该函数效果如下。
assert func("lilei") = "Lilei"
assert func("hanmeimei") = "Hanmeimei"
assert func("Hanmeimei") = "Hanmeimei"
'''

def capstr(name):
    return name.capitalize()
print(capstr('adfad'))

"""
2.定义一个func(name,callback=None),效果如下。
assert func("lilei") == "Lilei"
assert func("LILEI",callback=string.lower) == "lilei"
assert func("lilei",callback=string.upper) == "LILEI"

"""
import string
def func2(name,callback=None):
    if isinstance(name,str):
        if callback == None:
            return name.capitalize()
        else:
            return callback(name)
    else:
        return "nothing to do"

#print(func2('asdfAAs',callback=string.ascii_uppercase))

"""
3.定义一个func(*kargs),效果如下。

l = func(1,2,3,4,5)
for i in l:
	print i,
#输出 1 2 3 4 5

l = func(5,3,4,5,6)
for i in l:
	print i
#输出 5 3 4 5 6
"""


"""
4.定义一个func(*kargs)，该函数效果如下。

assert func(222,1111,'xixi','hahahah') == "xixi"
assert func(7,'name','dasere') == 'name'
assert func(1,2,3,4) == None
"""
def func3(*kargs):

    str_list = [i for i in kargs if isinstance(i, str)]
    str_len = [len(x) for x in str_list]
    if str_len:
        min_str = min(str_len)
        return str_list[str_len.index(min_str)]
    else:
        pass
    return None

#print(func3(222,1111,'adf','dsadf'))
assert func3(222,1111,'xixi','hahahah') == "xixi"
assert func3(7,'name','dasere') == 'name'
assert func3(1,2,3,4) == None
"""
5.定义一个func(name=None,**kargs),该函数效果如下。

assert func(“lilei”) == "lilei"
assert func("lilei",years=4) == "lilei,years:4"
assert func("lilei",years=10,body_weight=20) == "lilei,years:4,body_weight:20"

"""
def func4(name=None,**kwargs):
    data = []
    for x, y in kwargs.items():
        data.extend([',', str(x), ':', str(y)])
    info = ''.join(data)
    return '%s%s' % (name,info)
print(func4("lilei",years=4,exe='boy'))

def func5(name=None,**kwargs):
    lis = ["%s:%s" %(k, v) for k, v in kwargs.items()]
    lis.insert(0, 'name:%s' % name)
    return ','.join(lis)
print(func5("lilei",years=4,exe='boy'))