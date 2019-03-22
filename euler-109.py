# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 18:27:56 2019
https://projecteuler.net/problem=109
@author: matth

*** Explains the rules of darts ***
How many distinct ways can a player checkout with a score less than 100?
"""
def main():
    throws = [n for n in range(1,21)] + [2*n for n in range(1,21)] + [3*n for n in range(1,21)] + [25,50]
    one_dart_checkouts = [2*n for n in range(1,21)] + [50]
    two_dart_checkouts = [dart_two + dart_one for dart_two in one_dart_checkouts for dart_one in throws]
    # Three dart checkouts involve double counting. We assume the first dart always appears first in the list
    throw_pairs = [throws[m] + throws[n] for m in range(len(throws)) for n in range(len(throws)) if m >= n]
    three_dart_checkouts = [first_darts + dart_three for first_darts in throw_pairs for dart_three in one_dart_checkouts]
    print(len([n for n in one_dart_checkouts + two_dart_checkouts + three_dart_checkouts if n < 100]))
    
#############################

if __name__ == '__main__':
    main()