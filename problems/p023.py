from support.factorizer import Factorizer


def is_abundant(n, factorizer):
    factorizer.set(n)
    return sum(factorizer.factors) - n > n


def abundant_generator(continue_to=None):
    i = 2
    factorizer = Factorizer()
    while continue_to is None or i < continue_to:
        if is_abundant(i, factorizer):
            yield i
        i += 1


STOP_AT = 28124


def main():
    abundant_numbers = list(abundant_generator(STOP_AT))
    abundant_sums = set()
    for pos, i in enumerate(abundant_numbers):
        for j in abundant_numbers[pos:]:
            abundant_sum = i + j
            if abundant_sum >= STOP_AT:
                break
            abundant_sums.add(abundant_sum)

    return sum(set(xrange(1, STOP_AT)) - abundant_sums)


if __name__ == '__main__':
    print main()
