#1 Write a function countField which calculates the field of a given figure. It takes the following input parameters:
# - type: circle/rectangle/triangle/rhombus
# - x & optional y.
# For circle we get only x which stands for radius. For Rectangle x&y are the figure's sides, for triangle they are
# accordingly the base and the height and for rhombus - diagonals (4p)
from numpy import pi
from cs50 import get_float
data=[]
def counting(type,x,y=None):
    if type=="circle":
        return pi*(x**2)
    elif type=="triangle" or "rhombus":
        return (1/2)*x*y
    elif type=="rectangle":
        return x*y
def countField():
    type = input("choose type of figure: circle || triangle || rectangle || rhombus    ")
    while type!="circle" and type!="triangle" and type!="rectangle" and type!="rhombus""":
        type = input("you have chose wrong type of figure, try again: circle || triangle || rectangle || rhombus ")

    if type=="circle":
        x=get_float("input an radius:  ")
        return print(counting(type,x))
    elif type=="triangle" or "rhombus" or "rectangle":
        x,y=get_float("input x parameter:  "),get_float("input y parameter:  ")
        return  print(counting(type,x,y))


countField()
print('-'*30)
#2 Write a function which takes sets of parameters of two figures and compares their fields. (4p)
# The exemplary input is [[Circle, 4], [Rhombus, 2, 4]]
# Expected output would be 'The first figure (Circle) has larger field'
def exemplary_input():
    type = input("choose type of figure: circle || triangle || rectangle || rhombus    ")
    while type != "circle" and type!="triangle" and type!="rectangle" and type!="rhombus""":
        type = input("you have chose wrong type of figure, try again: circle || triangle || rectangle || rhombus ")
    if type=="circle":
        x=get_float("input an radius:  ")
        y=None
        data.append([type,x,y])
    elif type=="triangle" or "rhombus" or "rectangle":
        x,y=get_float("input x parameter:  "),get_float("input y parameter:  ")
        data.append([type,x,y])

def which_one(zestaw1,zestaw2):
    if counting(zestaw1[0],zestaw1[1],zestaw1[2])>counting(zestaw2[0],zestaw2[1],zestaw2[2]):
        print(f'The first figure ({zestaw1[0]}) has larger field which is {counting(zestaw1[0],zestaw1[1],zestaw1[2])}')
    else:
        print(f'The second figure ({zestaw2[0]}) has larger field which is {counting(zestaw2[0],zestaw2[1],zestaw2[2])}')

for i in range(2):
    exemplary_input()
which_one(data[0],data[1])
#3 Test your solutions