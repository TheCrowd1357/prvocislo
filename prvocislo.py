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


def power(a, n, p):


def isPrime(n, k):
