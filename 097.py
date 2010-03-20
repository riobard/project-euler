print (28433*(2<<(7830457-1)) + 1) % 10**10

# this is much faster
print str(pow(2,7830457,10**10) * 28433 + 1)[-10:]
