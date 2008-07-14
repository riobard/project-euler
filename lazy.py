''' Lazy List module

Two goals:
    1. Lazy lists should be no different from ordinary lists in users' view. 
    2. Provide a decorator function to transform a generator to a lazy list. 
'''

class LazyException(Exception): pass

class LazyList(object): 
    # must be new style class for slicing to work properly
    # otherwise l[:] will result in a slice object (0, sys.maxint, None)
    # instead of (None, None, None)

    def __init__(self, g):
        self.l  = []    # interal cache of generated list
        self.g  = g     # g is an instantiated generator

    def _extend(self, n):
        self.l.extend(self.g.next() for _ in range(n))

    def __getitem__(self, k):
        if isinstance(k, int):  # l[n]
            d   = k - len(self.l)
            if d>=0: self._extend(d+1)
            return self.l[k]
        elif isinstance(k, slice):  # l[start:stop:step]
            if k.stop is None:  # l[_:] -> extend to the end
                self.l.extend(self.g)
            else:
                d   = k.stop - len(self.l)
                if d>=0: self._extend(d+1)
            return self.l[k]
        else:
            raise LazyException('Invalid index: %s' % k)

    def __call__(self, k):  # mimic a callable function
        return self[k]

    def __iter__(self):
        def iter():
            for each in self.l:
                yield each

            for each in self.g:
                self.l.append(each) # incremental cache
                yield each

        return iter()

def lazylist(g):
    '''lazylist decorator.

    used to make a LazyList from generator definition'''

    return lambda *a: LazyList(g(*a))


def compact(s):
    '''Compact a sequence: [a,b,b,c,c,c] -> [(a,1),(b,2),(c,3)]'''

    @lazylist
    def g():
        seq = iter(s)   # make it an iterator, otherwise there will be one more
                        # count of the 1st element if s is a list/str/tuple
        cnt = 0
        for it in seq:  
            cnt = 1 # if the sequence is empty, cnt will be 0, which stops the
                    # last yield statement at the bottom
            break
        # TRICK: this will pop the 1st element from the sequence while leaving 
        # the rest untouched. this is useful to work with iterators, since a 
        # iterator only supports one-pass read

        for e in seq:
            if it==e:
                cnt += 1
            else:
                yield (it, cnt)
                it, cnt = e, 1  # reset counter

        if cnt: yield (it, cnt)

    return g()

def expand(s):
    '''Expand a sequence: [(a,1),(b,2),(c,3)] -> [a,b,b,c,c,c]'''

    @lazylist
    def g():
        for (e, cnt) in s:
            for i in range(cnt):
                yield e

    return g()
