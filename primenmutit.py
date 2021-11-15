""" An effort to understand parallel programming.
"""
import time


def primenumbers(n):
    '''This takes a number and outputs a list of all primes before it, order n**2, slow'''
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


def summingSeq(numbers):

    listsum = []
    for i in numbers:
        listsum.append([i, sum(primenumbers(i))])

    return listsum

    
if __name__ == '__main__':

    numlist = range(1000)
    
    startseq = time.perf_counter()
    pnumber = summingSeq(numlist)
    stopseq = time.perf_counter()
    
    print(pnumber)
    print(f'Elapsed time (sequential): {stopseq - startseq} s') 