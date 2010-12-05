from euler import totient

print sum(totient(d) for d in xrange(2, 1000000+1))
