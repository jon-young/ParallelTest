__author__ = 'jyoung'

import math
import time

def is_prime(start, end):
    """determine how many primes within given range"""
    numPrime = 0
    for n in range(start, end+1):
        isPrime = True
        for i in range(2, math.floor(math.sqrt(n))+1):
            if n % i == 0:
                isPrime = False
                break
        if isPrime:
            numPrime += 1
    if start == 1:
        numPrime -= 1
    return numPrime

if __name__ == "__main__":
    natNum = 0
    while natNum < 2:
        natNum = int(input('Enter a natural number greater than 1: '))
    startTime = time.time()
    finalResult = is_prime(1, natNum)
    print('Elapsed time:', time.time()-startTime, 'seconds')
    print('The number of primes <=', natNum, 'is', finalResult)