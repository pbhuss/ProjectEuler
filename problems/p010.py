'''
Created on Jul 26, 2013

@author: peter
'''

from support import factorizer

def main():
    print sum(factorizer.generate_primes(continue_to=1999999))

if __name__ == '__main__':
    main()
