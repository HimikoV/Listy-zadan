import numpy as np
from scipy import linspace , cos , exp, random, meshgrid, zeros
from scipy.optimize import fmin
from matplotlib.pyplot import plot, show, legend, figure, cm, contour, clabel
def f(x):
    return 5*(1-(x[0]**2+x[1]**3))*np.e**(-(x[0]**2+x[1]**2)/2)


def neg_f(x):
    return -f(x)

x0 = random.rand(2)
x_min0 = fmin(neg_f, x0)

from mpl_toolkits.mplot3d import Axes3D
for i in range(1000):
    if i % 2 == 0:
        x0 = random.rand(2)
        x_min = fmin(neg_f, x0)
        if np.abs(f(x_min))> np.abs(f(x_min0)):
            x_min0 = x_min
    if i % 2 == 0:
        x0 = random.rand(2)
        x_min = fmin(f, x0)
        if np.abs(f(x_min))> np.abs(f(x_min0)):
            x_min0 = x_min
delta = 5
x_knots = linspace(x_min0[0] - delta, x_min0[0] + delta, 41)
y_knots = linspace(x_min0[1] - delta, x_min0[1] + delta, 41)
X, Y = meshgrid(x_knots, y_knots)
Z = zeros(X.shape)

for i in range(Z.shape[0]):
    for j in range(Z.shape[1]):
        Z[i][j] = f([X[i, j], Y[i, j]])

ax = Axes3D(figure(figsize=(8, 5)))
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0.4) #maxymalizujemy ta funkcje Z(X,Y)
ax.plot([x_min0[0]], [x_min0[1]], [f(x_min)], color='k', marker='o', markersize=5, label='final') #tutaj tez (wyswietlamy optimum)
ax.legend()
show()