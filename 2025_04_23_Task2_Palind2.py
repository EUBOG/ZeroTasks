# Проверка на палиндром
# Напишите проверку на то, является ли строка палиндромом.
# Палиндром — это слово или фраза, которые одинаково читаются
# слева направо и справа налево.

# Вариант с учётом пунктуации (используя регулярные выражения)

import re

def is_palindrome(word):
    word = re.sub(r'[^a-zA-Zа-яА-Я]', '', word.lower())  # Удаляем всё, кроме букв
    return word == word[::-1]

# Примеры:
print(is_palindrome("Лёша на полке клопа нашёл")) # True
print(is_palindrome("АББА"))                      # True
print(is_palindrome("12321"))                     # True
print(is_palindrome("Madam, I'm Adam"))           # True (знаки препинания удалены)
print(is_palindrome("топот"))                     # True
print(is_palindrome("А роза упала на лапу Азора"))# True
print(is_palindrome("Python"))                    # False
print(is_palindrome("Привет"))                    # False
print(is_palindrome("радар"))                     # True