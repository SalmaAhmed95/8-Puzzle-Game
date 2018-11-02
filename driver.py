import puzzle_solver
import visualizer
from scipy.spatial import distance
from informed_util import Heuristic

matrix  = [[1,2,5],[3,4,0],[6,7,8]]

path, cost, explored, search_depth = puzzle_solver.solve(matrix, 'a_star', prioritized=True, heuristic=Heuristic(distance.cityblock))
# path, cost, explored, search_depth = puzzle_solver.solve(matrix, 'bfs')
path_list = []

print("PATH:")
while not path.empty():
    path_matrix = path.get().matrix
    print(path_matrix)
    path_list.append(path_matrix)
print()

print("COST:")
print(cost)
print()

print("EXPLORED:")
print([state.matrix for state in explored])
print()

print("SEARCH DEPTH:")
print(search_depth)
print()

puzzle_visualizer = visualizer.Visualizer(path_list, 140, -200, 240, 'black')
puzzle_visualizer.play()