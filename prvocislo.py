import sys
from math import sqrt
import random

def type_prime(input):
    match input:
        case int():
            return counting_prime(input)
        case float():
            return counting_prime(input)

def counting_prime(input):
    if(input == int(input)):
        if (input > 100_000):
            return isPrime(input, 3)


#Fermat's factorization method

# Iterative Function to calculate
# (a^n)%p in O(logy)
def power(a, n, p):
     
    # Initialize result
    result = 1
     
    # Update 'a' if 'a' >= p
    a = a % p 
     
    while n > 0:
         
        # If n is odd, multiply
        # 'a' with result
        if n % 2:
            result = (result * a) % p
            n = n - 1
        else:
            a = (a ** 2) % p
             
            # n must be even now
            n = n // 2
             
    return result % p


def isPrime(n, k):
