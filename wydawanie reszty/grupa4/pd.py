# change_making bedzie miec elementy od 1 do K (włącznie)
# wtedy change_making[i] oznacza optymalny sposob na wypłacenie reszty o wartości i z użyciem tych nominalow


def change_making_dynamic(K, nominaly, maks_size = 1000000):
    change_making = {} # klucz : wartosc
    for i in range(1,K+1):
        change_making[i] = [] #najpierw nie znamy przepisu na zadna z liczb
    for i in range(1,K+1):
        if i in nominaly: #jesli nasza liczba jest wsrod dostepnych nominalow - to najprosciej wydac ja na raz
            change_making[i].append(i)
            continue # nie ma bardziej optymalnego sposobu
        # inaczej rozwazamy wszystkie pary i wyszukujemy najmniejszego zestawu reszt
        min_size = maks_size
        min_ind = 1
        for j in range(1,i): #sprawdzamy czy i = j + (i-j) ile monet w reszcie nam generuje
            # len(change_making[j]) + len(change_making[i-j]) to ilosc monet w reszcie przy probie podzialu
            # i na j + (i-j)
            if min_size > len(change_making[j]) + len(change_making[i-j]):
                min_size = len(change_making[j]) + len(change_making[i-j])
                min_ind = j
        # przypisanie najoptymalniejszego podziału (dowolnego tj pierwszego) do tablicy wyników
        change_making[i] = change_making[min_ind].copy()
        change_making[i].extend(change_making[i-min_ind])
    return change_making

K = 12
nominaly = [1,4,6,10]
print(change_making_dynamic(K,nominaly))
# 2 = 1+1
# 3 = 1+2 = 2+1
# 5 = 1+4 = 2+3
# 7 = 1+6 (2) = 2+5 (4) = 3+4 (4)
# 12 = 1+11 (3) = 2+10 (4) = 3+9 (6) = 4+8 (3) = 5+7 (4) = 6+6 (2)

K = 14 #6+6+2
nominaly = [10,6,2,1]
print(change_making_dynamic(K,nominaly))

K = 14 #7 + 7
nominaly = [1, 7,10, 100, 1000]
print(change_making_dynamic(K,nominaly))
