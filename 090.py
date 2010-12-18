from euler import combinate

def validate(cube1, cube2):
    s1 = set(cube1)
    s2 = set(cube2)
    if 6 in s1: s1.add(9)
    if 9 in s1: s1.add(6)
    if 6 in s2: s2.add(9)
    if 9 in s2: s2.add(6)
    return all((a in s1 and b in s2) or (a in s2 and b in s1)
        for (a,b) in [(0,1), (0,4), (0,9), (1,6), (2,5), (3,6), (4,9), (6,4), (8,1)])



def run():
    s = set()
    cubes = list(combinate(range(10), 6))
    for cube1 in cubes:
        for cube2 in cubes:
            if validate(cube1, cube2):
                str1 = ''.join(str(d) for d in sorted(cube1))
                str2 = ''.join(str(d) for d in sorted(cube2))
                s.add((str1, str2))

    return len(s)//2    # order of the two cubes does not matter

print run()


'''
Comment:

The wording about distinct sets in the last but one paragraph is quite misleading: for the purpose of forming 2-digit numbers
    {1, 2, 3, 4, 5, 6} and
    {1, 2, 3, 4, 5, 9} both reprents the extended set {1, 2, 3, 4, 5, 6, 9}

But when counting the # of distinct arrangments of the two cubes, the cube
    {1, 2, 3, 4, 5, 6}
is considered a different cube than
    {1, 2, 3, 4, 5, 9}

I made the mistake that they are counted as one. 
'''
