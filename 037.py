# http://en.wikipedia.org/wiki/Truncatable_prime
# only 4260 left-truncatable primes and 83 right-tructable primes
# find the intersection

# two-sided (double trunctable) primes (excluding 2, 3, 5, 7) must be of the form
# [2357][1379]*[37]

# 2-digit: [2357][37]
# 23, 37, 53, 73

# 3-digit: [2357][1379][37]
# 313, 317, 373, 797

# 4-digit: [2357][1379][1379][37]
# 3137, 3797

# 6-digit: [2357][1379][1379][1379][1379][37]
# 739397


print sum([23, 37, 53, 73, 313, 317, 373, 797, 3137, 3797, 739397])
