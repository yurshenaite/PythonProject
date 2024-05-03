from datetime import datetime, timedelta

# TODO: ДЗ

MAX_DAY = timedelta(3)
YEAR = 2023


def convert_str_data_to_date_time(month, day, year=YEAR):
    return datetime(
        year=year,
        month=int(month),
        day=int(day)
    )


with open('input.txt', 'r', encoding='UTF-8') as file_r:
    content = file_r.readlines()

print(content)
# Структура content:
# ['04.06\n', '3\n', '1000 01.06\n', '1001 31.05\n', '2007 21.05\n']

# TODO: 1. Срезаем content[:2] получим ['04.06\n', '3\n']
#  2. Распакуем в переменные until_date, busy_cells_count,
#  тогда until_date = '04.06\n' busy_cells_count = '3\n'
#  3. Далее until_date очищаем от пробельных символов и
#  разобъём по символу . (точка), сразу распакуем в переменные
#  until_day, until_month = until_date,
#  тогда until_day = '04', until_month = '06'
#  4. busy_cells_count просто очищаем, чтобы была busy_cells_count = '3'

result = []
for cell_data in content[2:]:
    # Очищаем от пробельных символов и разбиваем по пробелу,
    # чтобы отделить номер ячейки от даты
    cell_num, date_info = cell_data.strip().split()
    print(cell_num, date_info)
    # cell_num = 1000
    # date_info = 01.06

    #  TODO: 5. Далее для date_info повторяем
    #   те же действия, что в шаге 3.
    #   6. Нужно использовать convert_str_data_to_date_time

    # if (until_date - current_date) > MAX_DAY:
    #     result.append(cell_num)

with open('output.txt', 'w', encoding='UTF-8') as file_w:
    file_w.writelines(result)
