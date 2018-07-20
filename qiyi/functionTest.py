import math


# 返回一个元组
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


def a():
    m = {"a": 1, "b": "dd"}
    n = 10
    return m, n


if __name__ == '__main__':
    x = a()
    print(x[0], x[1])
