from math import factorial


def main():
    factorials = dict(
        (x, factorial(x))
        for x in xrange(101)
    )
    result = 0
    for n in xrange(1, 101):
        # Note: could use fact that (n choose r) == (n choose (n-r))
        # to cut number of iterations by half
        for r in xrange(1, n):
            if factorials[n] / (factorials[r] * factorials[n - r]) > 1000000:
                result += 1
    return result


if __name__ == '__main__':
    print main()
