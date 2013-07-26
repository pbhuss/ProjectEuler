'''
Created on Jul 25, 2013

@author: peter
'''

if __name__ == '__main__':

    total = sum([i for i in xrange(1000) if i % 3 == 0 or i % 5 == 0])

    print total
