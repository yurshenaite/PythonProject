from datetime import datetime, timedelta

MAX_DAY = timedelta(3)
YEAR = 2023


def convert_str_data_to_date_time(day, month, year=YEAR):
    """Конвертирует строковые значения в datetime объект.

    :param day: День.
    :param month: Месяц.
    :param year: Год, по умолчанию равен YEAR.
    :return: Возвращает datetime объект.
    """
    return datetime(
        year=year,
        month=int(month),
        day=int(day)
    )


with open('input.txt', 'r', encoding='UTF-8') as file_r:
    content = file_r.readlines()

# print(content)

until_date, busy_cells_count = content[:2]
until_day, until_month = until_date.strip().split('.')
busy_cells_count = busy_cells_count.strip()

# CTRL + Q
end_date = convert_str_data_to_date_time(until_day, until_month)
# print(end_date.strftime('%d/%m/%Y %H:%M:%S'), type(end_date))

result = []
for cell_data in content[2:]:
    cell_num, date_info = cell_data.strip().split()
    day, month = date_info.split('.')
    # print(cell_num, date_info)
    start_date = convert_str_data_to_date_time(day, month)
    # print(type(start_date))

    if (end_date - start_date) > MAX_DAY:
        result.append(cell_num + '\n')

with open('output.txt', 'w', encoding='UTF-8') as file_w:
    file_w.writelines(result)
