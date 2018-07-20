#!/usr/bin/python
# -*-coding:utf-8-*-       #指定编码格式，python默认unicode编码

import os

directory = "./dir"
os.chdir(directory)  # 切换到directory目录
cwd = os.getcwd()  # 获取当前目录即dir目录下
print("------------------------current working directory------------------")


def deleteBySize(minSize):
    """删除小于minSize的文件（单位：K）"""
    files = os.listdir(os.getcwd())  # 列出目录下的文件
    for file in files:
        if os.path.getsize(file) < minSize * 1000:
            os.remove(file)  # 删除文件
            print(file + " deleted")
    return


def deleteNullFile():
    '''删除所有大小为0的文件'''
    files = os.listdir(os.getcwd())
    for file in files:
        if os.path.getsize(file) == 0:  # 获取文件大小
            os.remove(file)
            print(file + " deleted.")
    return


def create():
    '''根据本地时间创建新文件，如果已存在则不创建'''
    import time
    t = time.strftime('%Y-%m-%d', time.localtime())  # 将指定格式的当前时间以字符串输出
    suffix = ".docx"
    newfile = t + suffix
    if not os.path.exists(newfile):
        f = open(newfile, 'w')
        print
        newfile
        f.close()
        print
        newfile + " created."
    else:
        print
        newfile + " already existed."
    return


hint = '''funtion:
            1   create new file
            2   delete null file
            3   delete by size
please input number:'''
while True:
    option = raw_input(hint)  # 获取IO输入的值
    if cmp(option, '1') == 0:
        create()
    elif cmp(option, '2') == 0:
        deleteNullFile()
    elif cmp(option, '3') == 0:
        minSize = raw_input("minSize(K):")
        deleteBySize(minSize)
    elif cmp(option, 'q') == 0:
        print
        "quit !"
        break
    else:
        print("disabled input ,please try again....")

# 遍历文件夹
# 第一种：使用os.walk:

# -*- coding: utf-8 -*-
import os


def Test1(rootDir):
    list_dirs = os.walk(rootDir)
    for root, dirs, files in list_dirs:
        for d in dirs:
            print
            os.path.join(root, d)
        for f in files:
            print
            os.path.join(root, f)


# 第二种：使用os.listdir:

# -*- coding: utf-8 -*-
import os


def Test2(rootDir):
    for lists in os.listdir(rootDir):
        path = os.path.join(rootDir, lists)
        print
        path
        if os.path.isdir(path):
            Test2(path)
            # 对于第一种方法，输出总是先文件夹后文件名的，对于第二种，则是按照目录树结构以及按照首字母排序进行输出的。


# 对某目录下（包括子目录）的所有.ppm文件改为.jpg文件。

from PIL import Image
import os
import os.path


def change_format(rootDir):
    for root, dirs, files in os.walk(rootDir):
        for file in files:
            if os.path.splitext(file)[1] == '.ppm':
                im = Image.open(os.path.join(root, file))
                filename = os.path.join(root, file)
                im.save(os.path.splitext(filename)[0] + '.jpg', 'JPEG')


if __name__ == '__main__':
    _dir = "your directory"
    change_format(_dir)

# root为path（一直到file名字（除去文件名字）），file只是文件名字加上扩展名，此处os.path.join(root, file)为absolutepath，
# os.path.splitext(file)[1]为扩展名（os.path.splitext(file)[1][1:]为ppm不带.)，os.path.splitext(file)[0]为文件名

rootdir = 'F:\data'
list = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
for i in range(0, len(list)):
    path = os.path.join(rootdir, list[i])
    if os.path.isfile(path):
# 你想对文件的操作
