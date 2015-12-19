def fibonacci_generator():
    a = 1
    b = 0

    while True:
        yield a
        b += a
        yield b
        a += b


def main():
    for i, n in enumerate(fibonacci_generator(), start=1):
        if len(str(n)) == 1000:
            return i


if __name__ == '__main__':
    print main()
