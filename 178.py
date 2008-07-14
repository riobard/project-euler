def ispandigital(n):
    return set(str(n)) == set('01234556789')

def isstep(n):
    l   = map(int, str(n))
    print l

isstep(45656)
