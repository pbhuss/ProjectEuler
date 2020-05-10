from itertools import permutations

from util.factorizer import PrimeGenerator


def main():
    prime_generator = PrimeGenerator()

    digit_sets = (
        list(map(str, range(n, 0, -1)))
        for n in range(9, 0, -1)
    )

    # If sum of digits in number is 3, the number is divisible by 3
    # and thus not prime
    digit_sets = filter(
        lambda digit_set: sum(map(int, digit_set)) % 3 != 0,
        digit_sets
    )

    for digit_set in digit_sets:
        for perm in permutations(digit_set):
            x = int(''.join(perm))
            if x in prime_generator:
                # itertools.permutations yields in lexographic order
                # First prime is guaranteed to be the largest
                return x


if __name__ == '__main__':
    print(main())
