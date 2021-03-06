# -*- coding: utf-8 -*-
"""Untitled9.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eYz0XiS1tBA46vHK8esyz9PUEFe_CsrW
"""

from sympy import isprime
primesList = [p for p in range(10000) if isprime(p)]
primesSet = set(primesList)
len(primesList), max(primesList)

# Commented out IPython magic to ensure Python compatibility.
X = 9973
# %timeit X in primesList
# %timeit X in primesSet
# %timeit isprime(X)

# Commented out IPython magic to ensure Python compatibility.
X = 2
# %timeit X in primesList
# %timeit X in primesSet
# %timeit isprime(X)

def isin_linearSearch(L,item):
    'Returns True when item is in L, False otherwise'
    for e in L:
        if e == item:
            return True
    return False
isin_linearSearch(primesList, max(primesList))

L = [1, 3, 10 , 7, 4, 13,11,6,54, 3,17,5, 15, 2, 9]
sortedL = sorted(L)
print(len(L))
print(L)
print(sortedL)

def isin_binarySearch(L,item):
    '''Returns True when item is in L, False otherwise. 
    Assumes L is sorted in ascending order.'''
    low = 0
    high = len(L) - 1
    while low <= high:
        mid = (low + high) // 2
        print(low,mid,high)
        if L[mid] == item:
            return True
        if L[mid] > item: # list[mid] was too high
            high = mid - 1
        else: # The guess was too low.
            low = mid + 1
    return False # Item doesn't exist

print(isin_binarySearch(L, 7))

my_list = [1, 3, 5, 7, 9]
print(isin_binarySearch(my_list, 3))