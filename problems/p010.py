from support import factorizer


def main():
    return sum(factorizer.generate_primes(continue_to=1999999))


if __name__ == '__main__':
    print main()
