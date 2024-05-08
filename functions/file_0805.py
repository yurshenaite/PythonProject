# Функция

# Название
# Параметры != Аргументы
# Тело функции
# Функции всегда возвращают что-то (явно или неявно)

"""
f(x) = 2x + 5
g(x, y, z) = 3x - 2y + 4z - 10

f(4) = 2 * 4 + 5 = 13
f(5) = 15

g(1, 2, 3) = 3 * 1 - 2 * 2 + 4 * 3 - 10 = 1
g(4, 10, 40) = ?

h() = 10 + 5

h() = 15
h() = 15
"""

a = 10
b = 20


# definition - определить
# def - ключевое слово

def say_hello():
    print('Привет, Мир!')
    return -1


def say_hello_ret():
    return 'Используется return!'


# def say_hello_by_name(name='Неизвестно'):
def say_hello_by_name(name):
    print(f'Здравствуйте, {name}')


def check_even_or_odd(num):
    if num % 2 == 0:
        return 'Четное'
    else:
        return 'Нечетное'


def check_even_or_odd_pro(num):
    if num % 2 == 0:
        return 'Четное'
    return 'Нечетное'


res = say_hello()
res_2 = say_hello_by_name('Алекс')
res_3 = say_hello_ret()

print(check_even_or_odd(19))
print(check_even_or_odd(50))

print(res)
print(res_2)
print(res_3)
