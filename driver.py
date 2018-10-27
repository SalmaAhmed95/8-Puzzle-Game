from state import State
import puzzle_solver
import visualizer
from queue import LifoQueue, Queue, PriorityQueue
from heap_util import decrease_key
from scipy.spatial import distance
from informed_util import Heuristic
import copy

matrix  = [[1,2,5],[3,4,0],[6,7,8]]

# t = tuple(matrix)
# print(type(t))
# matrix2  = [[5,2,8],[4,1,7],[0,3,6]]
# testState = State(matrix2)
# print(testState.is_solvable())

path = puzzle_solver.solve_by_a_star(matrix, Heuristic(distance.cityblock))
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


#start = State(matrix, cost=8)
#end = State(matrix, cost=2)
#print(start)
#print(end)
#s = set()
#pq = PriorityQueue()
#s.add(start)
#pq.put(start)
#if end in s:
#    print('yes')
#else:
#    print('no')
#    
#print(pq.queue.index(end))
#print(pq.queue[pq.queue.index(end)].cost)
#print(end)


#matrix1 = [[1,2,6],[3,4,0],[5,7,8]]
#matrix2 = [[1,2,5],[3,4,0],[6,7,8]]
#state1 = State(matrix1, cost=5)
#state2 = State(matrix2, cost=1)
#state3 = State(matrix1, cost=3)
#pq = PriorityQueue()
#pq.put(state1)
#pq.put(state2)
#for i in range (len(pq.queue)):
#    print(i)
#    print(pq.queue[i])
#    print(pq.queue[i].cost)
#    print('-----------')
##print(pq.queue)
#print('================')
##state2.cost = 7
##decrease_key(pq.queue, 0, pq.queue.index(state2))
#decrease_key(pq.queue, 0, pq.queue.index(state3), state3)
#for i in range (len(pq.queue)):
#    print(i)
#    print(pq.queue[i])
#    print(pq.queue[i].cost)