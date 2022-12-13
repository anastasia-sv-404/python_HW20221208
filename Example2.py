# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка с нечетными индексами.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint as rnd

# ВАРИАНТ РЕШЕНИЯ AS IS
# def full_randon_int_list(min_value, max_value):  # Заполнение списка заданного размера рандомными int значениями.
#     size = int(input('Введите длину списка: '))
#     list = []
#     for i in range(size):
#         list.append(rnd(min_value, max_value))
#     return list
#
# list = full_randon_int_list(1, 100)
# print(list)
#
# sum = 0
#
# for item in range(len(list)):
#     if item % 2 != 0:
#         sum += list[item]
# print(f'Сумма элементов списка с нечетными индексами равна: {sum}')


# ВАРИАНТЫ РЕШЕНИЙ С ИЗМЕНЕНИЯМИ

# List Comprehension + enumerate
my_list = [rnd(1, 10) for x in range(1, 7)]
print(my_list)

my_list = list(enumerate(my_list))
print(my_list)

sum = 0
for i in range(len(my_list)):
    if my_list[i][0] % 2 != 0:
        sum += my_list[i][1]
print(f'Сумма элементов списка с нечетными индексами равна: {sum}')
