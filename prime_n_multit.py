""" An effort to understand parallel programming.
"""
import time
#import multiprocessing
#import threading

import numpy as np


def sieve_erat(n):
    """A better algorithm to find prime numbers, by eratosthenes, using numpy for speed"""
    if n < 2:
        return 0

    numbers = np.ones(n+1, dtype=np.bool_)
    p = 2
    while p * p <= n:
        if numbers[p] == np.True_:
            for i in range(p**2, n+1 , p):
                numbers[i] = np.False_
        p += 1
    numbers[0] = np.False_
    numbers[1] = np.False_
    return numbers.nonzero()

def summing_seq(n):
    '''outputs a list with sieve_erat, without multiple threads or processes'''
    listsum = []
    for i in n:
        listsum.append([i, np.sum(sieve_erat(i))])

    return listsum

def summing_multiprocess(n):
    '''outputs a list with sieve_erat, with multiprocessing'''
    pass

def summing_multithread(n):
    ''' outputs a list with sieve_erat, with multithreads'''
    pass


if __name__ == '__main__':

    numlist = range(100000,2500000,100000)

    startseq = time.perf_counter()
    pnumber = summing_seq(numlist)
    stopseq = time.perf_counter()

    print(pnumber)
    print(f'Elapsed time (sequential): {stopseq - startseq} s')
