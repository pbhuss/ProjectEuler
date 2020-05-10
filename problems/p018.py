from util.pathfinding import max_triangle_path


def main():
    with open('data/p018.txt', 'r') as fp:
        triangle = [
            [int(n) for n in line.strip().split(' ')]
            for line in fp
        ]
    return max_triangle_path(triangle)


if __name__ == '__main__':
    print(main())
