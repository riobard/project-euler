def quad():
    for a in range(1, 10):
        for b in range(a+1, 10):
            for c in range(b+1, 10):
                for d in range(c+1, 10):
                    yield a,b,c,d


OPS = [
    lambda x,y: x+y,
    lambda x,y: x-y,
    lambda x,y: x*y,
    lambda x,y: float(x)/y  # note: division by zero possible
    ]

# all possible full binary tree with 4 leaf nodes

TREES = [
    lambda op1, op2, op3, a, b, c, d: op1(op2(op3(a, b), c), d),
    lambda op1, op2, op3, a, b, c, d: op1(op2(a, op3(b, c)), d),
    lambda op1, op2, op3, a, b, c, d: op1(op2(a, b), op3(c, d)),
    lambda op1, op2, op3, a, b, c, d: op1(a, op2(op3(b, c), d)),
    lambda op1, op2, op3, a, b, c, d: op1(a, op2(b, op3(c, d)))
    ]


def ops_triple():
    for op1 in OPS:
        for op2 in OPS:
            for op3 in OPS:
                yield op1, op2, op3


def expr(a, b, c, d):
    from euler import permutate

    rs = set()

    for (op1, op2, op3) in ops_triple():
        for (a,b,c,d) in permutate([a, b, c, d]):
            for t in TREES:
                try:
                    n = t(op1, op2, op3, a, b, c, d)
                    if n > 0 and int(n) == n:
                        rs.add(n)
                except:
                    pass
    return rs


def maxn(a, b, c, d):
    n = 0
    for each in sorted(expr(a, b, c, d)):
        if each != n+1:
            return n
        else:
            n = each


print max((maxn(*t), t) for t in quad())
