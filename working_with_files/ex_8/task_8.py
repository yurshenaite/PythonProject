result = []
counter = 0
with open('input.txt', 'r', encoding='UTF-8') as file_r:
    content = file_r.readlines()

month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
first = month[0]
second = month[1]
third = month[2]
fourth = month[3]
fifth = month[4]
sixth = month[5]
seventh = month[6]
eighth = month[7]
ninth = month[8]
tenth = month[9]
eleventh = month[10]
twelfth = month[11]


for line in content[:first]:
    line = int(line.strip())
    counter += line
total_1 = round((counter / 31))
result.append(total_1)

for line in content[first:second]:
    line = int(line.strip())
    counter += line
total_2 = round((counter / 28))
result.append(total_2)

for line in content[second:third]:
    line = int(line.strip())
    counter += line
total_3 = round((counter / 31))
result.append(total_3)

for line in content[third:fourth]:
    line = int(line.strip())
    counter += line
total_4 = round((counter / 30))
result.append(total_4)

for line in content[fourth:fifth]:
    line = int(line.strip())
    counter += line
total_5 = round((counter / 31))
result.append(total_5)

for line in content[fifth:sixth]:
    line = int(line.strip())
    counter += line
total_6 = round((counter / 30))
result.append(total_6)

for line in content[sixth:seventh]:
    line = int(line.strip())
    counter += line
total_7 = round((counter / 31))
result.append(total_7)

for line in content[seventh:eighth]:
    line = int(line.strip())
    counter += line
total_8 = round((counter / 31))
result.append(total_8)

for line in content[eighth:ninth]:
    line = int(line.strip())
    counter += line
total_9 = round((counter / 30))
result.append(total_9)

for line in content[ninth:tenth]:
    line = int(line.strip())
    counter += line
total_10 = round((counter / 31))
result.append(total_10)

for line in content[tenth:eleventh]:
    line = int(line.strip())
    counter += line
total_11 = round((counter / 30))
result.append(total_11)

for line in content[eleventh:twelfth]:
    line = int(line.strip())
    counter += line
total_12 = round((counter / 31))
result.append(total_12)


with open('output.txt', 'w', encoding='UTF-8') as file_w:
    file_w.writelines(str(result) + '\n')