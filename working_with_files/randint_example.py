from random import randint

days = []
for _ in range(365):
    days.append(str(randint(5000, 20000)) + '\n')

with open('input.txt', 'w', encoding='UTF-8') as file_w:
    file_w.writelines(days)
