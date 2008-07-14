'''
This problem is a variant of P0076

C(5-1, 3-1) = 6 ways to separate 5 coins in 3 piles

1: o|o|o o o = 1 + 1 + 3
2: o|o o|o o = 1 + 2 + 2
3: o|o o o|o = 1 + 3 + 1
4: o o|o|o o = 2 + 1 + 2
5: o o|o o|o = 2 + 2 + 1
6: o o o|o|o = 3 + 1 + 1
'''

from euler import combination as C

print C(4,2)
