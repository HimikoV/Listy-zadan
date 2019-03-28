from numpy import pi
data=[[1,'circle'],[1,'circle']] #tutaj wpisywac dane
def counting(type,x,y=None):
    if type=="circle":
        return pi*(x**2)
    elif type=="triangle" or "rhombus":
        return (1/2)*x*y
    elif type=="rectangle":
        return x*y
def which_one(zestaw1,zestaw2):
    if zestaw1[0]=='circle' and zestaw2[0]== 'circle':
        if counting(zestaw1[0],zestaw1[1])>counting(zestaw2[0],zestaw2[1]):
            print(f'The first figure ({zestaw1[0]}) has larger field which is {counting(zestaw1[0],zestaw1[1])}')
        else:
            print(f'The second figure ({zestaw2[0]}) has larger field which is {counting(zestaw2[0],zestaw2[1])}')
    elif zestaw1[0]=='circle' and zestaw2!='circle':
        if counting(zestaw1[0],zestaw1[1])>counting(zestaw2[0],zestaw2[1],zestaw2[2]):
            print(f'The first figure ({zestaw1[0]}) has larger field which is {counting(zestaw1[0],zestaw1[1])}')
        else:
            print(f'The second figure ({zestaw2[0]}) has larger field which is {counting(zestaw2[0],zestaw2[1],zestaw2[2])}')
    elif zestaw2[0]=='circle' and zestaw1!='circle':
        if counting(zestaw1[0],zestaw1[1],zestaw1[2])>counting(zestaw2[0],zestaw2[1]):
            print(f'The first figure ({zestaw1[0]}) has larger field which is {counting(zestaw1[0],zestaw1[1],zestaw1[2])}')
        else:
            print(f'The second figure ({zestaw2[0]}) has larger field which is {counting(zestaw2[0],zestaw2[1])}')
    else:
        if counting(zestaw1[0],zestaw1[1],zestaw1[2])>counting(zestaw2[0],zestaw2[1],zestaw2[2]):
            print(f'The first figure ({zestaw1[0]}) has larger field which is {counting(zestaw1[0],zestaw1[1],zestaw1[2])}')
        else:
            print(f'The second figure ({zestaw2[0]}) has larger field which is {counting(zestaw2[0],zestaw2[1],zestaw2[2])}')
try:
    if len(data[0])==0 or len(data[1])==0:
        print('nic nie zrobie z pustej listy :(')
    elif (data[0][0]=='circle' and data[0][2]) or (data[1][0]=='circle' and data[1][2]) :
        print('kolko nie potrzebuje kilku promieni :)')

    else:
        which_one(data[0],data[1])
except:
    if not data:
        print("podana lista jest pusta :)")
    elif len(data)==1:
        print("nie mozna porownac 1 figury z niczym :)")
    elif type(data[0][0])==float or type(data[1][0]==float):
        print('podales dane w zlej kolejnosci')
    elif (data[0][0]!='circle' or data[1][0]!='circle') and (len(data[0])<3 or len(data[1])<3):
        print('podales za malo danych do obliczen :) ')
    else:
        print('cos poszlo nie tak')