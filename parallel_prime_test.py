__author__ = 'jyoung'

"""
Determine how many primes are less than a given natural number (in parallel)
"""

import math
import multiprocessing as mp
import numpy
import time


def is_prime(vec, output):
    """determine how many primes in vector"""
    numPrime = 0
    for n in vec:
        isPrime = True
        for i in range(2, math.floor(math.sqrt(n))+1):
            if n % i == 0:
                isPrime = False
                break
        if isPrime:
            numPrime += 1
    if vec[0] == 1:
        numPrime -= 1  # since 1 is not prime
    output.put(numPrime)


def chunks(vec, n):
    """evenly divide list into n chunks"""
    for i in range(0, len(vec), n):
        yield vec[i:i+n]

if __name__ == "__main__":
    natNum = 0
    while natNum < 2:
        natNum = int(input('Enter a natural number greater than 1: '))
    numProc = 0
    while numProc < 1:
        numProc = int(input('Enter the number of desired parallel processes: '))
    startTime = time.time()
    numSplits = math.ceil(natNum/numProc)
    splitList = list(chunks(tuple(range(1, natNum+1)), numSplits))
    output = mp.Queue()
    processes = [mp.Process(target=is_prime, args=(splitList[jobID], output))
                 for jobID in range(numProc)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    print('Elapsed time:', time.time()-startTime, 'seconds')
    procResults = [output.get() for p in processes]
    finalResult = numpy.sum(numpy.array(procResults))
    print('Results from each process:\n', procResults)
    print('The number of primes <=', natNum, 'is', finalResult)