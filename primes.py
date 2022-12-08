"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes < 1:
        raise ValueError('Number must be positive')
    list = []
    counter = 2
    while len(list) < number_of_primes:
        if PrimeCheck(counter) == True:
            list.append(counter)
        counter += 1
    return list


def PrimeCheck(num):
    for i in range (2,(num // 2) + 1 ):
        if (num % i) == 0:
            return False
    return True
