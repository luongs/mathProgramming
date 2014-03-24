# find summation of all primes below 2 million
# Create a list of prime numbers
'''
primeArray_length = 2000000
primeArray = []
sum = 0 
number = 3


while count < primeArray_length:
	for i in range(2,number):
		if number % i == 0:
			break
		if i == number - 1:
			primeArray.append(number)
			count += 1
	number += 1
print("done")
'''
from math import sqrt

def isPrime(n):
    if n == 2:
        return True
    elif n < 2 or n % 2 == 0:
        return False
    else:
        d = 3
        # switch to sieve? is this sieve? 
        limit = sqrt(n)
        while d <= limit:
            if n % d == 0:
                return False
            d = d + 2
    return True

def prime(k_max):
    k = 0
    n = 1
    sum =0
    while k < k_max:
        n = n + 1
        sum+=n
        if isPrime(n):
            k = k + 1
    return sum

x = prime(2000000)
print("The sum of all prime numbers are:")
print(x)