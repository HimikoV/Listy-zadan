x=float(input("podaj dowolną liczbę:"))
while x<=0 or x%1!=0:
    x=float(input("podałeś niepoprawna liczbe, podaj ja jeszcze raz:"))
y=1
for i in range(1,int(x)+1):
    y*=i
print(y)