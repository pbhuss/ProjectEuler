def main():
    for c in range(1000):
        for b in range(c):
            a = 1000 - c - b
            if (a ** 2 + b ** 2 == c ** 2):
                return a * b * c


if __name__ == '__main__':
    print(main())
