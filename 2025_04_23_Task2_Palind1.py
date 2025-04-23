# Проверка на палиндром
# Напишите проверку на то, является ли строка палиндромом.
# Палиндром — это слово или фраза, которые одинаково читаются
# слева направо и справа налево.

# Простой вариант (без учёта пробелов и регистра)

def is_palindrome(word):
    word = word.lower().replace(" ", "")  # Игнорируем пробелы и регистр
    return word == word[::-1]  # Сравниваем строку с её перевёрнутой версией

# Примеры использования:
print(is_palindrome("Лёша на полке клопа нашёл")) # True
print(is_palindrome("АББА"))                      # True
print(is_palindrome("12321"))                     # True
print(is_palindrome("Madam, I'm Adam"))           # False (знаки препинания не позволяют учесть палиндром)
print(is_palindrome("топот"))                     # True
print(is_palindrome("А роза упала на лапу Азора"))# True
print(is_palindrome("Python"))                    # False
print(is_palindrome("Привет"))                    # False
print(is_palindrome("радар"))                     # True