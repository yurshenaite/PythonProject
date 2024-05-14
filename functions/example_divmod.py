# //
# %

num = 567

first = (num // 100) % 10
second = (num // 10) % 10
third = num % 10

big_num = 3479

first = (big_num // 10 ** (4 - 1)) % 10
second = (big_num // 10 ** (4 - 2)) % 10
third = (big_num // 10 ** (4 - 3)) % 10
four = (big_num // 10 ** (4 - 4)) % 10

# print(first, second, third, four, sep='\n')


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
        if nums[i] >= max_digit:
            max_digit = nums[i]
            index = i

    return (max_digit, index)


res = get_digits(48578)
print(get_max_item_and_index(res))

# print(get_digits(4578))
# print(get_digits(-78))
print(get_digits(104674357547854371))
