# 111111111111111111111111111111111111111111111111111111
# def readtype(type = '+'):
#         with open('example_test_trial_demo_beta.txt') as file:
#             if type == '+':
#                 content = file.read()
#                 print(content)
#             elif type == '-':
#                 for line in file:
#                     print(line)
#             else:
#                 print('Введите валидное значение')
#                 readtype(input())
# print('Построчное чтение (-) Чтение целиком (+)')
# readtype(input())

# OR THIS?

# def readtype(type='+'):
#     f = open('example_test_trial_demo_beta.txt')
#     if type == '+':
#         print(*f.readlines())
#     elif type == '-':
#         for line in f:
#             print(line)
#     else:
#         print('Введите валидное значение')
#         readtype(input())
# print('Построчное чтение (-) Чтение целиком (+)')
# readtype(input())

# 222222222222222222222222222222222222222222222222222222222
# first
# file = open('user_input.txt', 'w+')
# file.write(input())
# # Строчка ниже вроде и не нужна :/
# file.close()
# # OR
# with open('user_input.txt', 'w+') as file:
#     file.write(input())

# second
# file = open('testtesttest.txt', 'a')
# file.write(input())
# OR
# with open('testtesttest.txt', 'a') as file:
#     file.write(input())

# 33333333333333333333333333333

# def readtype(type='+'):
#     try:
#         f = open('example_test_trial_demo_beta.txt')
#         if type == '+':
#             print(*f.readlines())
#         elif type == '-':
#             for line in f:
#                 print(line)
#         else:
#             print('Введите валидное значение')
#             readtype(input())
#     except FileNotFoundError:
#         print('Файл не найден :(')

# OR
def readtype(type='+'):
    try:
        with open('example_test_trial_demo_beta.txt') as file:
            if type == '+':
                content = file.read()
                print(content)
            elif type == '-':
                for line in file:
                    print(line)
            else:
                print('Введите валидное значение')
                readtype(input())
    except FileNotFoundError:
        print('Файл не найден :(')

print('Построчное чтение (-) Чтение целиком (+)')
readtype(input())