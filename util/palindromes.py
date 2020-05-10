def is_palindrome(string):
    for i in range((len(string) - 1) // 2 + 1):
        if string[i] != string[len(string) - i - 1]:
            return False
    return True
