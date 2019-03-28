# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 20:12:07 2019
https://projecteuler.net/problem=3
@author: matth

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

def main():
    print(max(factors(600851475143)))

def factors(n):
    """Returns a list of an integer's prime factors in increasing order with multiple factors listed multiple times"""
    p = 2
    while n > 1:
        while n % p == 0:
            yield p
            n /= p
        p += 1

#############################

if __name__ == '__main__':
    main()