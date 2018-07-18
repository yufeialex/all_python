__author__ = 'Administrator'
#!/usr/bin/python
# -*- coding:utf-8 -*-
import tensorflow as tf

matrix1 = tf.constant([[3, 3]])
matrix2 = tf.constant([[2], [2]])
product = tf.matmul(matrix1, matrix2)  # matrix multiply np.dot(m1, m2)

# method1
# sess = tf.Session() 因为Session是一个对象，所以要大写
# result = sess.run(product)
# print(result)
# sess.close()

# method2
with tf.Session() as sess:
    result2 = sess.run(product)
    print(result2)