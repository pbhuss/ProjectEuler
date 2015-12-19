SPIRAL_SIZE = 1001


def main():
    result = 1
    cur = 1
    offset = 2
    for spiral in xrange(SPIRAL_SIZE / 2):
        for i in xrange(4):
            cur += offset
            result += cur
            print cur
        offset += 2
    return result


if __name__ == '__main__':
    print main()
