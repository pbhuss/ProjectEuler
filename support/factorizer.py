'''
Created on Jul 25, 2013

@author: peter
'''

from math import ceil


class Factorizer(object):

    def __init__(self):
        self.primes = generate_primes(continue_to=10000)
        self.number = None

    def set(self, number):
        self.number = number
        self._factorize()

    def _factorize(self):
        sqrt = ceil(self.number ** 0.5)
        if sqrt > self.primes[-1]:
            self.primes = generate_primes(continue_to=sqrt, prev=self.primes)
        self._factors = {}

        cur = self.number
        index = 0
        while cur != 1:
            prime = self.primes[index]
            if cur % prime == 0:
                cur /= prime
                sqrt = cur ** 0.5
                self._factors[prime] = self._factors.get(prime, 0) + 1
            else:
                index += 1
                if index >= len(self.primes) or sqrt < self.primes[index]:
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
        for factor, count in self._factors.iteritems():
            new = set()
            for i in xrange(count + 1):
                for item in factors:
                    new.add(item * factor**i)
            factors |= new
        return factors

    @property
    def prime_factors(self):
        if self.number is None:
            raise Exception('must first set a number')
        return set(self._factors.keys())


def generate_primes(num=0, continue_to=0, prev=None):

    generated = 0

    if prev:
        cur_num = prev[-1] + 1
        primes = prev
    else:
        cur_num = 2
        primes = []

    while cur_num <= continue_to or generated < num:
        sqrt = cur_num ** 0.5
        is_prime = True
        for i in primes:
            if i > sqrt:
                break
            if cur_num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(cur_num)
            generated += 1

        cur_num += 1

    return primes

def least_common_demon(*integers):
    pfs = []
    f = Factorizer()
    for x in integers:
        f.set(x)
        pfs.append(f.prime_factorization)
    lcd_pf = dict()
    for pf in pfs:
        for factor, count in pf.iteritems():
            lcd_pf[factor] = max(count, lcd_pf.get(factor, 0))
    prod = 1
    for factor, count in lcd_pf.iteritems():
        prod *= (factor ** count)
    return prod
