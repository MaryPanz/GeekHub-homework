"""Написати функцію, яка приймає два параметри: ім'я (шлях) файлу та кількість символів. 
Файл також додайте в репозиторій. На екран має бути виведений список із трьома блоками - символи з початку, 
із середини та з кінця файлу. Кількість символів в блоках - та, яка введена в другому параметрі. 
Придумайте самі, як обробляти помилку, наприклад, коли кількість символів більша, ніж є в файлі або, наприклад, 
файл із двох символів і треба вивести по одному символу, то що виводити на місці середнього блоку символів?). 
Не забудьте додати перевірку чи файл існує."""

import os


my_file = "text.txt"
number = 10


def my_reader(my_file, number):


    if os.path.isfile(my_file):

        my_list = []
        with open(my_file, "rt") as file:
            lines = file.read()
            if len(lines) < number:
                print("Incorrect number!")
            elif number < 0:
                print("Number below 0")
            else: 
                file.seek(0)
                my_list.append(file.read(number))
                file.seek(0)
                start = len(lines) // 2 - number // 2
                my_list.append(lines[start:start + number])
                file.seek(0)
                my_list.append(lines[-number:])
                print(my_list)
    else:
        print("Something is wrong with the file!")
        

my_reader(my_file, number)
