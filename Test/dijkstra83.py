from time import clock
t = clock()
 
M = [map(int, line.strip().split(',')) for line in open('matrix.txt')]
N=len(M)-1

TM=[[10000*80 for a in range(N+1)] for a in range(N+1)]
 
def sol_up(a,b):
    if b==N and a==N:
        TM[a][b]=0
        return 0
    r=0
    if a<N:
        t=min(TM[a][b],M[a+1][b]+TM[a+1][b])
        if TM[a][b]!=t:
            TM[a][b]=t
            r=1
    if b<N:
        t=min(TM[a][b],M[a][b+1]+TM[a][b+1])
        if TM[a][b]!=t:
            TM[a][b]=t
            r=1
    if a>0:
        t=min(TM[a][b],M[a-1][b]+TM[a-1][b])
        if TM[a][b]!=t:
            TM[a][b]=t
            r=1
    if b>0:
        t=min(TM[a][b],M[a][b-1]+TM[a][b-1])
        if TM[a][b]!=t:
            TM[a][b]=t
            r=1
    return r
 
def sol_():
    r=0
    for b in range(N,-1,-1):
        for a in range(N,-1,-1):
            if sol_up(a,b): r+=1
    return r
 
s=0
z=1
while z:
    z=sol_()
    #print z
    s+=1
mi=TM[0][0]+M[0][0]
print mi
print clock()-t, 's', s
