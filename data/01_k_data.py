import sys
sys.path.append('..')

import shelve

import tushare as ts

from lib.utils import get_codes

def wget_data(start,end):
    codes = get_codes()
    kdata = dict()
    for code in codes:
        try:
            d = ts.get_k_data(code, ktype='D', start=start, end=end)
        except IOError:
            d = ts.get_k_data(code, ktype='D', start=start, end=end)

        kdata[code] = d
        if len(kdata) % 100 == 0:
            print('len of data:{}'.format(len(kdata)))
    data={'start':start,
          'end':end,
          'kdata':kdata}
    return data


if __name__=='__main__':
    kdataname='01'
    start='2017-04-11'
    end='2018-04-11'

    print('kdataname:',kdataname)
    print('start:',start)
    print('end:',end)

    db=shelve.open('kdata')
    data=wget_data(start,end)
    db[kdataname]=data
    db.close()
