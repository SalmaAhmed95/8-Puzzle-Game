import copy
import sys


class State:
    def __init__(self, matrix, parent=None, cost=0, empty_cell_index=None, heuristic=None):
        self.matrix = matrix
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic
        
        if heuristic is None:
            self.heuristic_cost = 0
        else:
            self.heuristic_cost = heuristic.evaluate(self.matrix)
            
        if empty_cell_index is None:
            self.emptyCellIndex = self.locate_empty_cell()
        else:
            self.emptyCellIndex = empty_cell_index

    def __eq__(self, other):
        return self.matrix == other.matrix

    def __lt__(self, other):
        try:
            return (self.cost + self.heuristic_cost) < (other.cost + other.heuristic_cost)
        except:
            print("Error when executing __lt__:", sys.exc_info()[0])
    
    def __hash__(self):
        return hash(tuple(tuple(x) for x in self.matrix))

    def locate_empty_cell(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == 0:
                    return [i,j]

    def generate_moves(self):
        next_states = []
        i = self.emptyCellIndex[0]
        j = self.emptyCellIndex[1]
        if i != len(self.matrix) - 1:
            down_matrix = copy.deepcopy(self.matrix)
            down_matrix[i + 1][j], down_matrix[i][j] = down_matrix[i][j], down_matrix[i + 1][j]
            next_states.append(State(down_matrix, parent=self, cost=self.cost + 1,
                                     empty_cell_index=[i + 1, j], heuristic=self.heuristic))
        if j != len(self.matrix[0]) - 1:
            left_matrix = copy.deepcopy(self.matrix)
            left_matrix[i][j + 1], left_matrix[i][j] = left_matrix[i][j], left_matrix[i][j + 1]
            next_states.append(State(left_matrix, parent=self, cost=self.cost + 1,
                                     empty_cell_index=[i, j + 1], heuristic=self.heuristic))
        if j != 0:
            right_matrix = copy.deepcopy(self.matrix)
            right_matrix[i][j - 1], right_matrix[i][j] = right_matrix[i][j], right_matrix[i][j - 1]
            next_states.append(State(right_matrix, parent=self, cost=self.cost + 1,
                                     empty_cell_index=[i, j - 1], heuristic=self.heuristic))
        if i != 0:
            up_matrix = copy.deepcopy(self.matrix)
            up_matrix[i - 1][j], up_matrix[i][j] = up_matrix[i][j], up_matrix[i - 1][j]
            next_states.append(State(up_matrix, parent=self, cost=self.cost + 1,
                                     empty_cell_index=[i - 1, j], heuristic=self.heuristic))

        return next_states

    def is_goal_state(self):
        counter = 0
        for row in self.matrix:
            for elem in row:
                if elem == counter:
                    counter += 1
                else:
                    return False
        return True

    def is_solvable(self):
        count = 0
        for i in range (len(self.matrix) * len(self.matrix)):
            i_i = i // len(self.matrix)
            i_j = i % len(self.matrix)
            for j in range(i+1, len(self.matrix) * len(self.matrix)):
                j_i = j // len(self.matrix)
                j_j = j % len(self.matrix)
                if self.matrix[i_i][i_j] > self.matrix[j_i][j_j] and self.matrix[j_i][j_j]:
                    count += 1
        return count%2 == 0

