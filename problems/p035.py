from support.factorizer import PrimeGenerator


def rotations(x):
    s = str(x)
    l = len(s)
    return set([
        int(s[l - i:] + s[:l - i])
        for i in xrange(l)
    ])


def main():
    evens = set(map(str, xrange(0, 10, 2)))
    circular = 1
    passed = set()
    failed = set()
    # 2, the first prime, is a special case
    prime_gen = PrimeGenerator(start_at=1)
    for prime in prime_gen:
        if prime >= 1000000:
            return circular
        if prime in failed or not set(str(prime)).isdisjoint(evens):
            continue
        if prime in passed:
            circular += 1
            continue
        rs = rotations(prime)
        if all(
            r in prime_gen
            for r in rs
        ):
            circular += 1
            passed.update(rs)
        else:
            failed.update(rs)
    return circular


if __name__ == '__main__':
    print main()
