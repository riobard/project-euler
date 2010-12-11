from itertools import count


def P062():
    d = {}
    for n in count(0):
        s = ''.join(sorted(str(n**3)))
        l = d.get(s, []) + [n]
        d[s] = l
        if len(l) == 5:
            break

    return min(l)**3


print P062()
