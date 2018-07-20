# coding=utf-8
f = open('print.txt', 'w', encoding='utf-8')
print("my name is", file=f),
print('wqb', file=f)
f.close()

r = open('print.txt', 'r', encoding='utf-8')
print(r.read())
r.close()

# import random
# a = random.
# print(a)


a = 3
if a:
    print(a)

import random
import sys

print(sys.argv[0])

a = random.randint(1, 100)
print(a)
