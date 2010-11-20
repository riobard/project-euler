'''
This problem is a variant of P0078

1   = 1

2   = 2
    = 1 + 1

3   = 3
    = 2 + 1
    = 1 + 1 + 1

4   = 4
    = 3 + 1
    = 2 + 2
    = 2 + 1 + 1
    = 1 + 1 + 1 + 1

5   = 5
    = 4 + 1
    = 3 + 2
    = 3 + 1 + 1
    = 2 + 2 + 1
    = 2 + 1 + 1 + 1
    = 1 + 1 + 1 + 1 + 1

6   = 6
    = 5 + 1
    = 4 + 2
    = 4 + 1 + 1
    = 3 + 3
    = 3 + 2 + 1
    = 3 + 1 + 1 + 1
    = 2 + 2 + 2
    = 2 + 2 + 1 + 1
    = 2 + 1 + 1 + 1 + 1
    = 1 + 1 + 1 + 1 + 1 + 1

7   = 7
    = 6 + 1
    = 5 + 2
    = 5 + 1 + 1
    = 4 + 3
    = 4 + 2 + 1
    = 4 + 1 + 1 + 1
    = 3 + 3 + 1
    = 3 + 2 + 2
    = 3 + 2 + 1 + 1
    = 3 + 1 + 1 + 1 + 1
    = 2 + 2 + 2 + 1
    = 2 + 2 + 1 + 1 + 1
    = 2 + 1 + 1 + 1 + 1 + 1
    = 1 + 1 + 1 + 1 + 1 + 1 + 1


Find the # of ways to partition a number

http://www.math.temple.edu/~melkamu/html/partition.pdf

p(<0) = 0 
p(0) = 1
p(n) = p(n-1) + p(n-2) - p(n-5) - p(n-7) + p(n-12) + p(n-15) - p(n-22) - p(n-26) + ...

pentagonal number
f(k) = k*3(3k-1)/2

# of ways to partition n 
p(n) = \sum_{k=1}^{\infinity} (-1)^(k+1) * { p(n-f(k)) + p(n-f(-k)) }
'''


from euler import memoized

def f(k):
    'pentagonal number'
    return k*(3*k-1)/2


@memoized
def p(n):
    if n < 0: 
        s   = 0
    elif n == 0:
        s   = 1
    else:
        s   = 0
        k   = 0
        while True:
            k   += 1
            sign= -1 if k%2==0 else 1
            f1  = f(k)
            f2  = f(-k)
            s   += sign * (p(n-f1) + p(n-f2))
            if n-f1 <= 0 or n-f2 <= 0:
                break

    return s



assert 7 == p(5)
assert 56 == p(11)
assert 190569291 == p(100)-1    # excluding itself (1-partition)
print p(100)-1
