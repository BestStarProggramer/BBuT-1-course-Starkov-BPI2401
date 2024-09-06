# def greet(name):
#     print('Салам алейкум, ' + name)
#
# print('Кто ты, воин?')
# greet(input())

# def square(number):
#     return (number**2)
# print('Число:')
# print(square(int(input())))

def max_of_two(x, y):
    return max(x, y)

print("Числа:")
x = int(input())
y = int(input())


print(f'Наибольшее число: {max_of_two(x, y)}')