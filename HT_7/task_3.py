"""3. Всі ви знаєте таку функцію як <range>. 
Напишіть свою реалізацію цієї функції. 
Тобто щоб її можна було використати у вигляді:

    for i in my_range(1, 10, 2):
        print(i)

    1
    3
    5
    7
    9

   P.S. Повинен вертатись генератор.
   P.P.S. Для повного розуміння цієї функції
 - можна почитати документацію по ній:
 https://docs.python.org/3/library/stdtypes.html#range
   P.P.P.S Не забудьте обробляти невалідні ситуації
 (типу range(1, -10, 5) тощо).
 Подивіться як веде себе стандартний range в таких випадках.
"""


def my_range(*args):

    
    if len(args) == 1:
        start, step, stop = 0, 1, args[0]
        while start < stop:
            yield start
            start += step
    elif len(args) == 2:
        start, step, stop = args[0], 1, args[1]
        while start < stop:
            yield start
            start += step
    elif len(args) == 3:
        start, stop, step = args[0], args[1], args[2]

        
    if step > 0:  # step arg is increasing
        while start < stop:
            yield start
            start += step
        return start
    elif step < 0:  # step arg is decreasing
        while start > stop:
            yield start
            start += step  # Adding a negative to decrease
        return start
            
for i in my_range(2,20,3):
    print(i)
    
