# coding = utf-8
'''
##习题1：
列表a = [11,22,24,29,30,32]
1 把28插入到列表的末端
2 在元素29后面插入元素57
3 把元素11修改成6
3 删除元素32
4 对列表从小到大排序

'''
a = [11, 22, 24, 29, 30, 32]
print("1.1--------")
a.append(28)
print(a)

print("1.2--------")
a.insert(4, 57)
print(a)

print("1.3--------")
a[0] = 6
print(a)

print("1.4--------")
del a[5]
# a.pop(5)
print(a)

print("1.5--------")
a.sort()
print(a)

'''
##习题2：
列表b = [1,2,3,4,5]
1 用2种方法输出下面的结果：
[1,2,3,4,5,6,7,8]
2 用列表的2种方法返回结果：[5,4]
3 判断2是否在列表里
'''
print("2.1---------")
print("方法一")
b = [1, 2, 3, 4, 5]
c = [6, 7, 8]
print(b + c)
print("方法二")
b = [1, 2, 3, 4, 5]
b.append(6)
b.append(7)
b.append(8)
print(b)
print("方法三")
b = [1, 2, 3, 4, 5]
b.extend([6, 7, 8])
print(b)

print("2.2----------")
print("方法二")
print(b[-4:-6:-1])

print("方法一")
b.reverse()
print(b[3:5])

print("2.3----------")
# c = set(b)
print(2 in b)

'''
##习题3：
b = [23,45,22,44,25,66,78]
用列表解析完成下面习题：
1 生成所有奇数组成的列表
2 输出结果: ['the content 23','the content 45']
3 输出结果: [25, 47, 24, 46, 27, 68, 80]

'''
print("3.1-----------")
b = [23, 45, 22, 44, 25, 66, 78]
print([x for x in b if x % 2 == 1])

print("3.2-----------")
print(['the conten %s' % i for i in b[:2]])

print("3.3------------")
print([i + 2 for i in b])

'''
##习题4：
用range方法和列表推导的方法生成列表：
[11,22,33]
'''
print([x * 11 for x in range(1, 4)])

'''
##习题5：
已知元组:a = (1,4,5,6,7)
1 判断元素4是否在元组里
2 把元素5修改成8
'''
a = (1, 4, 5, 6, 7)
print("5.1----------")
print(4 in a)

print("5.2--------------")
b = list(a)
b[2] = 8
print(tuple(b))

'''
##习题6：
已知集合:setinfo = set('acbdfem')和集合finfo = set('sabcdef')完成下面操作：
1 添加字符串对象'abc'到集合setinfo
2 删除集合setinfo里面的成员m
3 求2个集合的交集和并集
'''
finfo = set('sabcdef')
setinfo = set('acbdfem')
print("6.1---------")
setinfo.add('abc')
print(setinfo)

print("6.2-----------")
setinfo.remove('m')
print(setinfo)

print("6.3-----------")
print(setinfo & finfo)
print(setinfo | finfo)

'''
##习题7：
用字典的方式完成下面一个小型的学生管理系统。
1 学生有下面几个属性：姓名，年龄，考试分数包括：语文，数学，英语得分。
比如定义2个同学：
姓名：李明，年龄25，考试分数：语文80，数学75，英语85
姓名：张强，年龄23，考试分数：语文75，数学82，英语78
2 给学生添加一门python课程成绩，李明60分，张强：80分
3 把张强的数学成绩由82分改成89分
4 删除李明的年龄数据
5 对张强同学的课程分数按照从低到高排序输出。
6 外部删除学生所在的城市属性，不存在返回字符串 beijing
'''
print("7.1-------------")
student = {}
student['liming'] = {'name': 'liming', 'age': 25, 'score': {'chinese': 80, 'math': 75, 'englist': 85}}
student['zhangqiang'] = {'name': 'zhangqiang', 'age': 23, 'score': {'chinese': 75, 'math': 83, 'englist': 78}}
print(student)

print("7.2---------")
student['liming']['score']['python'] = 60
student['zhangqiang']['score']['python'] = 80
print(student)

print("7.3-----------")
student['zhangqiang']['score']['math'] = 89
print(student)

print("7.4-----------")
print(student['liming'].pop('age'))
print(student)

print("7.5-----------")
print(sorted(student['zhangqiang']['score'].values()))

print("7.6----------")
print(student.pop('city', 'beijing'))
