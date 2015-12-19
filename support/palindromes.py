def is_integer_palindrome(number):
    string = str(number)
    for i in xrange((len(string) - 1) / 2 + 1):
        if string[i] != string[len(string) - i - 1]:
            return False
    return True
