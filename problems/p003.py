'''
Created on Jul 25, 2013

@author: peter
'''

from support import factorizer

if __name__ == '__main__':

    f = factorizer.Factorizer()
    f.set(600851475143)

    print max(f.get_prime_factors())
