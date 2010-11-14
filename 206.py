MIN = 10203040506070809 ** .5 # ~= 101010101
MAX = int(19293949596979899 ** .5)+1


i   = 1010100
while i < MAX:
    i   += 3                    # numbers end in 3
    s   = str(i*i)
    if s[::2] == '123456789':
        print i * 10
        break

    i   += 4                    # numbers end in 7
    s   = str(i*i)
    if s[::2] == '123456789':
        print i * 10
        break

    i   += 3                    # end in 0 so next loop works the same
