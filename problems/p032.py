from itertools import permutations


def list_to_num(x):
    total = 0
    base = 1
    for digit in x[::-1]:
        total += base * digit
        base *= 10
    return total


def main():
    products = set()
    for perm in permutations(range(1, 10)):
        for split1 in range(1, 7):
            for split2 in range(split1 + 1, 8):
                i = list_to_num(perm[:split1])
                j = list_to_num(perm[split1: split2])
                k = list_to_num(perm[split2:])
                if i * j == k:
                    products.add(k)

    return sum(products)


if __name__ == '__main__':
    print(main())
