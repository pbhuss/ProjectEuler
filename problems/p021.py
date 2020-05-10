from util.factorizer import Factorizer


def is_amicable(n, factorizer):
    factorizer.set(n)
    proper_divisor_sum = sum(factorizer.factors) - n
    if proper_divisor_sum == n:
        return False
    factorizer.set(proper_divisor_sum)
    return sum(factorizer.factors) - proper_divisor_sum == n


def main():
    result = 0
    factorizer = Factorizer()
    for i in range(2, 10000):
        if is_amicable(i, factorizer):
            result += i
    return result


if __name__ == '__main__':
    print(main())
