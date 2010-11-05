'''

bit representation of a card

rrrr shdc 

0-3 shdc: suit of the card (Spade, Heart, Diamond, Club)
4-7 rrrr: rank of the card (0-12: "23456789TJQKA")

'''


RANK    = "23456789TJQKA"
SUIT    = "CDHS"
CARDMAP = dict((RANK[rank] + SUIT[suit], (rank<<4)|(1<<suit))
            for rank in range(len(RANK)) for suit in range(len(SUIT)))


# Rank of a hand of 5 cards
HIGHCARD        = 0
ONEPAIR         = 1
TWOPAIRS        = 2
THREEOFAKIND    = 3
STRAIGHT        = 4
FLUSH           = 5
FULLHOUSE       = 6
FOUROFAKIND     = 7
STRAIGHTFLUSH   = 8
ROYALFLUSH      = 9


def rank(hand):
    c1, c2, c3, c4, c5  = hand
    r1, r2, r3, r4, r5  = sorted((card>>4 for card in hand), reverse=True)

    # is the hand a flush?
    isflush     = c1 & c2 & c3 & c4 & c5 & 0b1111

    # is the hand a straight? ABCDE
    isstraight  = (r1-r2==r2-r3==r3-r4==r4-r5==1)

    if isflush and isstraight:
        if r1==11:
            return [ ROYALFLUSH ]
        else:
            return [ STRAIGHTFLUSH, r1 ]

    if isflush:
        return [ FLUSH, r1, r2, r3, r4, r5 ]
    
    if isstraight:
        return [ STRAIGHT, r1 ]


    # is the hand four of a kind? AAAAB or ABBBB
    is4ofakind  = (r2 == r3 == r4) and (r1==r2 or r4==r5)
    if is4ofakind:
        if r1==r2:  # AAAAB
            return [ FOUROFAKIND, r1, r5 ]
        else:   # ABBBB
            return [ FOUROFAKIND, r5, r1 ]

    # is the hand full house? AAABB or AABBB
    isfullhouse = (r1==r2==r3 and r4==r5) or (r1==r2 and r3==r4==r5)
    if isfullhouse:
        if r2==r3:  # AAABB
            return [ FULLHOUSE, r1, r5 ]
        else:  # AABBB
            return [ FULLHOUSE, r5, r1 ]


    # is the hand three of a kind? AAABC, ABBBC, ABCCC
    is3ofakind  = (r1==r2==r3) or (r2==r3==r4) or (r3==r4==r5)
    if is3ofakind:
        if r2==r3:
            if r3!=r4:   # AAABC
                return [ THREEOFAKIND, r1, r4, r5 ]
            else:   # ABBBC
                return [ THREEOFAKIND, r2, r1, r5 ]
        else:   # ABCCC
            return [ THREEOFAKIND, r5, r1, r2 ]


    # is the hand two pairs? AABBC, AABCC, ABBCC
    is2pairs    = (r1==r2 and r3==r4) or (r1==r2 and r4==r5) or (r2==r3 and r4==r5)
    if is2pairs:
        if r1==r2:
            if r3==r4:  # AABBC
                return [ TWOPAIRS, r1, r3, r5 ]
            else: # AABCC
                return [ TWOPAIRS, r1, r5, r3 ]
        else:   # ABBCC
            return [TWOPAIRS, r2, r5, r1 ]


    # is the hand one pair? AABCD, ABBCD, ABCCD, ABCDD
    is1pair = (r1==r2) or (r2==r3) or (r3==r4) or (r4==r5)
    if is1pair:
        if r1==r2:  # AABCD
            return [ ONEPAIR, r1, r3, r4, r5 ]
        elif r2==r3: # ABBCD
            return [ ONEPAIR, r2, r1, r4, r5 ]
        elif r3==r4: # ABCCD
            return [ ONEPAIR, r3, r1, r2, r5 ]
        else:
            return [ ONEPAIR, r5, r1, r2, r3 ]

    # else the hand must be a high card
    ishighcard  = True
    if ishighcard:
        return [ HIGHCARD, r1, r2, r3, r4, r5 ]



def p1win(hand_str):
    ''' if p1 wins '''
    hand    = [CARDMAP[card] for card in hand_str.strip().split(' ')]
    p1, p2  = hand[:5], hand[5:]

    return rank(p1) > rank(p2)


from sys import argv
print sum(p1win(line) for line in open(argv[1]))
