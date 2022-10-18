"""1. Написати функцію <square>, яка прийматиме один аргумент - сторону квадрата, і вертатиме 3 значення у вигляді кортежа:
периметр квадрата, площа квадрата та його діагональ."""

import math

one_side = int(input("Write the length of one side of the square: "))

def square(one_side):
    
    perimetre = 4 * one_side
    square_area = one_side ** one_side
    diagonal = one_side * math.sqrt(2)
    
    return perimetre, square_area, diagonal
    
print(square(one_side))
