items = [ ['laptop' , 3000, 2], ['smartfon', 1000, 0.350], ['recznik', 2, 0.5], ['budzik', 20, 0.1], ['Szafa', 800, 30] ]

size = 20

from itertools import chain, combinations

def powerset(iterable): #algorytm zachłany O(n), ten ma O(2^n)
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

# for i in powerset(items):
#     print(i)

def knapsack_full(items, size):
    max_combination = None
    max_value = 0

    def value_and_weight(combination):
        value = 0
        weight = 0
        for item in combination:
            value += item[1]
            weight += item[2]
        return value, weight

    for combination in powerset(items):
        value, weight = value_and_weight(combination)
        if weight > size: # ten układ przedmiotów nie mieści się w plecaku
            continue
        if value > max_value: # z pozostałych wybieramy ten o maksymalnej wartości
            max_value = value
            max_combination = combination
    return max_combination

print(knapsack_full(items, size))

items = [ ['A', 6 , 6], ['B', 4, 5], ['C', 4, 5] ]
size = 10

# opt = B + C
print(knapsack_full(items, size))