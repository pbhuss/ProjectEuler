from support import factorizer
from support.factorizer import PrimeGenerator


def main():
    prime_gen = PrimeGenerator()
    return prime_gen[10000]


if __name__ == '__main__':
    print main()
