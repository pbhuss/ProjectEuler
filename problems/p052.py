def main():
    i = 1
    while True:
        chars = set(str(i))
        passes = True
        for x in xrange(2, 7):
            if set(str(i * x)) != chars:
                passes = False
                break
        if passes:
            return i
        i += 1


if __name__ == '__main__':
    print main()
