from BlocksWorld import BlocksWorld
from BlocksWorldProblem import BlocksWorldProblem
from TreeNode import TreeNode


class Queue:
    "A container with a first-in-first-out (FIFO) queuing policy."

    def __init__(self):
        self.list = []

    def push(self, item):
        "Enqueue the 'item' into the queue"
        self.list.insert(0, item)

    def pop(self):
        """
          Dequeue the earliest enqueued item still in the queue. This
          operation removes the item from the queue.
        """
        return self.list.pop()

    def isEmpty(self):
        "Returns true if the queue is empty"
        return len(self.list) == 0


def breadth_first_search(problem):
    fringe = Queue()
    initial_node = TreeNode(problem.get_start_state(), None, 0, [], 1)
    fringe.push(initial_node)
    while True:
        if fringe.isEmpty():
            return []
        node = fringe.pop()
        if problem.is_goal_state(node.state):
            return node.action
        for new_node in problem.get_successors(node):
            fringe.push(new_node)


def create_blocks_world():
    start_state = {
        7: "A",
        9: "B",
        14: "C",
        2: "X"
    }
    # start_state = {
    #     13: "A",
    #     14: "B",
    #     15: "C",
    #     16: "X"
    # }
    return BlocksWorld(4, start_state)


blocks_world = create_blocks_world()
blocks_world.display_board()
problem = BlocksWorldProblem(blocks_world)
path = breadth_first_search(problem)
print('Found result:', path)
for p in path:
    print(p)
    blocks_world.move(p)
    blocks_world.display_board()
