# coding = utf-8

'''
习题：

1.定义一个方法 func，该func可以引入任意多的整型参数，结果返回其中最大与最小的值。
'''
def func1(*Max):
    for i in Max:
        if not isinstance(i,int):
            return ("请输入一个整数！")
    return "最大值：%d 最小值：%d" % (max(Max),min(Max))

print(func1(1,34,4,55))
##使用filter  过滤

'''
2.定义一个方法func，该func可以引入任意多的字符串参数，结果返回（长度）最长的字符串。
'''
def func2(*Max_len):
    Max_len = sorted(Max_len,key=lambda k:len(k),reverse=True)
    return Max_len[0]

print(func2('aAAAAAd','dad3','23432','af'))

'''
3.定义一个方法get_doc(module)，module参数为该脚本中导入或定义的模块对象，该函数返回module的帮助文档。

例 print get_doc(urllib),则会输出urllib这个模块的帮助文档。
'''
import time
import os
def get_doc(module):
    return  help(module)

def get_doc2(module):
    doc = 'pydoc %s' % module
    m = os.popen(doc,'r')

    return m
#print(get_doc("time"))

'''
4.定义一个方法get_text(f),f参数为任意一个文件的磁盘路径，该函数返回f文件的内容。
'''
def get_text(f):
    file = open(f,'r')
    text = file.read()
    file.close()
    return text
def get_text2(f):
    if os.path.exists(f):
        file_v = open('%s' % f,'r')
        text = file_v.read()
        file_v.close()
        return text
    else:return 'not found %s' % f

print(get_text2('info1.txt'))
'''
5.定义一个方法get_dir(folder),folder参数为任意一个文件夹，该函数返回folder文件夹的文件列表。提示（可以了解python的glob模块）
'''
import glob
def get_dir(Dir):
    a = glob.glob(Dir)
    # a = glob.iglob(Dir)
    # for py in a:
    #      print(py)
    return a
print(get_dir("C:/*"))

