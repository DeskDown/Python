import math

def check_rows(mat):
    for i in range(3):
        tot = math.prod(mat[i][:])
        if tot == 1:
            return 1
        elif tot == 8:
            return 2
    return 0


def check_diagonal(mat):
    tot_1 = math.prod([mat[0][0],mat[1][1],mat[2][2]])
    tot_2 = math.prod([mat[0][2],mat[1][1],mat[2][0]])
    if 1 in [tot_1,tot_2]:
        return 1
    elif 8 in [tot_1,tot_2]:
        return 2
        
    return 0


def check_collumns(mat):
    for i in range(3):
        tot = math.prod([row[i] for row in mat])
        if tot == 1:
            return 1
        elif tot == 8:
            return 2
    return 0


def find_winner(mat):
    r = check_rows(mat)
    if r:
        return r
    d = check_diagonal(mat)
    if d:
        return d
    c = check_collumns(mat)
    if c:
        return c
    return 0


def print_board(mat):
    header_footer = "-"*9 
    print(header_footer)
    for row in mat:
        str_row = [str(r) for r in row]
        print(f"| {' '.join(str_row)} |")
    print(header_footer)
    

def get_input(user, mat):
    inp = str(input(f"user {user} pick the place: (row,col)")).strip()
    r, c = int(inp[0]) - 1, int(inp[-1]) - 1
    if r not in (0,1,2) or c not in (0,1,2) or mat[r][c] != 0:
        print("Place not available, try again")
        return get_input(user, mat)
    return r, c


def fill_board(mat):
    space = 9
    turn = 2
    while space and not find_winner(mat):
        if turn == 1:
            turn = 2
        else:
            turn = 1
        print_board(mat)
        r, c = get_input(turn, mat)
        mat[r][c] = turn
        space -= 1

    return mat


if __name__ == "__main__":
    game_board = [[0, 0, 0],[0,0, 0],[0, 0, 0]]
    game_board = fill_board(game_board)
    winner = find_winner(game_board)
    if not winner:
        print("Tie!")
    else:
        print(f"winner is user: {winner}")
    print_board(game_board)
