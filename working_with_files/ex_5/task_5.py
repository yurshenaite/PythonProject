with open('input.txt', 'r', encoding='UTF-8') as file_r:
    content = file_r.readlines()

with open('output.txt', 'w', encoding='UTF-8') as file_w:
    try:
        num_1 = int(content[0].strip())
        num_2 = int(content[1].strip())
        num_3 = int(content[2].strip())
        res = (num_1 / num_2) + num_3
    except ZeroDivisionError:
        file_w.write('divison by 0')
    except ValueError:
        file_w.write('data error')
    else:
        file_w.write(str(res))
