# 🔢 Integer (int) Methods
print("🔢 Integer Methods")

num = -10
print("Absolute value:", abs(num))
print("Max of (10, 20, 30):", max(10, 20, 30))
print("Min of (10, 20, 30):", min(10, 20, 30))
print("Power (2^3) using pow():", pow(2, 3))
print("Power (2^3) using **:", 2 ** 3)
print("Convert '100' to int:", int("100"))
print("Convert float 3.9 to int:", int(3.9))  # Rounds down

# 🟡 Float (float) Methods
print("\n🟡 Float Methods")

fnum = -7.8
print("Absolute value:", abs(fnum))
print("Round 4.678:", round(4.678))
print("Round 4.678 to 2 decimals:", round(4.678, 2))
print("Convert '10.5' to float:", float("10.5"))
# 🔠 String (str) Methods
print("\n🔠 String Methods")

text = "  Hello World  "
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Title Case:", text.title())
print("Capitalized:", text.capitalize()) # заглавные буквы
print("Stripped spaces:", text.strip()) #  урезанные проьстранство
print("Left stripped:", text.lstrip())
print("Right stripped:", text.rstrip())
print("Index of 'World':", text.find("World")) # находить
print("Replace 'Hello' with 'Hi':", text.replace("Hello", "Hi"))
fruits = "apple,banana,orange"
words = fruits.split(",")
print("Split string:", words)
print("Joined string:", "-".join(words)) #печать
print("Starts with 'Hello':", text.startswith("Hello")) # начинается с
print("Ends with 'World':", text.endswith("World")) # заканчивается
print("Is '12345' all digits?:", "12345".isdigit()) # цыфра
print("Is 'abc' all letters?:", "abc".isalpha())
print("Is 'abc123' alphanumeric?:", "abc123".isalnum())
print("Is '   ' all spaces?:", "   ".isspace())

# 🔵 Boolean (bool) Methods
print("\n🔵 Boolean Methods")

print("Boolean of 0:", bool(0))  # False
print("Boolean of 1:", bool(1))  # True
print("Boolean of empty string:", bool(""))  # False
print("Boolean of non-empty string:", bool("hello"))  # True
print("Boolean of None:", bool(None))  # False
print("Boolean of empty list:", bool([]))  # False
print("Boolean of non-empty list:", bool([1, 2, 3]))  # True

# 🎯 Formatting Strings using f-strings
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")

