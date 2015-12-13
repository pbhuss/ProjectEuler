def main():
    n = 2**1000
    sum = 0
    for c in str(n):
        sum += int(c)
    return sum


if __name__ == '__main__':
    print main()
