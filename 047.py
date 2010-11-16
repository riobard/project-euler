from euler import primefactors, upf


def find():
    n   = 1
    while True:
        n += 1

        if all(4==len(set(primefactors(n+i))) for i in range(4)):
            print n
            break


def find2():
    n=1
    t=0
    while True:
        if len((upf(n)))==4:
            t+=1
            if t==4:
                print n-3
                break
        else: t=0
        n+=1


find2()
