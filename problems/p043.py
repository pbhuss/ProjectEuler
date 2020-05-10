from itertools import permutations

from util.factorizer import PrimeGenerator


def main():
    result = 0
    prime_gen = PrimeGenerator()
    primes = prime_gen[:7]   # [2, 3, 5, 7, 11, 13, 17]
    for digits in permutations(range(10)):
        if digits[0] == 0:
            continue
        passed = True
        for idx, prime in enumerate(primes, start=1):
            num = int(f'{digits[idx]}{digits[idx + 1]}{digits[idx + 2]}')
            if num % prime != 0:
                passed = False
                break
        if passed:
            result += int(''.join(map(str, digits)))
    return result


if __name__ == '__main__':
    print(main())
