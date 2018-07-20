# coding=utf-8

# 上面其实你随便写都可以，只要符合 coding[:|=]\s*([-\w.]+)
# 比如这种卖萌写法： #-*- coding： utf-8 -*-

import time  # 内置模块
import stand  # 自定义模块

print(stand.__doc__)
print(stand.new_str)
print(stand.hello())
print(time.timezone)

f = open("test.txt", "w")
f.write("2012来了。\n2012不是世界末日。\n2012欢乐多。")
f.close()
