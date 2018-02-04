def collatz_sequence_len(start, cache):
    cur = start
    seq = []
    while cur not in cache:
        seq.append(cur)
        if cur % 2 == 0:
            cur /= 2
        else:
            cur = 3 * cur + 1
    full_length = len(seq) + cache[cur]
    for offset, i in enumerate(seq):
        cache[i] = full_length - offset
    return full_length


def main():
    max_len = 0
    max_i = 0
    cache = {1: 1}
    for i in range(1, 1000000):
        cur_len = collatz_sequence_len(i, cache)
        if cur_len > max_len:
            max_len = cur_len
            max_i = i
    return max_i


if __name__ == '__main__':
    print(main())
