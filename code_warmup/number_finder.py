import numpy as np

def prime_finder(array):
    primes = []
    for i in array:
        if i <= 1: continue
        is_prime = True
        for n in np.arange(2, i):
            #print(i, n, i%n)
            if i%n == 0:
                is_prime = False
        if is_prime:
            primes.append(i)
    return np.array(primes)

def tribonacci_finder(array):
    tri_fib_nums = []
    first = array[0]
    second = array[1]
    third = array[2]
    for i in range(3, len(array)):
        fib_num = first + second + third
        #print(first, second, fib_num, array[i])
        if fib_num == array[i]:
            tri_fib_nums.append(array[i])
        first = second
        second = third
        third = array[i]
    return np.array(tri_fib_nums)

def fibonacci_finder(array):
    fib_nums = []
    first = array[0]
    second = array[1]
    for i in range(2, len(array)):
        fib_num = first + second
        #print(first, second, fib_num, array[i])
        if fib_num == array[i]:
            fib_nums.append(array[i])
        first = second
        second = array[i]
    return np.array(fib_nums)

