with open('input.txt', 'r', encoding='UTF-8') as file_r:
    content = file_r.readline()

with open('output.txt', 'w', encoding='UTF-8') as file_w:
    file_w.write(content.upper())
