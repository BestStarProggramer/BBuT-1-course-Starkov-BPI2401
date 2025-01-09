# # 111111111111111111111111111111111
# from math import sqrt
#
# from Success_package.basic_sum import summa
# from Success_package.farewell import polite_goodbye
# from Success_package.greet import polite_hello
#
# print(int(sqrt(49)))
#
# from datetime import date
# today = date.today()
# if today.day % 10 == 1:
#     ending = 'st'
# elif today.day % 10 == 2:
#     ending = 'nd'
# elif today.day % 10 == 3:
#     ending = 'rd'
# else:
#     ending = 'th'
# print(today.strftime(f'The %#d-{ending} of %B, %Y'))
#
# print()
# # 222222222222222222222222222222222222222222222
# import my_module
# my_module.prediction(18)

print()
# 33333333333333333333333333333333
import Success_package
Success_package.greet.polite_hello('Maksim')
Success_package.farewell.polite_goodbye('Jack')
Success_package.basic_sum.summa([3, 4, 2])