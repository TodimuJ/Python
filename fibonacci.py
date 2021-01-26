#Different ways to implement the Fibonacci Sequence

def fibonacci(n):
    fib = [0, 1, 1]
    if n <= 2:
        return fib[n]

    else:
        return fibonacci(n-1) + fibonacci(n-2) 

def fibonacci1(n):
    goldenRatio = ((1 + 5 ** 0.5) / 2)
  	return int((goldenRatio ** N + 1) / 5 ** 0.5)


for n in range(1, 13):
    print(n, ":", fibonacci(n) )