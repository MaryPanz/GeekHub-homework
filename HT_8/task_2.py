
import os

my_file = "text.txt"
number = 10


def my_reader(my_file, number):


    if os.path.isfile(my_file):

        my_list = []
        with open(my_file, "r") as file:
            lines = file.read()
            if len(lines) < number:
                print("The number is too small")

            else:
                file.seek(0)
                #first
                my_list.append(file.read(number))
                lines = file.read()
                #middle
                start = len(lines) // 2 - number // 2
                my_list.append(lines[start:start + number])
                #last
                my_list.append((lines[-number:]))

            print(my_list)
    else:
        print("Something is wrong with the file!")
        

my_reader(my_file, number)
