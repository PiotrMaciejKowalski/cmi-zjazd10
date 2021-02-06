def change_making_dynamic(K, nominaly, maks_size = 1000000):
    change_making = {}
    # change making zbiera optymalne sposoby na wydanie kazdej kwoty mniejszej od K
    for i in range(1,K+1):
        change_making[i] = [] #najpierw nie znamy przepisu na zadna z liczb
    for i in range(1,K+1):
        if i in nominaly: #jesli nasza liczba jest wsrod dostepnych nominalow - to najprosciej wydac ja na raz
            change_making[i].append(i)
            continue # nie ma bardziej optymalnego sposobu
        # inaczej rozwazamy wszystkie pary i wyszukujemy najmniejszego zestawu reszt
        min_size = maks_size
        min_ind = 1
        for j in range(1,i):
            # i = j + (i-j)
            # len(change_making[j]) + len(change_making[i-j]) to ilosc monet w reszcie przy probie podzialu
            # i na j + (i-j)
            if min_size > len(change_making[j]) + len(change_making[i-j]):
                min_size = len(change_making[j]) + len(change_making[i-j])
                min_ind = j
        # przypisanie najoptymalniejszego podziału (dowolnego tj pierwszego) do tablicy wyników
        change_making[i] = change_making[min_ind].copy()
        change_making[i].extend(change_making[i-min_ind])
    return change_making

nominaly = [1,7,10]

K = 14 # 14 = 7 + 7
print(change_making_dynamic(K, nominaly))
# 2 = 1+1
# 3 = 2 + 1 = 1+ 2
# 8 = 1+7 (2) = 2+6 (8) = 3+5 (8) = 4+4 (8)
# 14 = 1+13 (5) = 2+12 (5) = 3+11 (5) = 4+ 10 (5) = 5+9 (8) = 6+8(8) = 7+7 (2)

print(change_making_dynamic(10000, nominaly))