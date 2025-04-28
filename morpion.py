# morpion game

array = [[' ' for _ in range(3)] for _ in range(3)]
joueur_x = "X"
joueur_o = "O"

joueur_x = "X"
joueur_o = "O"

def check_valid_move(x, y):
    if x < 0 or x > 2 or y < 0 or y > 2:
        print("Invalid move: out of bounds")
        return False
    if array[x][y] != ' ':
        print("Invalid move: cell already occupied")
        return False
    print("Valid move")
    return True


def print_board():
    for row in array:
        print('|'.join(row))
        print('-' * 5)

def jouer_coup(axe_x, axe_y, joueur):
    if array[axe_x][axe_y] == ' ':
        array[axe_x][axe_y] = joueur
    else:
        print("Case déjà occupée, rejouez.")

print_board()
check_valid_move(4, 4)

print_board()
check_valid_move(4, 4)
