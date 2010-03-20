from euler import ispalindromic

print max(i*j 
        for i in range(100,1000) 
        for j in range(100,1000) 
        if ispalindromic(str(i*j)))
