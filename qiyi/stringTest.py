# 用+符号拼接
# 用%符号拼接
# 用join()方法拼接
# 用format()方法拼接
# 用string模块中的Template对象

# 方法1：直接通过加号(+)操作符连接,效率低
# 字符串是不可变的类型，使用 + 连接两个字符串时会生成一个新的字符串，需要重新申请内存，当连续相加的字符串很多时，效率低下就是必然的了

website = 'python' + 'tab' + '.com'

# 方法2：join方法
# 多个字符进行连接时效率高，只会有一次内存的申请。而且如果是对list的字符进行连接的时候，这种方法必须是首选
listStr = ['python', 'tab', '.com']
website = ''.join(listStr)

# 方法3：替换
# 字符串格式化，这种方法非常常用，本人也推荐使用该方法
website = '%s%s%s' % ('python', 'tab', '.com')
# 除了用元组的方法，还可以使用字典如下：
fruit1 = 'apples'
fruit2 = 'bananas'
fruit3 = 'pears'
str = 'There are %(fruit1)s,%(fruit2)s,%(fruit3)s on the table' % {'fruit1': fruit1, 'fruit2': fruit2, 'fruit3': fruit3}

# format()方法拼接如下:

str = 'There are {}, {}, {} on the table'
str.format(fruit1, fruit2, fruit3)

# 还可以指定参数对应位置：

str = 'There are {2}, {1}, {0} on the table'
str.format(fruit1, fruit2, fruit3)  # fruit1出现在0的位置

# 同样，也可以使用字典：

str = 'There are {fruit1}, {fruit2}, {fruit3} on the table'
str.format(fruit1=fruit1, fruit2=fruit2, fruit3=fruit3)

# 用string模块中的Template对象如下：


from string import Template

str = Template('There are ${fruit1}, ${fruit2}, ${fruit3} on the table')  # 此处用的是{}，别搞错了哦
str.substitute(fruit1=fruit1, fruit2=fruit2, fruit3=fruit3)  # 如果缺少参数，或报错如果使用safe_substitute()方法不会
str.safe_substitute(fruit1=fruit1, fruit2=fruit2)


# 输出'There are apples, bananas, ${fruit3} on the table'


# 格式化输出：

# python2要这么写

def a(x, y):
    print("%s : %s " % x, y)


# python3.x要这么写
def a(x, y):
    print("%s : %s " % (x, y))
