def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)


def main():
    print(factorial(5))
    