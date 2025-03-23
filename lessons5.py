# ### Lessons 5
# # Список (List) - это упорядочная изменяемая коллекция элементов
#
# # пример списка
# fruits = ["apple, banan, orange"]
# # print(fruits[0]) #aplle
# #
# # #список  могут содержать разные типы данных
# # mixed_list = [42, "hello", 3.14, [1,2,3]]
# # print(mixed_list[3][1]) # Доступ ко второму
# # print(mixed_list[1]), print(mixed_list[0] )
#
# # #negative index
# # print(mixed_list[-1])
# #
# # #aditing index
# # hello_world = "hello world"
# # mixed_list[1] = hello_world
# # mixed_list[2] = 33.45
# # print(mixed_list)
# #
# # #
# # print(len(mixed_list))
# # concatenated_list = mixed_list + fruits
# # print(concatenated_list)
# # # print(mixed_list + fruits)
# #
# # print(fruits * 2)
# # print([1] * 30)
# # #
# # # print(fruits)
# # # print("apple" in fruits)
# # # print("bananes" in mixed_list)
# #
# #
# # print(fruits)
# # fruits.append("pineapple")
# # fruits.pop()
# # ananas =fruits.pop()
# # print(ananas)
# # print(fruits)
# #
# #
# # # print(mixed_list)
# # # mixed_list.pop()
# # # print(mixed_list)
# # # mixed_list.remove(42)
# # # print(mixed_list)
# #
# #
# # print(mixed_list.index(33.45))
# # print(mixed_list.count(33.45))
# # mixed_list.append(33.45)
# # print(mixed_list.count(33.45))
# # print(mixed_list)
# #
# # numbers = [2, 5, 9, 4, 8, 6 ,5]
# # # print(numbers)
# # # print(sorted(numbers))
# # numbers.sort()
# # # print(numbers)
# #
# # print(numbers)
# # print(numbers[2:5])
#
#
#
# #1
# dishes = ["manty", "lagman", "samsa", "plov", "nsiguren"]
# print(len(dishes))
# print(dishes[2])
#
# #2
# numbers = [10, 20, 30, 40, 50]
# numbers[2] = 99
# numbers[4] = 3.14
# print(numbers)
#
# #3
# list1 = ["a", "b", "c"]
# list2 = [1,2,3]
# print(list1 + list2)

#4
list_1 = [4, 2, 9, 1]
list_1.append(7)
print(list_1)

#5
list_2 = ["python", "java", "c++", "javascript", "php"]
print(list_2[1:3])

#6
list_3 = ["Anya", "Boris", "Vika"]
print("Hi", list_3[1])
# print("Hi", list_3[2])
# print("Hi", list_3[3])

#7
list_4 = [[1, 2], [3, 4], [5, 6]]
print(list_4[1][1])