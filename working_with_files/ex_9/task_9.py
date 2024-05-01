import os

# TODO: ДЗ

chars = ['a\n', 'b\n', 'c\n']

directory_name = 'simple'
file_name = 'output.txt'

os.mkdir(directory_name)  # создание директории

output_file_path = os.path.join(directory_name, file_name)

with open(output_file_path, 'w', encoding='UTF-8') as file_w:
    file_w.writelines(chars)
