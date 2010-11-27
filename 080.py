'http://www.homeschoolmath.net/teaching/square-root-algorithm.php'


def sqrt(s, precision=100, as_str=False):

    def makepairs(d):
        pairs = []
        while True:
            d, r = divmod(d, 100)

            pairs += [r]

            if d == 0:
                break

        pairs.reverse()
        return pairs


    pairs = makepairs(s)
    p = i = 0
    b = pairs[p]
    int_digits  = []
    frac_digits = []

    while p < precision:

        for x in range(9, -1, -1):
            a = (20*i + x) * x
            if a <= b:
                break

        #print i, i*20+x, x, a, b, b-a

        if p < len(pairs):
            int_digits.append(x)
        else:
            frac_digits.append(x)


        i = i*10 + x
        p += 1
        b = (b - a)*100 + (pairs[p] if p < len(pairs) else 0)


        if b==0:    # perfect square
            break



    if as_str:
        int_part    = ''.join(map(str, int_digits))
        if len(frac_digits) > 0:
            frac_part   = ''.join(map(str, frac_digits))
            return int_part + '.' + frac_part
        else:
            return int_part
    else:
        return int_digits, frac_digits



s = 0
for n in range(100+1):
    intd, fracd = sqrt(n)
    if len(fracd) > 0:  
        # if it has fraction part, it is irrational; 
        # otherwise it is a perfect square. 
        s += sum(intd+fracd)

print s
