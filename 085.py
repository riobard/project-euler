def f(W, H):
    return sum([w * h for w in range(1, W+1) for h in range(1, H+1)])    # takes a long time


'''
Sum of the matrix: 

1x1 1x2 1x3 1x4 ... 1xW
2x1 2x2 2x3 2x4 ... 2xW
3x1 3x2 3x3 3x4 ... 3xW
.   .   .   .       .
.   .   .   .       .
.   .   .   .       .
Hx1 Hx2 Hx3 Hx4 ... HxW


for each column
    sum_col = w*(1+H)*H/2
where w = 1, 2, 3, ..., W

    sum = (1+W)*W/2 * (1+H)*H/2
'''


def g(W, H):
    return W*(1+W)/2 * H*(1+H)/2


def run():
    d = target = 2000000
    for W in range(1,2000+1):
        for H in range(W, 2000+1):
            n   = g(W, H)
            dd  = abs(n - target)
            if dd < d:
                d   = dd
                print n, W, H, W * H

run()



''' 
Another way to look at this problem:

There is an analytical way to solve this one. If you imagine a rectangular grid
measuring a units across and b units down. There are a+1 vertical lines and b+1
horizontal lines. Each rectangle formed on this grid is made up of two vertical
lines and two horizontal lines. As there are C(a+1,2)=a(a+1)/2 ways of picking
two vertical lines and, similarly, b(b+1)/2, ways of picking two horizontal
lines. Hence, there are a(a+1)b(b+1)/4 rectangles on an a by b rectangular
grid.  
'''

