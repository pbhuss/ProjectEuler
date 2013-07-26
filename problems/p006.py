'''
Created on Jul 26, 2013

@author: peter
'''

def main():
    n = 100
    print square_of_sum(n) - sum_of_squares(n)

def sum_of_squares(n):
    return n * (n + 1) * (2 * n + 1) / 6

def square_of_sum(n):
    return (n * (n + 1) / 2) ** 2

if __name__ == '__main__':
    main()
