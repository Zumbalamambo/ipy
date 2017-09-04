import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

def linear_train(x, y):
    # Create the model
    # x's shape: 1 * m;
    # y's shape: 1 * m;

    x_data = tf.Variable(x, dtype='float32')
    y_data = tf.Variable(y, dtype='float32')
    W = tf.Variable(tf.zeros([1, 1]))
    b = tf.Variable(tf.zeros([1]))

    y_output = tf.matmul(W, x_data) + b

    # Minimize the mean squared errors.
    loss = tf.reduce_mean(tf.square(y_output - y_data))
    optimizer = tf.train.GradientDescentOptimizer(0.01)
    train = optimizer.minimize(loss)

    init = tf.global_variables_initializer()

    # Launch the graph.
    with tf.Session() as sess:
        sess.run(init)

        for step in range(1500):
            sess.run(train)

            weights, bais, cost = sess.run([W, b, loss])
            if step % 20 == 0:
                print(step, weights[0][0], bais[0], cost)
        return weights[0][0], bais[0]


def plot_data(x, y, w = 0.0, b = 0.0):
    plt.plot(x, y, 'rx')
    plt.xlabel('Population of City in 10,000s')
    plt.ylabel('Profit in $10,000s')

    x_p = [min(x), max(x)]
    y_p = np.multiply(w, x_p) + b
    plt.plot(x_p, y_p, '-')

    plt.show()


if __name__ == "__main__":
    # load data
    data = np.loadtxt('ex1data1.txt', dtype=float, delimiter=',')

    X = data[:, 0]
    Y = data[:, 1]

    m = len(X)

    # plot_data(X, Y)

    w, b = linear_train(np.reshape(X, (1, m)), np.reshape(Y, (1, m)))

    plot_data(X, Y, w, b)