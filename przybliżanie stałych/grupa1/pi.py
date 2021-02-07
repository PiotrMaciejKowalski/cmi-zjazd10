import math
def pi_ciagowo(n):
    return 0.5 * n * math.sin(2*math.pi / n)

for i in range(1,100):
    print(f'Przybliżenie {i} wynosi {pi_ciagowo(i)}')

# pi = 3.1415

def pi_continued_fraction(n):
    tmp = 6
    for i in reversed(range(1,n)):
        tmp = 6 + (2*i+1)**2 / tmp
    return 3+1/tmp

for i in range(1,40):
    print(f'Przybliżenie {i} wynosi {pi_continued_fraction(i)}')