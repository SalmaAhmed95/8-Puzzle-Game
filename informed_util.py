def heuristic(matrix, distance_metric):
    n_rows = len(matrix)
    n_cols = len(matrix[0])
    h = 0
    for i, row in enumerate(matrix):
        for j, cur in enumerate(row):
            if cur != 0:
                goal_row = cur // n_rows # expected x-coordinate (row)
                goal_col = cur % n_cols # expected y-coordinate (col)
                h += distance_metric((i, j), (goal_row, goal_col))
    return h