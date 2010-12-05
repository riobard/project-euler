from euler import gcd

def f(d):
    return sum(1 if 2*x < d < 3*x and gcd(x, d)==1 else 0
        for x in xrange(d//3, d//2+1))

print sum(f(d) for d in xrange(2, 12000+1))





' another approach (slower and consume more memory) '

from collections import deque
def CPP(M=None):
    ' Generate coprime pairs (m, n) with m <= M if M is given '
    def branch(m, n, M=None):
        q = deque([(m, n)])

        while len(q)>0:
            (m, n) = q.popleft()
            yield (m, n)

            if M is None:
                q.append((2*m-n, m))
                q.append((2*m+n, m))
                q.append((m+2*n, n))
            else:
                if 2*m-n <= M: q.append((2*m-n, m))
                if 2*m+n <= M: q.append((2*m+n, m))
                if m+2*n <= M: q.append((m+2*n, n))


    if M is None:
        for each in branch(2, 1): yield each
        for each in branch(3, 1): yield each
    else:
        for each in branch(2, 1, M): yield each
        for each in branch(3, 1, M): yield each


def another_way():
    print sum(1 if (2*n < m < 3*n) else 0 for (m, n) in CPP(12000))
    
