keys    = open('keylog.txt').read().split()
passcode= list(set(''.join(keys)))

def swap(passcode, key):
    '''
    Produced a rearranged passcode according to key
    '''
    x,y,z   = key
    a,b,c   = sorted([passcode.index(k) for k in key])
    passcode[a] = x
    passcode[b] = y
    passcode[c] = z
    return passcode


for key in keys:
    # repeat rearranging to get the correct passcode
    passcode    = swap(passcode, key)
print ''.join(passcode)
