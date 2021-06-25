# sum1 = 0 #answer is 233168

# for i in range(1,1000):
#     if i%3 == 0 or i%5 == 0:
#         sum1 += i

# print(sum1)

######################################################################
# cache = {}

# def fib(n):
#     if n in cache:
#         return cache[n]

#     if n < 2:
#         value = 1

#     else:
#         value = fib(n-1) + fib(n-2)

    
#     cache[n] = value

#     return value

# print(fib(10))


####################################################################### Find target sum
arr = [2, 5, 6, 7, 9, 13, 16, 19, 23]

def targetSum(array, target):
    i = 0
    j = len(array)-1
    
    while i != j:
        if array[i] + array[j] == target:
            return [i,j]
        
        elif array[i] + array[j] > target:
            j -= 1
        
        else:
            i += 1
    
    return -1
    
    
print(targetSum(arr, 42))