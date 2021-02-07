def e_ciagiem(n):
    return (1.0+1.0/n)**n # 1+1+(n-1) = n+1
import math
print(e_ciagiem(10000))
print(math.e)

# definicja matematyczna to nie zawsze dobry punkt wyjścia do obliczeń
# własności liczby e

def e_taylor_series(n):
    sum = 0
    temp_factorial =1
    for i in range(1,n): # n*3
        temp_factorial *= i
        sum += 1/temp_factorial
    return sum+1 # 3n+1

for i in range(1,19):
    print(f'Taylor {i} wynik {e_taylor_series(i)}' )
print('               ', math.e)

# Granicy 54 iteracji - n  + 1 = 55 flo
# Taylora 18 iteracji - 3n+1 = 55 flo

print(e_ciagiem(54))

def e_continued_fraction(n):
    tmp = n
    for i in reversed(range(1,n)): # 2n+2
        tmp = i + i / tmp
    return 2+1/tmp

for i in range(1,19):
    print(f'Ułamek {i} wynik {e_continued_fraction(i)}' )
print('               ', math.e)

# Ułamek  17 iteracji - 2n+2
# Taylora 18 iteracji - 3n+1 = 55 flo
# Który algorytm wygrywa?

def e_brother_formula(n):
    sum = 1
    temp_factorial = 1
    for i in range(1,n):
        temp_factorial *= 2*i
        temp_factorial *= (2*i+1)
        sum += (i+1) / temp_factorial
    return 2*sum

for i in range(1,10):
    print(f'Brother {i} wynosi {e_brother_formula(i)}')
print('                ', math.e)
print(f'Ułamek {19} wynik  {e_continued_fraction(19)}' )