order   = '23456789TJQKA'   # Positions of the string are used to sort cards

def rank(hand):
    '''
    Given a hand (5 cards), return rank in the form of a list [r, v1, v2, ...].
    r is the rank of the hand, as follows:
        0: High Card
        1: One Pair
        2: Two Pairs
        3: Three of a Kind
        4: Straight
        5: Flush
        6: Full House
        7: Four of a Kind
        8: Straight Flush
        9: Royal Flush

    v1, v2, ... are the values of the most significant cards. 
    
    Examples 
        5H 5C 6S 7S KD  is in the form of One Pair, so r = 1. 
        Then the most significant card is 5H, since it is part of the pair. 
        Followed by KD 7S 6S, in decreasing orders. 
        The rank of this hand would be [1, 3, 11, 5, 4]. This list is used to
        compare two hands of cards. 

        Another hand 2C 3S 8S 8D TD, will have the rank of [1, 6, 8, 1, 0]. 
        
        Python compares lists by comparing each element from left to right. 
        Thus [1, 3, 11, 5, 4] < [1, 6, 8, 1, 0] becasue although the first 
        elements equal in both list, the second elements 3 < 6. 
    '''

    hand.sort(key=lambda card: -order.index(card[0]))    # sort: desc
    rank    = [False] * 10
    high    = [[]] * 10

    # Flush: All cards of the same suit
    rank[5] = all(hand[0][1] == hand[i][1] for i in range(1,5))
    # Significant cards:
    #   Each card from highest value to lowest
    high[5] = [order.index(hand[i][0]) for i in range(5)]

    # Straight: All cards are consecutive values
    # Value of 1st card - value of i-th card = i (i is 0-based index)
    rank[4] = all((order.index(hand[0][0]) - order.index(hand[i][0])) == i
                  for i in range(1,5))
    # Significant cards:
    #   The first card. All others are consecutive so no need to check
    high[4] = [order.index(hand[0][0])]

    # Straight Flush: All cards are consecutive values of same suit 
    rank[8] = rank[4] and rank[5]
    # Significant cards: 
    #   The first card. All others are consecutive so no need to check
    high[8] = [order.index(hand[0][0])]

    # Royal Flush: Ten, Jack, Queen, King, Ace in same suit
    # Straight Flush beginning with A: AKQJT
    rank[9] = rank[8] and (high[8] == 'A')
    # Sigificant cards: 
    #   None, since all royal flushes tie with each other
    high[9] = []

    # Four of a Kind: Four cards of the same value
    # Either AAAAB or ABBBB if sorted
    rank[7] = all(hand[0][0] == hand[i][0] for i in range(1,4)) or \
                  all(hand[1][0] == hand[i][0] for i in range(2,5))
    # Significant cards: 
    #   1. The midddle card, which is one of the Four of a Kind
    #   2. The card which is not one of the Four of a Kind
    high[7] = [order.index(hand[2][0]),
               order.index(hand[4][0]) if hand[0][0] == hand[2][0] else
               order.index(hand[0][0])]

    # Full House: Three of a kind and a pair
    # AAABB or AABBB
    rank[6] = (all(hand[0][0] == hand[i][0] for i in range(1,3)) and
               (hand[3][0] == hand[4][0])) or ((hand[0][0] == hand[1][0])
                and all(hand[2][0] == hand[i][0] for i in range(3,5)))
    # Significant cards:
    #   1. The middle card, which is one of the Three of a Kind
    #   2. The card of the pair
    high[6] = [order.index(hand[2][0]),
               order.index(hand[4][0]) if hand[0][0] == hand[2][0] else
               order.index(hand[0][0])]

    # Three of a Kind: Three cards of the same value
    # AAABC or ABBBC or ABCCC
    rank[3] = (hand[0][0] == hand[1][0] == hand[2][0]) or \
              (hand[1][0] == hand[2][0] == hand[3][0]) or \
              (hand[2][0] == hand[3][0] == hand[4][0])
    # Significant cards:
    #   1. The middle card, which is one of the Three of a Kind
    #   2. Other cards, from highest to lowest
    high[3] = [order.index(hand[2][0])] + [order.index(card[0])
               for card in hand if card[0] != hand[2][0]]

    # Two Pairs: Two different pairs
    # AABBC or AABCC or ABBCC
    rank[2] = ((hand[0][0] == hand[1][0]) and ((hand[2][0] == hand[3][0]) or 
               (hand[3][0] == hand[4][0]))) or ((hand[1][0] == hand[2][0]) and
               (hand[3][0] == hand[4][0]))
    # Significant cards:
    #   1. The higher pairs
    #   2. The lower pairs
    #   3. The remaining one card
    face    = [card[0] for card in hand]
    for each in face:
        if face.count(each) == 1:   # find the solo card
            face.remove(each)       # remove the solo
            break                   # leaving the two pairs, ordered
    high[2] = map(order.index, [face[0], face[2], each])

    # One Pair: Two cards of the same value
    # AABCD or ABBCD or ABCCD or ABCDD
    rank[1] = (hand[0][0] == hand[1][0]) or (hand[1][0] == hand[2][0]) or \
              (hand[2][0] == hand[3][0]) or (hand[3][0] == hand[4][0])
    # Significant cards:
    #   1. The pairs
    #   2. The remaining cards
    face    = [card[0] for card in hand]    # first get a list of face values
    for each in face:
        if face.count(each) == 2:                       # find the pair
            face    = [v for v in face if v != each]    # remove the pair
            break
    high[1] = [order.index(each)] + [order.index(v) for v in face]

    # High Card: Highest value card
    # True if all previous conditions are false
    rank[0] = all(not each for each in rank[1:])
    # Significant cards:
    #   All, from highest to lowest
    high[0] = [order.index(card[0]) for card in hand]

    r   = max(i for i in range(10) if rank[i])  # find the highest rank
    return [r] + high[r]    # return the rank list

print sum(rank(h1) > rank(h2) for (h1, h2) in 
          map(lambda cards: (cards[:5], cards[5:]), [line.split() 
          for line in open('poker.txt').read().strip().split('\n')]))
