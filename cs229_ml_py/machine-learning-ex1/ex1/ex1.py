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
x_data = X
y_data = Y
w = tf.Variable(tf.zeros([1]))
b = tf.Variable(tf.zeros([1]))

y_output = tf.multiply(w, x_data) + b

# Minimize the mean squared errors.
loss = tf.reduce_mean(tf.square(y_output - y_data)) / 2
optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)

# Before starting, initialize the variables. We will 'run' this first

init = tf.global_variables_initializer()

# Launch the graph.
sess = tf.Session()
sess.run(init)

print(sess.run(w), sess.run(b), sess.run(loss))
# loss expect to be 32.07.



# Fit the line.
for step in range(1500):
    sess.run(train)
    if step % 20 == 0:
        print(step, sess.run(w), sess.run(b), sess.run(loss))

predict1 = 1 * sess.run(b)[0] + 3.5 * sess.run(w)[0]
print(predict1)