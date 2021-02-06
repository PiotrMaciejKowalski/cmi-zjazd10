

def change_making_dynamic(K, nominaly, maks_size = 1000000):
    change_making = {} # rozwiązania optymalne wszystkich problemów aż do K
    for i in range(1,K+1):
        change_making[i] = [] #najpierw nie znamy przepisu na zadna z liczb
    for i in range(1,K+1):
        if i in nominaly: #jesli nasza liczba jest wsrod dostepnych nominalow - to najprosciej wydac ja na raz
            change_making[i].append(i)
            continue # nie ma bardziej optymalnego sposobu
        # inaczej rozwazamy wszystkie pary i wyszukujemy najmniejszego zestawu reszt
        min_size = maks_size
        min_ind = 1
        for j in range(1,i): # i = j + (i-j)
            # len(change_making[j]) + len(change_making[i-j]) to ilosc monet w reszcie przy probie podzialu
            # i na j + (i-j)
            if min_size > len(change_making[j]) + len(change_making[i-j]):
                min_size = len(change_making[j]) + len(change_making[i-j])
                min_ind = j
        # przypisanie najoptymalniejszego podziału (dowolnego tj pierwszego) do tablicy wyników
        change_making[i] = change_making[min_ind].copy()
        change_making[i].extend(change_making[i-min_ind])
    return change_making

K = 18 # 18 = 9 + 9 (2) # dlaczego nie mamy nominałów 0,99 gr
nominaly = [1, 9, 10]
print(change_making_dynamic(K,nominaly))
# 1 -> 1 (1)
# 2 -> 2 = 1 + 1
# 11 -> 11 = 1 + 10 (2) = 2+9 (3) = 3+8 (11) = 4+ 7 (11) = 5+6 (11)
# 18 -> 18 = 17 + 1 (9) = 16 + 2 (9) = 15 + 3 (9) = 14+4 (9) = 13 + 5 (9) = 12 + 6 (9) = 11 + 7 (9) = 10 + 8 (9) = 9+9 (2)