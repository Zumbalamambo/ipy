import numpy as np
import matplotlib.pyplot as plt


# 直径、高度
d = 0.5
h = 0.6

# 网格
delta_X = 0.05
delta_Y = 0.05

nx = int(d/delta_X)
ny = int(h/delta_Y)
nodes = np.zeros([ny, nx])

temp_nodes = np.zeros([ny, nx])

x = np.arange(0, d, delta_X)
y = np.arange(h, 0, -delta_Y)
X, Y = np.meshgrid(x, y)

# 步长
d_teps = 0.05

# 初始化参数
t0 = 100
tf = 200
h = 27
lamda = 4.2

bi = h * delta_X / lamda

for j in range(0, nx):
    nodes[0][j] = 100

for k in range(0, 1000):
    for i in range(1, ny - 1):
        for j in range(1, nx - 1):
            nodes[i][j] = (nodes[i - 1][j] + nodes[i + 1][j] + nodes[i][j - 1] + nodes[i][j + 1]) / 4

    for i in range(1, ny - 1):
        nodes[i][0] = (2 * nodes[i][1] + nodes[i - 1][0] + nodes[i + 1][0] + 2 * bi * tf) / 2 / (bi + 2)
        nodes[i][nx - 1] = (2 * nodes[i][nx - 2] + nodes[i - 1][nx - 1] + nodes[i + 1][nx - 1] + 2 * bi * tf) / 2 / (bi + 2)

    for j in range(1, nx - 1):
        nodes[ny - 1][j] = (2 * nodes[ny - 2][j] + nodes[ny - 1][j - 1] + nodes[ny - 1][j + 1] + 2 * bi * tf) / 2 / (bi + 2)

    nodes[ny - 1][0] = (nodes[ny - 2][0] + nodes[ny - 1][1] + 2 * bi * tf) / 2 / (bi + 1)
    nodes[ny - 1][nx - 1] = (nodes[ny - 2][nx - 1] + nodes[ny - 1][nx - 2] + 2 * bi * tf) / 2 / (bi + 1)

    dtmax = 0.0

    for i in range(0, ny):
        for j in range(0, nx):
            dtmax = max(abs(nodes[i][j] - temp_nodes[i][j]), dtmax)

    for i in range(0, ny):
        for j in range(0, nx):
            temp_nodes[i][j] = nodes[i][j]
    print(nodes)
    print(k)
    if dtmax < d_teps:
        print(k)
        break


'''
nodes = [[100.0 for j in range(nx)] for i in range(ny)]
temp_nodes = [[100.0 for j in range(nx)] for i in range(ny)]

x = np.arange(0, 0.5, delta_X)
y = np.arange(0.6, 0, -delta_Y)
X, Y = np.meshgrid(x, y)

d_teps = 0.01

t0 = 100
tf = 200
h = 27
lamda = 4.2

bi = h * delta_X /lamda

for j in range(0, nx):
    nodes[0][j] = 100

for k in range(0, 10000):
    for i in range(1, ny - 1):
        for j in range(1, nx - 1):
            nodes[i][j] = (nodes[i - 1][j] + nodes[i + 1][j] + nodes[i][j - 1] + nodes[i][j + 1]) / 4

    for i in range(1, ny - 1):
        nodes[i][0] = (2 * nodes[i][1] + nodes[i - 1][0] + nodes[i + 1][0] + 2 * bi * tf) / 2 / (bi + 2)
        nodes[i][nx - 1] = (2 * nodes[i][nx - 2] + nodes[i - 1][nx - 1] + nodes[i + 1][nx - 1] + 2 * bi * tf) / 2 / (bi + 2)

    for j in range(1, nx - 1):
        nodes[ny - 1][j] = (2 * nodes[ny - 2][j] + nodes[ny - 1][j - 1] + nodes[ny - 1][j + 1] + 2 * bi * tf) / 2 / (bi + 2)

    nodes[ny - 1][0] = (nodes[ny - 2][0] + nodes[ny - 1][1] + 2 * bi * tf) / 2 / (bi + 1)
    nodes[ny - 1][nx - 1] = (nodes[ny - 2][nx - 1] + nodes[ny - 1][nx - 2] + 2 * bi * tf) / 2 / (bi + 1)

    dtmax = 0.0

    for i in range(0, ny):
        for j in range(0, nx):
            dtmax = max(abs(nodes[i][j] - temp_nodes[i][j]), dtmax)

    for i in range(0, ny):
        for j in range(0, nx):
            temp_nodes[i][j] = nodes[i][j]
    #print nodes
    print k
    if dtmax < d_teps:
        print k
        break

for i in range(0, ny):
    s = ''.join('%3.1f ' % (nodes[i][j]) for j in range(0, nx))
    print s

print nodes

plt.figure()
CS = plt.contour(X, Y, nodes)
plt.clabel(CS, inline=1, fontsize=10)
plt.title('Simplest default with labels')
plt.show()

 
Q = 0.0
for j in range(0, nx):
    dA =  3.14 / 4 * d *d / nx / nx * ((j + 1) * (j + 1) - j * j)
    Q = Q + lamda * dA * (nodes[1][j] - nodes[0][j]) / delta_Y
print Q

Q = 0.0
for j in range(0, nx):
    dA = 3.14 / 4 * d * d / nx / nx * ((j + 1) * (j + 1) - j * j)
    Q = Q + h * dA * (nodes[5][j] - nodes[4][j])

for i in range(0, ny):
    dA = 3.14 * d * delta_Y
    Q = Q + h * dA * (tf - nodes[i][0])
print Q




'''
