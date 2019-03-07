#2 Find X & Y that satisfy: X is divisible by Y and both X & Y are even. (0.5p)
from cs50 import get_int
iks=get_int("iks:")
igrek=get_int("igrek:")
while iks%igrek!=0 or iks%2!=0 or igrek%2!=0 or iks==0 or igrek==0:
    iks = get_int("iks:")
    igrek = get_int("igrek:")
print(f"iks:{iks} igrek:{igrek}")