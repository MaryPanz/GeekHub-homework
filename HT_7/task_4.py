"""4. Реалізуйте генератор, який приймає на вхід будь-яку ітерабельну послідовність (рядок, список, кортеж) і повертає генератор, який буде повертати значення з цієї послідовності, при цьому, якщо було повернено останній елемент із послідовності - ітерація починається знову.

   Приклад (якщо запустили його у себе - натисніть Ctrl+C ;) ):
   for elem in my_generator([1, 2, 3]):
       print(elem)

   1
   2
   3
   1
   2
   3
   1"""


#something = "This is a cat"
#something = [1, 2, 3]
something = ("a", "b", "c")


def my_generator(something):


    while True:
        for i in something:
            yield i
my_generator(something)


for i in my_generator(something):
    print(i)
