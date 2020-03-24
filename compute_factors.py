import sys
import time
import numpy as np
import os
import psutil

def run_job():
    '''
    Computes factors
    '''

    print('Started factors')
    k = 30000
    m,n = np.random.rand(k,k), np.random.rand(k,k)
    result =  m * n
    print(result.shape)
    time.sleep(60)

    process = psutil.Process(os.getpid())
    print(process.memory_info().rss)  # in bytes 
    print('Finished factors')


if __name__ == '__main__':
    run_job()