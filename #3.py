#3 write a function which takes an array of numbers as an input and finds the lowest value. Return the index of that element and its value (1p)
from numpy import where,array
lista_liczb=array([1,1,1,2])
def najmniejsza_liczba(lista):
    najmniejsza=lista[0]
    for i in range(1,len(lista)):
        if lista[i]<najmniejsza:
            najmniejsza=lista[i]
    najmniejsza_index=where(lista==najmniejsza)[0]
    print("najmniejsza liczba: ", najmniejsza, "|index w liscie:",najmniejsza_index)
print('lista liczb:',lista_liczb)
najmniejsza_liczba(lista_liczb)