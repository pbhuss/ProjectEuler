from functools import reduce

import numpy as np

from operator import mul


def main():
    with open('data/p008.txt', 'r') as fp:
        num_str = fp.readline().strip()
    num_arr = np.array([int(i) for i in num_str])
    best = None
    for i in range(0, len(num_arr) - 13 + 1):
        cur = reduce(mul, num_arr[i:i+13])
        if best is None:
            best = cur
        best = np.max([best, cur])
    return best


if __name__ == '__main__':
    print(main())
