K = 132
# 132 = 50 r 82 = 50 + 50 r 32 = 50 + 50 + 20 r 12 = 50 + 50 +20 + 10 + 2

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

dobre = [1, 10, 100, 1000, 10000] #kolejnymi pozycjami w układzie 10
dobre2 = [1, 2, 4, 8, 16, 32, 64] # kolejne pozycje w układzie binarnym
dobre3 = [1,5,10,50, 100, 500] # sprawdzamy czy dany nominał jest podzielny przez wszystkie poprzedzające

# cw1 spróbować uruchomić sobie ten program z innymi parametrami - czyli zmienic kwote, układ nominałów
# cw2 spróbować znaleźć taką parę kwota i nominały, gdzie algorytm zachłanny - zwróci nieoptymalny wynik

K = 8 # 8 = 4 + 4 (2) = 5 + 1 + 1 +1 (4)
nominaly = [1,4,5]
print(change_making_greedy(K,nominaly))

K = 12 # 12 = 4 +4 +4 (3)
nominaly = [1,4,5]
print(change_making_greedy(K,nominaly))

nominaly = [1, 2, 5, 10, 20, 50, 99, 100, 200, 500]
K = 198 # 99 + 99 (2)
print(change_making_greedy(K,nominaly))

## Ustalić K < M. Oszukać K oraz układ nominałów w którym rozwiązanie zachłanne i optymalne
## różnią się ilością monet w sposób najwiekszy

nominaly = [1,3,8,12,21]
K = 24 # 12+12 (2)
print(change_making_greedy(K,nominaly))

nominaly = [1, 2, 3, 5, 9]
K = 10 # 5+5
print(change_making_greedy(K,nominaly))

nominaly = [1,20,51,100,101]
K = 151 # 100+51
print(len(change_making_greedy(K, nominaly)))