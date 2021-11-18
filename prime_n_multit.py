""" An effort to understand parallel programming.
"""
import time
import multiprocessing as mp
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

def worker_multiprocess_pool(n):
    '''similar to the sequential one, but it outputs only a pair of values'''
    output = [n, np.sum(sieve_erat(n))]
    return output

def summing_multiprocess_pool(list_of_numbers, n_process = 4):
    '''outputs a list with sieve_erat, with multiprocessing, using Pool object'''
    with mp.Pool(n_process) as pool:
       results = pool.map(worker_multiprocess_pool, list_of_numbers)
    pool.join
    return results

def worker_multiprocess_process(n, data_queue):
    '''This needs a queue object to store data, since the Process object
    does not return the function output'''

    for i in n:
        data_queue.put([i, np.sum(sieve_erat(i))])


def summing_multiprocess_process(list_of_numbers, n_process = 4):
    '''outputs a list with sieve_erat, with multiprocessing, using Process object, this gets
    more convoluted with each new process.
    This seems low level, three for cycles?'''
    chunksize = int (len(list_of_numbers) / n_process)
    data_queue = mp.Queue()
    process_list = []
    output = []
    for i in range(n_process):
        p = mp.Process(target=worker_multiprocess_process, args=(list_of_numbers[chunksize * i: chunksize * (i + 1)], data_queue))
        process_list.append(p)
        p.start()
    # I really don't like this way of managing process data
    for i in list_of_numbers:
        output.append(data_queue.get())
    
    for pn in process_list:
        pn.join()
    
    return output

def summing_multithread(n):
    ''' outputs a list with sieve_erat, with multithreads'''
    pass


if __name__ == '__main__':

    numlist = range(100000,2500000,100000)

    startseq = time.perf_counter()
    pnumber_seq = summing_seq(numlist)
    stopseq = time.perf_counter()
    
    startmp = time.perf_counter()
    pnumber_mp = summing_multiprocess_pool(numlist)
    stopmp = time.perf_counter()

    startmpp = time.perf_counter()
    pnumber_mpp = summing_multiprocess_process(numlist)
    stopmpp= time.perf_counter()
    '''
    startmt = time.perf_counter()
    pnumber_mt = summing_multithread(numlist)
    stopmt = time.perf_counter()
    '''    
    print(pnumber_seq)
    print(pnumber_mp)
    print(pnumber_mpp)
    print(f'Elapsed time (sequential): {stopseq - startseq} s')
    print(f'Elapsed time (multiprocessing Pool): {stopmp - startmp} s')
    print(f'Elapsed time (multiprocessing Process): {stopmpp - startmpp} s')
