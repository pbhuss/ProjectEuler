from support.factorizer import PrimeGenerator


def main():
    prime_gen = PrimeGenerator()
    result = 0
    for prime in prime_gen:
        if prime >= 2000000:
            break
        result += prime
    return result


if __name__ == '__main__':
    print(main())
