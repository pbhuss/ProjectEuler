from scipy.misc import comb


def main():
    n = 20
    return comb(2 * n, n, exact=True)


if __name__ == '__main__':
    print(main())
