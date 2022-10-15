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
