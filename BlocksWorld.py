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
                if self.board[row][col] == 'X':
                    self.agent_location = row, col

    def move(self, direction):
        if direction == 'UP':
            new_location = self.agent_location[0] - 1, self.agent_location[1]
        elif direction == 'DOWN':
            new_location = self.agent_location[0] + 1, self.agent_location[1]
        elif direction == 'LEFT':
            new_location = self.agent_location[0], self.agent_location[1] - 1
        elif direction == 'RIGHT':
            new_location = self.agent_location[0], self.agent_location[1] + 1
        else:
            raise ValueError('Invalid move')

        old_value = self.board[self.agent_location[0]][self.agent_location[1]]
        self.board[self.agent_location[0]][self.agent_location[1]] = self.board[new_location[0]][new_location[1]]
        self.board[new_location[0]][new_location[1]] = old_value
        self.agent_location = new_location

    def get_legal_move(self):
        legal_moves = []
        row, col = self.agent_location
        if row != 0:
            legal_moves.append('UP')
        if row != self.size - 1:
            legal_moves.append('DOWN')
        if col != 0:
            legal_moves.append('LEFT')
        if col != self.size - 1:
            legal_moves.append('RIGHT')
        return legal_moves

    def get_agent_location(self):
        print(self.agent_location)

    def is_goal(self):
        if self.board[self.size - 3][self.size - 3] == 'A' and self.board[self.size - 2][self.size - 3] == 'B' and \
                self.board[self.size - 1][self.size - 3] == 'C':
            return True
        else:
            return False

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
