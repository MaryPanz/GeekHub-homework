#something = "This is a cat"
#something = [1, 2, 3]
something = ("a", "b", "c")
def my_generator(something):
    while True:
        for i in something:
            print(i)
my_generator(something)
