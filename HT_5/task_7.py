"""7. Написати функцію, яка приймає на вхід список (через кому), підраховує кількість однакових елементів у ньому і виводить результат. Елементами списку можуть бути дані будь-яких типів.
    Наприклад:
    1, 1, 'foo', [1, 2], True, 'foo', 1, [1, 2] ----> 1 -> 3, foo -> 2, [1, 2] -> 2, True -> 1 """

import pandas as pd

n = [1, 1, 'foo', [1, 2], True, 'foo', 1, [1, 2], False]

def element_occurrences(n):

    for i in range(len(n)):
        if type(n[i]) == bool and n[i]:
            n[i] = 'True'
        elif type(n[i]) == bool and not n[i]:
            n[i] = 'False'
    print(n)

    index = pd.Index(n)
    print(index.value_counts())

element_occurrences(n)
