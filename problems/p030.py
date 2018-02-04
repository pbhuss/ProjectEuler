def power_sum(val):
    return sum(map(lambda x: int(x) ** 5, str(val)))


def main():
    # TODO: prove this limit
    limit = 500000
    total = 0

    for i in range(10, limit):
        if i == power_sum(i):
            total += i

    return total


if __name__ == '__main__':
    print(main())
