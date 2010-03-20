from collections import defaultdict

d   = defaultdict(int)  # d[key] default to 0 when first accessed
for a in range(1,500):
    for b in range(a,500):
        c   = (a**2+b**2)**.5
        ci  = int(c)
        if c == ci:
            p   = a+b+ci
            if p < 1000:
                d[p]    += 1

print max((d[k],k) for k in d)
