#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
shenbo@hotmail.com
@ 2017.07.05
"""

import tensorflow as tf
import numpy as np

from tensorflow.examples.tutorials.mnist import input_data

# import data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

# Create the model
x = tf.placeholder(tf.float32, [None, 784])
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))
y = tf.nn.softmax(tf.matmul(x, W) + b)

# Define loss and optimizer
y_ = tf.placeholder(tf.float32, [None, 10])
cross_entropy = -tf.reduce_sum(y_ * tf.log(y))
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

init_op = tf.initialize_all_variables()


sess = tf.Session()
sess.run(init_op)


for i in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))

accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))

print (sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.
test.labels}))


#
# # Train the model and save the model to disk as a model.ckpt file
# # file is stored in the same directory as this python script is started
# """
# The use of 'with tf.Session() as sess:' is taken from the Tensor flow documentation
# on on saving and restoring variables.
# https://www.tensorflow.org/versions/master/how_tos/variables/index.html
# """
# with tf.Session() as sess:
#     sess.run(init_op)
#     for i in range(1000):
#         batch_xs, batch_ys = mnist.train.next_batch(100)
#         sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})
#
#     save_path = saver.save(sess, "model.ckpt")
#     print("Model saved in file: ", save_path)