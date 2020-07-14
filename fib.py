# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

def slow_fibonacci(n):
    # base case
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)



cache = {}

def fibonacci(n):
    if n <= 1:
        return n

    if n not in cache:
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)

    return cache[n]


print(fibonacci(8))
print(fibonacci(9))
print(fibonacci(15))
print(fibonacci(25))
print(fibonacci(45))


