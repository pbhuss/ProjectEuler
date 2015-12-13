from support import factorizer


def main():
    return factorizer.generate_primes(num=10001)[10000]


if __name__ == '__main__':
    print main()
