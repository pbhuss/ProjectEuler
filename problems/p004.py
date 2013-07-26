'''
Created on Jul 25, 2013

@author: peter
'''

from support import palindromes

if __name__ == '__main__':
    best = -1
    for i in xrange(100, 1000):
        for j in xrange(100, i + 1):
            prod = i * j
            if prod > best and palindromes.is_integer_palindrome(prod):
                best = prod

    print best
