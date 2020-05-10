from util.factorizer import Factorizer


def main():
    factorizer = Factorizer()
    i = 1
    while True:
        passed = True
        for j in range(4):
            factorizer.set(i + j)
            if len(factorizer.prime_factors) != 4:
                passed = False
                i = i + j + 1
                break
        if passed:
            return i


if __name__ == '__main__':
    print(main())
