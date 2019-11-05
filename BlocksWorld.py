
class BlocksWorld:

    def __init__(self, size):
        self.size = size
        self.board = [[0 for x in range(size)] for x in range(size)]
        for i in range(size):
            for j in range(size):
                self.board[i][j] = ' '
        
    def create_board_string(self):
        lines = []
        horizontal_line = '-' * (self.size * 4 + 1)
        lines.append(horizontal_line)
        for row in range(self.size):
            row_line = '|'
            for col in range(self.size):
                row_line = row_line + ' ' + self.board[col][row] + ' |'
            lines.append(row_line)
            lines.append(horizontal_line)
        return '\n'.join(lines)

    def display_board(self):
        print(self.create_board_string())

