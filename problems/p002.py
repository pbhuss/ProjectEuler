'''
Created on Jul 25, 2013

@author: peter
'''

def main():

    prev = 1
    cur = 2
    total = 0

    while (cur <= 4000000):
        if (cur % 2 == 0):
            total += cur
            print cur
        temp = cur
        cur += prev
        prev = temp

    print total

if __name__ == '__main__':
    main()
