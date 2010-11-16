'''
Form:

ab/bc = a/c

where 
a = [1-9], b = [1-9], c = [0-9]
ab < bc
ab * c = bc * a

'''
for a in range(1, 10):
    for b in range(1,10):
        for c in range(10):
            if 10*a+b<10*b+c and (10*a+b)*c==(10*b+c)*a:
                print '%d%d/%d%d = %d/%d' % (a, b, b, c, a, c)
