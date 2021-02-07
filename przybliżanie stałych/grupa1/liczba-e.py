def e_ciagiem(n): #n+1
    return (1.0+1.0/n)**n
# dzielenie 1/n +1 flo
# dodawania 1.0+1.0/n +1 flo
# potęgowanie **n - n-1 flo
# wykonanie tej funkcji n+1 flo

for i in range(1,100):
    print(f'Iteracja Granicą {i} wartość {e_ciagiem(i)}')

def e_taylor_series(n): #złożoność obliczeniową mamy na poziomie 3n+1 -> 18 iteracji -> 55
    sum = 0
    temp_factorial =1
    for i in range(1,n):
        temp_factorial *= i
        sum += 1/temp_factorial
    return sum+1

for i in range(1,20):
    print(f'Iteracja Taylor {i} wartość {e_taylor_series(i)}')

# przy ilości operacji flo 55


def e_continued_fraction(n):
    tmp = n
    for i in reversed(range(1,n)):
        tmp = i + i / tmp
    return 2+1/tmp

for i in range(1,20):
    print(f'Iteracja Uł-łań {i} wartość {e_continued_fraction(i)}')

# wzór ułamka - 17 iteracja -> 2n+2 = 36
# wzór Taylora - 18 iteracji -> 3n+1 = 55

def e_brother_formula(n): # 8n+1
    sum = 1
    temp_factorial = 1
    for i in range(1,n):
        temp_factorial *= 2*i
        temp_factorial *= (2*i+1)
        sum += (i+1) / temp_factorial
    return 2*sum

for i in range(1,40):
    print(f'Iteracja Brother {i} wartość {e_brother_formula(i)}')

# wzor Brothera 9 iter  = 2.7182818284590446
# wzór ciągowy dał wynik: 2.6935323893818506
# wzór Taylora dał wynik: 2.7182818284590455
# wzór uł. łań dał wynik: 2.7182818284590455 - float, 64bit
# wartość faktyczna     : 2.718281828459045

