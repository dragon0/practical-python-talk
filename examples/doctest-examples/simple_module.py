
def factorial(n):
    '''
    >>> factorial(5)
    120
    '''

    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()

