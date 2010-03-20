from euler import memoized

# note there is a simple formula. read Pascal's triangle for more

@memoized
def a(x, y):
    if (x==0 or y==0):
        return 1
    else:
        return a(x-1, y) + a(x, y-1)

print a(20, 20)
