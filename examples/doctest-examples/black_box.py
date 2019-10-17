def piecewise(x):
    '''
    f(x) = -x - 3      if x <= -3
         | x + 3       if -3 < x < 0
         | -2x + 3     if 0 <= x < 3
         | 0.5x - 4.5  if x >= 3
    '''

if __name__ == '__main__':
    import doctest
    doctest.testmod()

