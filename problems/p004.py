'''
Created on Jul 25, 2013

@author: peter
'''

from support import palindromes

def main():
    best = -1
    for i in xrange(100, 1000):
        for j in xrange(100, i + 1):
            prod = i * j
            if prod > best and palindromes.is_integer_palindrome(prod):
                best = prod

    print best

if __name__ == '__main__':
    main()
