# Задача: Написать функцию arithmetic, принимающую 3 аргумента: первые 2 -
# числа, третий - операция, которая должна быть произведена над
# ними. Если третий аргумент +, сложить их; если —, то вычесть; * —
# умножить; / — разделить (первое на второе). В остальных случаях
# вернуть строку "Неизвестная операция".

def arithmetic(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:  # Проверка деления на ноль
            return num1 / num2
        else:
            return "Ошибка: деление на ноль!"
    else:
        return "Неизвестная операция"


# Примеры использования:
print(arithmetic(5, 3, '+'))  # 8
print(arithmetic(5, 3, '-'))  # 2
print(arithmetic(5, 3, '*'))  # 15
print(arithmetic(5, 3, '/'))  # 1.666...
print(arithmetic(5, 0, '/'))  # Ошибка: деление на ноль!
print(arithmetic(5, 3, '^'))  # Неизвестная операция