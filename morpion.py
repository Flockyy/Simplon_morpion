# morpion game

array = [[' ' for _ in range(3)] for _ in range(3)]

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

def check_is_full():
    for row in array:
        if ' ' in row:
            return False
    return True

def play(axe_x, axe_y, joueur):
    if check_valid_move(axe_x, axe_y):
        array[axe_x][axe_y] = joueur
    else:
        print("Case déjà occupée, rejouez.")

def check_winner():
    # Check rows
    for row in array:
        if row[0] == row[1] == row[2] != ' ':
            return True

    # Check columns
    for col in range(3):
        if array[0][col] == array[1][col] == array[2][col] != ' ':
            return True

    # Check diagonals
    if array[0][0] == array[1][1] == array[2][2] != ' ':
        return True
    if array[0][2] == array[1][1] == array[2][0] != ' ':
        return True

    return False

def main():
    print("Welcome to Morpion!")
    print_board()

    current_player = joueur_x

    while True:
        
        valid_move = False
        
        while not valid_move:
            try:
                axe_x = int(input(f"Player {current_player}, enter row (0-2): "))
                axe_y = int(input(f"Player {current_player}, enter column (0-2): "))
                valid_move = check_valid_move(axe_x, axe_y)
            except ValueError:
                print("Invalid input. Please enter numbers between 0 and 2.")
                continue
            
        play(axe_x, axe_y, current_player)

        print_board()

        if check_winner():
            print(f"Player {current_player} wins!")
            break

        if check_is_full():
            print("It's a draw!")
            break

        current_player = joueur_o if current_player == joueur_x else joueur_x
        
if __name__ == "__main__":
    main()
