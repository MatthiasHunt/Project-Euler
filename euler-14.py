# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 18:54:20 2019
https://projecteuler.net/problem=14
@author: matth

Which starting number, under one million, produces the longest chain?
"""
def main():
    collatz_values = [len(collatz(i)) for i in range(2,1000000)]
    print(collatz_values.index(max(collatz_values))+2)

def collatz(n):
    """Returns the chain of terms starting at n, ending at one"""
    chain = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
            chain.append(n)
        else:
            n = 3*n + 1
            chain.append(n)
    return chain

#############################

if __name__ == '__main__':
    main()