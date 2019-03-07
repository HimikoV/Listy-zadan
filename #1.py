#1 calculate & print the value of function y = 2x^2 + 2x + 2 for x=[56, 57, ... 100] (0.5p)
y=[]
for x in range(56,101):
    y.append(2*x**2 + 2*x +2)
print(y)