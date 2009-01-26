'''
There are various methods to determine if a point is an interior/exterior
point of a polygon. http://local.wasp.uwa.edu.au/~pbourke/geometry/insidepoly/
'''


'''
This  works for all convex polygon

Walk along the edges of a convex polygon in a direction (clockwise/counter-
clockwise). If point p is always on the same side (right/left) as you walk, p
is an interior point of the convex polygon; otherwise p is an exterior point.
'''

def position(p, line):
    '''Return the sign of relation between point p and line

    This method makes use of exterior product of vector A->P and B->P to
    calculate the signed area of the parallelogram formed by the two vectors. 
    '''
    px, py              = p
    (ax, ay), (bx, by)  = line
    s, t                = px-ax, py-ay  # vector AP
    u, v                = px-bx, py-by  # vector BP
    return s*v - t*u    # exterior product of vector AP and BP, a.k.a signed
                        # area of the parallelogram formed by the two vectors


def pointinpolygon(pt, pts):
    ''' Check if point pt is an interior point of polygon specified by a list of
    points pts
    '''
    shiftpts    = pts[1:] + [pts[0]]    # shift the points ...
    pairs       = zip(pts, shiftpts)    # ... to generate a list of pairs
    signs       = [position(pt, pair) for pair in pairs]
    return all(map(lambda x: x>=0, signs)) or all(map(lambda x: x<=0, signs))

print sum(pointinpolygon((0, 0), [(ax,ay),(bx,by),(cx,cy)])
          for ax,ay,bx,by,cx,cy in 
          (map(int, line.split(',')) for line in open('triangles.txt')))


'''
Signed Area and orientation of polygons

Need some modern geometry knowledge to understand ...
'''
def signedarea(x1,y1,x2,y2,x3,y3):
    # the order of the three points determines the orientation of the triangle
    # positive if counterclockwise, negative if clockwise
    return (-x2*y1 + x3*y1 + x1*y2 - x3*y2 - x1*y3 + x2*y3) * .5
    # this is the signed area of the triangle. half of the parallelogram
    # calculated by exterior product of the two vectors

def orientation(x1,y1,x2,y2,x3,y3):
    return signedarea(x1,y1,x2,y2,x3,y3) > 0

def contains(x1,y1,x2,y2,x3,y3,xp,yp):
    # for point p (xp, yp) lies in the triangle, the three sub-triangles must
    # have the same orientation
    o1  = orientation(x1,y1,x2,y2,xp,yp)
    o2  = orientation(x2,y2,x3,y3,xp,yp)
    o3  = orientation(x3,y3,x1,y1,xp,yp)
    return o1 == o2 == o3


print sum(contains(ax,ay,bx,by,cx,cy, 0, 0) for ax,ay,bx,by,cx,cy in 
          (map(int, line.split(',')) for line in open('triangles.txt')))


'''
A more elegant way

Triangle ABC contains P if the A(ABP) + A(ACP) + A(BCP) = A(ABC)

A() is the area function of a triangle

Heron's formula to calcuate area of triangles

A   = (s * (s - a) * (s - b) * (s - c)) ** .5
where
    s   = (a + b + c)/2
    a,b,c are the length of the three sides

Note this method is not very perfect due to rounding error in area
'''

def distance(x1,y1,x2,y2):
    return ((x1-x2)**2 + (y1-y2)**2)**.5

def area(a, b, c):
    s   = (a + b + c) * .5
    return (s * (s - a) * (s - b) * (s - c)) ** .5

def areatriangle(x1,y1,x2,y2,x3,y3):
    a   = distance(x1,y1,x2,y2)
    b   = distance(x1,y1,x3,y3)
    c   = distance(x2,y2,x3,y3)
    return area(a,b,c)

def contain(x0,y0,x1,y1,x2,y2,x3,y3):
    s0  = areatriangle(x1,y1,x2,y2,x3,y3)
    s1  = areatriangle(x0,y0,x1,y1,x2,y2)
    s2  = areatriangle(x0,y0,x1,y1,x3,y3)
    s3  = areatriangle(x0,y0,x2,y2,x3,y3)
    return  abs((s1 + s2 + s3) - s0) < .0001    # combat rounding error

print sum(contain(0, 0, ax,ay,bx,by,cx,cy) for ax,ay,bx,by,cx,cy in 
          (map(int, line.split(',')) for line in open('triangles.txt')))
