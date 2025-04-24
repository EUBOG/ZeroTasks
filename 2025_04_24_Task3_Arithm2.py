# Задача: Написать функцию arithmetic, принимающую 3 аргумента: первые 2 -
# числа, третий - операция, которая должна быть произведена над
# ними. Если третий аргумент +, сложить их; если —, то вычесть; * —
# умножить; / — разделить (первое на второе). В остальных случаях
# вернуть строку "Неизвестная операция".

# Функция расширена:
# Добавлены операции возведения в степень ** и целочисленного деления //;
# Использован словарь с лямбда-функциями.

def arithmetic_advanced(num1, num2, operation):
    operations = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b if b != 0 else "Ошибка: деление на ноль!",
        '**': lambda a, b: a ** b,
        '//': lambda a, b: a // b
    }
    return operations.get(operation, lambda a, b: "Неизвестная операция")(num1, num2)


# Примеры использования:
print(arithmetic_advanced(5, 3, '+'))  # 8
print(arithmetic_advanced(5, 3, '-'))  # 2
print(arithmetic_advanced(5, 3, '*'))  # 15
print(arithmetic_advanced(5, 3, '/'))  # 1.666...
print(arithmetic_advanced(5, 0, '/'))  # Ошибка: деление на ноль!
print(arithmetic_advanced(5, 3, '**'))  # 125
print(arithmetic_advanced(5, 3, '//'))  # 1
print(arithmetic_advanced(5, 3, '^'))  # Неизвестная операция