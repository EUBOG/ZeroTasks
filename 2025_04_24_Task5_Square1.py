# Задача: Написать функцию square, принимающую 1 аргумент — сторону
# квадрата, и возвращающую 3 значения (с помощью кортежа):
# периметр квадрата, площадь квадрата и диагональ квадрата.

# Формулы:
# Периметр квадрата: P = 4 * a
# Площадь квадрата: S = a²
# Диагональ квадрата: d = a√2 (используем math.sqrt(2) для вычисления корня).

import math  # Для вычисления квадратного корня

def square(side):
    perimeter = 4 * side
    area = side ** 2
    diagonal = side * math.sqrt(2)
    return (perimeter, area, diagonal)

# Пример использования
side_length = 5
result = square(side_length)
print(f"Для квадрата со стороной {side_length}:")
print(f"Периметр: {result[0]}")
print(f"Площадь: {result[1]}")
print(f"Диагональ: {result[2]:.2f}")  # Округляем до 2 знаков после запятой