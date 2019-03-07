#3 Check if X is divisible by Y (do it in one line of code), print 'X is divisible by Y' or 'X is not divisible by Y'. (1p)
#Ad 3 Hint- use the "ternary operator" as we did calculating xIsEvenLog above.
from cs50 import get_float
xx=get_float("xx:")
yy=get_float("yy:")
while yy==0:
    yy=get_float("yy:")
print(f"xx is divisible by yy" if xx%yy==0 else "xx is not divisible by yy")
#4 Add rounding for the above x/y operation. Round to 2 decimal points. Hint: look up in Google "python limiting number of decimals". (1p)
print("%s" %round(xx/yy,2)) #nie dziala, dla wszystkich przypadków
print(f"{xx/yy}.2f") #nie działa
print("{0:.2f}".format(xx/yy)) #dziala
print("{0:.1500f}".format(xx/yy))