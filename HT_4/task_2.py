"""2. Створіть 3 рiзних функцiї (на ваш вибiр). Кожна з цих функцiй повинна повертати якийсь результат (напр. інпут від юзера,
результат математичної операції тощо). Також створiть четверту ф-цiю, яка всередині викликає 3 попередні,
обробляє їх результат та також повертає результат своєї роботи. Т
аким чином ми будемо викликати одну (четверту) функцiю, а вона в своєму тiлi - ще 3."""


def write_animal():
    animal = input("Write an animal: ")
    return animal
def write_food():
    food = input("Write your favourite food in plural: ")
    return food
def write_age():
    age = input("Write your age: ")
    return age
def print_sentence():
    print(f"You are {write_age()} years old. Your favourite animal is a {write_animal()}. You like to eat {write_food()}!")
    
print_sentence()
