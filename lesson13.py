"""
Урок 13: Углубленное изучение списков: генераторы списков.
Циклы в словарях, zip(), enumerate()
"""

# Генераторы списков
"""
Генераторы списков позволяют создавать списки в одну строку кода, что делает их удобными и читаемыми.

Синтаксис:
[выражение for переменная in последовательность if условие]

Пример:
# """
# # Создадим список квадратов чисел от 1 до 10
# squares = [x ** 2 for x in range(1, 11)]
# print(squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#
# # Оставим только чётные квадраты
# even_squares = [x ** 2 for x in range(1, 11) if x % 2 == 0]
# print(even_squares)  # [4, 16, 36, 64, 100]
#
# # Циклы в словарях
# """
# Когда работаем со словарями, часто нужно итерироваться по ключам, значениям или сразу по парам (ключ, значение).
# """
# example_dict = {'apple': 3, 'banana': 5, 'cherry': 2}
#
# # Перебор ключей
# for key in example_dict:
#     print(key)
#
# # Перебор значений
# for value in example_dict.values():
#     print(value)
#
# # Перебор ключей и значений
# for key, value in example_dict.items():
#     print(f"{key}: {value}")
#
# # Функция zip()
# """
# Функция zip() используется для объединения нескольких последовательностей в кортежи.
# """
# names = ["Alice", "Bob", "Charlie"]
# scores = [85, 92, 78]
#
# for name, score in zip(names, scores):
#     print(f"{name} набрал {score} баллов")
#
# # Функция enumerate()
# """
# enumerate() добавляет индекс к элементам последовательности.
# """
# fruits = ["apple", "banana", "cherry"]
# for index, fruit in enumerate(fruits, start=1):
#     print(f"{index}. {fruit}")

# ДОМАШНЕЕ ЗАДАНИЕ (45 задач)

# 1. Создайте список квадратов чисел от 1 до 20 с помощью генератора списков.
s = [x ** 2 for x in range(1, 20)]
print(s)

# 2. Создайте список четных чисел от 1 до 50.
s = [x for x in range(1, 50)]
print(s)
# 3. Создайте список чисел от 1 до 50, заменяя все числа, кратные 3, на 'Fizz'.
list = ['Fizz' if x % 3 == 0 else x for x in range(1, 51)]
print(list)

# 4. Создайте список из первых 10 чисел Фибоначчи с помощью генератора списков и цикла.
s = [0, 1]
for i in range(9):
    s.append(s[-1] + s[-2])
print(s)

# 5. Запросите у пользователя 5 чисел и сохраните их в список, умножив каждое на 2.
s = int(input("число: "))
for i in range(5):
    print(s)
# 6. Запросите у пользователя строку и создайте список, содержащий только гласные буквы.
text = input("Cтрока")
v = [v for ch in text if ch.lower()]
print(v)

# 7. Создайте словарь, где ключи — числа от 1 до 5, а значения — их квадраты.
# 8. Используя zip(), объедините два списка и создайте из них словарь.
# 9. Запросите у пользователя 3 пары ключ-значение и сохраните их в словарь.
# 10. Используя enumerate(), создайте список строк формата "Индекс: значение" из списка чисел.
# 11. Переберите словарь и выведите только те пары, где значение больше 10.
# 12. Создайте генератор списка, содержащий длины слов в заданной строке.
# 13. Переберите список кортежей (имя, возраст) и выведите строки "Имя - возраст".
# 14. Создайте словарь квадратов чисел от 1 до 10.
# 15. Сгенерируйте список кортежей (число, его квадрат) для чисел от 1 до 10.
# 16. Запросите у пользователя 5 чисел. Если введено отрицательное число — прекратите ввод (break).
# 17. Используя zip(), объедините два списка в список кортежей.
# 18. Переберите словарь с разными типами данных и выведите только числовые значения.
# 19. Используя zip(), создайте словарь из двух списков (названия стран и их столицы).
# 20. Запросите у пользователя строку и создайте список её символов в обратном порядке.
# 21. Используйте генератор списка для создания списка кубов чисел от 1 до 10.
# 22. Используйте enumerate(), чтобы вывести все элементы списка с их индексами.
# 23. Переберите словарь и удалите из него элементы, где значение меньше 5.
# 24. Объедините два списка в список кортежей и отсортируйте его по второму элементу.
# 25. Запросите у пользователя числа, добавляйте их в список, пока не введёт 'стоп' (break).
# 26. Запросите у пользователя строку и создайте словарь с подсчетом всех символов.
# 27. Создайте словарь, где ключами будут числа от 1 до 10, а значениями их факториалы.
# 28. Создайте список всех слов из строки, начинающихся с определённой буквы.
# 29. Используя zip(), создайте список пар (число, его факториал) для чисел от 1 до 5.
# 30. Создайте список, содержащий произведения пар чисел из двух списков.
# 31. Используйте генератор списка, чтобы получить все чётные числа из списка.
# 32. Переберите словарь и замените все его значения на их квадраты.
# 33. Используя zip(), создайте список пар значений из трёх списков разной длины.
# 34. Запросите у пользователя 10 чисел, если число нечётное — пропустите его (continue).
# 35. Используйте zip(), чтобы поменять местами ключи и значения в словаре.
# 36. Используя генератор списка, создайте список всех четных чисел от 1 до 100.
# 37. Используя zip() и enumerate(), создайте словарь с индексами элементов списка.
# 38. Создайте список кортежей (буква, её ASCII-код) для всех букв алфавита.
# 39. Используя генератор списка, создайте список всех слов длиннее 5 символов.
# 40. Используя zip(), объедините несколько списков и найдите среднее значение каждого набора значений.

# 41. Используйте set(), чтобы оставить только уникальные элементы в списке чисел.
# 42. Запросите у пользователя строку и создайте множество уникальных символов.
# 43. Используйте set(), чтобы найти пересечение двух списков чисел.
# 44. Используйте defaultdict() для создания словаря со значением по умолчанию.
# 45. Создайте вложенный словарь, где ключ — имя человека, а значение — другой словарь с возрастом и городом проживания.
