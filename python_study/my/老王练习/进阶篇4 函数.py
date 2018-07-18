# __*__coding:utf-8__*__
#  Author:   benson

# 2 定义一个方法get_cjsum(),求1-100范围内的所有整数的平方和。返回结果为整数类型。

def get_cjsum(num):
    '''
    
    :param num:  a int 
    :return:    返回1 - num 的整数平方和
    '''
    sum_num = 0
    if not isinstance(num, int):
        return 'plz enter a int num.'
    for i in range(1, num):
        sum_num = sum_num + i**2
    print(i)
    return sum_num

print(get_cjsum(101))
