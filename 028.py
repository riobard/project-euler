'''
Some observations:
    1. the clock-wise-spining spiral always ends in the top-right corner
    2. the length of each side inreases by 2 every circle outward
    3. except the center, the 4 corners are easy to find

'''


from itertools import count, takewhile

# my complex version

def take(n, iter):
    return [iter.next() for i in range(n)]

def g(r):
    ' generate the # of elements in each circle of a spiral of radius r '
    last    = 0
    accu    = 0
    for each in (n**2 for n in xrange(1, r+1, 2)):
        last    = each - accu
        yield last
        accu    = each

def g2():
    cnt = count(1)
    for circle in (take(n, cnt) for n in g(1001)):
        for each in circle[::-1][::max(1, len(circle)//4)][::-1]:
            yield each

print sum(g2())

# another elegant solution
# it turns out that working backwards (counter-clockwise) is much simpler

def g3():
    for i in range(1001, 1, -2):
    # work backwards # of elements in each circle of the spiral
        k   = i**2      # the top-right corner value
        for j in range(4):  # work backwards the 4 corner values
            yield k - j*(i-1)
    yield 1     # the center of the spiral

print sum(g3())
