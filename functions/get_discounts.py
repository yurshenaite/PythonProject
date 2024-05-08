def get_discounts(numbers, d):
    coeff, *_ = d.split('%')
    coeff = int(coeff) / 100

    result = []
    for num in numbers:
        result.append(num * coeff)

    return result


print(get_discounts([2, 4, 6, 11], "50%"))  # ➞ [1, 2, 3, 5.5]
print(get_discounts([10, 20, 40, 80], "75%"))  # ➞ [7.5, 15, 30, 60]
print(get_discounts([100], "45%"))  # ➞ [45]
