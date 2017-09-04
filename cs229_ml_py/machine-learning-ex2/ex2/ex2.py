import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf


def logic_train(x, y):
    # Create the model
    # x's shape: 2 * m;
    # y's shape: 1 * m;

    plt.scatter(x[:, 0], x[:, 1], c=y)
    plt.xlabel('X')
    plt.ylabel('Y')
    # plt.show()
    plt.ion()

    # Create the model
    x_data = tf.Variable(x, dtype='float32')
    y_data = tf.Variable(y, dtype='float32')
    W = tf.Variable(tf.zeros([2, 1]))
    b = tf.Variable(0.01)

    h = tf.matmul(x_data, W) + b

    loss = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(labels=y_data, logits=h))

    optimizer = tf.train.GradientDescentOptimizer(0.0005)
    train = optimizer.minimize(loss)

    init = tf.global_variables_initializer()

    with tf.Session() as sess:
        sess.run(init)
        for step in range(100):
            _, we, ba, los = sess.run([train, W, b, loss])
            if step % 1 == 0:
                print(step, we[0][0], we[1][0], ba, los)
                plt.cla()
                plt.scatter(x[:, 0], x[:, 1], c=Y)
                plt.xlabel('X')
                plt.ylabel('Y')

                x_p = [min(x[0, :]), max(x[0, :])]
                y_p = - np.multiply(x_p, we[0][0] / we[1][0]) + ba
                plt.plot(x_p, y_p, 'y-')

                plt.text(10, 20, 'Loss=%.4f' % los)
                plt.pause(0.001)


if __name__ == "__main__":
    # load data
    data = np.loadtxt('ex2data1.txt', dtype=float, delimiter=',')

    X = data[:, 0:2]
    Y = data[:, 2]

    assert len(X) == len(Y)
    m = len(X)

    logic_train(X.reshape(m, 2), Y.reshape(m, 1))
