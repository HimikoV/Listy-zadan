#1 Perimeter & field of circles with given radius X for the first circle & Y for the second one. (1p)
from numpy import pi
from cs50 import get_float
X,Y=-1,-1
while X<0 or Y<0:
    X=get_float("R1:")
    Y=get_float("R2:")
def kola(promien):
    Perimeter=2*pi*promien
    Field=pi*promien**2
    return "obwod:", Perimeter,"pole:", Field
print(f" kolo #1: {kola(X)} kolo #2: {kola(Y)}")