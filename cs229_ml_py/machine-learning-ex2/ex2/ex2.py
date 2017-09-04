import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

# load data
data = np.loadtxt('ex2data1.txt', dtype=float, delimiter=',')

X = data[:, 0:2]
Y = data[:, 2]
assert len(X) == len(Y)

# print(X.shape)
# print(Y.shape)

m = len(X)

plt.scatter(X[:, 0], X[:, 1], c=Y)
plt.xlabel('X')
plt.ylabel('Y')

# plt.show()


# Create the model
x_data = tf.Variable(np.transpose(X), dtype='float32')
y_data = tf.Variable(Y, dtype='float32')
W = tf.Variable(tf.zeros([1, 2]))
b = tf.Variable(tf.zeros([1]))

z = tf.matmul(W, x_data) + b

logit = tf.sigmoid(z)

# Minimize the mean squared errors.
loss = tf.reduce_sum(tf.square(logit - y_data))

optimizer = tf.train.GradientDescentOptimizer(0.1)
train = optimizer.minimize(loss)

# Before starting, initialize the variables. We will 'run' this first

init = tf.global_variables_initializer()

# Launch the graph.
sess = tf.Session()
sess.run(init)

print(sess.run(W), sess.run(b), sess.run(loss))


# Fit the line.
for step in range(100):
    sess.run(train)
    if step % 20 == 0:
        print(step, sess.run(W), sess.run(b), sess.run(loss))


predict1 = 1 * sess.run(b)[0] + 45 * sess.run(W)[0][0] + 85 * sess.run(W)[0][1]
print(predict1)