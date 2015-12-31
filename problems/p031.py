def make_change(remaining, coins, pos=0):
    coin = coins[pos]
    if pos == len(coins) - 1:
        if remaining % coin == 0:
            return 1
        return 0
    num_ways = 0
    for i in xrange(remaining / coin + 1):
        num_ways += make_change(remaining - i * coin, coins, pos + 1)
    return num_ways


def main():
    coins = sorted([1, 2, 5, 10, 20, 50, 100, 200], reverse=True)
    return make_change(200, coins)


if __name__ == '__main__':
    print main()
