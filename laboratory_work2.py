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


print('Число:')
def is_prime(number):
    if number <= 1:
        print('Число не является простым')
        return
    for i in range(2, int(number**0.5)+1):
        if number%i == 0:
            print('Число не является простым')
            return
    print('Число простое')
is_prime(int(input()))


