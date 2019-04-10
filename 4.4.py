#4 Look at the example of optimization for exponential function.
# Did you encounter any errors? Where in code do we display the optimal point? Do we minimize or maximize and which function?
# Start your search always from the point (0, -2). (1p)
# Optimizing exponential
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


from scipy import linspace , cos , exp, random, meshgrid, zeros
from scipy.optimize import fmin
from matplotlib.pyplot import plot, show, legend, figure, cm, contour, clabel
def f(x):
    return exp(-x[0] ** 2 - x[1] ** 2)


def neg_f(x):
    return -f(x)

x0 = random.randn(2)
x_min = fmin(neg_f, x0)

from mpl_toolkits.mplot3d import Axes3D

delta = 3
x_knots = linspace(x_min[0] - delta, x_min[0] + delta, 41)
y_knots = linspace(x_min[1] - delta, x_min[1] + delta, 41)
X, Y = meshgrid(x_knots, y_knots)
Z = zeros(X.shape)

for i in range(Z.shape[0]):
    for j in range(Z.shape[1]):
        Z[i][j] = f([X[i, j], Y[i, j]])

ax = Axes3D(figure(figsize=(8, 5)))
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0.4) #maxymalizujemy ta funkcje Z(X,Y)
ax.plot([x0[0]], [x0[1]], [f(x0)], color='g', marker='o', markersize=5, label='initial') #tutaj
ax.plot([x_min[0]], [x_min[1]], [f(x_min)], color='k', marker='o', markersize=5, label='final') #tutaj tez (wyswietlamy optimum)
ax.legend()
show()

