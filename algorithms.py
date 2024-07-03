import random
import time
from halma import move_states, is_first_player_won, is_second_player_won
from heuristic import move_heuristics, distance, base, move, wide_and_height, base_for_moves


def minimax(board, max_depth, player, heuristic_num):
    min = float('inf')
    max = float('-inf')
    start_time = time.time()
    nodes = 0
    next_boards = []
    next_states = move_states(board, player)
    if player == 1:
        for state in next_states:
            nodes += 1
            if is_first_player_won(state): return state, nodes, time.time() - start_time
            min_max, nodes = minimax_rec(state, 1, max_depth, 2, heuristic_num, nodes)
            if max < min_max:
                max = min_max
                next_boards = [state]
            elif max == min_max: next_boards.append(state)
        #print(max)
    else:
        for state in next_states:
            nodes += 1
            if is_second_player_won(state): return state, nodes, time.time() - start_time
            min_max, nodes = minimax_rec(state, 1, max_depth, 1, heuristic_num, nodes)
            if min > min_max:
                min = min_max
                next_boards = [state]
            elif min == min_max: next_boards.append(state)
        #print(min)
    return next_boards[random.randrange(len(next_boards))], nodes, time.time() - start_time

def minimax_rec(board, depth, max_depth, player, heuristic_num, nodes):
    if depth >= max_depth:
        if heuristic_num == 1: return distance(board) + base(board), nodes
        elif heuristic_num == 2: return distance(board)*8 + base(board)*16 + move(board), nodes
        else: return distance(board) + base(board) + wide_and_height(board), nodes
    min = float('inf')
    max = float('-inf')
    if depth >= max_depth-1:
        next_heuristics = move_heuristics(board, player, heuristic_num)
        if player == 1:
            for heuristic in next_heuristics:
                nodes += 1
                if max < heuristic: max = heuristic
            return max, nodes
        if player == 2:
            for heuristic in next_heuristics:
                nodes += 1
                if min > heuristic: min = heuristic
            return min, nodes
    next_states = move_states(board, player)
    if player == 1:
        for state in next_states:
            nodes += 1
            if is_first_player_won(state): return float('inf'), nodes
            min_max, nodes = minimax_rec(state, depth+1, max_depth, 2, heuristic_num, nodes)
            if max < min_max: max = min_max
        return max, nodes
    else:
        for state in next_states:
            nodes += 1
            if is_second_player_won(state): return float('-inf'), nodes
            min_max, nodes = minimax_rec(state, depth+1, max_depth, 1, heuristic_num, nodes)
            if min > min_max: min = min_max
        return min, nodes


def alfa_beta(board, max_depth, player, heuristic_num):
    min = float('inf')
    max = float('-inf')
    alfa = float('-inf')
    beta = float('inf')
    start_time = time.time()
    nodes = 0
    next_boards = []
    next_states = move_states(board, player)
    if player == 1:
        for state in next_states:
            nodes += 1
            if is_first_player_won(state): return state, nodes, time.time() - start_time
            min_max, nodes = alfa_beta_rec(state, 1, max_depth, 2, heuristic_num, alfa, beta, nodes)
            if max < min_max:
                max = min_max
                next_boards = [state]
            elif max == min_max: next_boards.append(state)
            if alfa < min_max: alfa = min_max
        #print(max)
    else:
        for state in next_states:
            nodes += 1
            if is_second_player_won(state): return state, nodes, time.time() - start_time
            min_max, nodes = alfa_beta_rec(state, 1, max_depth, 1, heuristic_num, alfa, beta, nodes)
            if min > min_max:
                min = min_max
                next_boards = [state]
            elif min == min_max: next_boards.append(state)
            if beta > min_max: beta = min_max
        #print(min)
    return next_boards[random.randrange(len(next_boards))], nodes, time.time() - start_time

def alfa_beta_rec(board, depth, max_depth, player, heuristic_num, alfa, beta, nodes):
    if depth >= max_depth:
        if heuristic_num == 1: return distance(board) + base(board), nodes
        elif heuristic_num == 2: return distance(board) * 8 + base_for_moves(board) * 8 + move(board), nodes
        else: return distance(board) + base(board) + wide_and_height(board), nodes
    min = float('inf')
    max = float('-inf')
    if depth >= max_depth-1:
        next_heuristics = move_heuristics(board, player, heuristic_num)
        if player == 1:
            for heuristic in next_heuristics:
                nodes += 1
                if max < heuristic: max = heuristic
                if alfa < heuristic: alfa = heuristic
                if beta < alfa: break
            return max, nodes
        else:
            for heuristic in next_heuristics:
                nodes += 1
                if min > heuristic: min = heuristic
                if beta > heuristic: beta = heuristic
                if beta < alfa: break
            return min, nodes
    next_states = move_states(board, player)
    if player == 1:
        for state in next_states:
            nodes += 1
            if is_first_player_won(state): return float('inf'), nodes
            min_max, nodes = alfa_beta_rec(state, depth+1, max_depth, 2, heuristic_num, alfa, beta, nodes)
            if max < min_max: max = min_max
            if alfa < min_max: alfa = min_max
            if beta < alfa: break
        return max, nodes
    else:
        for state in next_states:
            nodes += 1
            if is_second_player_won(state): return float('-inf'), nodes
            min_max, nodes = alfa_beta_rec(state, depth+1, max_depth, 1, heuristic_num, alfa, beta, nodes)
            if min > min_max: min = min_max
            if beta > min_max: beta = min_max
            if beta < alfa: break
        return min, nodes
