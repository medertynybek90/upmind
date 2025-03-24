# from kivy.parser import parse_int
#
# student = {                    # создания словаря # Пустой словарь my_dict = {}
#     "name": "Alex",
#     "age": 21,
#     "City": "Moscow"
# }
# print(student["age"])
# print(student.get(333, "default value")) #дефолтоное значение в случае отсуствие ключа в аргументе
# print(student.get("status"))
#
# print(student.keys()) # возвращение все ключи в словоря
# print(student.values()) # возварщает все ключи словоря
# print(student.items()) # возвращает все пары (ключ, згначения)
# student.update({"first key": "first"}) # обновляет словарь
# print(student)
# print(student.pop("name"))                # удоляет ключи возвращает его значения
# # student.clear()                        # очищает словарь
#
#
# #добовление и изменение элементов
# student["age"] = 22 #изменения значения
# student["grade"] = "A" #добовлении новой пары
#
# #Удаление элементов
# # student.pop("city") #Удаляет пару с ключом "city"
# # del student["name"] #Удаляет ключ "name"
#
#
# #проверка наличии ключа
# if "name" in student:
#     print("ключ 'name' есть в словаре")
#
# #ознакомительные задачи:
# Ознакомительные задачи:
# 1. Создай словарь, содержащий информацию о книге (название, автор, год издания). Выведи автора книги.
book = {
    "name": "48 законов власти",
    "autor": "Robbert Green",
    "year": 1997
        }
print(book["autor"])
# 2. Создай пустой словарь и добавь в него три ключа: имя, возраст, город.

dictionary = {} #my_dict = dict() #{}
dictionary.update({"name": "Meder", "year": 35, "city": "Bali"})
print(dictionary.get("name"))
print(dictionary)

# 3. Удали ключ "город" из словаря и выведи результат.
dictionary.pop("city")
print(dictionary)

# 4. Проверь, есть ли ключ "телефон" в словаре и выведи сообщение об этом.
if "phone" in dictionary:
    print("ключ 'phone' нет в словаре")


# 5. Измени значение ключа "возраст" на 30.
dictionary["year"] = 30
print(dictionary)

# 6. Создай словарь с именами друзей и их любимыми цветами. Выведи любимый цвет одного из друзей.
freand = {
    "Djahongir": "Black",
    "Nuraym": "Grean",
    "Nurzat": "Blue",
    "Aichurok": "Brown",
    "Nazik": "Whaite"
}
print(freand["Nuraym"])


# 7. Создай словарь студентов и их оценок. Выведи всех студентов и их оценки.
students = {
    "Djahongir": 5,
    "Nuraym": 4,
    "Nurzat": 3,
    "Aichurok": 2,
    "Nazik": 1
}
print(students.items())

# 8. Используя .get(), получи значение несуществующего ключа с выводом "Нет такого ключа".
freand.get("")
# 9. Создай словарь с продуктами и их ценами. Добавь новый продукт и выведи обновленный словарь.
products = {
    "apple": 100,
    "banane": 80,
    "milk": 150
}
products["breat"] = 50
print(products)

# 10. Подсчитай количество ключей в словаре.
print(len(products))


# 11. Создай словарь с номерами автомобилей и их владельцами. Выведи владельца одного из автомобилей.
cars = {
    "A123BC": "Dilmurat",
    "B456DE": "Ulan",
    "C789FG": "Azim"
}
print(cars["B456DE"])

# 12. Добавь нового владельца и автомобиль в словарь.
cars["D987XY"] = "Adis"
print(cars)

# 13. Удали информацию о владельце автомобиля по номеру.
cars.pop("A123BC")
print(cars)

# 14. Используй метод .items() для вывода всех пар "ключ: значение".
print(cars.items())

# 15. Используй метод .values() для получения всех значений словаря.
print(cars.values())

# 16. Создай словарь с названиями стран и их столицами. Выведи столицу указанной страны.
country = {
    "Russia": "Moscow",
    "Kyrgyzstan": "Bishkek",
    "Germani": "Berlin"
}
print(country["Kyrgyzstan"])

# 17. Измени название столицы одной из стран.
country["Germani"] = "munhen"
print(country)

# 18. Проверь наличие страны в словаре перед получением её столицы.
country_name = "Spanish"
if country_name in country:
    print(country[country_name])
else:
    print("Страны нет в словаре")

# 19. Используй метод .update() для объединения двух словарей.
country1 = {
    "italy": "Roma",
    "spanish": "madrid"
}
country.update(country1)
print(country)

# 20. Создай словарь с логинами и паролями пользователей. Проверь правильность пароля для заданного логина.
users = {
    "user1": "pass123",
    "admin": "admin123",
    "guest": "guest123"
}
login = "admin"
password = "admin123"
if users == password:
    print("Пароль верный")

# 21. Создай словарь с днями недели и их порядковыми номерами. Выведи номер среды.
weekdays = {
    "Понедельник": 1,
    "Вторник": 2,
    "Среда": 3,
    "Четверг": 4,
    "Пятница": 5,
    "Суббота": 6,
    "Воскресенье": 7
}
print(weekdays["Среда"])

# 22. Проверь, есть ли в словаре ключ "воскресенье".
if "Воскресенье" in weekdays:
    print("Воскресен есть в словаре")

# 23. Создай словарь с курсами валют и их значениями. Получи значение курса доллара.
currency = {
    "USD": 87,
    "EUR": 95,
    "CNY": 12.7
}
print(currency["USD"])

# 24. Добавь новую валюту и её курс.
currency["KGZ"] = 115.4
print(currency)

# 25. Создай словарь с любимыми фильмами друзей. Выведи фильмы одного из друзей.
FM = {
    "Djahongir": "Harry Potter",
    "Nazik": "Inception",
    "Nurzat": "Matrix"
}
print(FM["Nurzat"])

# 26. Измени фильм в словаре для одного из друзей.
FM["Nazik"] = "Sekcet"
print(FM)

# 27. Создай словарь с наименованиями товаров и их количеством. Уменьши количество одного из товаров.
product = {
    "apple": 50, # не работает
    "banana": 30,
    "milk": 20
}
product["apple"] = 10
print(product)
# 28. Используй метод .clear() для очистки словаря.
product.clear()
print(product)

# 29. Создай словарь с именами сотрудников и их должностями. Выведи должность указанного сотрудника.
sotrudniki = {
    "Aktan": "Desinger",
    "Aruuke": "OtdelProdaj",
    "Asan": "Marketer"
}
print(sotrudniki["Aruuke"])
# 30. Удали информацию о сотруднике по имени.
sotrudniki.pop("Aktan")
print(sotrudniki)

# 31. Создай словарь с предметами и их баллами. Посчитай общую сумму баллов.
grades = {
    "Matematika": 90,
    "Fizika": 85,
    "Himiya": 88
}
print(sum(grades.values()))

# 32. Создай словарь с животными и их звуками. Выведи звук указанного животного.
animals = {
    "cat": "Mau",
    "Dog": "gav",
    "cow": "mu"
}
print(animals["cat"])
# 33. Измени звук одного из животных.
animals["Dog"] = "Loh"
print(animals)

# 34. Создай словарь с товарами и их ценами. Увеличь цену одного из товаров на 10%.
products = {
    "Breat": 50, # не работает
    "milk": 100,
    "sugar": 80
}
products["milk"] = 10
print(products)

# 35. Создай словарь с именами студентов и их возрастом. Выведи возраст студента с заданным именем.
student = {
    "Nazik": 25,
    "Nurzat": 24,
    "Dilmurat": 37
}
print(student["Nurzat"])
# 36. Проверь наличие студента в словаре перед выводом его возраста.
sname = "Dilmurat"
if sname in student:
    print(student[sname])

# 37. Создай словарь с названиями городов и численностью населения. Увеличь численность одного из городов.
city = {
    "moscow": 16000000, # не работат
    "Bishkek": 1200000,
    "Bali": 1500000
}
city["moscow"] * 500_000
print(city)
# 38. Используй метод .pop() для удаления ключа и получения его значения.
city1 = city.pop("Osh")
print(city1)

# 39. Создай словарь с играми и их рейтингами. Выведи игру с наивысшим рейтингом.
games = {
    "2077": 9.0, # не работает
    "Dota 2": 9.8,
    "GTA V": 9.5
}
best_game = max(games.get("Dota 2"))
print(best_game)

# 40. Создай словарь с контактами и их телефонами. Выведи телефон указанного контакта.
contacts = {
    "meder": "+996999450450",
    "Tynybek": "+996509992919",
    "Jainagul": "+996707862212"
}
print(contacts["meder"])