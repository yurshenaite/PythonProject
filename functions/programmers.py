# https://codechick.io/challenges/83

def programmers(one, two, three):
    list = []
    list.append(one)
    list.append(two)
    list.append(three)

    salary_max = max(list)
    salary_min = min(list)

    total = salary_max - salary_min

    return total

print(programmers(143, 33, 526))
