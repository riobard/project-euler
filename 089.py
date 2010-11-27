ROMAN = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
        }

COMBO = {
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900
        }


DESC    = [(n, r) for (r, n) in ROMAN.items()] + [(n, r) for (r, n) in COMBO.items()]
DESC.sort(reverse=True)
# DESC = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

def parse_roman(s):
    ' parse a valid Roman numeral to its integer value '

    i = 0
    n = 0
    p = 1000
    while i < len(s):
        current = s[i]
        next = s[i+1] if i+1 < len(s) else ''
        pair = current + next

        if pair in COMBO:
            v = COMBO[pair]
            if p < v:
                return 0
            else:
                p = v
                n += v
                i += 2
        else:
            v = ROMAN[current]
            if p < v:
                return 0
            else:
                p = v
                n += v
                i += 1
    return n



def test_parse_roman():
    assert 3 == parse_roman('III')
    assert 4 == parse_roman('IIII') # valid but not minimal (should be IV)
    assert 4 == parse_roman('IV')
    assert 0 == parse_roman('IIV')  # invalid
    assert 16 == parse_roman('XVI')
    assert 16 == parse_roman('XIIIIII') # valid but not minimal
    assert 16 == parse_roman('VVVI') # valid but not minimal
    assert 19 == parse_roman('XIX') # valid but not minimal
    assert 0 == parse_roman('IXX') # invalid



def format_roman(k):
    ' format integer n as a minimal Roman numeral '

    roman = ''
    i = 0
    while k > 0:
        (n, r) = DESC[i]
        d = k - n
        if d >= 0:
            roman += r
            k = d
        else:
            i += 1

    return roman




def test_format_roman():
    assert format_roman(3) == 'III'
    assert format_roman(4) == 'IV'
    assert format_roman(5) == 'V'
    assert format_roman(6) == 'VI'
    assert format_roman(7) == 'VII'
    assert format_roman(8) == 'VIII'
    assert format_roman(9) == 'IX'
    assert format_roman(453) == 'CDLIII'
    assert format_roman(3390) == 'MMMCCCXC'

    print 'format_roman() tested'
    

#test_format_roman()


def main():
    from sys import stdin

    num_digits_saved = 0
    for each in stdin:
        roman = each.strip()
        formatted = format_roman(parse_roman(roman))
        num_digits_saved += len(roman) - len(formatted)
    print num_digits_saved


main()
