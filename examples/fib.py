with open('fib.txt', 'r', encoding='UTF-8') as file:
    n = int(file.readline())
    a = int(file.readline())
    b = int(file.readline())

    for i in range(3, n + 1):
        current = int(file.readline())

        if current != (a + b):
            print('Incorrect', current)
            break

        a = b
        b = current
