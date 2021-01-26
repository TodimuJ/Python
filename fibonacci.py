#Different ways to implement the Fibonacci Sequence

def fibonacci(n):
    fib = [0, 1, 1]
    if n <= 2:
        return fib[n]

    else:
        return fibonacci(n-1) + fibonacci(n-2) 



def fibonacci1(n):
    #Efficient algorithm using memoization where previous terms are stored in memory rather than computed
    fibonacci_cache = {}
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    # Compute the Nth term
    if n == 1 or n == 2:
        value =  1 
    
    elif n > 2:
        value = fibonacci1(n-1) + fibonacci1(n-2)

    #Store value in cache
    fibonacci_cache[n] = value
    return value



def fibonacci2(n):
    goldenRatio = ((1 + 5 ** 0.5) / 2)
    return int((goldenRatio ** n + 1) / 5 ** 0.5)


for n in range(1, 13):
    print(n, ":", fibonacci(n))


print(fibonacci2(10))