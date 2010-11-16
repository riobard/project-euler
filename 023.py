from euler import properdivisors


def isabundant(n):
    return sum(properdivisors(n)) > n


abundants  = [n for n in range(1,28123) if isabundant(n)]

sumofabundants  = set()

for i in range(len(abundants)):
    ai  = abundants[i]
    for j in range(i+1):
        aj  = abundants[j]
        s   = ai + aj
        sumofabundants.add(s)
        if s > 28123:
            break

print sum(set(n for n in range(28123)) -  sumofabundants)
