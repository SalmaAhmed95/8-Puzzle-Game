from state import State
import puzzle_solver
import visualizer
from queue import LifoQueue, Queue
import copy

matrix  = [[1,2,5],[3,4,0],[6,7,8]]

# t = tuple(matrix)
# print(type(t))
# matrix2  = [[5,2,8],[4,1,7],[0,3,6]]
# testState = State(matrix2)
# print(testState.is_solvable())

path = puzzle_solver.solve_by_bfs(matrix)
path_list = []
while not path.empty():
    path_matrix = path.get().matrix
    print(path_matrix)
    path_list.append(path_matrix)

puzzle_visualizer = visualizer.Visualizer(path_list, 140, -200, 240, 'black')
puzzle_visualizer.play()




# test2 = State(matrix2)
# print(test2.is_goal_state())
# matrix2 = copy.deepcopy(matrix)
# test2 = State(matrix2)
# print(testState.emptyCellIndex)
#
# nextStates = testState.generate_moves()
# nextStates2 = test2.generate_moves()

# print(nextStates[0] == nextStates2[0])
# for state in nextStates:
#     print(state.matrix)
