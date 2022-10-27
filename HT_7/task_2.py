"""2. Запишіть в один рядок генератор списку
 (числа в діапазоні від 0 до 100 не включно),
 сума цифр кожного елемент якого буде дорівнювати 10.
   Результат: [19, 28, 37, 46, 55, 64, 73, 82, 91]"""


my_list = list(range(1,100))
result = [number for number in my_list if number > 10 if int(str(number)[1:]) + int(str(number)[:1]) == 10]
print(result)
