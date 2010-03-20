n   = 10000//3
d   = {}
for a in range(1,n+1):
    for b in range(a+1, n+1):
        s   = a*a + b*b
        c   = int(s**.5)
        l   = a + b + c
        if l > 10000:
            break
        if (s == c*c):
            if l in d:
                d[l]  += 1
            else:
                d[l]  = 1

print sum(d[k] == 1 for k in d)
