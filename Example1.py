# Задайте список из n чисел последовательности (1 + 1/n)^n.

# ВАРИАНТ РЕШЕНИЯ AS IS
# number = int(input('Введите количество чисел N: '))
#
# sum = 0
# list = []
#
# for i in range(1, number + 1):
#     list.append(round((1 + 1 / i) ** i, 2))
# print(f'Список из последовательности количества {number} чисел по формуле (1 + 1/n)^n - это {list}')



# ВАРИАНТЫ РЕШЕНИЙ С ИЗМЕНЕНИЯМИ

# List Comprehension
# number = int(input('Введите количество чисел N: '))
#
# def subsequence(i):
#     return round((1 + 1 / i) ** i, 2)
#
# list = [subsequence(i) for i in range(1, number + 1)]
# print(f'Список из последовательности количества {number} чисел по формуле (1 + 1/n)^n - это {list}')


# List Comprehension + lambda
# number = int(input('Введите количество чисел N: '))
#
# expression = lambda i: round((1 + 1 / i) ** i, 2)
#
# list = [expression(i) for i in range(1, number + 1)]
# print(f'Список из последовательности количества {number} чисел по формуле (1 + 1/n)^n - это {list}')


# List Comprehension + lambda + map
# number = int(input('Введите количество чисел N: '))
#
#
# def subsequence(i):
#     return (1 + 1 / i) ** i
#
#
# my_list = [subsequence(i) for i in range(1, number + 1)]
# my_list = list(map(lambda i: round(i, 2), my_list))
# print(f'Список из последовательности количества {number} чисел по формуле (1 + 1/n)^n - это {my_list}')


# ВОПРОС
# Подскажи, пожалуйста, почему вот такой вариант использования lambda не работает?

# number = int(input('Введите количество чисел N: '))
#
# list = [lambda i: round((1 + 1 / i) ** i, 2) for i in range(1, number + 1)]
# print(f'Список из последовательности количества {number} чисел по формуле (1 + 1/n)^n - это {list}')

# В частности выдает вот такой ответ в терминале:
# [<function <listcomp>.<lambda> at 0x0000017A3E08B130>, <function <listcomp>.<lambda> at 0x0000017A3E08B1C0>, <function <listcomp>.<lambda> at 0x0000017A3E08B250>]
