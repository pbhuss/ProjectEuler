from support import factorizer


def main():

    f = factorizer.Factorizer()
    f.set(600851475143)

    return max(f.prime_factors)


if __name__ == '__main__':
    print(main())
