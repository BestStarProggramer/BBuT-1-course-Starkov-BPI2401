# def greet(name):
#     print('Салам алейкум, ' + name)
#
# print('Кто ты, воин?')
# greet(input())

# def square(number):
#     return (number**2)
# print('Число:')
# print(square(int(input())))

# def max_of_two(x, y):
#     return max(x, y)
#
# print("Числа:")
# x = int(input())
# y = int(input())
#
#
# print(f'Наибольшее число: {max_of_two(x, y)}')

# def describe_person(name, age=30):
#     print(f'Имя: {name}, возраст: {age}')
# describe_person('one')


def is_prime(number):
    if number <= 1:
        return 0
    for i in range(2, int(number**0.5)+1):
        if number%i == 0:
            return 1

def prime(number):
    a = []
    for i in range(0, number+1):
        a.append(i)
    for i in a:
        if is_prime(i):
            for j in range(i, len(a), i):
                a[j] = 0
    a = a[2:]
    a = set(a)
    a.remove(0)
    print(a)

prime(50)



