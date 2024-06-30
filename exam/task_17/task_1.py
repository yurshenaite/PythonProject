"""
- Определите количество троек элементов последовательности, в которых
хотя бы один элемент оканчивается на 3 и является трёхзначным числом, а

- сумма всех элементов меньше максимального элемента последовательности,
оканчивающегося на 3 и являющегося трёхзначным числом.

- В ответе запишите количество найденных троек, затем максимальную из сумм элементов таких троек.

В данной задаче под тройкой подразумевается три идущих подряд элемента последовательности.
"""

with open('input.txt', 'r', encoding='UTF-8') as file_r:
    content = [
        row for row in file_r.readlines()
        if row.replace('-', '').strip().isdigit()
    ]

    # сумма всех элементов меньше максимального элемента последовательности,
    # оканчивающегося на 3 и являющегося трёхзначным числом.
    nums_endswith_three = [
        int(row.strip()) for row in content
        if len(row.strip().replace('-', '')) == 3
           and row.strip().endswith('3')
    ]
    max_endswith_three = max(nums_endswith_three)

    # - Определите количество троек элементов последовательности, в которых
    # хотя бы один элемент оканчивается на 3 и является трёхзначным числом, а
    count = 0
    three_seq_max_sum = 0
    for i in range(len(content) - 2):
        seq = [content[i], content[i + 1], content[i + 2]]
        sum_seq = sum([int(num.strip()) for num in seq])

        flag = any(
            [
                row for row in seq
                if len(row.strip().replace('-', '')) == 3
                   and row.strip().endswith('3')
            ]
        )

        if flag and sum_seq < max_endswith_three:
            count += 1
            if sum_seq > three_seq_max_sum:
                three_seq_max_sum = sum_seq

    print(count)
    print(three_seq_max_sum)
