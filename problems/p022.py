def char_val(char):
    return ord(char) - ord('A') + 1


def main():
    with open('data/p022.txt', 'r') as fp:
        names = fp.readline().split(',')
    names = map(lambda name: name.replace('"', ''), names)

    total = 0
    for idx, name in enumerate(sorted(names), start=1):
        total += idx * sum(map(char_val, name))

    return total


if __name__ == '__main__':
    print(main())
