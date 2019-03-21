# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 18:08:51 2019
https://projecteuler.net/problem=4
@author: matth

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def main():
    print(max(a*b for a in range(900,1000) for b in range(900,1000) if is_palindrome(a*b)))

def is_palindrome(n):
    n = str(n)
    while len(n) > 1:
        if n[0] != n[-1]:
            return False
        n = n[1:-1]
    return True

#############################

if __name__ == '__main__':
    main()