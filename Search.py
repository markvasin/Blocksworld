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


def create_blocks_world():
    # start_state_for_bfs = {
    #     7: "A",
    #     9: "B",
    #     14: "C",
    #     2: "X"
    # }

    start_state_for_dfs = {
        2: "A",
        6: "B",
        14: "C",
        10: "X"
    }

    # start_state = {
    #     13: "A",
    #     14: "B",
    #     15: "C",
    #     16: "X"
    # }
    return BlocksWorld(4, start_state_for_dfs)


blocks_world = create_blocks_world()
blocks_world.display_board()
search_problem = BlocksWorldProblem(blocks_world)
path = depth_first_search(search_problem)
print('Found result:', path)
for p in path:
    print(p)
    blocks_world.move(p)
    blocks_world.display_board()
