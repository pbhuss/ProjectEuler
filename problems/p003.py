'''
Created on Jul 25, 2013

@author: peter
'''

from support import factorizer

def main():

    f = factorizer.Factorizer()
    f.set(600851475143)

    print max(f.prime_factors)

if __name__ == '__main__':
    main()
