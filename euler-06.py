# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 19:18:11 2019
https://projecteuler.net/problem=6
@author: matth

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def main():
    n = 100
    # These are well-known theorems
    sum_of_squares = n * (n+1) * (2*n+1) // 6
    square_of_sum = (n * (n+1) // 2)**2
    print(square_of_sum - sum_of_squares)


#############################

if __name__ == '__main__':
    main()