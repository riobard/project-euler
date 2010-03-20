from __future__ import division
from os import times
from sys import platform, version_info
from time import time, sleep

from collections import defaultdict

def groupcount(sq):
    ''' Accept a sequence, sq, and count its elements by group '''
    d   = defaultdict(int)  # default 0
    for each in sq:
        d[each] += 1
    return dict(d)

def timex():
    ' Return elapsed (user time, system time, real time) since last call '
    (utime, stime, _, _, _), rtime  = times(), time()
    if platform=='win32' and version_info[0]<=2 and version_info[1]<=5:
        utime, stime    = stime, utime

    while True:
        (utime2, stime2, _, _, _), rtime2 = times(), time()
        if platform=='win32' and version_info[0]<=2 and version_info[1]<=5:
            utime2, stime2    = stime2, utime2
        dutime, dstime, drtime  = utime2 - utime, stime2 - stime, rtime2 - rtime
        rs  = (dutime, dstime, drtime)
        print '%.4fu %.4fs %.4fr' % rs
        yield rs
        utime, stime, rtime = utime2, stime2, rtime2
timex   = timex().next



def bin(n):
    ''' Return the binary representation 

    >>> bin(4)
    '0b100'
    >>> bin(-4)
    '-0b100'
    '''

    sign    = '' if n >= 0 else '-'
    n       = abs(n)
    s       = []
    while n:
        n, r    = divmod(n, 2)
        s.append(r)
    return sign+'0b'+(''.join(map(str, s[::-1])) if len(s)>0 else '0')


if __name__ == '__main__':
    timex()
    max(xrange(10**7))
    sleep(5)
    timex()
