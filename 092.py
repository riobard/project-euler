from euler import factorial

def naive():
    
    def a89(n):
        while True:
            if n == 1:
                return False

            if n == 89:
                return True

            n   = sum(int(each)**2 for each in str(n))

    c   = 0
    for n in range(1, 10000000):
        if a89(n):
            c   += 1

    print c



def slightlybetter():

    def chain(n):
        while True:
            if n == 0 or n == 1 or n == 89:
                return n

            n   = sum(int(each)**2 for each in str(n))

    c567    = [chain(n) for n in range(567+1)]

    c   = 0
    for n in range(10000000):
        if 89 == c567[sum(int(each)**2 for each in str(n))]:
            c   += 1
    print c



def efficient():

    def chain(n):
        while True:
            if n == 0 or n == 1 or n == 89:
                return n

            n   = sum(int(each)**2 for each in str(n))


    

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
            d *= factorial[v]

        return factorial[l] / d



    def g():

        for d0 in range(10):
            for d1 in range(d0+1):
                for d2 in range(d1+1):
                    for d3 in range(d2+1):
                        for d4 in range(d3+1):
                            for d5 in range(d4+1):
                                for d6 in range(d5+1):
                                    yield [d6, d5, d4, d3, d2, d1, d0]



    c567    = [chain(n) for n in range(567+1)]
    c   = 0
    for each in g():
        if 89 == c567[sum(d**2 for d in each)]:
            c   += permutation(each)

    return c


print efficient()
