'''
Created on Jul 25, 2013

@author: peter
'''

from math import ceil


class Factorizer(object):

    def __init__(self):
        self.primes = generate_primes(continue_to=10000)

    def set(self, number):
        self.number = number
        self._factorize()

    def _factorize(self):
        sqrt = ceil(self.number ** 0.5)
        if sqrt > self.primes[len(self.primes) - 1]:
            self.primes = generate_primes(continue_to=sqrt, prev=self.primes)
        self.factors = {1: 1}

        cur = self.number
        index = 0
        while cur != 1:
            prime = self.primes[index]
            if cur % prime == 0:
                cur /= prime
                sqrt = cur ** 0.5
                self.factors[prime] = self.factors.get(prime, 0) + 1
            else:
                index += 1
                if index >= len(self.primes) or sqrt < self.primes[index]:
                    self.factors[cur] = self.factors.get(cur, 0) + 1
                    break

    def get_prime_factorization(self):
        return self.factors

    def get_factors(self):
        factor_counts = [(factor, count + 1) for (factor, count) in self.factors.iteritems()]
        prod = 1
        for _, count in factor_counts:
            prod *= count
        factors = set()
        for i in xrange(1, prod):
            cur = 1
            for factor, count in factor_counts:
                cur *= (factor ** (i % count))
            factors.add(cur)
        return factors

    def get_prime_factors(self):
        return set(self.factors.keys())


def generate_primes(num=0, continue_to=0, prev=None):

    generated = 0

    if prev:
        cur_num = prev[len(prev) - 1] + 1
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

def least_common_demon(num_set):
    pfs = []
    f = Factorizer()
    for x in num_set:
        f.set(x)
        pfs.append(f.get_prime_factorization())
    lcd_pf = dict()
    for pf in pfs:
        for factor, count in pf.iteritems():
            lcd_pf[factor] = max(count, lcd_pf.get(factor, 0))
    prod = 1
    for factor, count in lcd_pf.iteritems():
        prod *= (factor ** count)
    return prod
