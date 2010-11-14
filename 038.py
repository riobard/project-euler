# The number must be of the form
# ABCD.EFGHI where ABCD * 2 = EFGHI

from euler import permutate

for permu in sorted(permutate('987654321'), reverse=True):
    i1, i2  = map(lambda x: int(''.join(x)), [permu[:4], permu[4:]])
    if i1*2 == i2:
        print int(''.join(permu))
        break
