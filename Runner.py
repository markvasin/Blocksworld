import os

from BlocksWorld import BlocksWorld


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


start_state = {
    13: "A",
    14: "B",
    15: "C",
    16: "X"
}

size = int(input('Please select board size: '))
blocks_world = BlocksWorld(size, start_state)

while not blocks_world.is_goal():
    blocks_world.display_board()
    print('Movable direction: ' + ', '.join(blocks_world.get_legal_move()))
    user_input = input('Please input direction (w = up, a = left, s = down, d = right)\n')
    direction = ''
    if user_input == 'w':
        direction = 'UP'
    elif user_input == 'a':
        direction = 'LEFT'
    elif user_input == 's':
        direction = 'DOWN'
    elif user_input == 'd':
        direction = 'RIGHT'

    if direction != '':
        blocks_world.move(direction)
    cls()

blocks_world.display_board()
print("You have won")
