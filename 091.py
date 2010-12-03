



def is_right_triangle(x0, y0, x1, y1, x2, y2):
    a2 = (x1-x0)**2 + (y1-y0)**2
    b2 = (x2-x0)**2 + (y2-y0)**2
    c2 = (x2-x1)**2 + (y2-y1)**2
    return (a2>0 and b2>0 and c2>0) and (a2+b2==c2 or a2+c2==b2 or b2+c2==a2)


M = 50+1

print sum(is_right_triangle(0, 0, x1, y1, x2, y2)
    for x1 in range(M) for y1 in range(M)
    for x2 in range(M) for y2 in range(M)) // 2

