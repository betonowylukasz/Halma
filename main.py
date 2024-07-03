import sys
from halma import move_states, is_first_player_won, is_second_player_won, copy_list_in_list
from algorithms import minimax, alfa_beta
from colorama import Fore, Style
from heuristic import move, wide_and_height

def read_input():
    board = []
    for _ in range(16):
        row = list(map(int, input().split()))
        board.append(row)
    return board

def print_board(board):
    for row in board:
        print(' '.join(map(str, row)), file=sys.stdout)

def print_diff_board(prev_board, curr_board):
    for prev_row, curr_row in zip(prev_board, curr_board):
        row_output = ''
        for prev_square, curr_square in zip(prev_row, curr_row):
            if prev_square == curr_square:
                row_output += f"{curr_square} "
            else:
                row_output += f"{Fore.YELLOW}{curr_square}{Style.RESET_ALL} "
        print(row_output.strip(), file=sys.stdout)


def game_manager(board, name, depth, algorithm, heuristic1, heuristic2):
    round = 1
    while round <= 200:
        print()
        new_board, nodes, time = algorithm(board, depth, 1, heuristic1)
        with open(name, 'a') as file:
            file.write(str(nodes))
            file.write(', '+ str(time))
            file.write("\n")
        print(f"Liczba odwiedzonych węzłów: {nodes}", file=sys.stderr)
        print(f"Czas działania algorytmu: {time} sekund", file=sys.stderr)
        print_diff_board(board, new_board)
        board = new_board
        if is_first_player_won(board):
            print(f"Runda {round}     Wygrywa gracz numer 1!")
            break
        else: print(f"Runda {round}")
        print()
        new_board, nodes, time = algorithm(board, depth, 2, heuristic2)
        with open(name, 'a') as file:
            file.write(str(nodes))
            file.write(', '+ str(time))
            file.write("\n")
        print(f"Liczba odwiedzonych wezlow: {nodes}", file=sys.stderr)
        print(f"Czas dzialania algorytmu: {time} sekund", file=sys.stderr)
        print_diff_board(board, new_board)
        board = new_board
        if is_second_player_won(board):
            print(f"Runda {round}     Wygrywa gracz numer 2!")
            break
        else: print(f"Runda {round}")
        round += 1

def game_manager2(board, name, depth, algorithm, heuristic1, heuristic2):
    round = 1
    while round <= 200:
        print()
        new_board, nodes, time = algorithm(board, depth, 1, heuristic1)
        print(f"Liczba odwiedzonych węzłów: {nodes}", file=sys.stderr)
        print(f"Czas działania algorytmu: {time} sekund", file=sys.stderr)
        print_diff_board(board, new_board)
        board = new_board
        if is_first_player_won(board):
            with open(name, 'a') as file:
                file.write(str(heuristic1))
                file.write("\n")
            print(f"Runda {round}     Wygrywa gracz numer 1!")
            break
        else: print(f"Runda {round}")
        print()
        new_board, nodes, time = algorithm(board, depth, 2, heuristic2)
        print(f"Liczba odwiedzonych wezlow: {nodes}", file=sys.stderr)
        print(f"Czas dzialania algorytmu: {time} sekund", file=sys.stderr)
        print_diff_board(board, new_board)
        board = new_board
        if is_second_player_won(board):
            with open(name, 'a') as file:
                file.write(str(heuristic2))
                file.write("\n")
            print(f"Runda {round}     Wygrywa gracz numer 2!")
            break
        else: print(f"Runda {round}")
        round += 1



if __name__ == "__main__":
    print("Podaj plansze 16x16 (1 - gracz pierwszy, 2 - gracz drugi, 0 - pole puste):")
    board = read_input()
    print()
    print("Wczytana plansza:")
    print_board(board)
    print()
    game_manager(copy_list_in_list(board), "trash.txt", 3, alfa_beta, 1, 3)
    # # for _ in range(5):
    # #     game_manager(copy_list_in_list(board), "depth1minimax.txt", 1, minimax, 1, 1)
    # #     game_manager(copy_list_in_list(board), "depth2minimax.txt", 2, minimax, 1, 1)
    # #     game_manager(copy_list_in_list(board), "depth1alfabeta.txt", 1, alfa_beta, 1, 1)
    # #     game_manager(copy_list_in_list(board), "depth2alfabeta.txt", 2, alfa_beta, 1, 1)
    # #     game_manager(copy_list_in_list(board), "depth3alfabeta.txt", 3, alfa_beta, 1, 1)
    # for _ in range(3):
    #    game_manager(copy_list_in_list(board), "depth3minimax.txt", 3, minimax, 1, 1)
    #    game_manager(copy_list_in_list(board), "depth4alfabeta.txt", 4, alfa_beta, 1, 1)
    # for _ in range(5):
    #     game_manager2(copy_list_in_list(board), "first_vs_third.txt", 1, alfa_beta, 1, 3)
    #     game_manager2(copy_list_in_list(board), "first_vs_third.txt", 1, alfa_beta, 3, 1)
    #     game_manager2(copy_list_in_list(board), "first_vs_third.txt", 2, alfa_beta, 1, 3)
    #     game_manager2(copy_list_in_list(board), "first_vs_third.txt", 2, alfa_beta, 3, 1)
    #     game_manager2(copy_list_in_list(board), "first_vs_third.txt", 3, alfa_beta, 1, 3)
    #     game_manager2(copy_list_in_list(board), "first_vs_third.txt", 3, alfa_beta, 3, 1)
    # for _ in range(4):
    #     game_manager2(copy_list_in_list(board), "first_vs_second.txt", 1, alfa_beta, 1, 2)
    #     game_manager2(copy_list_in_list(board), "first_vs_second.txt", 1, alfa_beta, 2, 1)
    #     game_manager2(copy_list_in_list(board), "first_vs_second.txt", 2, alfa_beta, 1, 2)
    #     game_manager2(copy_list_in_list(board), "first_vs_second.txt", 2, alfa_beta, 2, 1)
    #    game_manager2(copy_list_in_list(board), "first_vs_second.txt", 3, alfa_beta, 1, 2)
    #    game_manager2(copy_list_in_list(board), "first_vs_second.txt", 3, alfa_beta, 2, 1)
    # for _ in range(5):
    #     game_manager2(copy_list_in_list(board), "second_vs_third.txt", 1, alfa_beta, 2, 3)
    #     game_manager2(copy_list_in_list(board), "second_vs_third.txt", 1, alfa_beta, 3, 2)
    #     game_manager2(copy_list_in_list(board), "second_vs_third.txt", 2, alfa_beta, 2, 3)
    #     game_manager2(copy_list_in_list(board), "second_vs_third.txt", 2, alfa_beta, 3, 2)
    #   game_manager2(copy_list_in_list(board), "second_vs_third.txt", 3, alfa_beta, 2, 3)
    #   game_manager2(copy_list_in_list(board), "second_vs_third.txt", 3, alfa_beta, 3, 2)
    # for _ in range(5):
    #     game_manager(copy_list_in_list(board), "depth1second.txt", 1, alfa_beta, 2, 2)
    #     game_manager(copy_list_in_list(board), "depth2second.txt", 2, alfa_beta, 2, 2)
    #     game_manager(copy_list_in_list(board), "depth1third.txt", 1, alfa_beta, 3, 3)
    #     game_manager(copy_list_in_list(board), "depth2third.txt", 2, alfa_beta, 3, 3)
    #    game_manager(copy_list_in_list(board), "depth3second.txt", 3, alfa_beta, 2, 2)
    # for _ in range(5):
    #     game_manager(copy_list_in_list(board), "depth1third.txt", 1, alfa_beta, 3, 3)
    #     game_manager(copy_list_in_list(board), "depth2third.txt", 2, alfa_beta, 3, 3)
    #     game_manager(copy_list_in_list(board), "depth3third.txt", 3, alfa_beta, 3, 3)



