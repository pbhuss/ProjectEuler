from support.factorizer import PrimeGenerator


def main():
    prime_gen = PrimeGenerator()
    best_n = -1
    best_a = None
    best_b = None
    for a in xrange(-999, 1000):
        for b in xrange(-999, 1000):
            n = 0
            while True:
                term = n**2 + a * n + b
                if term not in prime_gen:
                    if n > best_n:
                        best_a, best_b, best_n = a, b, n
                    break
                n += 1
    return best_a * best_b


if __name__ == '__main__':
    print main()
