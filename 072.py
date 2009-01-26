from euler import hcf

def nocoprimes(n):
    ''' return the number of coprimes for each number < n '''
    return sum(hcf(i, n) == 1 for i in range(1,n))


def lenfarey(n):
    ''' return the length of Farey Sequence of order n '''
    return 2 + sum(nocoprimes(x) for x in range(2, n+1))

#print lenfarey(10**3)
#print sum(sum(hcf(x,y)==1 for x in range(1,y)) for y in range(2,10**4+1))

