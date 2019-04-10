# TASKS (9p)
#1 Looking at the Euler method above create your own function which takes:
# a (from x' = ax)
# h - step
# T time range
# as an input and plots the solution of a differential equation x' = ax (1p)
#1

import numpy as np
import matplotlib.pyplot as plt

T = 12
h = 1

# x' = ax
a = 0.08
initial_x = 1

t = np.arange(0,T,h)
x = np.zeros(t.shape)
x[0] = initial_x

for i in range(t.size-1):
    x[i+1] = x[i] + h * (a * x[i])
plt.plot(t,x,label="not ideal plot")

#2

h=0.001
t = np.arange(0,T,h)
x = np.zeros(t.shape)
x[0] = initial_x

for i in range(t.size-1):
    x[i+1] = x[i] + h * (a * x[i])
plt.plot(t,x,color="green",label="ideal")
plt.legend()
plt.xlabel('t', fontsize=14)
plt.ylabel('x', fontsize=14)
plt.show()

