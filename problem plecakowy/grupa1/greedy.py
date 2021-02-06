# ['nazwa przedmiotu', wartosc, waga ]
items = [ ['toster', 2, 4] , ['biżuteria', 4, 2] , ['kamera', 2, 2], ['laptop', 3, 3],
          ['dzieło sztuki', 4, 1] ]
# 4 + 2 + 4 -> 10; 2+2+1 -> 5
# 4 + 3 + 4 -> 11; 2+3+1 -> 6
size = 6

import copy

def knapsack_greedy(items, size): # O(n) - liniowy
    inner_items = copy.deepcopy(items)
    for item in inner_items:
        item.append(item[1]/item[2]) # ratio, stosunek wartosć / wage
    inner_items.sort(key=lambda x : x[1], reverse = True)
    inner_items.sort(key=lambda x : x[3], reverse = True)
    knapsack = {}
    for item in inner_items:
        if item[2] <= size:
            size -= item[2]
            knapsack[item[0]] = item[:]
    return knapsack

print(knapsack_greedy(items, size))

## Czy zawsze opłaca się być zachłannym? Jest optymalny?

items = [ ['A', 6, 6], ['B', 4 , 5], ['C', 4, 5]]
size = 10
print(knapsack_greedy(items, size)) # A -> 6
# opt := B+C -> 4+4 = 8
