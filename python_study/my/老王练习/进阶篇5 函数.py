# __*__coding: utf-8__*__
'''
今天习题：
1 用lambda和filter完成下面功能：输出一个列表，列表里面包括：1-100内的所有偶数。（提示：可以用filter,lambda）
'''
ou = list(filter(lambda x:  x & 1 == 0, range(1, 101)))
#print(ou)

'''
2 用位置匹配，关键字匹配，收集匹配(元组收集,字典收集)分别写4个函数，完成功能；
传递3个列表参数：
[1,2,3],[1,5,65],[33,445,22]

返回这3个列表中元素最大的那个，结果是：445
'''
def fun1(arg1,arg2,arg3):
    # for i in (arg1,arg2,arg3):
    #     if not isinstance(i, list):
    #         return "%s  is not a list plz" % i
    max_num = [max(x) for x in (arg1,arg2,arg3) if isinstance(x, list)]
    return max(max_num)
print(fun1(1,[1,5,65],[33,445,22]))

def fun2(*karg):
    max_num = [max(i) for i in karg if isinstance(i, list)]
    return max(max_num)
print(fun2(1,[1,5,65],[33,445,22]))
'''
3 递归函数解释，用自己的话说明这个递归函数的工作流程。

def func1(i):
	if i<100:
		return i + func1(i+1)
	return i
print func1(0)


'''
d = lambda x: x+1 if x > 0 else "error"
g = lambda x: [(x, i) for i in range(1,10)]
#print(g(1))
#print(d(-22))
