from support.factorizer import generate_primes


def rotations(x):
    s = str(x)
    l = len(s)
    return set([
        int(s[l - i:] + s[:l - i])
        for i in xrange(l)
    ])


def main():
    evens = set(map(str, xrange(0, 10, 2)))
    primes = generate_primes(continue_to=1000000)
    circular = 1
    passed = set()
    failed = set()
    for prime in primes[1:]:  # 2, the first prime, is a special case
        if prime in failed or not set(str(prime)).isdisjoint(evens):
            continue
        if prime in passed:
            circular += 1
            continue
        r = rotations(prime)
        if r.issubset(primes):
            circular += 1
            passed.update(r)
        else:
            failed.update(r)
    return circular


if __name__ == '__main__':
    print main()
