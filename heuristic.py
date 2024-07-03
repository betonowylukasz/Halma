from halma import move_states, copy_list_in_list

def distance(board):
    heuristic = 0
    for row, y in zip(board, range(16)):
        for square, x in zip(row, range(16)):
            if square == 1: heuristic += (15 - x) + (15- y)
            elif square == 2: heuristic -= x + y
    return heuristic

def base(board):
    heuristic = 0
    for x in range(5):
        if board[0][x] != 0: heuristic += 1
    for x in range(5):
        if board[1][x] != 0: heuristic += 1
    for x in range(4):
        if board[2][x] != 0: heuristic += 1
    for x in range(3):
        if board[3][x] != 0: heuristic += 1
    for x in range(2):
        if board[4][x] != 0: heuristic += 1
    for x in range(5):
        if board[15][15-x] != 0: heuristic -= 1
    for x in range(5):
        if board[14][15-x] != 0: heuristic -= 1
    for x in range(4):
        if board[13][15-x] != 0: heuristic -= 1
    for x in range(3):
        if board[12][15-x] != 0: heuristic -= 1
    for x in range(2):
        if board[11][15-x] != 0: heuristic -= 1
    if board[0][5] == 1: heuristic -= 1
    if board[5][0] == 1: heuristic -= 1
    if board[10][15] == 2: heuristic += 1
    if board[15][10] == 2: heuristic += 1
    return heuristic

def base_for_moves(board):
    heuristic = 0
    for x in range(5):
        if board[0][x] != 0: heuristic += 7 - x
    for x in range(5):
        if board[1][x] != 0: heuristic += 6 - x
    for x in range(4):
        if board[2][x] != 0: heuristic += 5 - x
    for x in range(3):
        if board[3][x] != 0: heuristic += 4 - x
    for x in range(2):
        if board[4][x] != 0: heuristic += 3 - x
    for x in range(5):
        if board[15][15-x] != 0: heuristic -= 7 - x
    for x in range(5):
        if board[14][15-x] != 0: heuristic -= 6 - x
    for x in range(4):
        if board[13][15-x] != 0: heuristic -= 5 - x
    for x in range(3):
        if board[12][15-x] != 0: heuristic -= 4 - x
    for x in range(2):
        if board[11][15-x] != 0: heuristic -= 3 - x
    if board[0][5] == 1: heuristic -= 1
    if board[5][0] == 1: heuristic -= 1
    if board[10][15] == 2: heuristic += 1
    if board[15][10] == 2: heuristic += 1
    return heuristic

def wide_and_height(board):
    min_width1 = 16
    max_width1 = -1
    min_height1 = 16
    max_height1 = -1
    min_width2 = 16
    max_width2 = -1
    min_height2 = 16
    max_height2 = -1
    for row, y in zip(board, range(16)):
        for square, x in zip(row, range(16)):
            if square == 1:
                if x < min_width1: min_width1 = x
                if x > max_width1: max_width1 = x
                if y < min_height1: min_height1 = y
                if y > max_height1: max_height1 = y
            elif square == 2:
                if x < min_width2: min_width2 = x
                if x > max_width2: max_width2 = x
                if y < min_height2: min_height2 = y
                if y > max_height2: max_height2 = y
    return min_width1 - max_width1 + min_height1 - max_height1 - min_width2 + max_width2 - min_height2 + max_height2

def move(board):
    moves = 0
    for row, y in zip(board, range(16)):
        for square, x in zip(row, range(16)):
            if square == 1: moves += available_moves_amount(board, x, y, 1)
            elif square == 2: moves -= available_moves_amount(board, x, y, 2)
    return moves

def available_moves_amount(board, x, y, player):
    moves = 0
    if y > 0:
        if board[y-1][x] == 0: moves += 1
        if x > 0 and board[y-1][x - 1] == 0: moves += 1
        if x < 15 and board[y-1][x + 1] == 0: moves += 1
    if y < 15:
        if board[y+1][x] == 0: moves += 1
        if x > 0 and board[y+1][x - 1] == 0: moves += 1
        if x < 15 and board[y+1][x + 1] == 0: moves += 1
    if x > 0 and board[y][x-1] == 0: moves += 1
    if x < 15 and board[y][x+1] == 0: moves += 1
    return moves + jump_moves_amount(board, {(y, x)}, x, y, player)

# def jump_moves_amount(board,x, y):
#     moves = 0
#     if y > 1:
#         if board[y-1][x] > 0 and board[y-2][x] == 0:
#             moves += 1
#         if x > 1 and board[y-1][x - 1] > 0 and board[y-2][x-2] == 0:
#             moves += 1
#         if x < 14 and board[y - 1][x + 1] > 0 and board[y - 2][x + 2] == 0:
#             moves += 1
#     if y < 14:
#         if board[y+1][x] > 0 and board[y+2][x] == 0:
#             moves += 1
#         if x > 1 and board[y+1][x - 1] > 0 and board[y+2][x-2] == 0:
#             moves += 1
#         if x < 14 and board[y + 1][x + 1] > 0 and board[y + 2][x + 2] == 0:
#             moves += 1
#     if x > 1:
#         if board[y][x-1] > 0 and board[y][x-2] == 0:
#             moves += 1
#     if x < 14:
#         if board[y][x+1] > 0 and board[y][x+2] == 0:
#             moves += 1
#     return moves

def jump_moves_amount(board, visited, x, y, player):
    moves = 0
    if y > 1:
        if board[y-1][x] > 0 and board[y-2][x] == 0 and (y-2, x) not in visited:
            next_board = copy_list_in_list(board)
            next_board[y - 2][x] = player
            next_board[y][x] = 0
            moves += 1
            visited.add((y-2, x))
            moves += jump_moves_amount(next_board, visited, x, y-2, player)
        if x > 1 and board[y-1][x - 1] > 0 and board[y-2][x-2] == 0 and (y-2, x-2) not in visited:
            next_board = copy_list_in_list(board)
            next_board[y-2][x - 2] = player
            next_board[y][x] = 0
            moves += 1
            visited.add((y-2, x-2))
            moves += jump_moves_amount(next_board, visited, x-2, y-2, player)
        if x < 14 and board[y - 1][x + 1] > 0 and board[y - 2][x + 2] == 0 and (y - 2, x + 2) not in visited:
            next_board = copy_list_in_list(board)
            next_board[y - 2][x + 2] = player
            next_board[y][x] = 0
            moves += 1
            visited.add((y - 2, x + 2))
            moves += jump_moves_amount(next_board, visited, x + 2, y - 2, player)
    if y < 14:
        if board[y+1][x] > 0 and board[y+2][x] == 0 and (y+2, x) not in visited:
            next_board = copy_list_in_list(board)
            next_board[y + 2][x] = player
            next_board[y][x] = 0
            moves += 1
            visited.add((y+2, x))
            moves += jump_moves_amount(next_board, visited, x, y+2, player)
        if x > 1 and board[y+1][x - 1] > 0 and board[y+2][x-2] == 0 and (y+2, x-2) not in visited:
            next_board = copy_list_in_list(board)
            next_board[y+2][x - 2] = player
            next_board[y][x] = 0
            moves += 1
            visited.add((y+2, x-2))
            moves += jump_moves_amount(next_board, visited, x-2, y+2, player)
        if x < 14 and board[y + 1][x + 1] > 0 and board[y + 2][x + 2] == 0 and (y + 2, x + 2) not in visited:
            next_board = copy_list_in_list(board)
            next_board[y + 2][x + 2] = player
            next_board[y][x] = 0
            moves += 1
            visited.add((y + 2, x + 2))
            moves += jump_moves_amount(next_board, visited, x + 2, y + 2, player)
    if x > 1:
        if board[y][x-1] > 0 and board[y][x-2] == 0 and (y, x-2) not in visited:
            next_board = copy_list_in_list(board)
            next_board[y][x-2] = player
            next_board[y][x] = 0
            moves += 1
            visited.add((y, x-2))
            moves += jump_moves_amount(next_board, visited, x-2, y, player)
    if x < 14:
        if board[y][x+1] > 0 and board[y][x+2] == 0 and (y, x+2) not in visited:
            next_board = copy_list_in_list(board)
            next_board[y][x+2] = player
            next_board[y][x] = 0
            moves += 1
            visited.add((y, x+2))
            moves += jump_moves_amount(next_board, visited, x+2, y, player)
    return moves


def move_heuristics(board, player, heuristic_num):
    copy_board = copy_list_in_list(board)
    heuristic = distance(board)
    for row, y in zip(board, range(16)):
        for square, x in zip(row, range(16)):
            if square == player:
                for result in available_heuristics(copy_board, x, y, player, heuristic, heuristic_num):
                    yield result

# def available_heuristics(board, x, y, player, heuristic, heuristic_num):
#     if y > 0:
#         if board[y-1][x] == 0:
#             next_board = copy_list_in_list(board)
#             next_board[y-1][x] = player
#             next_board[y][x] = 0
#             if heuristic_num == 1: yield heuristic + 1 + base(next_board)
#             elif heuristic_num == 2: yield (heuristic + 1)*8 + base(next_board)*16 + move(next_board)
#         if x > 0 and board[y-1][x - 1] == 0:
#             next_board = copy_list_in_list(board)
#             next_board[y-1][x - 1] = player
#             next_board[y][x] = 0
#             if heuristic_num == 1:
#                 yield heuristic + 2 + base(next_board)
#             elif heuristic_num == 2:
#                 yield (heuristic + 2) * 8 + base(next_board) * 16 + move(next_board)
#         if x < 15 and board[y-1][x + 1] == 0:
#             next_board = copy_list_in_list(board)
#             next_board[y-1][x + 1] = player
#             next_board[y][x] = 0
#             if heuristic_num == 1:
#                 yield heuristic + base(next_board)
#             elif heuristic_num == 2:
#                 yield heuristic * 8 + base(next_board) * 16 + move(next_board)
#     if y < 15:
#         if board[y+1][x] == 0:
#             next_board = copy_list_in_list(board)
#             next_board[y+1][x] = player
#             next_board[y][x] = 0
#             if heuristic_num == 1:
#                 yield heuristic - 1 + base(next_board)
#             elif heuristic_num == 2:
#                 yield (heuristic - 1) * 8 + base(next_board) * 16 + move(next_board)
#         if x > 0 and board[y+1][x - 1] == 0:
#             next_board = copy_list_in_list(board)
#             next_board[y+1][x - 1] = player
#             next_board[y][x] = 0
#             if heuristic_num == 1:
#                 yield heuristic + base(next_board)
#             elif heuristic_num == 2:
#                 yield heuristic * 8 + base(next_board) * 16 + move(next_board)
#         if x < 15 and board[y+1][x + 1] == 0:
#             next_board = copy_list_in_list(board)
#             next_board[y+1][x + 1] = player
#             next_board[y][x] = 0
#             if heuristic_num == 1:
#                 yield heuristic - 2 + base(next_board)
#             elif heuristic_num == 2:
#                 yield (heuristic - 2) * 8 + base(next_board) * 16 + move(next_board)
#     if x > 0 and board[y][x-1] == 0:
#         next_board = copy_list_in_list(board)
#         next_board[y][x-1] = player
#         next_board[y][x] = 0
#         if heuristic_num == 1:
#             yield heuristic + 1 + base(next_board)
#         elif heuristic_num == 2:
#             yield (heuristic + 1) * 8 + base(next_board) * 16 + move(next_board)
#     if x < 15 and board[y][x+1] == 0:
#         next_board = copy_list_in_list(board)
#         next_board[y][x+1] = player
#         next_board[y][x] = 0
#         if heuristic_num == 1:
#             yield heuristic - 1 + base(next_board)
#         elif heuristic_num == 2:
#             yield (heuristic - 1) * 8 + base(next_board) * 16 + move(next_board)
#     for result in jump_heuristics(board, {(y, x)}, x, y, player, heuristic, heuristic_num):
#         yield result

def available_heuristics(board, x, y, player, heuristic, heuristic_num):
    if y > 0:
        if board[y-1][x] == 0:
            board[y - 1][x] = player
            board[y][x] = 0
            if heuristic_num == 1: yield heuristic + 1 + base(board)
            elif heuristic_num == 2: yield (heuristic + 1)*8 + base_for_moves(board)*8 + move(board)
            else: yield heuristic + 1 + base(board) + wide_and_height(board)
            board[y - 1][x] = 0
            board[y][x] = player
        if x > 0 and board[y-1][x - 1] == 0:
            board[y - 1][x - 1] = player
            board[y][x] = 0
            if heuristic_num == 1: yield heuristic + 2 + base(board)
            elif heuristic_num == 2: yield (heuristic + 2)*8 + base_for_moves(board)*8 + move(board)
            else:
                yield heuristic + 2 + base(board) + wide_and_height(board)
            board[y - 1][x - 1] = 0
            board[y][x] = player
        if x < 15 and board[y-1][x + 1] == 0:
            board[y - 1][x + 1] = player
            board[y][x] = 0
            if heuristic_num == 1: yield heuristic + base(board)
            elif heuristic_num == 2:
                yield heuristic*8 + base_for_moves(board)*8 + move(board)
            else:
                yield heuristic + base(board) + wide_and_height(board)
            board[y - 1][x + 1] = 0
            board[y][x] = player
    if y < 15:
        if board[y+1][x] == 0:
            board[y + 1][x] = player
            board[y][x] = 0
            if heuristic_num == 1: yield heuristic - 1 + base(board)
            elif heuristic_num == 2:
                yield (heuristic - 1)*8 + base_for_moves(board)*8 + move(board)
            else:
                yield heuristic - 1 + base(board) + wide_and_height(board)
            board[y + 1][x] = 0
            board[y][x] = player
        if x > 0 and board[y+1][x - 1] == 0:
            board[y + 1][x - 1] = player
            board[y][x] = 0
            if heuristic_num == 1: yield heuristic + base(board)
            elif heuristic_num == 2:
                yield heuristic + base_for_moves(board)*8 + move(board)
            else:
                yield heuristic + base(board) + wide_and_height(board)
            board[y + 1][x - 1] = 0
            board[y][x] = player
        if x < 15 and board[y+1][x + 1] == 0:
            board[y + 1][x + 1] = player
            board[y][x] = 0
            if heuristic_num == 1: yield heuristic - 2 + base(board)
            elif heuristic_num == 2:
                yield (heuristic - 2)*8 + base_for_moves(board)*8 + move(board)
            else:
                yield heuristic - 2 + base(board) + wide_and_height(board)
            board[y + 1][x + 1] = 0
            board[y][x] = player
    if x > 0 and board[y][x-1] == 0:
        board[y][x - 1] = player
        board[y][x] = 0
        if heuristic_num == 1: yield heuristic + 1 + base(board)
        elif heuristic_num == 2:
            yield (heuristic + 1)*8 + base_for_moves(board)*8 + move(board)
        else:
            yield heuristic + 1 + base(board) + wide_and_height(board)
        board[y][x - 1] = 0
        board[y][x] = player
    if x < 15 and board[y][x+1] == 0:
        board[y][x + 1] = player
        board[y][x] = 0
        if heuristic_num == 1: yield heuristic - 1 + base(board)
        elif heuristic_num == 2:
            yield (heuristic - 1)*8 + base_for_moves(board)*8 + move(board)
        else:
            yield heuristic - 1 + base(board) + wide_and_height(board)
        board[y][x + 1] = 0
        board[y][x] = player
    for result in jump_heuristics(board, {(y, x)}, x, y, player, heuristic, heuristic_num):
        yield result


def jump_heuristics(board, visited, x, y, player, heuristic, heuristic_num):
    if y > 1:
        if board[y-1][x] > 0 and board[y-2][x] == 0 and (y-2, x) not in visited:
            next_board = copy_list_in_list(board)
            next_board[y - 2][x] = player
            next_board[y][x] = 0
            if heuristic_num == 1: yield heuristic+2+base(next_board)
            elif heuristic_num == 2:
                yield (heuristic + 2)*8 + base_for_moves(next_board)*8 + move(next_board)
            else:
                yield heuristic + 2 + base(next_board) + wide_and_height(next_board)
            visited.add((y-2, x))
            for result in jump_heuristics(next_board, visited, x, y-2, player, heuristic+2, heuristic_num):
                yield result
        if x > 1 and board[y-1][x - 1] > 0 and board[y-2][x-2] == 0 and (y-2, x-2) not in visited:
            next_board = copy_list_in_list(board)
            next_board[y-2][x - 2] = player
            next_board[y][x] = 0
            if heuristic_num == 1: yield heuristic+4+base(next_board)
            elif heuristic_num == 2:
                yield (heuristic + 4)*8 + base_for_moves(next_board)*8 + move(next_board)
            else:
                yield heuristic + 4 + base(next_board) + wide_and_height(next_board)
            visited.add((y-2, x-2))
            for result in jump_heuristics(next_board, visited, x-2, y-2, player, heuristic+4, heuristic_num):
                yield result
        if x < 14 and board[y - 1][x + 1] > 0 and board[y - 2][x + 2] == 0 and (y - 2, x + 2) not in visited:
            next_board = copy_list_in_list(board)
            next_board[y - 2][x + 2] = player
            next_board[y][x] = 0
            if heuristic_num == 1: yield heuristic+base(next_board)
            elif heuristic_num == 2:
                yield heuristic*8 + base_for_moves(next_board)*8 + move(next_board)
            else:
                yield heuristic + base(next_board) + wide_and_height(next_board)
            visited.add((y - 2, x + 2))
            for result in jump_heuristics(next_board, visited, x + 2, y - 2, player, heuristic, heuristic_num):
                yield result
    if y < 14:
        if board[y+1][x] > 0 and board[y+2][x] == 0 and (y+2, x) not in visited:
            next_board = copy_list_in_list(board)
            next_board[y + 2][x] = player
            next_board[y][x] = 0
            if heuristic_num == 1: yield heuristic-2+base(next_board)
            elif heuristic_num == 2:
                yield (heuristic - 2)*8 + base_for_moves(next_board)*8 + move(next_board)
            else:
                yield heuristic - 2 + base(next_board) + wide_and_height(next_board)
            visited.add((y+2, x))
            for result in jump_heuristics(next_board, visited, x, y+2, player, heuristic-2, heuristic_num):
                yield result
        if x > 1 and board[y+1][x - 1] > 0 and board[y+2][x-2] == 0 and (y+2, x-2) not in visited:
            next_board = copy_list_in_list(board)
            next_board[y+2][x - 2] = player
            next_board[y][x] = 0
            if heuristic_num == 1: yield heuristic+base(next_board)
            elif heuristic_num == 2:
                yield heuristic*8 + base_for_moves(next_board)*8 + move(next_board)
            else:
                yield heuristic + base(next_board) + wide_and_height(next_board)
            visited.add((y+2, x-2))
            for result in jump_heuristics(next_board, visited, x-2, y+2, player, heuristic, heuristic_num):
                yield result
        if x < 14 and board[y + 1][x + 1] > 0 and board[y + 2][x + 2] == 0 and (y + 2, x + 2) not in visited:
            next_board = copy_list_in_list(board)
            next_board[y + 2][x + 2] = player
            next_board[y][x] = 0
            if heuristic_num == 1: yield heuristic-4+base(next_board)
            elif heuristic_num == 2:
                yield (heuristic - 4)*8 + base_for_moves(next_board)*8 + move(next_board)
            else:
                yield heuristic - 4 + base(next_board) + wide_and_height(next_board)
            visited.add((y + 2, x + 2))
            for result in jump_heuristics(next_board, visited, x + 2, y + 2, player, heuristic-4, heuristic_num):
                yield result
    if x > 1:
        if board[y][x-1] > 0 and board[y][x-2] == 0 and (y, x-2) not in visited:
            next_board = copy_list_in_list(board)
            next_board[y][x-2] = player
            next_board[y][x] = 0
            if heuristic_num == 1: yield heuristic+2+base(next_board)
            elif heuristic_num == 2:
                yield (heuristic + 2)*8 + base_for_moves(next_board)*8 + move(next_board)
            else:
                yield heuristic + 2 + base(next_board) + wide_and_height(next_board)
            visited.add((y, x-2))
            for result in jump_heuristics(next_board, visited, x-2, y, player, heuristic+2, heuristic_num):
                yield result
    if x < 14:
        if board[y][x+1] > 0 and board[y][x+2] == 0 and (y, x+2) not in visited:
            next_board = copy_list_in_list(board)
            next_board[y][x+2] = player
            next_board[y][x] = 0
            if heuristic_num == 1: yield heuristic-2+base(next_board)
            elif heuristic_num == 2:
                yield (heuristic - 2)*8 + base_for_moves(next_board)*8 + move(next_board)
            else:
                yield heuristic - 2 + base(next_board) + wide_and_height(next_board)
            visited.add((y, x+2))
            for result in jump_heuristics(next_board, visited, x+2, y, player, heuristic-2, heuristic_num):
                yield result


