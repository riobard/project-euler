m   = ['zero', 'one', 'two', 'three',  'four', 'five', 'six', 'seven', 
        'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
        'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty',
        'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
n   = range(21) + range(30,91,10)
d   = dict(zip(n,m))

def num2word(n):
    if n in d:
        return d[n]
    elif n < 100:
        return '%s-%s' % (d[n // 10 * 10], d[n % 10])
    elif n < 1000:
        n100, n = n // 100, n % 100
        if n > 20:
            n10, n  = n // 10 * 10, n % 10
            return ('%s hundred' % d[n100]) + (' and %s' % d[n10] if n10 else '')\
                    + ('-%s' % d[n] if n else '')
        else:
            return ('%s hundred' % d[n100]) + (' and %s' % d[n] if n else '')

    elif n == 1000:
        return 'one thousand'
    else:
        raise 'Error'

print sum(len(num2word(i).replace(' ', '').replace('-','')) 
        for i in range(1,1001))
