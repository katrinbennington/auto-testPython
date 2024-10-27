"""
Напишите функцию square, принимающую 1 аргумент — сторону квадрата — и возвращающую площадь квадрата.
Площадь квадрата = сторона * сторона.
Если переданный аргумент был не целым, округлите результат вверх.
"""

import math


def square(side):
    area = side * side
    return math.ceil(area)


side_length = 4.3
result = (square(side_length))

print(f"Площадь квадрата = {side_length} * {result}")
