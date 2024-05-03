from datetime import datetime, timedelta

# TODO: ДЗ

max_day = timedelta(3)
total_list = []
list_of_cells = []

def convert_str_data_to_date_time(month, day):
    return datetime(
        year=2023,
        month=int(month),
        day=int(day)
    )


with open('input.txt', 'r', encoding='UTF-8') as file_r:
    content = file_r.readlines()

current_date = content[0].strip().split('.')
busy_cells = int(content[1].strip())
cur_day, cur_moth = current_date

#for cell in busy_cells:
    #list_of_cells.append(cell)
    #number_of_cell, cell_date =

cell_day, cell_moth = ['31', '05']

cur_day_date = convert_str_data_to_date_time(cur_moth, cur_day)
cell_date = convert_str_data_to_date_time(cell_moth, cell_day)

if (cell_date - current_date) > max_day:
    total_list.append('')

with open('output.txt', 'w', encoding='UTF-8') as file_w:
    file_w.writelines(total_list)
