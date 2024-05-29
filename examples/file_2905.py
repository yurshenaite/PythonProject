# Типы данных
a: list[int] = [0] * 1000

# Кортеж - это конечный список.

info_of_world = (12, 31)
# info_of_world = [12, 31]
# info_of_world = list(info_of_world)
# info_of_world = tuple(info_of_world)

# info_of_world[1] = 25
print(info_of_world)


def say_hello():
    print('Привет, мир!')


say_hello()  # Вызов функции
print(2 * 3)
