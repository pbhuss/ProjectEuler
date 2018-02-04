from math import ceil


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


class PrimeGenerator():

    def __init__(self, prev=None, start_at=0):
        self.reset(start_at)
        if prev:
            self._cur_num = prev[-1] + 1
            self._primes = prev
            self._prime_set = set(prev)
        else:
            self._cur_num = 2
            self._primes = []
            self._prime_set = set()

    def __iter__(self):
        return self

    def __contains__(self, n):
        while not self._primes or self._primes[-1] < n:
            self._generate_next()
        return n in self._prime_set

    def __getitem__(self, item):
        while len(self._primes) <= item:
            self._generate_next()
        return self._primes[item]

    def __next__(self):
        self._yield_pos += 1
        return self[self._yield_pos]

    def next(self):
        return self.__next__()

    def reset(self, start_at):
        self._yield_pos = start_at - 1

    def _generate_next(self):
        while True:
            sqrt = self._cur_num ** 0.5
            is_prime = True
            for i in self._primes:
                if i > sqrt:
                    break
                if self._cur_num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                self._primes.append(self._cur_num)
                self._prime_set.add(self._cur_num)
                self._cur_num += 1
                return
            self._cur_num += 1

    def is_prime(self, n):
        return n in self

    def is_composite(self, n):
        if n < 2:
            return False
        return not n in self


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
