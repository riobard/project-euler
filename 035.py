from euler import primesieve

def circular(n):
    '''
    Return a list of n rotation
    '''
    s   = str(n)
    return [int(s[i:] + s[:i]) for i in range(len(s))]

def f(n):
    # filter out all primes > 10 and containing 024568
    if n < 10:
        return True

    s   = str(n)
    for each in '024568':
        if each in s:
            return False
    else:
        return True


def iscircularprime(n):
    return all(each in primes for each in circular(n))

primes  = [x for x in primesieve(10**6) if f(x)]
print sum(iscircularprime(x)  for x in primes)
