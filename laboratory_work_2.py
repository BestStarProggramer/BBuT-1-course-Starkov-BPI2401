# Задание 1: Написание простых функций


def greet(name):
    print(f"Привет, {name}!")


def square(number):
    return number ** 2


def max_of_two(x, y):
    return x if x > y else y



"""
# Задание 2: Работа с аргументами функций

def describe_person(name, age=30):
    print(f"Имя: {name}, Возраст: {age}")


# Задание 3: Использование функций для решения алгоритмических задач


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
"""
