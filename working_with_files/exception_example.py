# try - пробовать
# except - поймать
# else - тогда
# finally - финиш, итог, Завершение

try:
    num = int(input('Введите число: '))
    print(1 / num)

except (ValueError, ZeroDivisionError) as err:
    print('Ошибка', err)
else:
    print('Успех', num * 2)
finally:
    print('Завершение программы')

print('a')