# ['nazwa przedmiotu', wartosc, waga ]
items = [ ['lampa od teściowej', 2, 4] , ['złoty zegarek', 4, 2] , ['toster', 2, 2], ['mikrofala', 3, 3],\
          ['pierścionek', 4, 1] ]

size = 4

import copy

def knapsack_greedy(items, size):
    inner_items = copy.deepcopy(items)
    for item in inner_items:
        item.append(item[1]/item[2])
    inner_items.sort(key=lambda x: x[1], reverse = True)
    inner_items.sort(key=lambda x : x[3], reverse = True)
    knapsack = {}
    for item in inner_items:
        if item[2] <= size:
            size -= item[2]
            knapsack[item[0]] = item[:]
    return knapsack

print(knapsack_greedy(items, size))

# przedmiot który po wybraniu marnuje dużo miejsca w plecaku (inne wartościowe przedmioty już się nie zmieszczą)

items = [ ['A', 6, 6], ['B', 4, 5], ['C', 4, 5] ]

size = 10

print(knapsack_greedy(items, size)) # B +C 