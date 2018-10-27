from queue import Queue, LifoQueue, PriorityQueue
from state import State

"""
TODO: ONE SOLVE METHOD WITH A HELPER FACTORY METHOD
      GENERATING THE APPROPERIATE DATA STRUCTURE
"""

def solve_by_bfs(matrix):
    queue = Queue()
    frontier_set = set() # for later search
    start_state = State(matrix)
    if start_state.is_solvable():
        queue.put(start_state)
        frontier_set.add(start_state)
        return graph_search(queue, frontier_set)
    

def solve_by_dfs(matrix):
    stack = LifoQueue()
    frontier_set = set() # for later search
    start_state = State(matrix)
    if start_state.is_solvable():
        stack.put(start_state)
        frontier_set.add(start_state)
        return graph_search(stack, frontier_set)


def solve_by_a_star(matrix):
    priority_queue = PriorityQueue()
    frontier_set = set() # for later search
    start_state = State(matrix)
    if start_state.is_solvable():
        priority_queue.put(start_state)
        frontier_set.add(start_state)
        return graph_search(priority_queue)


def graph_search(frontier_list, frontier_set):
    explored = set()
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


def get_path(current_state):
    path = LifoQueue()
    path.put(current_state)
    while current_state.parent is not None:
        path.put(current_state.parent)
        current_state = current_state.parent
    return path







