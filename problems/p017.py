NUM_LENGTH = {
    1: {
        0: '',  # special case
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
    },
    2: {
        2: 'twenty',
        3: 'thirty',
        4: 'forty',
        5: 'fifty',
        6: 'sixty',
        7: 'seventy',
        8: 'eighty',
        9: 'ninety',
    },
    3: 'hundred',
    4: 'thousand',
}


def main():
    result = 0
    for i in range(1, 1001):
        num_str = ''
        thousands = (i % 10000) // 1000
        hundreds = (i % 1000) // 100
        tens = (i % 100) // 10
        ones = i % 10
        if thousands > 0:
            num_str += NUM_LENGTH[1][thousands]
            num_str += NUM_LENGTH[4]
        if hundreds > 0:
            num_str += NUM_LENGTH[1][hundreds]
            num_str += NUM_LENGTH[3]
        if (hundreds > 0 or thousands > 0) and (tens > 0 or ones > 0):

            num_str += 'and'
        if tens >= 2:
            num_str += NUM_LENGTH[2][tens]
            num_str += NUM_LENGTH[1][ones]
        else:
            num_str += NUM_LENGTH[1][i % 100]
        result += len(num_str)

    return result


if __name__ == '__main__':
    print(main())
