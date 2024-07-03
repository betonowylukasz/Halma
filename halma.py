def move_states(board, player):
    for row, y in zip(board, range(16)):
        for square, x in zip(row, range(16)):
            if square == player:
                for state in available_moves(board, x, y, player):
                    yield state

def available_moves(board, x, y, player):
    if y > 0:
        if board[y-1][x] == 0:
            next_board = copy_list_in_list(board)
            next_board[y-1][x] = player
            next_board[y][x] = 0
            yield next_board
        if x > 0 and board[y-1][x - 1] == 0:
            next_board = copy_list_in_list(board)
            next_board[y-1][x - 1] = player
            next_board[y][x] = 0
            yield next_board
        if x < 15 and board[y-1][x + 1] == 0:
            next_board = copy_list_in_list(board)
            next_board[y-1][x + 1] = player
            next_board[y][x] = 0
            yield next_board
    if y < 15:
        if board[y+1][x] == 0:
            next_board = copy_list_in_list(board)
            next_board[y+1][x] = player
            next_board[y][x] = 0
            yield next_board
        if x > 0 and board[y+1][x - 1] == 0:
            next_board = copy_list_in_list(board)
            next_board[y+1][x - 1] = player
            next_board[y][x] = 0
            yield next_board
        if x < 15 and board[y+1][x + 1] == 0:
            next_board = copy_list_in_list(board)
            next_board[y+1][x + 1] = player
            next_board[y][x] = 0
            yield next_board
    if x > 0 and board[y][x-1] == 0:
        next_board = copy_list_in_list(board)
        next_board[y][x-1] = player
        next_board[y][x] = 0
        yield next_board
    if x < 15 and board[y][x+1] == 0:
        next_board = copy_list_in_list(board)
        next_board[y][x+1] = player
        next_board[y][x] = 0
        yield next_board
    for state in jump_moves(board, {(y, x)}, x, y, player):
        yield state


def jump_moves(board, visited, x, y, player):
    if y > 1:
        if board[y-1][x] > 0 and board[y-2][x] == 0 and (y-2, x) not in visited:
            next_board = copy_list_in_list(board)
            next_board[y - 2][x] = player
            next_board[y][x] = 0
            yield next_board
            visited.add((y-2, x))
            for state in jump_moves(next_board, visited, x, y-2, player):
                yield state
        if x > 1 and board[y-1][x - 1] > 0 and board[y-2][x-2] == 0 and (y-2, x-2) not in visited:
            next_board = copy_list_in_list(board)
            next_board[y-2][x - 2] = player
            next_board[y][x] = 0
            yield next_board
            visited.add((y-2, x-2))
            for state in jump_moves(next_board, visited, x-2, y-2, player):
                yield state
        if x < 14 and board[y - 1][x + 1] > 0 and board[y - 2][x + 2] == 0 and (y - 2, x + 2) not in visited:
            next_board = copy_list_in_list(board)
            next_board[y - 2][x + 2] = player
            next_board[y][x] = 0
            yield next_board
            visited.add((y - 2, x + 2))
            for state in jump_moves(next_board, visited, x + 2, y - 2, player):
                yield state
    if y < 14:
        if board[y+1][x] > 0 and board[y+2][x] == 0 and (y+2, x) not in visited:
            next_board = copy_list_in_list(board)
            next_board[y + 2][x] = player
            next_board[y][x] = 0
            yield next_board
            visited.add((y+2, x))
            for state in jump_moves(next_board, visited, x, y+2, player):
                yield state
        if x > 1 and board[y+1][x - 1] > 0 and board[y+2][x-2] == 0 and (y+2, x-2) not in visited:
            next_board = copy_list_in_list(board)
            next_board[y+2][x - 2] = player
            next_board[y][x] = 0
            yield next_board
            visited.add((y+2, x-2))
            for state in jump_moves(next_board, visited, x-2, y+2, player):
                yield state
        if x < 14 and board[y + 1][x + 1] > 0 and board[y + 2][x + 2] == 0 and (y + 2, x + 2) not in visited:
            next_board = copy_list_in_list(board)
            next_board[y + 2][x + 2] = player
            next_board[y][x] = 0
            yield next_board
            visited.add((y + 2, x + 2))
            for state in jump_moves(next_board, visited, x + 2, y + 2, player):
                yield state
    if x > 1:
        if board[y][x-1] > 0 and board[y][x-2] == 0 and (y, x-2) not in visited:
            next_board = copy_list_in_list(board)
            next_board[y][x-2] = player
            next_board[y][x] = 0
            yield next_board
            visited.add((y, x-2))
            for state in jump_moves(next_board, visited, x-2, y, player):
                yield state
    if x < 14:
        if board[y][x+1] > 0 and board[y][x+2] == 0 and (y, x+2) not in visited:
            next_board = copy_list_in_list(board)
            next_board[y][x+2] = player
            next_board[y][x] = 0
            yield next_board
            visited.add((y, x+2))
            for state in jump_moves(next_board, visited, x+2, y, player):
                yield state

def is_first_player_won(board):
    for x in range(5):
        if board[0][x] != 1: return False
    for x in range(5):
        if board[1][x] != 1: return False
    for x in range(4):
        if board[2][x] != 1: return False
    for x in range(3):
        if board[3][x] != 1: return False
    for x in range(2):
        if board[4][x] != 1: return False
    return True

def is_second_player_won(board):
    for x in range(5):
        if board[15][15-x] != 2: return False
    for x in range(5):
        if board[14][15-x] != 2: return False
    for x in range(4):
        if board[13][15-x] != 2: return False
    for x in range(3):
        if board[12][15-x] != 2: return False
    for x in range(2):
        if board[11][15-x] != 2: return False
    return True


def copy_list_in_list(list):
    new_list = []
    for elem in list:
        new_list.append(elem.copy())
    return new_list


