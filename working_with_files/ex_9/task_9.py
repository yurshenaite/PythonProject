import os


directory_name = 'simple'
file_name = 'output.txt'

os.mkdir(directory_name)  # создание директории
output_file_path = os.path.join(directory_name, file_name)

total = []
with open('input.txt', 'r', encoding='UTF-8') as file_r:
    content = file_r.readlines()

for i in range(len(content)):
    if i % 2 == 1:
        total.append(content[i])

with open(output_file_path, 'w', encoding='UTF-8') as file_w:
    file_w.writelines(total)
