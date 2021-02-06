# ['nazwa przedmiotu', wartosc, waga ]
items = [ ['smartwatch', 500, 0.2] , ['telefon', 100, 0.4] , ['suche kwiaty', 0.1, 0.2],
          ['suunto 5' , 1192.88, 0.066], ['kostka masła', 4.99, 0.2] ]

size = 0.5

import copy

def knapsack_greedy(items, size): # algorytm O(n)
    inner_items = copy.deepcopy(items)
    for item in inner_items:
        item.append(item[1]/item[2]) # ratio
    inner_items.sort(key=lambda x : x[3], reverse = True)
    knapsack = {}
    for item in inner_items:
        if item[2] <= size:
            size -= item[2]
            knapsack[item[0]] = item[:]
    return knapsack

print(knapsack_greedy(items, size))

# Czy zawsze opłaca się być zachłannym złodziejem?

# Kiedy weźmiemy duży przedmiot (bardzo wartościowy), ale który zostawi nam dużo
# 'powietrza' w plecaku

dom = [ ['A', 6, 6], ['B', 4, 5], ['C', 4,5] ]
rozmiar = 10
print(knapsack_greedy(dom, rozmiar))
# greedy -> 6, opt -> 8 (B+C)