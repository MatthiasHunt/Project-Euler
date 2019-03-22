# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 18:49:59 2019
https://projecteuler.net/problem=5
@author: matth

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
def main():
    print(lcmm(*range(1,21)))

def gcd(m,n):
    if n > m:
        return gcd(n,m)
    # The Euclidean Algorithm
    if m % n == 0:
        return n
    else:
        return (gcd(n, m % n))
    
def lcm(m,n):
    # This is a theorem involving lcm and gcd
    return m * n // gcd(m,n)

def lcmm(*args):
    tot = 1
    for num in args:
        tot = lcm(tot,num)
    return tot

#############################

if __name__ == '__main__':
    main()