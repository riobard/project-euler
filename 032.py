# only two forms of permutations are possible 
# ABC x DE = FGHI
# ABCD x E = FGHI


from euler import permutate

rs  = set()
for permu in permutate('123456789'):

    m1, m2, prod  = int(''.join(permu[:3])), int(''.join(permu[3:5])), int(''.join(permu[5:]))

    if m1 * m2 == prod:
        print m1, 'x', m2, '=', prod
        rs.add(prod)


    m1, m2, prod  = int(''.join(permu[:4])), int(''.join(permu[4:5])), int(''.join(permu[5:]))
    if m1 * m2 == prod:
        print m1, 'x', m2, '=', prod
        rs.add(prod)
    

print 'All products:', rs
print 'Sum:', sum(rs)
