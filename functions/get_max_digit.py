#  Найти максимальную цифру числа и индекс этой цифры
#  (если несколько вхожение этой цифры,
#  то нужно вывести индекс первого вхождения)

def get_digits(num):
    if num < 0:
        num = abs(num)

    digits = []

    while num > 0:
        last_digit = num % 10
        digits.append(last_digit)
        num = num // 10

    digits.reverse()
    return digits


def get_max_item_and_index(nums):
    max_digit = nums[0]
    index = 0

    for i in range(len(nums)):
        if nums[i] > max_digit:
            max_digit = nums[i]
            index = i

    return (max_digit, index)

res = get_digits(364793792)
print(get_max_item_and_index(res))