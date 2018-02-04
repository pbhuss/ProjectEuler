from math import factorial


def factorial_sum(val):
    return sum(
        factorial(int(x))
        for x in str(val)
    )


def main():
    total = 0

    # TODO: prove this limit
    for i in range(10, 100000):
        if factorial_sum(i) == i:
            total += i
    return total


if __name__ == '__main__':
    print(main())
