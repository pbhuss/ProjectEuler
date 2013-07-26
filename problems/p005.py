'''
Created on Jul 25, 2013

@author: peter
'''

from support import factorizer

def main():
    num_set = set(i for i in xrange(2, 21))
    print factorizer.least_common_demon(num_set)

if __name__ == '__main__':
    main()