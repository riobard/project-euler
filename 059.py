from __future__ import division
from itertools import cycle

msg     = map(int, open('cipher1.txt').read().split(','))
cyc     = len(msg) // 3 + 1
common  = set(ord(c) for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ,abcdefghijklmnopqrstuvwxyz 0123456789.')
lower   = [ord(c) for c in 'abcdefghijklmnopqrstuvwxyz']

def guess(key):
    #rs  = [m ^ k for m, k in zip(msg, key*cyc)]
    rs  = [m ^ k for m, k in zip(msg, cycle(key))]
    return sum(c in common for c in rs) / len(rs)


prob, key   = max((guess([a,b,c]), [a,b,c]) 
                  for a in lower for b in lower for c in lower)

decrypted   = [m ^ k for m, k in zip(msg, cycle(key))]
print ''.join(map(chr, decrypted))
print sum(decrypted)

