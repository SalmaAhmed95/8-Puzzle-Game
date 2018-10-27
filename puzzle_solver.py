from queue import Queue, LifoQueue, PriorityQueue
from heap_util import decrease_key
from state import State


def solve(matrix, algorithm, prioritized=False, heuristic=None):
    frontier_list = frontier(algorithm)
    frontier_set = set() # for later search
    explored = set()
    start_state = State(matrix, heuristic=heuristic)
    if start_state.is_solvable():
        frontier_list.put(start_state)
        frontier_set.add(start_state)
        while not frontier_list.empty():
            current_state = frontier_list.get()
            frontier_set.remove(current_state)
            explored.add(current_state)
            if current_state.is_goal_state():
                return get_path(current_state)
            next_states = current_state.generate_moves()
            for state in next_states:
                if state not in explored and state not in frontier_set:
                    frontier_list.put(state)
                    frontier_set.add(state)
                elif prioritized:
                    if state in frontier_set:
                        if decrease_key(frontier_list.queue, 0, frontier_list.queue.index(state), state):
                            frontier_set.remove(state)
                            frontier_set.add(state)
    else:
        return LifoQueue()

'''
CLEAN
'''
def frontier(algorithm):
    if algorithm == 'bfs':
        return Queue()
    elif algorithm == 'dfs':
        return LifoQueue()
    elif algorithm == 'a_star':
        return PriorityQueue()


def get_path(current_state):
    path = LifoQueue()
    path.put(current_state)
    while current_state.parent is not None:
        path.put(current_state.parent)
        current_state = current_state.parent
    return path







