def fibonacci_gen():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Using the generator to print the first 10 Fibonacci numbers
fib = fibonacci_gen()
for _ in range(10):
    print(next(fib))
