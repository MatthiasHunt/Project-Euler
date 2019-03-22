# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 19:23:14 2019
https://projecteuler.net/problem=7
@author: matth

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
def main():
    print(primes(10001)[-1])

def primes(n):
    """Returns a list of the first n primes in increasing order - Not useful past 10,000"""
    prime_list = [2]
    p = 3
    while (len(prime_list) < n):
        if all ([p % prime != 0 for prime in prime_list]):
            prime_list.append(p)
        p += 1
    return prime_list

#############################

if __name__ == '__main__':
    main()