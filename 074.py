'Similar to problem 92. Also related to problem 34.'

from euler import memoized, factorial as F



@memoized
def next(n):
    s   = 0
    while n!=0:
        n, r = divmod(n, 10)
        s   += F(r)

    return s


@memoized
def cycle(n):
    def recur(n, c, s=set()):
        if n in s:
            return c
        else:
            return recur(next(n), c+1, s ^ set([n]))
    return recur(n, 0)


def run():
 

    def permutation(seq):
        '''number of all permutations of a sequence without repetition

        there might be repeated elements in the sequence though

        e.g. [1, 1, 2, 3, 3, 4, 5]

        there are
            2 x 1's (A = 2) 
            1 x 2's (B = 1)
            2 x 3's (C = 2)
            1 x 4's (D = 1)
            1 x 5's (E = 1)

        total permutations: (A+B+C+D+E)! / (A! * B! * C! * D! * E!)
        '''


        l   = len(seq)

        f   = {}
        for each in seq:
            f[each] = f.get(each, 0) + 1

        d   = 1
        for v in f.values():
            d *= F(v)

        return F(l) / d



    def g():
        for d5 in range(9, 0, -1):  # 1st digit cannot be 0
            yield [d5] # 1-digit
            for d4 in range(d5, -1, -1):
                yield [d5, d4]  # 2-digit
                for d3 in range(d4, -1, -1):
                    yield [d5, d4, d3]  # 3-digit
                    for d2 in range(d3, -1, -1):
                        yield [d5, d4, d3, d2]  # 4-digit
                        for d1 in range(d2, -1, -1):
                            yield [d5, d4, d3, d2, d1]  # 5-digit
                            for d0 in range(d1, -1, -1):
                                yield [d5, d4, d3, d2, d1, d0]  # 6-digit


    s   = 0
    for seq in g():
        n   = int(''.join(str(d) for d in seq))
        if 60 == cycle(n):
            p   = permutation(seq)
            if 0 in seq:
                p0  = permutation([d for d in seq if d!=0])
                print seq, p, '-', p0 , '=', p - p0
                s   += p - p0
            else:
                print seq, p
                s   += p
    return s

print 'Positions of digits do not matter as long as there is no 0. Notice if there is any 0 in the sequence, they cannot be at the beginning. Subtract those permutations accordingly. '
print run()
