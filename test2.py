#!/usr/bin/env python
# -*- coding: utf-8 -*-



from pylab import *

delta_X = 0.01
delta_Y = 0.01

nx = 50
ny = 60

nodes = [[i*j for j in range(nx)] for i in range(ny)]

x = np.arange(0, 0.5, delta_X)
y = np.arange(0, 0.6, delta_Y)
X, Y = np.meshgrid(x, y)

print nodes

# Create a simple contour plot with labels using default colors.  The
# inline argument to clabel will control whether the labels are draw
# over the line segments of the contour, removing the lines beneath
# the label
plt.figure()
CS = plt.contour(X, Y, nodes)
plt.show()