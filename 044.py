
def find():
    ps  = set()
    d   = {}
    n   = 0
    while True:
        n   += 1
        p   = n*(3*n-1)/2
        if p in d:
            return d[p]

        for each in ps:
            diff    = p - each
            if diff in ps:
                d[p + each] = diff

        ps.add(p)


print find()
