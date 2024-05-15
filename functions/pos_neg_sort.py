# 1127
#
#
# def sort_positive_numbers(lst):
#     positives = sorted([num for num in lst if num >= 0])
#     result = []
#     for num in lst:
#         if num < 0:
#             result.append(num)
#         else:
#             positives.pop(0)
#     return result
#
#
# # Пример использования
# numbers = [5, -1, 3, -2, 8, -6, 10]
# sorted_numbers = sort_positive_numbers(numbers)
# print(sorted_numbers)
#
#
# # TODO:
# def pos_neg_sort(my_list):
#     for i in range(len(my_list)):
#         if my_list[i] > 0:
#             for j in range(len(my_list)):
#                 if my_list[j] > 0 and my_list[i] > my_list[j]:
#                     my_list[i], my_list[j] = my_list[j], my_list[i]
#                     break
#
#
# numbers = [3, -1, 5, -2, 8, -6, 10]
# print(numbers)
# pos_neg_sort(numbers)
# print(numbers)


def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        x = array[i]
        j = i

        while j > 0 and array[j - 1] > x:
            array[j] = array[j - 1]
            j -= 1

        array[j] = x

    return array


print(insertion_sort([6, 5, 3, 8, 9, 1]))  # [1, 3, 5, 6, 8, 9]
# print(insertion_sort([5, 6, -4, 3, -15, 8, -54, 9, -1, 1]))  # [1, 3, 5, 6, 8, 9]

# [6, 5, 3, 8, 9, 1]
