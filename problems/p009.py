def main():
    for c in xrange(1000):
        for b in xrange(c):
            a = 1000 - c - b
            if (a ** 2 + b ** 2 == c ** 2):
                return a * b * c


if __name__ == '__main__':
    print main()
