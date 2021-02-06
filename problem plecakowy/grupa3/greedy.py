# ['nazwa przedmiotu', wartosc, waga ]
#items = [ ['a', 2, 4] , ['b', 4, 2] , ['c', 2, 2], ['d', 3, 3], ['e', 4, 1] ]

#size = 6

items = [ ['laptop' , 3000, 2], ['smartfon', 1000, 0.350], ['recznik', 2, 0.5], ['budzik', 20, 0.1], ['Szafa', 800, 30] ]

size = 20

import copy

def knapsack_greedy(items, size):
    inner_items = copy.deepcopy(items)
    for item in inner_items:
        item.append(item[1]/item[2])
    inner_items.sort(key=lambda x : x[3], reverse = True)
    knapsack = {}
    for item in inner_items:
        if item[2] <= size:
            size -= item[2]
            knapsack[item[0]] = item[:]
    return knapsack

print(knapsack_greedy(items, size))

## zachłanny - czy on będzie optymalny? NIE

## bardzo wartościowy przedmiot - spowoduje że w plecaku pozostanie na koniec dużo 'powietrza'

items = [ ['A', 6 , 6], ['B', 4, 5], ['C', 4, 5] ]
size = 10

# opt = B + C
print(knapsack_greedy(items, size))