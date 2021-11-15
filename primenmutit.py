""" An effort to understand parallel programming.
"""
import time
import numpy as np

def primenumbers(n):
    '''This takes a number and outputs a list of all primes before it, order at least n**2, slow'''
    primes = [2]
    if n <= 2:
        return []
    else:
        for i in range(3, n):
            for p in range(2, i):

                if i % p == 0:
                    break
                elif i % p != 0 and p == i - 1:
                    primes.append(i)

    return primes


def sieveErat(n):
    """A better algorithm to find prime numbers, by eratosthenes, using numpy for speed"""
    if n < 2:
        return 0

    numbers = np.ones(n+1, dtype=np.bool_)
    p = 2
    while (p * p <= n):
        if (numbers[p] == np.True_):
            for i in range(p**2, n+1 , p):
                numbers[i] = np.False_
        p += 1
    numbers[0] = np.False_
    numbers[1] = np.False_
    return numbers.nonzero()

def summingSeq(n):

    listsum = []
    for i in n:
        listsum.append([i, np.sum(sieveErat(i))])

    return listsum

    
if __name__ == '__main__':

    numlist = range(2, 10)
    
    startseq = time.perf_counter()
    pnumber = summingSeq(numlist)
    stopseq = time.perf_counter()
    
    print(pnumber)
    print(f'Elapsed time (sequential): {stopseq - startseq} s') 