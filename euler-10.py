# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 13:49:58 2019
https://projecteuler.net/problem=10
@author: matth

Find the sum of all the primes below two million.
"""
import numpy as np

def main():
    print(sum(primes_bounded(2000000)))

def primes_bounded(n):
    """Returns an ordered list of all primes less than integer n"""
    primes_bool = np.ones(n, dtype=bool)
    primes_bool[0] = False
    primes_bool[1] = False
    for p in range(2,n):
        if primes_bool[p]:
            primes_bool[2*p:n:p] = False
    return[i for (i,is_prime) in enumerate(primes_bool) if is_prime]
    
#############################

if __name__ == '__main__':
    main()