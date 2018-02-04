def triangle_gen():
    n = 1
    while True:
        yield n * (n + 1) // 2
        n += 1

def pentagonal_gen():
    n = 1
    while True:
        yield n * (3 * n - 1) // 2
        n += 1

def hexagonal_gen():
    n = 1
    while True:
        yield n * (2 * n - 1)
        n += 1

def main():
    generators = [triangle_gen(), pentagonal_gen(), hexagonal_gen()]
    vals = [next(g) for g in generators]

    for idx, generator in enumerate(generators):
        while vals[idx] <= 40755:
            vals[idx] = next(generator)

    while vals[0] != vals[1] or vals[1] != vals[2]:
        if vals[0] < vals[1] or vals[0] < vals[2]:
            vals[0] = next(generators[0])
        if vals[1] < vals[0] or vals[1] < vals[2]:
            vals[1] = next(generators[1])
        if vals[2] < vals[0] or vals[2] < vals[1]:
            vals[2] = next(generators[2])

    return vals[0]


if __name__ == '__main__':
    print(main())
