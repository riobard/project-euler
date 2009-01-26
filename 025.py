from euler import fibonacci
from itertools import count, izip, takewhile

print max(izip(count(), (takewhile(lambda x:x<10**999, fibonacci))))[0] + 1
# the fibonacci sequence in this problem starts from 1 instead of 0, so +1
