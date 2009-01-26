words   = open('words.txt').read().replace('"','').split(',')

def istriangle(n):
    i   = int((n*2) ** .5)
    return i*(i+1)/2 == n

def istriangleword(w):
    return istriangle(sum(ord(c)-64 for c in w))

print len([w for w in words if istriangleword(w)])

print sum(1 for w 
        in open('words.txt').read().replace('"','').split(',') 
        if istriangle(sum(ord(c)-64 for c in w)))
