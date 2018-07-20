import datetime
import time  # 引入time模块

ticks = time.time()
print("当前时间戳为:", ticks)

# 可以直接用于mongoDB时间字段
print(datetime.datetime.now())
