
def rindex(s, v):
    return len(s)+ ~list(reversed(s)).index(v)


def frac(a, b):
    '''Return the precise representation of fraction a/b with recurring cycle
    
    e.g.
        1/2 = 0.5  => 0, [5], []
        1/3 = 0.(3) => 0, [], [3]
        1/6 = 0.1(6) = 0, [1], [6]
    '''
    rs  = []
    ds  = []
    d, r    = divmod(a, b)
    id  = d     # digits before the dot
    if r != 0:
        while True:
            a   = r
            cnt = 0
            while a < b:
                a *= 10
                cnt += 1

            if cnt > 1:
                ds  += [0]*(cnt-1)
                rs  += [-1]*(cnt-1)

            d, r    = divmod(a, b)

            if r == 0:  # finite fraction
                ds  += [d]
                return id, ds, []

            if r in rs:
                i   = rindex(rs, r)
                if d != ds[i]:      # merge 0.3(3) into 0.(3)
                    ds  += [d]
                    if i == len(rs) - 1:    # dealing with edge cases 1/6 = 0.1(6)
                        i   += 1
                        #''.join(map(str, ds[i:])))
                return id, ds[:i], ds[i:]

            ds  += [d]
            rs  += [r]


def pp(a, b):
    'Pretty print the decimal representation of a/b'
    id, nonrecur, recur  = frac(a, b) 
    rs   ='%s.%s' % (id, ''.join(map(str, nonrecur)))
    if len(recur) > 0:
       rs += '(%s)' % (''.join(map(str, recur)))
    return rs



c   = []
for n in range(2, 1000):
    id, nonrecur, recur = frac(1, n)

    c   += [(len(recur), n)]

k, n    = max(c)

print "1/%d = " % n, pp(1, n), 'contains a recurring cycle of length', k
