from math import ceil

from util.generators import MemoizedGenerator


class Factorizer(object):

    def __init__(self):
        self._prime_gen = PrimeGenerator()
        self.number = None

    def set(self, number):
        self.number = number
        self._factorize()

    def _factorize(self):
        sqrt = int(ceil(self.number ** 0.5))
        self._factors = {}

        cur = self.number
        index = 0
        while cur != 1:
            prime = self._prime_gen[index]
            if cur % prime == 0:
                cur /= prime
                sqrt = cur ** 0.5
                self._factors[prime] = self._factors.get(prime, 0) + 1
            else:
                index += 1
                if sqrt < self._prime_gen[index]:
                    self._factors[cur] = self._factors.get(cur, 0) + 1
                    break

    @property
    def prime_factorization(self):
        if self.number is None:
            raise Exception('must first set a number')
        return self._factors

    @property
    def factors(self):
        if self.number is None:
            raise Exception('must first set a number')
        factors = {1}
        for factor, count in self._factors.items():
            new = set()
            for i in range(count + 1):
                for item in factors:
                    new.add(item * factor**i)
            factors |= new
        return factors

    @property
    def prime_factors(self):
        if self.number is None:
            raise Exception('must first set a number')
        return set(self._factors.keys())


class PrimeGenerator(MemoizedGenerator):

    def __init__(self, start_at=0, contains_fn='_contains_v2'):
        super().__init__(self._prime_generator(), start_at=start_at)
        self._primes = self._mem
        self._prime_set = set()
        self._contains_fn = getattr(self, contains_fn)

    def __contains__(self, n):
        return self._contains_fn(n)

    def _contains_v1(self, n):
        while not self._primes or self._primes[-1] < n:
            self._generate_next()
        return n in self._prime_set

    def _contains_v2(self, n):
        if n in self._prime_set:
            return True
        if self._primes and self._primes[-1] > n:
            return False
        while not self._primes or self._primes[-1] ** 2 < n:
            self._generate_next()
        for prime in self._primes:
            if n == prime:
                return True
            if n % prime == 0:
                return False
            if n < prime ** 2:
                return True
        return True

    def _prime_generator(self):
        cur_num = 2
        while True:
            sqrt = cur_num ** 0.5
            is_prime = True
            for i in self._primes:
                if i > sqrt:
                    break
                if cur_num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                self._prime_set.add(cur_num)
                yield cur_num
            cur_num += 1

    def is_prime(self, n):
        return n in self

    def is_composite(self, n):
        if n < 2:
            return False
        return n not in self


def least_common_demon(*integers):
    pfs = []
    f = Factorizer()
    for x in integers:
        f.set(x)
        pfs.append(f.prime_factorization)
    lcd_pf = dict()
    for pf in pfs:
        for factor, count in pf.items():
            lcd_pf[factor] = max(count, lcd_pf.get(factor, 0))
    prod = 1
    for factor, count in lcd_pf.items():
        prod *= (factor ** count)
    return prod
