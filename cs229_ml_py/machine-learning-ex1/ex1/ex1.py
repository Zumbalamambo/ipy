import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf


def linear_train(x, y):
    # Create the model
    # x's shape: m * 1;
    # y's shape: m * 1;

    plt.scatter(x, y)
    plt.xlabel('Population of City in 10,000s')
    plt.ylabel('Profit in $10,000s')
    # plt.show()
    plt.ion()

    x_data = tf.Variable(x, dtype='float32')
    y_data = tf.Variable(y, dtype='float32')
    W = tf.Variable(tf.zeros([1, 1]))
    b = tf.Variable(1.0)

    y_output = tf.matmul(x_data, W) + b

    # Minimize the mean squared errors.
    loss = tf.reduce_mean(tf.square(y_output - y_data))
    optimizer = tf.train.GradientDescentOptimizer(0.01)
    train = optimizer.minimize(loss)

    init = tf.global_variables_initializer()

    # Launch the graph.
    with tf.Session() as sess:
        sess.run(init)
        for step in range(1000):
            _, we, ba, los, yo = sess.run([train, W, b, loss, y_output])
            if step % 20 == 0:
                print(step, we[0][0], ba, los)
                plt.cla()
                plt.scatter(x, y)
                plt.xlabel('Population of City in 10,000s')
                plt.ylabel('Profit in $10,000s')

                x_p = [min(x[:, 0]), max(x[:, 0])]
                y_p = np.multiply(x_p, we[0][0]) + ba
                plt.plot(x_p, y_p, 'y-')

                plt.text(10, 20, 'Loss=%.4f' % los)
                plt.pause(0.1)


if __name__ == "__main__":
    # load data
    data = np.loadtxt('ex1data1.txt', dtype=float, delimiter=',')

    X = data[:, 0]
    Y = data[:, 1]

    m = len(X)

    linear_train(X.reshape(m, 1), Y.reshape(m, 1))
