from numpy import *
from numpy.random import *
from matplotlib.pyplot import *
x=int(input("podaj długość wykresu:"))
y=linspace(0,x)
z=((y-10)**2)*tan(y)
plot(y,z,color="green")
show()