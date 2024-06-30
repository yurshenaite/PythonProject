with open('input.txt', 'r', encoding='UTF-8') as file_r:
    content = [
        [int(num) for num in row.strip().split()]
        for row in file_r.readlines()
        if ''.join(row.strip().split()).isdigit()
    ]

    count = 0
    for row in content:
        a, b, c, d = sorted(row)
        if (a + d) <= (b + c):
            count += 1

print(count)
