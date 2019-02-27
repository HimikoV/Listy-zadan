# Installation, preparation: https://www.youtube.com/watch?v=2y2F7x2TPPA
# from decimal import *
#
# print("Hello Matthew!")
#
# name = "            Matthew Magda"
# greeting = "Hello"
# print(greeting, name.upper())
# print(greeting, name.strip())
#
# x = 1
# y = 10
#
# print(x/y)
# #how to add the description?
# print(f"X/Y: {x/y}")
# #how to do decimal roundings?
# print(f"{x/y:.2f}")
# print(f"{x/y:.4f}")
# print(f"{x/y:.50f}")
# #went wrong? This is casued by approximation in calculations. How to fix this?
# getcontext().prec = 50
# x = Decimal(x)
# y = Decimal(y)
# print(f"{x/y:.50f}")
#
# print('-'*20)
#
# #loops - repeating the operation automatically
# #print numbers from 0 to 4
# for i in range(5):
#     print(i)
#
# print('-' * 20)
#
# #range of numbers from 10 to 15
# for i in range(10, 16):
#     print(i)
#
# print('-' * 20)
#
# #print revision numbers
# for i in range(5):
#     print("Revision number", i + 1)
#
# print('-'*20)
# #print exponential values for y = 2^x
# for i in range(5):
#     print(2**i)
#
# print('-'*20)
#
# #functions
# def exponentialOf2(x):
#     return 2**x
# #print exponential values for y = 2^x using predefined function exponentialOf2
# for i in range(5):
#     print(exponentialOf2(i))
#
# print('-'*20)
#
# # print('Insert your value here:')
# # x = int(input())
# # print('The inserted value times 2 is', 2 * x)
#
# print('-'*20)
#
# #tables
#
# y = [0, 1, 2, 3, 4]
# print(y)
# print(len(y))
#
# print('-'*20)
#

#TASKS (4p)
#1 calculate & print the value of function y = 2x^2 + 2x + 2 for x=[56, 57, ... 100] (0.5p)
y=[]
for x in range(56,101):
    y.append(2*x**2 + 2*x +2)
print(y)
#2 ask the user for a number and print its factorial (1p)
x=int(input("podaj dowolną liczbę:"))
y=1
for i in range(1,x+1):
    y*=i
print(y)

#3 write a function which takes an array of numbers as an input and finds the lowest value. Return the index of that element and its value (1p)
lista_liczb=[122,67,34,98,64,324,65,32,27,125,754,29]
def najmniejsza_liczba(lista):
    najmniejsza=lista[0]
    najmniejsza_index=None
    for i in range(1,len(lista)):
        if lista[i]<najmniejsza:
            najmniejsza=lista[i]
            najmniejsza_index=i
    print("najmniejsza liczba: ", najmniejsza, "index w liscie:",najmniejsza_index)
najmniejsza_liczba(lista_liczb)

#4 looking at lab1-input and lab1-plot files create your own python script that takes a number and returns any chart of a given length.
#the length of a chart is the input to your script. The output is a plot (it doesn't matter if it's a y=x or y=e^x+2x or y=|x| function, use your imagination)
#test your solution properly. Look how it behaves given different input values. (1p)
from numpy import *
from numpy.random import *
from matplotlib.pyplot import *
x=int(input("podaj długość wykresu:"))
y=[]
for i in range(x):
    y.append(randint(-100,100))
plot(y)
show()
#5 upload the solution as a Github repository. I suggest creating a directory for the whole python course and subdirectories lab1, lab2 etc. (0.5p)
#Ad 5 Hint write in Google "how to create a github repo". There are plenty of tutorials explaining this matter.

#my github repository: https://github.com/HimikoV/Listy-zadan