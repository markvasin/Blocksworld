import copy


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

    def __init__(self, size, objects_pos):
        self.size = size
        self.board = [['' for x in range(size)] for x in range(size)]
        for row in range(size):
            for col in range(size):
                self.board[row][col] = objects_pos.get(size * row + col + 1, ' ')
                if self.board[row][col] == 'X':
                    self.agent_location = row, col

        self.goal = {'A': (self.size - 3, self.size - 3), 'B': (self.size - 2, self.size - 3),
                     'C': (self.size - 1, self.size - 3)}

    def get_block_pos(self):
        block_location = {}
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col] == 'A':
                    block_location['A'] = row, col
                if self.board[row][col] == 'B':
                    block_location['B'] = row, col
                if self.board[row][col] == 'C':
                    block_location['C'] = row, col
        return block_location

    def get_goal_state(self):
        return self.goal

    def move(self, direction):
        new_agent_loc = self.get_new_agent_location(direction)
        old_value = self.board[self.agent_location[0]][self.agent_location[1]]
        self.board[self.agent_location[0]][self.agent_location[1]] = self.board[new_agent_loc[0]][new_agent_loc[1]]
        self.board[new_agent_loc[0]][new_agent_loc[1]] = old_value
        self.agent_location = new_agent_loc

    def get_new_agent_location(self, direction):
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
        return new_location

    def get_new_state(self, direction):
        new_agent_loc = self.get_new_agent_location(direction)
        new_board = copy.deepcopy(self.board)
        old_value = new_board[self.agent_location[0]][self.agent_location[1]]
        new_board[self.agent_location[0]][self.agent_location[1]] = new_board[new_agent_loc[0]][new_agent_loc[1]]
        new_board[new_agent_loc[0]][new_agent_loc[1]] = old_value
        new_obj_pos = get_objects_pos(new_board, self.size)
        return BlocksWorld(self.size, new_obj_pos)

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

    def __eq__(self, other):
        for row in range(self.size):
            if self.board[row] != other.board[row]:
                return False
        return True

    def __hash__(self):
        return hash(str(self.board))


def get_objects_pos(board, size):
    pos = {}
    for row in range(size):
        for col in range(size):
            if board[row][col] == 'A':
                pos[size * row + col + 1] = 'A'
            elif board[row][col] == 'B':
                pos[size * row + col + 1] = 'B'
            elif board[row][col] == 'C':
                pos[size * row + col + 1] = 'C'
            elif board[row][col] == 'X':
                pos[size * row + col + 1] = 'X'
    return pos
