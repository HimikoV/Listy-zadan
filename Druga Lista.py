#alternative way of reading inputs - using library:
#in terminal/command line write pip install cs50
#restart your IDE (Pycharm, VSCode, whatever it is)
#remember to use python3 in your project
#add "from cs50 import get_int" to the top of your file
from cs50 import get_int,get_float,get_char
# x = get_int("x: ")
# y = get_int("y: ")
#
# print("x:")
# x = int(input())
# print("y:")
# y = int(input())
#
# print("-"*10)
# print(x + y)
# print("-"*10)
#
# print(f"x + y: {x + y}")
# print(f"x - y: {x - y}")
# print(f"x * y: {x * y}")
# print(f"x / y: {x / y}")
# print(f"x modulo y: {x % y}")
#
# xIsEven = x % 2 == 0
# xIsEvenLog = 'X is even' if xIsEven else 'X is not even'
# print(xIsEvenLog)


# TASKS (8p)- calculate & print:
#0 Use alternative way of reading inputs - using library (0.5p)
x=get_int("podaj liczbe całkowita:") #tylko całkowite liczby
y=get_char("podaj litere:") #tylko 1 litera
z=get_float("podaj liczbe zmiennoprzecinkowa:") #jaka kolwiek liczba
print(f"int:{x} char:{y} float:{z}")
print('-'*15)
#1 Perimeter & field of circles with given radius X for the first circle & Y for the second one. (1p)
from numpy import pi
X=get_float("R1:")
Y=get_float("R2:")
def kola(promien):
    Perimeter=2*pi*promien
    Field=pi*promien**2
    return print(f"obwod: {Perimeter},pole: {Field}")
print(f" kolo #1: {kola(X)} kolo #2: {kola(Y)}")
print('-'*15)
#2 Find X & Y that satisfy: X is divisible by Y and both X & Y are even. (0.5p)
iks=get_int("iks:")
igrek=get_int("igrek:")
while iks%igrek!=0 or iks%2!=0 or igrek%2!=0 or iks==0 or igrek==0:
    iks = get_int("iks:")
    igrek = get_int("igrek:")
print(f"iks:{iks} igrek:{igrek}")
print('-'*15)
#3 Check if X is divisible by Y (do it in one line of code), print 'X is divisible by Y' or 'X is not divisible by Y'. (1p)
#Ad 3 Hint- use the "ternary operator" as we did calculating xIsEvenLog above.
xx=get_float("xx:")
yy=get_float("yy:")
print(f"xx is divisible by yy" if xx%yy==0 else "xx is not divisible by yy")
print('-'*15)
#4 Add rounding for the above x/y operation. Round to 2 decimal points. Hint: look up in Google "python limiting number of decimals". (1p)
print("%s" %round(xx/yy,2)) #nie dziala, dla wszystkich przypadków
print(f"{xx/yy}.2f") #nie działa
print("{0:.2f}".format(xx/yy)) #dziala
print("{0:.1500f}".format(xx/yy))
print('-'*15)
#5 Look at lab2-plot.py and create your own script which takes a number as an input and plots the same 3D wave but with different characteristics
# it's totally up to your imagination how do you want to amend the figure according to the input number (1p)
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

#6 Test your code. Check various edge cases. In other words: does your program (1, 3, 4 & 5)work for all input values?
# In case of task 4  do not forget to round to different amount of decimals and see if it still works.(3p)
