__author__ = 'jyoung'

import multiprocessing as mp
import numpy
import time

def sum_range_serial(start, end):
    return numpy.sum(numpy.arange(start, end+1))

def sum_range_par(start, end, output):
    output.put(numpy.sum(numpy.arange(start, end+1)))

sumLimit = int(input('Enter a number to sum to: '))

print('\nSerial job')
startTime = time.time()
serialSum = sum_range_serial(1, sumLimit)
print('Elapsed time:', time.time()-startTime)
print('The sum is', serialSum)

print('\nParallel job')
numProc = int(input('Enter the desired number of parallel processes: '))
output = mp.Queue()
processes = [mp.Process(target=sum_range_par,
                        args=(jobID*sumLimit/numProc+1,
                              (jobID+1)*sumLimit/numProc, output))
             for jobID in range(numProc)]
startTime = time.time()
for p in processes:
    p.start()
for p in processes:
    p.join()
print('Elapsed time:', time.time()-startTime)
procResults = [output.get() for p in processes]
parSum = numpy.sum(numpy.array(procResults))
print("Each processes' results:", procResults)
print('The sum is', parSum)