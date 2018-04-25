import sys
sys.path.append('..')

import shelve
import numpy as np
import pandas as pd
from lib.utils import *


'''
Different from 02_ml_data.py
k2x add a extra column 'average' to record the average of high and low price
transform open,close,high,low to the percentage of the average
'''

def k2x(kline):
    '''Generate x, y from a duration
    '''
    #x=kline.iloc[:-1][['open','close','high','low','volume']].values.flatten()

    close=kline.iloc[-2]['close']
    high=kline.iloc[-1]['high']
    low=kline.iloc[-1]['low']
    if low>close:
        y=1
    elif low<=close<=high:
        y=0
    elif high<close:
        y=-1

    ave_price=np.mean(kline[['open', 'close', 'high', 'low']].values)
    x=kline[['open', 'close', 'high', 'low']]*100/ave_price-100
    x['volumne']=kline['volume']
    x=x.values.flatten()
    np.hstack((x, ave_price))
    return x,y

def _dataset(kline,start,end,duration):
    '''kline is kline data from a single stock
    '''
    start,end=str2date(start),str2date(end)
    if start>end: start,end=end,start
    kline=kline[kline['date'].apply(lambda x: start<=str2date(x)<=end)]

    if len(kline)<=duration:
        return None,None,None,None

    train=[kline.iloc[i:i+duration] for i in range(len(kline)-duration)]
    test=kline.iloc[len(kline)-duration:len(kline)]

    x_train,y_train=list(zip(*[k2x(k) for k in train]))
    x_test,y_test=k2x(test)

    return np.vstack(x_train),np.hstack(y_train),x_test,y_test



def dataset(kdata,start,end,duration):
    '''create train and test dataset from kdata.
    test data is generate by the newest several days' data.
    kdata: pandas DataFrame variable which create by 01_k_data.py
    start: start data
    end: end data
    duration: amount of continues days to generate a sample. The last day is for test.
    '''
    x_train,y_train=[],[]
    x_test,y_test=[],[]
    for code,kline in kdata.items():
        if int(code)%1000==0:
            print(code)
        if len(kline)<=duration: continue
        x1,y1,x2,y2=_dataset(kline,start,end,duration)
        if x1 is None: continue
        x_train.append(x1)
        y_train.append(y1)
        x_test.append(x2)
        y_test.append(y2)

    x_train,y_train=np.vstack(x_train),np.hstack(y_train)
    x_test,y_test=np.vstack(x_test),np.array(y_test)

    return x_train,y_train,x_test,y_test

if __name__=='__main__':
    kdataname='01'
    mldataname='02'
    start='2018-03-11'
    end='2018-04-11'
    duration=7

    print('kdataname:',kdataname)
    print('mldataname:',mldataname)
    print('start:',start)
    print('end:',end)
    print('duration:',duration)

    db=shelve.open('kdata','r')
    kdata=db[kdataname]['kdata']
    db.close()

    db=shelve.open('ml_data')
    x_train,y_train,x_test,y_test=dataset(kdata,'2018-03-11','2018-04-11',7)

    ml_data=dict({'start':start,
                 'end':end,
                 'duration':duration,
                 'ml_data':(x_train,y_train,x_test,y_test)}
                 )
    db[mldataname]=(x_train,y_train,x_test,y_test)
    db.close()