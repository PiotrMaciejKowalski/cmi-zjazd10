
from decimal import *
getcontext().prec = 100

def e_taylor_series_decimal(n):
    sum = Decimal(0)
    temp_factorial = Decimal(1);
    for i in range(1,n):
        temp_factorial *= Decimal(i)
        sum += Decimal(1)/temp_factorial
    return sum+1
def e_continued_fraction_decimal(n):
    tmp = Decimal(n)
    for i in reversed(range(1,n)):
        tmp = Decimal(i) + Decimal(i) / tmp
    return 2+1/tmp
def e_brother_formula_decimal(n):
    sum = Decimal(1)
    temp_factorial = Decimal(1)
    for i in range(1,n):
        temp_factorial *= Decimal(2*i)
        temp_factorial *= Decimal(2*i+1)
        sum += Decimal(i+1) / temp_factorial
    return Decimal(2)*sum

for i in range(1,20):
    print(f'''Przybliżenie {i} \nwynosi {e_taylor_series_decimal(i)} \nwynosi {e_continued_fraction_decimal(i)}\nwynosi {e_brother_formula_decimal(i)}    ''')
