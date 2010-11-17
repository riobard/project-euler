from euler import ispalindromic


def islychrel(n):

    for _ in range(50):
        nr  = int(''.join(reversed(str(n))))
        s   = n + nr
        if ispalindromic(str(s)):
            return False
        else:
            n   = s

    return True


print len([n for n in range(10000) if islychrel(n)])
