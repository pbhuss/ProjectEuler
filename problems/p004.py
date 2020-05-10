from util import palindromes


def main():
    best = -1
    for i in range(100, 1000):
        for j in range(100, i + 1):
            prod = i * j
            if prod > best and palindromes.is_palindrome(str(prod)):
                best = prod

    return best


if __name__ == '__main__':
    print(main())
