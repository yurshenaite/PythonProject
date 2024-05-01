from datetime import datetime, timedelta

# TODO: ДЗ

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
max_day = timedelta(3)


def convert_str_data_to_date_time(month, day):
    return datetime(
        year=2023,
        month=int(month),
        day=int(day)
    )


with open('input.txt', 'r', encoding='UTF-8') as file_r:
    content = file_r.readlines()

until = content[0].strip().split('.')
busy_cells = content[1].strip()
end_day, end_moth = until

start_day, start_moth = ['31', '05']
start_date = convert_str_data_to_date_time(
    start_moth, start_day
)
end_date = convert_str_data_to_date_time(
    end_moth, end_day
)

if (end_date - start_date) < max_day:
    print('YES')
else:
    print('NO', max_day)

"""
31.05

04.06
"""
