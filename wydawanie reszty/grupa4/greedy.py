K = 12 # kwota do wydania

nominaly = [1,4,6,10,40] # nominałom do wydawania

def change_making_greedy(K, nominaly): # złożoność O(n)
    nominaly.sort(reverse = True) #nominaly posortuj malejaco
    coins = [] #uzupelniana nominalami w miare jak wydajemy reszt
    for i in nominaly:
        while K >= i: #czy kwota do wydania przekracza wybrany nominal
            coins.append(i)
            K -= i
    return coins

print(change_making_greedy(K, nominaly))

# znaleźć sytuację kiedy dana kwota zostala przez ten algorytm wyliczona w spobób nieoptymalny.

# przykłady
K = 12
nominaly = [1,4,6,10]
print(change_making_greedy(K, nominaly))

K = 8 # 4+4, 6+1+1
nominaly = [1,4,6,10]
print(change_making_greedy(K, nominaly))

K = 14 #6+6+2
nominaly = [10,6,2,1]
print(change_making_greedy(K, nominaly))

K = 1031
nominaly = [1,2,4,8,16,32,64, 128, 256, 512, 1024]

K = 14 #7 + 7
nominaly = [1, 7,10, 100, 1000]
print(change_making_greedy(K, nominaly))

K = 36 # 9 + 9 + 9 + 9 <- 4
nominaly = [ 1, 9 , 10]
print(change_making_greedy(K, nominaly))

# odszukać dla K < M, taką kwotę i układ nominalów, że różnica pomiędzy ilością monet rozwiązania
# optymalnego oraz zachłannego jest możliwie największa

# zachłanne - 9
# optymalne - 4
# różnica +5
