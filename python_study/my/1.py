import string


def string_test():
    a = "adf sd    "
    b = "iiiii"
    d = " python是动态语言   "
    e = " "
    f = "ADADSF"
    g = "aadfDA"
    print(str.capitalize(a))
    print(str.casefold(a))
    print(str.encode(a))
    print(str.find("abc", "abc"))
    print("----------------")
    print(a.islower())
    print(b.isnumeric())
    print(e.isspace())  # 是否是空格字符串
    print(d.ljust(20, '0'))  # 调整到指定长度，用0填充
    print("----------------")
    print(f.lower())
    print(g.rstrip('DA'))  # 去掉右侧的内容，如果不指定就去掉空格
    print(b.upper())
    print(d.replace("p", "pp"))
    print("----------------")

    hs = "哈哈哈"
    print(str.__len__(hs))
    h = u"哈哈哈"
    print(h)
    print(str.__len__(h))
    print(a[2])  # 下标从0开始
    print(f[len(f) - 1])
    print(f[-1])
    print(str.join(",", [f, g, h]))


def string_test1():
    d = " python是动态语言   "

    print(d.strip())
    print(d.lstrip())
    print(d.rstrip())  # 去掉右侧的内容，如果不指定就去掉空格
    print(d.replace(" ", ""))
    print(id(d))
    print(type(d))
    # 组成3部分。
    # 身份
    # id方法来看一看他的唯一标示符，内存地址靠这个哦！
    # 类型
    # type来看一看。
    # 值
    # 数据项。


def file_test():
    file = open("test.txt", "w")
    file.write("ni hao\nmy name is")
    file.close()


def format_test():
    # 格式化
    a = "my name is %s and i am %d year old" % ("wqb", 24)
    b = "my name is {1} and i am {0} year old".format("wqb", "24")
    c = "my name is {name} and i am {age} year old".format(name="wqb", age=24)  # 推荐使用
    c1 = "my name is {} and i am {} year old".format("wqb", 24)  # 推荐使用，如果写标志位，就按照默认的顺序
    d = "my name is %(name)s and i am %(age)d year old" % {"name": "wqb", "age": 24}  # 字典

    print(a)
    print(b)
    print(c)
    print(c1)
    print(d)


def test_inner_func():
    help(string)
    dir(string)
    type(string)


class A:
    def __add__(self, other):
        print("A __add__")

    def __radd__(self, other):
        print("A __radd__")


class B:
    pass


def test_ab():
    a = A()
    b = B()
    c = B()
    print(a + b)
    print(b + a)  # A重载操作符了，B没有，打印A的函数和None
    # print(b + c)  # 没重载，报错


def ax():
    a = "adfsd"
    b = "iiiii"
    print(str.__add__(a, b))
    # print(str.__rmod__(a, b)) python3中没有了
    print(str.__sizeof__(a))


if __name__ == '__main__':
    # ax()
    # test_ab()
    # format_test()
    # string_test()
    string_test1()
