#print str(sum(x**x for x in range(1,1001)))[-10:]
#print sum(x**x for x in range(1,1001)) % 10**10
L   = 10**10
print sum(pow(x,x,L) for x in range(1,1001)) % L
