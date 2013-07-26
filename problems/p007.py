'''
Created on Jul 26, 2013

@author: peter
'''

from support import factorizer

def main():
    print factorizer.generate_primes(num=10001)[10000]

if __name__ == '__main__':
    main()