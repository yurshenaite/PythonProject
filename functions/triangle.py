# https://codechick.io/challenges/336

def triangle(n):
    num_list = []
    prev_num = 0

    for i in range (n+1):
        i = prev_num + i
        num_list.append(i)
        prev_num = i

    num_list.pop(0)
    total = num_list[-1]
    return total


res = triangle(215)
print(res)
