import util
from BlocksWorld import BlocksWorld
from BlocksWorldProblem import BlocksWorldProblem
from TreeNode import TreeNode


def breadth_first_search(problem):
    fringe = util.Queue()
    initial_node = TreeNode(problem.get_start_state(), None, 0, [], 1)
    fringe.push(initial_node)
    while True:
        if fringe.is_empty():
            return []
        node = fringe.pop()
        if problem.is_goal_state(node.state):
            return node.action
        for new_node in problem.get_successors(node):
            fringe.push(new_node)


def depth_first_search(problem):
    fringe = util.Stack()
    initial_node = TreeNode(problem.get_start_state(), None, 0, [], 1)
    fringe.push(initial_node)
    while True:
        if fringe.is_empty():
            return []
        node = fringe.pop()
        if problem.is_goal_state(node.state):
            return node.action
        for new_node in problem.get_successors(node):
            fringe.push(new_node)


def iterative_deepening_search(problem):
    depth = 0
    while True:
        result = depth_limited_search(problem, depth)
        if result != "cutoff":
            return result
        depth += 1


def depth_limited_search(problem, limit):
    def recursive_dls(node):
        cutoff_occurred = False
        cutoff = "cutoff"
        failure = "fail"
        if problem.is_goal_state(node.state):
            return node.action
        elif node.depth == limit:
            return cutoff
        else:
            for new_node in problem.get_successors(node):
                result = recursive_dls(new_node)
                if result == cutoff:
                    cutoff_occurred = True
                elif result != failure:
                    return result
        if cutoff_occurred:
            return cutoff
        else:
            return failure

    initial_node = TreeNode(problem.get_start_state(), None, 0, [], 1)
    return recursive_dls(initial_node)


def a_star_search():
    print()


def create_blocks_world():
    start_state_for_bfs = {
        7: "A",
        9: "B",
        14: "C",
        2: "X"
    }

    start_state_for_dfs = {
        2: "A",
        6: "B",
        14: "C",
        10: "X"
    }

    start_state = {
        13: "A",
        14: "B",
        15: "C",
        16: "X"
    }
    return BlocksWorld(4, start_state)


blocks_world = create_blocks_world()
blocks_world.display_board()
search_problem = BlocksWorldProblem(blocks_world)
path = iterative_deepening_search(search_problem)
print('Found result:', path)
for p in path:
    print(p)
    blocks_world.move(p)
    blocks_world.display_board()
