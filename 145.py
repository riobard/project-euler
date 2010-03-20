def isreversible(n):
    if n%10:
        s   = n + int(str(n)[::-1])
        return all(i%2 for i in (map(int, str(s))))
    else:
        return False


def nreversible(d):
    '''
    # of reversible numbers with n digits
    '''
    n, r    = divmod(d, 4)
    if r == 0 or r == 2:
        n   = d // 2
        return 20*(30**(n-1))       # 2n digit solutions (4n+0 or 4n+2)
    elif r == 1:
        return 0                    # no 4n+1 digits solutions
    else:
        return 5*20*((25*20)**n)    # 4n+3 digits solutions

for i in range(1,10):
    print i, nreversible(i)


'''
print sum(isreversible(i) for i in range(10**6,10**7))

for i in range(100000,1000000,12):
    if isreversible(i):
        print i, int(str(i)[::-1])
'''

'''
A good explanation by unknonw commenter:

I used only pencil and paper this time, and I must admit that this problem is
very interesting.

Essentially I followed the reasoning that smq explained in the third post, but
without thinking to the general solution as he did after the brute force, but
instead trying all possible (and valid) combinations of digit sums.

If one plots all the possible digit sums, you understand that:
* there are 25 couples of digits that have an even sum and bring no carry
* there are 25 couples of digits that have an even sum and bring a carry to
* the next sum there are 30 couples of digits with odd sum and no carry (10 of
* them include the 0, that sometimes we have to drop) the remaining 20 couples
* give a odd sum with carry

Furthermore, as we're adding only two numbers, the carry between a column and
the previous one can only be 1 or be absent. So, if we want to obtain a odd
sum, we need a odd sum if the incoming carry is zero, or a even sum if the
incoming carry is one.

In the following paragraphs, lines starting with * are almost evident
hypothesis. Assumptions follow the hypothesis.

Reasoning on 4-digit numbers (abcd+dcba):
* a+d is always odd and b+c must never give a carry
If a+d gives a carry, then b+c should be even with a carry to the next sum.
This case is contrast with the hypothesis and must be discarded.  If a+d does
not give a carry, b+c is odd with no carry.  -> So there are 20*30=600
solutions with 4 digits (I'm using 20 as first factor as a and d cannot be
zero).

Reasoning on 5-digit numbers (abcde+edcba):
* a+e is always odd and b+d must never give a carry. c+c is obviously always
* even. So, we need a carry from b+d to guarantee that c+c+<carry> is odd, but
* this is in contrast with the previous hypothesis.
-> No solutions.

Reasoning on 6-digit numbers (abcdef+fedcba):
* a+f is always odd and b+e must never give a carry
If a+f gives a carry, then b+e must be even. This means also that c+d must
give a carry, as we need a odd sum in the second column from the left. In this
case c+d should be both even (to make a odd sum in the third column) and odd
(to make a odd sum in the fourth column). Contrast, so wrong assumption.  If
a+f does not give a carry, then b+e is odd. This implies that c+d has no carry
and, furthermore, that this sum is odd.  -> So there are 20*30*30=18000
solutions with 6 digits

Reasoning on 7-digit numbers (abcdefg+gfedcba):
* a+g is always odd and b+f must never give a carry. d+d is obviously always
* even.
If a+g gives a carry, then b+f is even. This implies that c+e gives a carry.
c+e must also be odd, as we need a odd sum in the fifth column from left. This
implies also that d+d must not give a carry (as we need a odd result in the
    third column).  If a+g does not give a carry, then b+f must be odd. This
means that c+e must not give a carry (as we need a odd sum in the second
    column). But, in this case, there is no possibility to obtain a odd sum in
the middle column (as d+d is even and there is no carry available). Wrong
assumption.  -> So there are 20*25*20*5=50000 solutions with 7 digits

Reasoning on 8-digit numbers (abcdefgh+hgfedcba):
* a+h is always odd and b+g must never give a carry.
If a+h gives a carry, b+g is even. Then, c+f must be odd (see the sixth
    column) and give a carry (second column). d+e must not give a carry, as we
already have an odd sum in the third column. If d+e is even, in the fourth
column we have an even sum (d+e+<no carry>). If d+e is odd, in the fifth
column we have an even sum (d+e+<carry from c+f>). So again we're stuck.  If
a+h does not give a carry, b+g is odd. f+c, then is odd too (sixth column) and
gives no carry (see second column). This is good as now we need d+e odd and
with no carry to complete the puzzle.  -> So there are 20*30*30*30=540000
solutions with 8 digits

This is a long (read: confused :) ) explanation but now I'm happy of having
written it :)

'''
