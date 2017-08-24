import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

# load data
data = np.loadtxt('ex1data1.txt', dtype=float, delimiter=',')

X = data[:, 0]
Y = data[:, 1]
assert len(X) == len(Y)

m = len(X)

plt.plot(X, Y, 'rx')
plt.xlabel('Population of City in 10,000s')
plt.ylabel('Profit in $10,000s')
# plt.show()


# Create the model
x = X
W = tf.Variable(tf.zeros([1]))
b = tf.Variable(tf.zeros([1]))

y = W * x + b

# Minimize the mean squared errors.
loss = tf.reduce_mean(tf.square(y - Y))
optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)

# Before starting, initialize the variables. We will 'run' this first

init = tf.global_variables_initializer()

# Launch the graph.
sess = tf.Session()
sess.run(init)

# Fit the line.
for step in range(1500):
    sess.run(train)
    if step % 20 == 0:
        print(step, sess.run(W), sess.run(b), sess.run(loss))


# Learns best fit is W: [0.1], b: [0.3]
