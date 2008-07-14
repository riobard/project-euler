from time import time
t0 = time()
f = open("matrix.txt")
filetext = f.read()
f.close()
matrix = filetext.strip().split("\n")
for i in range(0,len(matrix)):
    matrix[i] = matrix[i].split(",")
    for j in range(0,len(matrix[i])):
        matrix[i][j] = int(matrix[i][j])
 
Neighbors = {}
MinSoFar = {}
for c in range(0,80):
        if c == 79: dcs = [-1]
        elif c == 0: dcs = [1]
        else: dcs = [-1,1]
        for r in range(0,80):
            MinSoFar[(r,c)] = 1600000
            if r == 79: drs = [-1]
            elif r == 0: drs = [1]
            else: drs = [-1,1]
            Neighbors[(r,c)] = []
            for dc in dcs:
                Neighbors[(r,c)].append((r,c+dc))
            for dr in drs:
                Neighbors[(r,c)].append((r+dr,c))
MinSoFar[(79,79)] = matrix[79][79]
NodesToCheck = set([(78,79),(79,78)])
 
def UpdateMatrix():
    global matrix,Neighbors,MinSoFar,NodesToCheck
    CheckNextTime = set()
    for (r,c) in NodesToCheck:
        if (r,c) in CheckNextTime:
            CheckNextTime.remove((r,c))
        minneighborval = 1600000
        rcneighbors = list(Neighbors[(r,c)])
        for nbr in rcneighbors:
            neighborval = MinSoFar[nbr]
            if neighborval < minneighborval:
                minneighborval = neighborval
                minneighbor = nbr
        newval = matrix[r][c] + minneighborval
        if newval == MinSoFar[(r,c)]: continue
        MinSoFar[(r,c)] = newval
        rcneighbors.remove(minneighbor)
        for nbr in rcneighbors: CheckNextTime.add(nbr)
        NodesToCheck = CheckNextTime
 
iteration = 0
limit = 164
while iteration < limit:
    UpdateMatrix()
    iteration += 1
 
print "the answer is", MinSoFar[0,0]
print "took", time()-t0

