# mam jakąś kwotę do wypłaty
## 79zł
## 50 zł + 20 zł + 5zł + 2zł + 2zł = 79zł

K = 69
nominaly = [1, 2, 5, 10, 20, 50] # dobry układ nominalow - zauważmy że każdy nominal jest podzielny przez każdy mniejszy
nominaly1 = [ 1,10, 100, 1000] #dlatego, że liczby te odpowiadają kolejny pozycjom w układzie 10tkowym
nominaly2 = [ 1,2,4,8,16,32,64] # to samo ale w dwojkowym
nominaly3 = [1,5,10,50]
nominaly4 = [1,2,10,20,100,200]

def change_making_greedy(K, nominaly): # ma złożoność O(n)
    nominaly.sort(reverse = True)
    coins = []
    for i in nominaly:
        while K >= i: # kwota do wypłacenie jest wieksza od nominalu ktory rozwazamy
            coins.append(i)
            K -= i
    return coins

print(change_making_greedy(K, nominaly))

# ćw - zmienić K oraz nominaly i zobaczyc czy dziala
# ćw - poszukali K oraz nominaly gdzie ten algorytm nie wygeneruje optymalnego rozwiazania
# a znaleźliby układ który ma równowartościowe - tez warto się zgłosić !

nominaly = [1,7,10]
K  = 9 # 4+4+1
print(change_making_greedy(K, nominaly))

K = 14 # 14 = 7 + 7
print(change_making_greedy(K, nominaly))

nominaly = [1,4,7,12]
K = 14 # 14 = 7 + 7
print(change_making_greedy(K, nominaly))

# K < M, znalezieniu kwoty oraz układu nominalow w ktorym różnica pomiędzy
# ilością monet rozwiazania zachłannego a optymalnego jest możliwie największa
# 3-2 = 1 <-

nominaly = [1,5,7,11]
K = 10 # 5+5
print(change_making_greedy(K, nominaly))
K = 15 # 5+5+5, 7+7+1
print(change_making_greedy(K, nominaly))

nominaly = [1, 99, 100]
K = 198 # 99+99 -> 99-2 = 97
print(len(change_making_greedy(K, nominaly)))

nominaly = [1,7,10]
print(change_making_greedy(10000, nominaly))