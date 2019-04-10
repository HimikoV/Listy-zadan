from matplotlib.pyplot import plot, show, legend, figure, cm, contour, clabel,ylim
import numpy as np
import matplotlib.pyplot as plt


def g(x):
    return x**7 -5*x**6 -32*x**5 +178*x**4 +157*x**3-1397*x**2+450*x+1800
def f(x):
    funkcja=np.poly1d([1,-5,-32,178,157,-1397,450,1800])
    pochodna=funkcja.deriv()
    return pochodna(x)
def w(x):
    funkcja = np.poly1d([1, -5, -32, 178, 157, -1397, 450, 1800])
    pochodna = funkcja.deriv(2)
    return pochodna(x)

kozak=0
lista=np.linspace(-5.1,5.1,15)
for initial_point in lista:
    for i in range(5):
        x=initial_point
        a=w(x)
        y=f(x)
        b=y-a*x
        z = np.linspace(-5.1, 5.1, 100)
        t = [0] * 100
        ylim(bottom=-11000, top=12000)
        plt.plot(z, t, color='black')
        plt.plot(z, f(z), color='pink',label='pochodna 1 stopnia')
        plt.plot(z, g(z), color='blue',label='funkcja')
        plt.plot(z,w(z),color='yellow',label='pochodna 2 stopnia')
        plt.plot(z,a*z+b,color='cyan',label='styczna')
        plt.legend()
        plt.show()
        initial_point=-b/a
    if np.abs(g(kozak))<np.abs(g(initial_point)) and initial_point>-5.1 and initial_point<5.1:
        kozak=initial_point
        print(kozak)

### PLOT
x=np.linspace(-5.1,5.1,100)
y=[0]*100
ylim(bottom=-11000,top=12000)
plt.plot(x,y,color='black')
plt.plot(x,f(x),color='pink',label='pochodna 1 stopnia')
plt.plot(x,g(x),color='blue',label='funkcja')
plt.plot(kozak,f(kozak),marker='o',markersize=5,color='yellow',label='miejsce zerowe pochodnej')
plt.plot(kozak,g(kozak),marker='o',markersize=3,color='red',label='optimum')
plt.legend()
plt.show()