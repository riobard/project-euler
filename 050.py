from euler import primesieve

MAX = 1000000
p1m = primesieve(MAX)
p1ms= set(p1m)
l   = len(p1m)

def maxchainlen(MAX):
    # longest chain of consequtive primes that sums < MAX
    s   = 0
    for i in range(l):
        s   += p1m[i]
        if not s < MAX:
            return i


def find():
    mcl = maxchainlen(MAX)
    for chainlen in range(mcl, 0, -1):
        for i in range(l-chainlen):
            s   = sum(p1m[i:i+chainlen])

            if s >= MAX:
                break

            if s in p1ms:
                return s


print find()
