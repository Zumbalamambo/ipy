import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf


def logic_train(x, y):
    # Create the model
    # x's shape: 2 * m;
    # y's shape: 1 * m;

    # print(x)
    # print(y)

    plt.scatter(x[:, 0], x[:, 1], c=y)
    # plt.show()
    plt.ion()

    # Create the model
    x_data = tf.Variable(x, dtype='float32')
    y_data = tf.Variable(y, dtype='float32')
    W = tf.Variable(tf.random_normal((2, 1), 0.0, 0.01, dtype='float32'))
    b = tf.Variable(0.1)

    z = tf.matmul(x_data, W) + b

    h = tf.sigmoid(z)

    j = y_data * tf.log(h) + (1 - y_data) * tf.log(1 - h)

    loss = tf.reduce_mean(-j)

    optimizer = tf.train.GradientDescentOptimizer(0.001)
    train = optimizer.minimize(loss)

    init = tf.global_variables_initializer()

    with tf.Session() as sess:
        sess.run(init)
        print(sess.run(W))
        print(sess.run(b))
        print(np.average(sess.run(z)))
        print(np.average(sess.run(h)))
        print(np.average(sess.run(j)))
        print(sess.run(loss))
        print('----------')

        for step in range(2):
            sess.run(train)
            if step % 1 == 0:
                print(sess.run(W))
                print(sess.run(b))
                print(np.average(sess.run(z)))
                print(np.average(sess.run(h)))
                print(np.average(sess.run(j)))
                print(sess.run(loss))
                print('----------')

                # plt.cla()
                # plt.scatter(x[:, 0], x[:, 1], c=y)
                #
                # x_p1 = min(x[0, :])
                # x_p2 = max(x[0, :])
                # y_p1 = (- ba - x_p1 * we[1][0]) / we[0][0]
                # y_p2 = (- ba - x_p2 * we[1][0]) / we[0][0]
                #
                # # print([x_p1, y_p1], [x_p2, y_p2])
                #
                # plt.plot([x_p1, x_p2], [y_p1, y_p2], 'y-')
                #
                # plt.text(10, 20, 'Loss=%.4f' % los)
                # plt.pause(0.001)


if __name__ == "__main__":
    # load data
    data = np.loadtxt('logic_data1.txt', dtype=float, delimiter=',')

    X = data[:, 0:2]
    Y = data[:, 2]

    assert len(X) == len(Y)
    m = len(X)

    logic_train(X.reshape(m, 2), Y.reshape(m, 1))