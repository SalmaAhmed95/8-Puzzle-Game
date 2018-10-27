class Heuristic:
    def __init__(self, heuristic_fn):
        self.heuristic_fn = heuristic_fn
        
    def evaluate(self, matrix):
        n_rows = len(matrix)
        n_cols = len(matrix[0])
        h = 0
        for i, row in enumerate(matrix):
            for j, cur in enumerate(row):
                if cur != 0:
                    goal_row = cur // n_rows # expected x-coordinate (row)
                    goal_col = cur % n_cols # expected y-coordinate (col)
                    h += self.heuristic_fn((i, j), (goal_row, goal_col))
        return h