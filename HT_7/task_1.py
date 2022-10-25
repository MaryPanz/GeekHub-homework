my_gen = (i for i in range(1, 100) if i % 3 != 0 and i % 5 == 0)
print([next(my_gen) for j in range(13)])
