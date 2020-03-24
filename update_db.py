import sys
import time
import numpy as np
import pandas as pd 
def run_job():
    '''
    Daily price updates
    '''
    df = pd.read_csv('https://query1.finance.yahoo.com/v7/finance/download/%5EGSPC?period1=1553441378&period2=1585063778&interval=1d&events=history')
    print(df.shape)
    print('update db started')
    k = 30000
    m,n = np.random.rand(k,k), np.random.rand(k,k)
    result =  m * n
    print(result.shape)
    time.sleep(60)
    print('update db finished')


if __name__ == '__main__':
    run_job()