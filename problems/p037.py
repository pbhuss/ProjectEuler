from support.factorizer import PrimeGenerator


def truncations(x):
    s = str(x)
    result = set()
    for i in range(len(s)):
        result.add(int(s[:i + 1]))
        result.add(int(s[i:]))
    return result


def main():
    truncatable_primes = []
    prime_gen = PrimeGenerator()
    while len(truncatable_primes) != 11:
        prime = prime_gen.next()
        if prime < 10:
            continue
        if all(
            t in prime_gen
            for t in truncations(prime)
        ):
            truncatable_primes.append(prime)
    return sum(truncatable_primes)


if __name__ == '__main__':
    print(main())
