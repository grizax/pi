import math


def factorial(n):

    ''' Computes the factorial of n '''

    if n == 0:
        return 1
    else:
        recurse = factorial(n - 1)
        result = n * recurse
        return result


def pi():

    '''
    Computes an estimation of pi with the Srinivasa Ramanujan algorithm.
    https://en.wikipedia.org/wiki/Pi#Rapidly_convergent_series
    '''

    total = 0
    k = 0
    first = 2 * math.sqrt(2) / 9801
    while True:
        num = factorial(4 * k) * (1103 + 26390 * k)
        den = factorial(k)**4 * 396**(4 * k)
        term = first * num / den
        total += term

        if abs(term) < 1e-15:
            break
        k += 1

    return 1 / total

print(pi())
