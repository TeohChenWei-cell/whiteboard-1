def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def generate_fibonacci(count):
    for i in range(count):
        print(fibonacci(i), end=", ")

generateFibonacci(100) //type how many you fibonacci you wanted to generate
