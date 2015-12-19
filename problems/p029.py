def main():
    powers = set()
    for a in xrange(2, 101):
        for b in xrange(2, 101):
            powers.add(a**b)
    return len(powers)


if __name__ == '__main__':
    print main()
