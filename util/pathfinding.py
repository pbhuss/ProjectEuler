import functools


def triangle_path(agg, triangle):
    path = [[triangle[0][0]]]
    for i, row in enumerate(triangle[1:], start=1):
        path_row = []
        for j, node in enumerate(row):
            if j == 0:
                path_row.append(node + path[i-1][j])
            elif j == len(row) - 1:
                path_row.append(node + path[i-1][j-1])
            else:
                path_row.append(
                    node + agg(path[i-1][j-1], path[i-1][j]))
        path.append(path_row)
    return agg(*path[-1])


max_triangle_path = functools.partial(triangle_path, max)


min_triangle_path = functools.partial(triangle_path, min)
