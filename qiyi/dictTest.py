# https://segmentfault.com/a/1190000010567015
dict1 = {"lo": "beij"}
dict2 = {"mm": "shang"}
# 方法1，不好
# 在内存中创建两个列表，再创建第三个列表，拷贝完成后，创建新的dict，删除掉前三个列表。这个方法耗费性能，而且对于python3，
# 这个无法成功执行，因为items()返回是个对象。
# 你必须明确的把它强制转换成list，z = dict(list(x.items()) + list(y.items()))，这太浪费性能了。
# 另外，想以来于items()返回的list做并集的方法对于python3来说也会失败，而且，并集的方法，导致了重复的key在取值时的不确定，所以，
# 如果你对两个dict合并有优先级的要求，这个方法就彻底不合适了。
dictMerged1 = dict(dict1.items() + dict2.items())

x = {'a': 2}
y = {'a': 1}
dict(x.items() | y.items())
# 可能留下了x，但是我想要y

# 方法2，**的意思是基于字典的可变长函数参数。
# 比前面的两步的方法高效多了，但是可阅读性差，不够pythonic，如果当key不是字符串的时候，python3中还是运行失败
# Guido van Rossum 大神说了：宣告dict（{}， {1：3}）是非法的，因为毕竟是滥用机制。虽然这个方法比较hacker，但是太投机取巧了。
dictMerged2 = dict(dict1, **dict2)

# 方法3
dictMerged3 = dict1.copy()
dictMerged3.update(dict2)

# 方法4，python3.5中支持
dictMerged4 = {**dict1, **dict2}


def merge_two_dicts(x, y):
    """Given two dicts, merge them into a new dict as a shallow copy."""
    z = x.copy()
    z.update(y)
    return z


z = merge_two_dicts(x, y)


def merge_dicts(*dict_args):
    """
    Given any number of dicts, shallow copy and merge into a new dict,
    precedence goes to key value pairs in latter dicts.
    """
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result


z = merge_dicts(a, b, c, d, e, f, g)

# 一些性能较差但是比较优雅的方法
# 下面这些方法，虽然性能差，但也比items方法好多了。并且支持优先级。


{k: v for d in dicts for k, v in d.items()}

# python2.6中可以这样

dict((k, v) for d in dicts for k, v in d.items())

# itertools.chain:

import itertools

z = dict(itertools.chain(x.iteritems(), y.iteritems()))
