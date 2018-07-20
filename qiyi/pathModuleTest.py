import os

# dirname()  用于去掉文件名，返回目录所在的路径
os.path.dirname('d:\\library\\book.txt')
# 'd:\\library'

# basename()   用于去掉目录的路径，只返回文件名
os.path.basename('d:\\library\\book.txt')
# 'book.txt'

# join()   用于将分离的各部分组合成一个路径名
os.path.join('d:\\library', 'book.txt')
# 'd:\\library\\book.txt'

# split()  用于返回目录路径和文件名的元组
os.path.split('d:\\library\\book.txt')
# ('d:\\library', 'book.txt')

# splitdrive()    用于返回盘符和路径字符元组
os.path.splitdrive('d:\\library\\book.txt')
# ('d:', '\\library\\book.txt')

# splitext()    用于返回文件名和扩展名元组
os.path.splitext('d:\\library\\book.txt')
# ('d:\\library\\book', '.txt')
os.path.splitext('book.txt')
# ('book', '.txt')
