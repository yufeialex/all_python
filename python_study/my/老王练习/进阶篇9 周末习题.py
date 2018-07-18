# __*__coding:utf-8__*__
#  Author:   benson

'''
1.定义一个func（url,folder_path）,获取url的地址的内容。保存到folder_path的文件目录下，并随生成一个文件名。
2.定义一个func（folder_path），合并改目录下的所有文件，生成一个all.txt.
3.定义一个func（url），分析改url内容里有多少个链接
4.定义一个func（url），获取它？后的参数，并返回一个dict。
    assert('http://url/api?param=2$param2=4') == {"param":"2", "param2":"4"}
5.定义一个func（folder），删除改folder下的所有文件
'''
import random
import urllib.request
import os

#1.定义一个func（url,folder_path）,获取url的地址的内容。保存到folder_path的文件目录下，并随生成一个文件名。
def get_url_conten(url, folder_path=None):
    if not (url.startswith('http://') or url.startswith('https://')):
        return u"url 无效"
    '''
        try:
            conten = urllib.request.urlopen(url)
        except Exception as e:
            print(e)
            return u"该网页无法打开"
    '''
    if not os.path.isdir(folder_path):
        return "%s is not dir" % folder_path
    conten = urllib.request.urlopen(url)
    content = conten.read()
    rand_filename = 'test_%s' % random.randint(1, 1000)
#   file_path = '%s/%s' % (folder_path, rand_filename)
    file_path = os.path.join(folder_path, rand_filename)
    f = open(file_path, 'w')
    f.write(str(content))
    f.close()
    return file_path

#print(get_url_conten('http://www.baidu.com', 'e:/test'))


#2.定义一个func（folder_path），合并改目录下的所有文件，生成一个all.txt.







#3.定义一个func（url），分析改url内容里有多少个链接

def url_count(url):
    if not (url.startswith('http://') or url.startswith('https://')):
        return "url 无效"
    conten = urllib.request.urlopen(url)
    count = len(str(conten.read()).split('<a href')) - 1
    return count
print(url_count('http://www.baidu.com'))

# 4.定义一个func（url），获取它？后的参数，并返回一个dict。
#   assert qs('http://url/api?param=2$param2=4') == {"param":"2", "param2":"4"}
import urllib.parse

def get_url_param(url):
    if not (url.startswith('http://') or url.startswith('https://')):
        return u"url 无效"

    param = urllib.parse.urlparse(url).query
    print(param)
#   url_list = url.split('?')
#   param_list = url_list[1].split('$')
#    return dict([(k, v[0]) for k, v in urllib.parse.parse_qs(param).items()])
    return urllib.parse.parse_qs(param)

print(get_url_param('http://url/api?param=2&param2=4'))

#2.定义一个func（folder_path），合并改目录下的所有文件，生成一个all.txt.
def merge_foler(folder_path) :
    '''
    
    :param folder_path: 
    :return: 
    '''

    import os
    if not os.path.exists(folder_path):
        return 'not exists %s' % folder_path
    for f in os.listdir(folder_path):
        file_path = os.path.join(folder_path, f)
        if os.path.isdir(file_path):
            merge_foler(file_path)
        else:
            merge_file = open('./merge_test', 'ab+')
            content = open(file_path, 'r').read()
            print(content)
            merge_file.write(content)
            merge_file.close()

merge_foler('C:/test/')

#5.定义一个func（folder），删除改folder下的所有文件

def delete_folder(folder_path):
    '''
    
    :param folder_path: 磁盘路径 
    :return: 
    '''

    if not os.path.exists(folder_path):
        return "not exists %s", folder_path

    print(os.listdir(folder_path))
    for f in os.listdir(folder_path):
        file_path = os.path.join(folder_path,f)
        if os.path.isdir(file_path):
            delete_folder(file_path)
        else:
            os.remove(file_path)

#delete_folder('c:/test/')





#5.定义一个func（folder），删除改folder下的所有文件




