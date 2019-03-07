#5 Look at lab2-plot.py and create your own script which takes a number as an input and plots the same 3D wave but with different characteristics
# it's totally up to your imagination how do you want to amend the figure according to the input number (1p)
from cs50 import get_float
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
number=get_float("number for plot:")
x_knots = np.linspace(-number*np.e,number*np.e,201)
y_knots = np.linspace(-number*np.e,number*np.e,201)
X, Y = np.meshgrid(x_knots, y_knots)
R = np.sqrt(X**2+ np.absolute(X) + Y**2 +np.sin(Y)**2)
XX=2*np.cos(R)+np.sin(2*R)*np.cos(60*R)
YY=np.sin(2*R)+np.sin(60*R)
ax = Axes3D(plt.figure(figsize=(10,6)))
ax.plot_surface(XX, YY, R, rstride=1, cstride=1, cmap=plt.cm.rainbow, linewidth=0.7)
plt.show()
