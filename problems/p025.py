from util.generators import fibonacci_generator


def main():
    for i, n in enumerate(fibonacci_generator(), start=1):
        if len(str(n)) == 1000:
            return i


if __name__ == '__main__':
    print(main())
