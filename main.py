'''Написать программу, которая:
- Создаёт случайный список из 20 значений по 4 случайных целых чисел от -10 до 10.
- Находит все уникальные комбинации (порядок значений не учитывать) из этих значений и выводит их в виде списка кортежей.
- Пользователь вводит целое число.
- Вычисляет количество пар, чья сумма меньше заданного пользователем значения.'''
import random  # Импортируем модуль `random` для работы со случайными числами
random_list = [[random.randint(-10, 10) for _ in range(4)] for _ in range(20)]  # Создаем список random_list с помощью вложенных генераторов списков
unique_pairs = []  # Создаем пустой список `unique_pairs` для хранения уникальных пар
for i in range(len(random_list)):  # Внешний цикл проходит по всем подспискам random_list
  for j in range(len(random_list[i])):  # Внутренний цикл проходит по каждому числу в текущем подсписке
    for k in range(j + 1, len(random_list[i])):  # Цикл проходит по оставшимся числам в текущем подсписке, начиная с элемента после j
      pair = tuple(sorted((random_list[i][j], random_list[i][k])))  # Создаем пару из двух чисел, сортируем ее, чтобы гарантировать уникальность, и преобразуем в кортеж
      if pair not in unique_pairs:  # Проверяем, не встречалась ли эта пара уже в unique_pairs
        unique_pairs.append(pair)  # Если пара новая, добавляем ее в список unique_pairs
print("Уникальные пары:")  # Выводим заголовок "Уникальные пары:"
for i in range(0, len(unique_pairs), 5):  # Цикл проходит по индексам unique_pairs с шагом 5, чтобы выводить пары по 5 штук в строке
  print(" ".join(str(pair) for pair in unique_pairs[i:i+5]))  # Выводим "кусок" списка unique_pairs из 5 элементов, преобразовывая каждую пару в строку и соединяя их пробелом
user_value = int(input("Введите целое число: "))  # Запрашиваем у пользователя целое число
count = 0  # Создаем счетчик для пар, сумма которых меньше user_value
for pair in unique_pairs:  # Цикл проходит по каждой уникальной паре
  if sum(pair) < user_value:  # Проверяем, меньше ли сумма элементов пары заданного пользователем значения
    count += 1  # Если условие выполняется, увеличиваем счетчик count
print(f"Количество пар, сумма которых меньше {user_value}: ", count)  # Выводим результат - количество пар, сумма элементов которых меньше user_value