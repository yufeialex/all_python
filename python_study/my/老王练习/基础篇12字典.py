# coding=utf-8
'''
字典习题:

已知字典：ainfo = {'ab':'liming','ac':20}

完成下面的操作

1 使用2个方法，输出的结果：

ainfo = {'ab':'liming','ac':20,'sex':'man','age':20}

2 输出结果：['ab','ac']

3 输出结果：['liming',20]

4 通过2个方法返回键名ab对应的值。

5 通过2个方法删除键名ac对应的值。

'''
anfo = {'ab': "liming", "ac": 20}
print("1-----------")
print("方法一")
anfo['sex'] = 'man'
anfo['age'] = 20
print(anfo)
print("方法二")
anfo = {'ab': "liming", "ac": 20}
anfo.update({'sex': 'man', 'age': 20})
print(anfo)

print("2--------------")
anfo = {'ab': "liming", "ac": 20}
print(anfo.keys())

print("3------------")
print(anfo.values())

print("4-----------")
print("方法一")
print(anfo['ab'])
print("方法二")
print(anfo.get('ab'))

print("5--------------")
print("方法一")
del anfo['ac']
print(anfo)
print("方法二")
anfo = {'ab': "liming", "ac": 20}
anfo.pop('ac')
print(anfo)
print("--------------has_key")
binfo = {'a': 1, 'b': 2}
print('a' in binfo)
