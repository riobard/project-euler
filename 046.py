from euler import prime, isprime

c   = 1
while True:
    c += 2
    thisisit    = True  # assume c is the target
    if not isprime(c):
        for p in prime:
            if p == 2:
                continue

            if p < c:
                a   = int(((c - p) / 2)**.5)
                if c == p + 2 * a * a:
                    thisisit    = False     # c is not
                    #print '%d == %d + 2 * %d * %d' % (c, p, a, a)
                    break
            else:
                break

        if thisisit:
            print c
            break
