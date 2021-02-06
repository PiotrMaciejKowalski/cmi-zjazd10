items = [ ['smartwatch', 500, 0.2] , ['telefon', 100, 0.4] , ['suche kwiaty', 0.1, 0.2],
          ['suunto 5' , 1192.88, 0.066], ['kostka masła', 4.99, 0.2] ]
size = 0.5

from itertools import chain, combinations

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


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

    for combination in powerset(items): # O(2^n)
        value, weight = value_and_weight(combination)
        if weight > size: #tego układu przedmiotów nie upakujemy w plecaku
            continue
        if value > max_value:
            max_value = value
            max_combination = combination
    return max_combination

print(knapsack_full(items, size))

dom = [ ['A', 6, 6], ['B', 4, 5], ['C', 4,5] ]
rozmiar = 10
print(knapsack_full(dom, rozmiar))