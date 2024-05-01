with open('input.txt', 'r', encoding='UTF-8') as file_r:
    content = file_r.readlines()

with open('output.txt', 'w', encoding='UTF-8') as file_w:
    try:
        N = int(content[0].strip())
    except ValueError:
        file_w.write('ERROR')
    else:
        if N == len(content) - 1:
            file_w.write('YES')
        else:
            file_w.write('NO')
