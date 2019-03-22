# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 21:03:23 2019
https://projecteuler.net/problem=9
@author: matth

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

def main():
    for c in range(334,500):
        for b in range((1000 - c)//2, c):
            #print(1000-b-c,b,c)
            if b**2 + (1000 - b - c)**2 == c**2:
                print(1000-b-c,b,c)
                print((1000-b-c)*b*c)
                
#############################

if __name__ == '__main__':
    main()