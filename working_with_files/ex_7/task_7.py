result = []
with open('input.txt', 'r', encoding='UTF-8') as file_r:
    content = file_r.readlines()

    for line in content:
        if line.strip() != '100':
            result.append(line)

with open('output.txt', 'w', encoding='UTF-8') as file_w:
    file_w.writelines(result)
