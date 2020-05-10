from util.palindromes import is_palindrome


def main():
    total = 0
    for i in range(1000000):
        if is_palindrome(str(i)) and is_palindrome(bin(i)[2:]):
            total += i
    return total


if __name__ == '__main__':
    print(main())
