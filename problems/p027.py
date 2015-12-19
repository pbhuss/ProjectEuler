from support.factorizer import generate_primes


def main():
    primes = generate_primes(100)
    primes_set = set(primes)
    best_n = -1
    best_a = None
    best_b = None
    for a in xrange(-999, 1000):
        for b in xrange(-999, 1000):
            n = 0
            while True:
                term = n**2 + a * n + b
                if term > primes[-1]:
                    generate_primes(
                        continue_to=2*term,
                        prev=primes)
                    primes_set = set(primes)
                if term not in primes_set:
                    if n > best_n:
                        best_a, best_b, best_n = a, b, n
                    break
                n += 1
    return best_a * best_b


if __name__ == '__main__':
    print main()
