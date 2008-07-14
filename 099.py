from math import log as ln
lines   = open('base_exp.txt').read().split()
print max(zip(range(1,len(lines)+1), 
              map(lambda x: map(int, x.split(',')), lines)),
          key=lambda x: x[1][1]*ln(x[1][0]))
