

from sys import argv
from pprint import pprint
from itertools import takewhile, count
from math import ceil
from euler import memoized


@memoized
def swaps(n=9):
    ' all square anagram digit pairs with n digits '
    anagrams = {}

    lo = int(ceil((10**(n-1))**.5))
    hi = int((10**n)**.5)

    for each in (x**2 for x in range(lo, hi)):
        s = str(each)
        ss = ''.join(sorted(s, reverse=True))
        if ss in anagrams:
            anagrams[ss].append(s)
        else:
            anagrams[ss] = [s]


    pairs = []
    for v in anagrams.values():
        if len(v) > 1:
            v = sorted(v)
            for a in v:
                for b in v[1:]:
                    if a != b:
                        pairs.append((a, b))
    return pairs




def swap(word1, word2):
    ' word1 and word2 are a square anagram word pair '

    if sorted(word1) == sorted(word2):
        patterns = swaps(len(word1))
        for (p1, p2) in patterns:
            l1 = sorted(zip(word1, p1))
            l2 = sorted(zip(word2, p2))
            if l1 == l2:

                d_char = {}
                d_digit = {}
                flag = True
                for (char, digit) in l1:
                    if char in d_char:
                        if d_char[char] != digit:
                            flag = False
                            break
                    else:
                        d_char[char] = digit


                    if digit in d_digit:
                        if d_digit[digit] != char:
                            flag = False
                            break
                    else:
                        d_digit[digit] = char


                if flag:
                    yield p1, p2




def anagrams(words):
    ' return all pairs of anagrams from a list of words '
    rs = {}
    for word in words:
        w = ''.join(sorted(word))
        if w in rs:
            rs[w].add(word)
        else:
            rs[w] = set([word])

    pairs = []
    for (k, v) in rs.items():
        if len(v)>1:
            v = sorted(v)
            for a in v:
                for b in v[1:]:
                    if a != b:
                        pairs.append((a,b))

    return pairs



def main():
    words = open(argv[1]).read().replace('"', '').split(',')
    for (word1, word2) in anagrams(words):
        for (p1, p2) in swap(word1, word2):
            p1 = int(p1)
            p2 = int(p2)
            yield max(p1, p2), min(p1, p2), word1, word2



print max(main())
