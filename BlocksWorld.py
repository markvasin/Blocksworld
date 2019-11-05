class BlocksWorld:
    """
       Blocksworld tile puzzle as described in the AI coursework
       The puzzle can be of any N x N size depends on the input.
       This class defines the mechanics of the puzzle.
       The following are what represent each object in the game.
       X represents an agent.
       Empty space represents empty tile.
       Alphabet letter (A, B, C) represents the block.
       The goal of this game is to arrange the block according to the rule (goal state).
       """

    def __init__(self, size, start_state):
        self.size = size
        self.board = [['' for x in range(size)] for x in range(size)]
        for row in range(size):
            for col in range(size):
                self.board[row][col] = start_state.get(size * row + col + 1, ' ')

    def is_goal(self):
        return True

    def create_board_string(self):
        lines = []
        vertical_line = '|'
        horizontal_line = '-' * (self.size * 4 + 1)
        for row in range(self.size):
            row_line = ''
            for col in range(self.size):
                row_line += vertical_line + ' ' + str(self.board[row][col]) + ' '
            lines.append(horizontal_line)
            lines.append(row_line + vertical_line)
        lines.append(horizontal_line)
        return '\n'.join(lines)

    def display_board(self):
        print(self.create_board_string())
