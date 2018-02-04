from support.factorizer import Factorizer


def triangle_numbers():
    cur = 0
    i = 0
    while True:
        i += 1
        cur += i
        yield cur


def main():
    factorizer = Factorizer()
    for triangle_number in triangle_numbers():
        factorizer.set(triangle_number)
        if len(factorizer.factors) > 500:
            return triangle_number


if __name__ == '__main__':
    print(main())
