# https://codechick.io/challenges/341

def missing_num(lst):
    lst = str(lst)
    for i in range(11):
        if lst.find(str(i)) == -1:
            index = i

    return index

res = missing_num([7, 2, 3, 6, 5, 9, 1, 4, 8])
print(res)
