n = int(input("Type a number from 0 to 1000: "))

def is_prime(n):
    if n < 2:
        return "It is neither prime nor composite!"
    else:
        for i in range(2, n):
            if (n % i) == 0:
                return False
        return True

print(is_prime(n))
