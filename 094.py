'''
Heron's formula:

Area = sqrt(s * (s - a) * (s - b) * (s - c))

s = (a + b + c) / 2

a, b, c are the lengths of the three sides of the triangle. 


here we need 

a, a, a + 1

or 

a, a, a - 1


therefore 

A = (a+1) * sqrt((3a+1) * (a-1)) / 4

or 

A = (a-1) * sqrt((3a-1) * (a+1)) / 4

where A must be integral. 
'''

def naive():
    acc = 0
    a = 1
    while a <= 10**9//3:
        a += 1      # a > 2 otherwise 1, 1, 2 or 1, 1, 0 is not a triangle
        p1 = 3*a+1
        p2 = 3*a-1

        r1 = p1 * (a - 1)
        if int(r1**.5)**2 == r1 and ((a+1)**2 * r1) % 16==0:
            acc += p1
            print a, a, a + 1

        r2 = p2 * (a + 1)
        if int(r2**.5)**2 == r2 and ((a-1)**2 * r2) % 16==0:
            acc += p2
            print a, a, a - 1

    return acc

#print naive()


'''
http://en.wikipedia.org/wiki/Heronian_triangle#Almost-equilateral_Heronian_triangles
'''



def PPT():
    ' Primitive Pythagorean Triples '

    from collections import deque
    fifo = deque([(3, 4, 5)])
    while True:
        (a, b, c) = fifo.popleft()
        yield (a, b, c)
        fifo.append((a-2*b+2*c, 2*a-b+2*c, 2*a-2*b+3*c))
        fifo.append((a+2*b+2*c, 2*a+b+2*c, 2*a+2*b+3*c))
        fifo.append((-a+2*b+2*c, -2*a+b+2*c, -2*a+2*b+3*c))




def use_ppt():
    acc = 0
    for (x, y, z) in PPT():
        if z==2*x+1 or z==2*x-1:
            p = 2*z + 2*x
            if p > 10**9: break
            print z, z, 2*x
            acc += p

            
        if z==2*y+1 or z==2*y-1:
            p = 2*z + 2*y
            if p > 10**9: break
            print z, z, 2*y
            acc += p

    assert 518408346 == acc
    print acc

use_ppt()

'needs PyPy for both implementation ...'
