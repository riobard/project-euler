from calendar import weekday as wday
print sum(1 for y in range(1901,2001) for m in range(1,13) if wday(y,m,1) == 6)
