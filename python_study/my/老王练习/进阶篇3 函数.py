#coding = utf-8

'''
习题：
'''
print("1 定义一个方法get_num(num),num参数是列表类型，判断列表里面的元素为数字类型。其他类型则报错，并且返回一个偶数列表：（注：列表里面的元素为偶数）。")

import sys
def get_Num(num):
    '''
    :param num: num is list 
    :return: new list all even number
    '''
    new_num = []
    if not isinstance(num,list):   #判断参数是否为列表
        print("%s is not a list,plz check!" % num)
        sys.exit(1)
    for i in num:
        if isinstance(i,int):
            if i % 2 == 0:
                new_num.append(i)
            else:
                pass
        else:
            print("%s is a list but not all number,plz again!" % i)
            continue
    return new_num

print(get_Num(['s',2,3,5,4,6]))


print("2 定义一个方法get_page(url),url参数是需要获取网页内容的网址，返回网页的内容。提示（可以了解python的urllib模块）。")
import urllib.request

def get_Page(url):
    '''

    :param url: url 地址 
    :return: 网页内容
    '''
    url_conten = urllib.request.urlopen(url).read()
    return  url_conten

#print(get_Page('http://www.baidu.com'))


print("3 定义一个方法 func，该func引入任意多的列表参数，返回所有列表中最大的那个元素。")
def fun(*List_max):
    '''
    :param List_max: 任何列表参数
    :return:  max_list_num
    '''
    max_list_num = []
    for i in List_max:
        if isinstance(i,list):
            for j in i:
                if not isinstance(j,int):
                    print("%s is a list but not all num" % i)
                    return 'error'
            max_list_num.append(max(i))
        else:
            print("%s is not a list" % i)
            continue
    return max(max_list_num)
print(fun('asdf',[3,10,6],[1,2,7]))


print("4 定义一个方法get_dir(f),f参数为任意一个磁盘路径，该函数返回路径下的所有文件夹组成的列表，如果没有文件夹则返回Not dir。")
import os.path

def get_dir(*f):
    '''
    
    :return: 
    '''
    dir_list_all = []
    for i in f:
        if os.path.exists(i) & os.path.isdir(i):
            for d in os.listdir(i):
                if os.path.isdir('%s/%s' % (i, d)):
                    dir_list_all.append(d)
        else:
            print("%s is not a dir or not found." % i)
            dir_list_all = "not dir"
    return dir_list_all

print(get_dir("f:/", 'c:'))
'''
注明：吸取上次作业遇到的问题，要求写的函数逻辑清楚，并且考虑一些特殊的情况处理，能做断言的尽量用断言。
'''
