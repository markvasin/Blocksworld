from TreeNode import TreeNode


class BlocksWorldProblem:

    def __init__(self, blocks_world):
        self.start_state = blocks_world

    def get_start_state(self):
        return self.start_state

    def is_goal_state(self, blocks_world):
        return blocks_world.is_goal()

    def get_successors(self, node):
        successors = []
        for direction in node.state.get_legal_move():
            new_state = node.state.get_new_state(direction)
            new_node = TreeNode(new_state, node, node.depth + 1, node.action + [direction], node.cost + 1)
            successors.append(new_node)
        return successors
