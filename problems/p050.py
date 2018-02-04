from support.factorizer import PrimeGenerator


def main():
    prime_gen = PrimeGenerator()
    best_prime = None
    best_n = 1
    i = 0
    while prime_gen[i] < 1000000 / best_n:
        sum = 0
        j = 0
        while sum < 1000000:
            sum += prime_gen[i + j]
            j += 1
            if sum in prime_gen:
                if j - i > best_n:
                    best_n = j - i
                    best_prime = sum
        i += 1
    return best_prime


if __name__ == '__main__':
    print(main())
