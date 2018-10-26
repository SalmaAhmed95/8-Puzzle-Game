from queue import LifoQueue, Queue
from state import State


def solve_by_dfs(matrix):
    stack = LifoQueue()
    start_state = State(matrix)
    if start_state.is_solvable():
        stack.put(start_state)
        return graph_search(stack)


def solve_by_bfs(matrix):
    queue = Queue()
    start_state = State(matrix)
    if start_state.is_solvable():
        queue.put(start_state)
        return graph_search(queue)


def graph_search(frontier_list):
    explored = set()
    while not frontier_list.empty():
        current_state = frontier_list.get()
        if current_state.is_goal_state():
            return get_path(current_state)
        next_states = current_state.generate_moves()
        for state in next_states:
            if state not in explored:
                frontier_list.put(state)
                explored.add(state)


def get_path(current_state):
    path = LifoQueue()
    path.put(current_state)
    while current_state.parent is not None:
        path.put(current_state.parent)
        current_state = current_state.parent
    return path







