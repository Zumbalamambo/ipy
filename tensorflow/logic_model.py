import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf


def logic_train(x_, y_):

    mx = len(x_)
    # plt.scatter(x_[:, 0], x_[:, 1], c=y_)
    # plt.show()
    plt.ion()

    X = tf.placeholder(tf.float32)
    y = tf.placeholder(tf.float32)

    W = tf.Variable(tf.zeros([2, 1]))
    b = tf.Variable([-2.0])

    z = tf.matmul(X, tf.reshape(W, [-1, 1])) + b
    h = tf.sigmoid(z)

    j1 = y * tf.log(h)
    j2 = (1 - y) * tf.log(1 - h)
    j = (j1 + j2) / -mx
    loss = tf.reduce_sum(j)

    optimizer = tf.train.GradientDescentOptimizer(0.001)
    train = optimizer.minimize(loss)

    init = tf.global_variables_initializer()

    with tf.Session() as sess:
        sess.run(init)
        feed_dict = {X: x_, y: y_}

        for step in range(100000):
            sess.run(train, feed_dict)
            if step % 1000 == 0:
                w_, b_ = sess.run([W, b])
                print(step, w_[0], w_[1], b_,)

                plt.cla()
                plt.scatter(x_[:, 0], x_[:, 1], c=y_)

                x_p = x_[0, :]
                y_p = (- b_ - x_p * w_[1]) / w_[0]
                plt.plot(x_p, y_p, 'y-')
                plt.pause(0.001)


if __name__ == "__main__":
    # load data
    data = np.loadtxt('logic_data1.txt', dtype=float, delimiter=',')

    data_x = data[:, 0:2]
    data_y = data[:, 2]

    assert len(data_x) == len(data_y)
    m = len(data_x)

    logic_train(data_x.reshape(m, 2), data_y.reshape(m, 1))