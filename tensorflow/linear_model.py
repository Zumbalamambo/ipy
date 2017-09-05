import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# data
x_data = np.random.rand(100).astype("float32")
y_data = x_data * 0.1 + 0.3 + 0.01 * np.random.normal(0.0, 1.0, (100))

# plotdata
plt.scatter(x_data, y_data)
# plt.show()
plt.ion()


# tf model
W = tf.Variable(tf.random_uniform([1], 1.0, 1.0))
b = tf.Variable(tf.zeros([1]))
y_output = W * x_data + b

# Minimize the mean squared errors.
loss = tf.reduce_mean(tf.square(y_output - y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)


init = tf.global_variables_initializer()
# Launch the graph.
with tf.Session() as sess:
    sess.run(init)

    # Fit the line.
    for step in range(201):
        _, we, ba, los, yo = sess.run([train, W, b, loss, y_output])
        if step % 5 == 0:
            print(step, sess.run(W), sess.run(b))
            plt.cla()
            plt.scatter(x_data, y_data)

            x_p = [min(x_data), max(x_data)]
            y_p = np.multiply(x_p, we[0]) + ba
            plt.plot(x_p, y_p, 'y-')

            plt.text(0.5, 0.5, 'Loss=%.4f' % los)
            plt.pause(0.1)

    # Learns best fit is W: [0.1], b: [0.3]
