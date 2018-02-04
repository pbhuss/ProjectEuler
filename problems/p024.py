from itertools import permutations


def main():
    perms = sorted(permutations(range(10)))
    for idx, perm in enumerate(perms, start=1):
        if idx == 1000000:
            return int(''.join(map(str, perm)))


if __name__ == '__main__':
    print(main())
