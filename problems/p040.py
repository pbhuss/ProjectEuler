def main():
    result = 1
    for i in range(7):
        result *= find_at(10 ** i)
    return result


def find_at(pos):
    exp = 1
    digits = 0
    while True:
        r = range(10 ** (exp - 1), 10 ** exp)
        new_digits = exp * len(r)
        if digits + new_digits < pos:
            digits += new_digits
            exp += 1
        else:
            remaining = pos - digits
            r_idx = (remaining - 1) // exp
            sub_pos = (remaining - 1) % exp
            return int(str(r[r_idx])[sub_pos])


if __name__ == '__main__':
    print(main())
