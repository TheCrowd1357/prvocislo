import sys
from math import sqrt
import random


# https://en.wikipedia.org/wiki/Fermat%27s_factorization_method


def type_prime(input):
    match input:
        case int():
            return counting_prime(input)
        case float():
            return counting_prime(input)
        case str():
            try:
                return counting_prime(float(input))
            except ValueError:
                return False
        case _:
            return False


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


# If n is prime, then always returns true,
# If n is composite than returns false with
# high probability Higher value of k increases
# probability of correct result
def isPrime(n, k):
     
    # Corner cases
    if n == 1 or n == 4:
        return False
    elif n == 2 or n == 3:
        return True
     
    # Try k times
    else:
        for i in range(k):
             
            # Pick a random number
            # in [2..n-2]     
            # Above corner cases make
            # sure that n > 4
            a = random.randint(2, n - 2)
             
            # Fermat's little theorem
            if power(a, n - 1, n) != 1:
                return False
    return True
    
if __name__ == "__main__":
    repeat = "y"
    while (repeat == "y"):
        n = input("Enter a whole number: ")
        if (type_prime(n)):
            print(n + " is a whole number")
        else:
            print(n + " is not a whole number")
        repeat = input("Wish to test another number? Type y: ")

