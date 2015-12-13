from support import factorizer


def main():
    num_set = set(i for i in xrange(2, 21))
    return factorizer.least_common_demon(*num_set)


if __name__ == '__main__':
    print main()
