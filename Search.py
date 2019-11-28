import random
import time

import util
from BlocksWorld import BlocksWorld
from BlocksWorldProblem import BlocksWorldProblem
from BlocksWorldStates import start_state, all_start_states
from Solution import Solution
from TreeNode import TreeNode


def breadth_first_search(problem):
    print('Running breadth-first search...')
    node_expanded = 0
    fringe = util.Queue()
    initial_node = TreeNode(problem.get_start_state(), None, 0, [], 0)
    fringe.push(initial_node)
    while True:
        if fringe.is_empty():
            return Solution([], node_expanded, -1, -1)  # No solution found
        node = fringe.pop()
        node_expanded += 1
        if problem.is_goal_state(node.state):
            return Solution(node.action, node_expanded + fringe.size(), node.depth, node.cost)
        for new_node in problem.get_successors(node):
            fringe.push(new_node)


def depth_first_search(problem):
    print('Running depth-first search...')
    node_expanded = 0
    fringe = util.Stack()
    initial_node = TreeNode(problem.get_start_state(), None, 0, [], 0)
    fringe.push(initial_node)
    while True:
        if fringe.is_empty():
            return Solution([], node_expanded, -1, -1)  # No solution found
        node = fringe.pop()
        node_expanded += 1
        if problem.is_goal_state(node.state):
            return Solution(node.action, node_expanded + fringe.size(), node.depth, node.cost)
        successors = problem.get_successors(node)
        random.shuffle(successors)  # Randomise the order of expansion in DFS
        for new_node in successors:
            fringe.push(new_node)


def iterative_deepening_search(problem):
    print('Running iterative deepening search...')
    node_expanded = 0
    depth = 0
    while True:
        result = depth_limited_search(problem, depth)
        node_expanded += result.total_nodes
        if result.path != "cutoff":
            return Solution(result.path, node_expanded, result.depth, result.cost)
        depth += 1


def depth_limited_search(problem, limit):
    node_expanded = 0

    def recursive_dls(node):
        nonlocal node_expanded
        node_expanded += 1
        cutoff_occurred = False
        cutoff = "cutoff"
        failure = "fail"
        if problem.is_goal_state(node.state):
            return Solution(node.action, node_expanded, node.depth, node.cost)
        elif node.depth == limit:
            return Solution(cutoff, node_expanded, node.depth, node.cost)
        else:
            for new_node in problem.get_successors(node):
                result = recursive_dls(new_node)
                if result.path == cutoff:
                    cutoff_occurred = True
                elif result.path != failure:
                    return result
        if cutoff_occurred:
            return Solution(cutoff, node_expanded, node.depth, node.cost)
        else:
            return Solution(failure, node_expanded, node.depth, node.cost)

    initial_node = TreeNode(problem.get_start_state(), None, 0, [], 0)
    return recursive_dls(initial_node)


def a_star_search(problem, heuristic):
    print('Running A star heuristic search...')
    node_expanded = 0
    fringe = util.PriorityQueue()
    initial_node = TreeNode(problem.get_start_state(), None, 0, [], 0)
    fringe.push(initial_node, heuristic(problem.get_start_state()))
    while True:
        if fringe.is_empty():
            return Solution([], node_expanded, -1, -1)  # No solution found
        node = fringe.pop()
        node_expanded += 1
        if problem.is_goal_state(node.state):
            return Solution(node.action, node_expanded + fringe.size(), node.depth, node.cost)
        for new_node in problem.get_successors(node):
            fringe.push(new_node, new_node.cost + heuristic(new_node.state))


def manhattan_heuristic(board):
    distance = 0
    block_pos = board.get_block_pos()
    for key, value in block_pos.items():
        distance += manhattan_distance(value, board.get_goal_state()[key])
    return distance


def manhattan_distance(xy1, xy2):
    return abs(xy1[0] - xy2[0]) + abs(xy1[1] - xy2[1])


def breadth_first_search_graph(problem):
    print('Running breadth-first graph search...')
    node_expanded = 0
    closed = set()
    fringe = util.Queue()
    initial_node = TreeNode(problem.get_start_state(), None, 0, [], 0)
    fringe.push(initial_node)
    while True:
        if fringe.is_empty():
            return Solution([], node_expanded, -1, -1)  # No solution found
        node = fringe.pop()
        node_expanded += 1
        if problem.is_goal_state(node.state):
            return Solution(node.action, node_expanded + fringe.size(), node.depth, node.cost)
        if node.state not in closed:
            closed.add(node.state)
            for new_node in problem.get_successors(node):
                fringe.push(new_node)


def depth_first_search_graph(problem):
    print('Running depth-first graph search...')
    node_expanded = 0
    closed = set()
    fringe = util.Stack()
    initial_node = TreeNode(problem.get_start_state(), None, 0, [], 0)
    fringe.push(initial_node)
    while True:
        if fringe.is_empty():
            return Solution([], node_expanded, -1, -1)  # No solution found
        node = fringe.pop()
        node_expanded += 1
        if problem.is_goal_state(node.state):
            return Solution(node.action, node_expanded + fringe.size(), node.depth, node.cost)
        if node.state not in closed:
            closed.add(node.state)
            successors = problem.get_successors(node)
            random.shuffle(successors)  # Randomise the order of expansion in DFS
            for new_node in successors:
                fringe.push(new_node)


def a_star_search_graph(problem, heuristic):
    print('Running A star heuristic graph search...')
    node_expanded = 0
    closed = set()
    fringe = util.PriorityQueue()
    initial_node = TreeNode(problem.get_start_state(), None, 0, [], 0)
    fringe.push(initial_node, heuristic(problem.get_start_state()))
    while True:
        if fringe.is_empty():
            return Solution([], node_expanded, -1, -1)  # No solution found
        node = fringe.pop()
        node_expanded += 1
        if problem.is_goal_state(node.state):
            return Solution(node.action, node_expanded + fringe.size(), node.depth, node.cost)
        if node.state not in closed:
            closed.add(node.state)
            for new_node in problem.get_successors(node):
                fringe.push(new_node, new_node.cost + heuristic(new_node.state))


def print_path_grid(path):
    for p in path:
        print(p)
        blocks_world.move(p)
        blocks_world.display_board()


# Code to run the search problem
grid_size = 4
blocks_world = BlocksWorld(grid_size, start_state)
blocks_world.display_board()
search_problem = BlocksWorldProblem(blocks_world)
start = time.time()
solution = a_star_search(search_problem, manhattan_heuristic)
# solution = depth_first_search(search_problem)
end = time.time()
print('Found result:', solution.path)
print('Total elapse time in second:', end - start)
print('Total node generated:', solution.total_nodes)
print('Depth of the solution:', solution.depth)
print('Total cost from start to goal state:', solution.cost)
print_path_grid(solution.path)


# Code to get the number of node generated with increasing problem difficulty
nodes_generated = []
for start in all_start_states:
    blocks_world = BlocksWorld(grid_size, start)
    search_problem = BlocksWorldProblem(blocks_world)
    # blocks_world.display_board()
    solution = depth_first_search(search_problem)
    print('Found result:', solution.path)
    print('Total node generated:', solution.total_nodes)
    nodes_generated.append(solution.total_nodes)
    print(nodes_generated)
