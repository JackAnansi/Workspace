NUMERALS = '0123456789abcdef'

def arb(n, base=10):
    """Converts an integer to a string for an arbitrary base (default base 10).

    >>> arb(255, base=2)
    '11111111'
    >>> arb(255, base=16)
    'ff'
    """
    assert base <= 16, "Cannot handle base greater than base 16"

    d, m = divmod(n, base)
    digits = [m]
    while d:
        d, m = divmod(d, base)
        digits.append(m)

    return ''.join(NUMERALS[c] for c in reversed(digits))

if __name__=="__main__":
    print( arb( 3, 3) )
