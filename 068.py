from euler import permutate


def ring3(a):
    line1 = a[0], a[1], a[2]
    line2 = a[3], a[2], a[5]
    line3 = a[4], a[5], a[1]
    if sum(line1)==sum(line2)==sum(line3):
        start = min(line1[0], line2[0], line3[0])
        if line1[0] == start:
            return line1 + line2 + line3
        elif line2[0] == start:
            return line2 + line3 + line1
        else:
            return line3 + line1 + line2

def find3():
    s = set()
    for each in permutate([1,2,3,4,5,6]):
        rs = ring3(each)
        if rs is not None:
            s.add(rs)

    for each in sorted(s):
        print each



def ring5(a):
    line1 = a[0], a[1], a[2]
    line2 = a[3], a[2], a[5]
    line3 = a[4], a[5], a[6]
    line4 = a[7], a[6], a[9]
    line5 = a[8], a[9], a[1]
    if sum(line1)==sum(line2)==sum(line3)==sum(line4)==sum(line5):
        start = min(line1[0], line2[0], line3[0], line4[0], line5[0])
        if line1[0]==start:
            return line1 + line2 + line3 + line4 + line5
        elif line2[0]==start:
            return line2 + line3 + line4 + line5 + line1
        elif line3[0]==start:
            return line3 + line4 + line5 + line1 + line2
        elif line4[0]==start:
            return line4 + line5 + line1 + line2 + line3
        else:
            return line5 + line1 + line2 + line3 + line4



def find5():
    s = set()
    for each in permutate([1,2,3,4,5,6,7,8,9,10]):
        rs = ring5(each)
        if rs is not None:
            ds = ''.join(str(d) for d in rs)
            if len(ds)==16:
                print ds
                s.add(ds)


    return max(s)

print find5()
