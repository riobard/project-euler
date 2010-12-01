from euler import memoized

@memoized
def sum_of_proper_divisors(n):
    s = 1
    i = 2
    while i**2 <= n:
        if n%i==0:
            s += i
            k = n // i
            if k != i:
                s += k
        i += 1

    return s



def amicable_chain(n, threshold=10**6):
    seen = set()
    chain = []
    while n not in seen:
        if n > threshold: return []
        seen.add(n)
        chain.append(n)
        n = sum_of_proper_divisors(n)

    return chain[chain.index(n):]



def search(threshold):
    n = 1
    longest = 0
    while n <= threshold:
        chain = amicable_chain(n)
        l = len(chain)
        if l > longest:
            longest = l
            print l, min(chain), chain

        n += 1

#search(10**6)  # takes about 1 min using PyPy; not good



def sieve_divisor_sum(limit):
    ' sieving for divisor sums '
    divsum = [0]*limit 
    for i in xrange(1,limit):
        for j in xrange(2*i, limit, i):
            divsum[j] += i

    return divsum



def main():

    threshold = 10**6
    divsum = sieve_divisor_sum(threshold)

    def amicable_chain(n):
        seen = set()
        chain = []
        while n not in seen:
            seen.add(n)
            chain.append(n)
            if n < threshold:
                n = divsum[n]
            else:
                return []

        return chain[chain.index(n):]


    def search():
        n = 1
        longest = 0
        while n <= threshold:
            chain = amicable_chain(n)
            l = len(chain)
            if l > longest:
                longest = l
                print l, min(chain), chain

            n += 1


    search()
    


main()
