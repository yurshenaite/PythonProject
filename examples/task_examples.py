from itertools import combinations

exp = ['1', '+', '2', '-', '3', '*', '4', '/', '5', '6']
print(list(combinations(exp, 4)))

data = [4, 5, 3, 1, 9, 0, 7, 2, 6, 8]

"""
Отсортировано по возрастанию:
0 < 1 < 2 < 3 < 4 < 5 < 6 < 7 < 8 < 9

Отсортировано по убыванию:
9 > 8 > 7 > 6 > 5 > 4 > 3 > 2 > 1 > 0
"""


def bubble_sort(array, reverse=False):
    n = len(array)

    for i in range(n):
        for j in range(0, n - i - 1):
            if reverse:
                if array[j] < array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
            else:
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]


bubble_sort(data, reverse=True)
print(data)

# 8 -> 10
# 8 -> 1000
# 6 -> 012

print(bin(8))

"""
2 - 01
3 - 012
4 - 0123
8 <-> 01234567
10 <-> 0123456789
16 <-> 0123456789ABCDEF
"""

example = '854AFC'
print(int(example, 16))
