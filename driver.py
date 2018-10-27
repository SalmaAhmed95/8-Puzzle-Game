from state import State
import puzzle_solver
import visualizer
from queue import LifoQueue, Queue, PriorityQueue
from heap_util import decrease_key
from scipy.spatial import distance
from informed_util import Heuristic
import copy

matrix  = [[1,4,2],[6,5,8],[7,3,0]]

path, search_depth = puzzle_solver.solve(matrix, 'a_star', prioritized=True, heuristic=Heuristic(distance.cityblock))
#path, search_depth = puzzle_solver.solve(matrix, 'dfs')
print ('search_depth = ', search_depth)
path_list = []
while not path.empty():
    path_matrix = path.get().matrix
    print(path_matrix)
    path_list.append(path_matrix)

puzzle_visualizer = visualizer.Visualizer(path_list, 140, -200, 240, 'black')
puzzle_visualizer.play()