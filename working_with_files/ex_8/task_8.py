with open('input.txt', 'r', encoding='UTF-8') as file_r:
    content = file_r.readlines()

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

months_data = []
prev_month = 0
for curr_month in days:
    temp = content[prev_month:curr_month + prev_month]
    months_data.append(temp)
    prev_month += curr_month

result = []
for data in months_data:
    total_sum = 0
    for line in data:
        line = int(line.strip())
        total_sum += line
    res = round((total_sum / len(data)))
    result.append(str(res) + '\n')

with open('output.txt', 'w', encoding='UTF-8') as file_w:
    file_w.writelines(result)

print(result)
