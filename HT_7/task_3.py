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
        while start < stop:
            yield start
            start += step
            
    
for i in my_range(1, 10, 2):
    print(i)
