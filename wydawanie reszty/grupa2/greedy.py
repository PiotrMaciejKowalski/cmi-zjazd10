K = 132 # 50 + 82 = 50 + 50 + 32 = 50 + 50 + 20 + 12 = 50 + 50 + 20 + 10 + 2

nominaly = [1, 2, 5, 10, 20, 50]

def change_making_greedy(K, nominaly):
    nominaly.sort(reverse = True)
    coins = []
    for i in nominaly:
        while K >= i:
            coins.append(i)
            K -= i
    return coins

print(change_making_greedy(K, nominaly))

dobrym = [1,10,100,1000,10000] # są to odpowiedniki 1 na kolejnych pozycjach w systemie 10
dobrym2 = [1,2,4,8,16,32,64,128] # bo to odpowiedniki 1 na kolejnych pozycjach w systemie 2
dobrym3 = [1, 2, 5, 10, 20, 50] # nominaly mniejsze są zawsze dzielnikami kolejnych

# cw 1 - spróbować zmienić sobie reszte oraz nominały (zobacz działanie)
# cw 2 - spróbować znaleźć taka resztę i układ nominałów przy którym wynik z alg. zachłannego
#       nie jest optymalny

# 1 brakuje - Problem Frobeniusa - układ nominałów - poszukujemy najmniejszej reszty, której nie uda sie nam wydać

K = 8 # 8 = 4 +4 (2)
nominaly = [1,4,5]
print(change_making_greedy(K,nominaly))

K = 18 # 18 = 9 + 9 (2) # dlaczego nie mamy nominałów 0,99 gr
nominaly = [1, 9, 10]
print(change_making_greedy(K,nominaly))

K = 12 # 12 = 8 + 4 (2) = 4 + 4 + 4 (3)
nominaly = [1,4,8,10]
print(change_making_greedy(K,nominaly))


## K < M. Znaleźć K, nominały takie, że różnica pomiędzy tym w jaki sposób wydaje resztę
## algorytm zachłanny a ile wynosi optymalna był możliwie największy

K = 198 # 99+99 (2)

nominaly = [1, 99, 100]
print(len(change_making_greedy(K,nominaly)))

# greedy - 99 , opt - 2 -> +97


nominaly = [600,500,5]
K = 1000
print(change_making_greedy(K,nominaly))

nominaly = [1,7,8]
K = 14 # 7+7 (2)
print(change_making_greedy(K,nominaly))

