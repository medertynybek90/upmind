#1
# 1. Система входа с ограничением попыток
# Запроси у пользователя логин и пароль.
# У пользователя есть 3 попытки для ввода правильных данных.
# Если неверный ввод трижды, вывести "Доступ заблокирован".


# login = "admin"
# password = "1234"
#
# tries = 3
# login_1 = input("логин: ")
# password_1 = input("пароль: ")
# if login_1 == login and password_1 == password:
#     print("разрешен")
# else:
#     tries = 1
#     login_1 = input("логин: ")
#     password_1 = input("пароль: ")
#     if login_1 == login_1 and password_1 == password:
#         print("Доступ разрешен")
#     else:
#         tries = 1
#         login_1 = input("логин: ")
#         password_1 = input("пароль: ")
#         if login == login and password_1 == password:
#             print("Доступ разрешен")
#         else:
#             print("Доступ заблокирован")


# 2. Разрешение на въезд в страну
# Человек может въехать, если у него есть виза или гражданство, и срок действия паспорта не истек.
# Запроси есть_виза (bool), гражданство (bool), паспорт_действителен (bool).
# Выведи "Разрешен въезд" или "Въезд запрещен".


# viza = bool(int(input("Есть виза:  (1- True , 0- Falce): " )))
# citizenship = bool(int(input("Есть гражданство: (1- True , 0- Falce): ")))
# pasport = bool(int(input("Паспорт действителен: (1- True , 0- Falce): ")))
# if (viza or citizenship) and pasport:
#     print("Разрешен въезд")
# else:
#     print("Въезд запрещен")

# 3. Определение високосного года
# Запроси у пользователя год.
# Год високосный, если делится на 4, но не делится на 100, или делится на 400.
# Выведи "Високосный" или "Обычный".

# year = int(input("lead the year: "))
# if (year % 4 == 0 and year % 100 == 0) or (year % 400 == 0):
#     print("Високосный")
# else:
#     print("Обычный")

# 4. Проверка корректности пароля
# Запроси пароль у пользователя.
# Он должен быть не короче 8 символов и содержать хотя бы одну цифру.
# Выведи "Пароль надежный" или "Пароль слабый".


# password = input("Password: ")
# if password >=str(8): #and int("0, 1, 2, 3, 4, 5, 6, 7, 8, 9,"):
#     print("Пароль надежный")
# else:
#     print("Пароль слабый")
#

# 5. Определение температуры воды
# Запроси температуру воды.
# Выведи "Лед", если <= 0, "Жидкость", если 1–99, "Пар", если >= 100.
# temp = int(input("Введите температуру воды: "))
# if temp <= 0:
#     print("ice")
# elif temp < 1-99:
#     print("liquid")
# elif temp >= 100:
#     print("steam")
# 6. Калькулятор налогов
# Запроси доход.
# Если <= 10 000 – налог 5%, от 10 001 до 50 000 – 10%, больше 50 000 – 20%.
# Выведи сумму налога.

# 7. Игра "Камень, ножницы, бумага"
# Пользователь и компьютер вводят "камень", "ножницы" или "бумага".
# Определи победителя по стандартным правилам.
# comp = input("s")
# user = input()
# 8. Проверка суммы цифр числа
# Запроси у пользователя число.
# Если сумма его цифр четная, выведи "Сумма четная", иначе "Сумма нечетная".
# print(input("number: "))
# sum_of_digits = sum(int(c) for c in число)
# print("Сумма четная" if sum_of_digits % 2 == 0 else "Сумма нечетная")

# 9. Парковка для электромобилей
# Запроси у пользователя тип машины ("электро" или "бензин").
# Если "электро" – парковка бесплатна, иначе 100 рублей.

# car =input("enter the type of the cat: ")
# if car == "e":
#     print("Parking is free")
# else:
#     print("Fine, 100 r")



# 10. Кратность чисел
# Запроси два числа a и b.
# Выведи "a кратно b", если a % b == 0, иначе "a не кратно b".

# a = int(input("Введите число a: "))
# b = int(input("Введите число b: "))
# print("a кратно b" if a % b == 0 else "a не кратно b")

# 11. Проверка на счастливый билет
# Запроси шестизначное число.
# Если сумма первых трех цифр равна сумме последних трех – "Счастливый билет!".

# 12. Время года по номеру месяца
# Запроси номер месяца (1-12).
# Используя тернарный оператор, определи и выведи время года.

# 13. Определение знака числа
# Запроси число.
# Используя тернарный оператор, выведи "+", "-" или "0".
# num = int(input("number: "))
# print("+" if num > 0 else "-" if num < 0 else "0")

# num = int(input("enter a number "))
# print("+" if num > 0 else "-" if num < 0 else "0")
# sing = (сробатают в случае если условия итстина) (сработает в случае если условие ложь)


# 14. Минимальное из трех чисел
# Запроси три числа.
# Используя тернарный оператор, найди минимальное.
# num1 = int(input("число 1"))
# num2 = int(input("число 2"))
# num3 = int(input("число 3"))
# # print("0" if num1 < 0 else num2 < 0 else num3 < 0)
# print(num1 if num1 < num2 and num1 < num3 else num2 if num2 > num3 else num3)
# 15. Оценка успеваемости
# Запроси у пользователя его средний балл (0–100).
# Выведи "Отлично" (>= 85), "Хорошо" (70-84), "Удовлетворительно" (50-69), "Неудовлетворительно" (< 50).

# балл = int(input("Введите средний балл (0-100): "))
# print("Отлично" if балл >= 85 else "Хорошо" if балл >= 70 else "Удовлетворительно" if балл >= 50 else "Неудовлетворительно")
#

# 16. Выбор места в театре
# Запроси у пользователя ряд и место.
# Если ряд <= 3 – "VIP-зона", если 4-10 – "Средний сектор", иначе "Бюджетная зона".

# ряд = int(input("Введите ряд: "))
# print("VIP-зона" if ряд <= 3 else "Средний сектор" if ряд <= 10 else "Бюджетная зона")

# 17. Определение дня недели
# Запроси число от 1 до 7.
# Выведи соответствующий день (1 – Понедельник, ..., 7 – Воскресенье).

# день = int(input("Введите число от 1 до 7: "))
# дни = print(int("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"))
# print(int("день - 1"))

# 18. Подсчет цифр числа
# Запроси число.
# Выведи количество его цифр.
# num = input("number: ")


# 19. Сортировка трех чисел
# Запроси три числа.
# Выведи их в порядке возрастания.

num1 = input("num 1: ")
num2 = input("num 2: ")
num3 = input("num 3: ")
# print("num1" if num2 > num3 and num3 else num2 > num3 if num3:

# 20. Проверка доступа по возрасту
# Запроси возраст пользователя.
# Если возраст меньше 18, вывести "Доступ запрещен", иначе "Доступ разрешен".
# возраст = int(input("Введите ваш возраст: "))
# print("Доступ разрешен" if возраст >= 18 else "Доступ запрещен")