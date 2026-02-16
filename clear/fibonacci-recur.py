
def fibonacci(n):
    if n > 0:
        return n * fibonacci(n - 1)
    else:
        return 1


print(fibonacci(10))