import math

def pi_ciagowo(n):
    return 0.5 * n * math.sin(2*math.pi / n)

for i in range(3,400):
    print(f'Przybliżenie {i} wynosi {pi_ciagowo(i)}')


def pi_continued_fraction(n):
    tmp = 6
    for i in reversed(range(1,n)):
        tmp = 6 + (2*i+1)**2 / tmp
    return 3+1/tmp

for i in range(1,40):
    print(f'Przybliżenie {i} wynosi {pi_continued_fraction(i)}')

def pi_viete(n):
    root = 0
    result = 1
    for i in range(n):
        root = math.sqrt(2+root)
        result *= root
        result /= 2
    return 2/result

for i in range(1,40):
    print(f'Viete {i} wynosi {pi_viete(i)}')