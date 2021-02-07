# definicja (punkt wyjścia, ale kiepski punkt do obliczeń)

def e_ciagiem(n): # 1+1+n-1 = n+1
    return (1.0+1.0/n)**n
import math
print(e_ciagiem(100000))
print(math.e)

def e_taylor_series(n):
    sum = 0
    temp_factorial =1
    for i in range(1,n): # n*3
        temp_factorial *= i
        sum += 1/temp_factorial
    return sum+1 # 3n+1
for i in range(1,20):
    print(f'Wzór Taylora it {i} wynik {e_taylor_series(i)}')
print('                        ',math.e)

# Taylora - 18 -> 3n+1 = 55 flo
# Ciagowy - 54 -> n +1 = 55 flo

print(e_ciagiem(54))

def e_continued_fraction(n):
    tmp = n
    for i in reversed(range(1,n)): # 2n
        tmp = i + i / tmp
    return 2+1/tmp # 2n + 2

for i in range(1,20):
    print(f'Wzór Uł łań it {i} wynik {e_continued_fraction(i)}')
print('                        ',math.e)

# czy Taylor czy uł łańcuchowy
# T : 18 it -> 3n+1
# U : 17 it -> 2n+2
# Kto wygrał?

def e_brother_formula(n):
    sum = 1
    temp_factorial = 1
    for i in range(1,n): #n*4 + 1
        temp_factorial *= 2*i
        temp_factorial *= (2*i+1)
        sum += (i+1) / temp_factorial
    return 2*sum

for i in range(1,10):
    print(f'Przybliżenie {i} wynosi {e_brother_formula(i)}')
print('                     ', math.e)