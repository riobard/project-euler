from itertools import takewhile
from euler import fibonacci
print sum(e for e in (takewhile(lambda x: x<4*10**6, fibonacci)) if e%2==0)
