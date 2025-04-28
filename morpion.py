# morpion game

array = [[' ' for _ in range(3)] for _ in range(3)]
joueur_x = "X"
joueur_o = "O"

print(array)

def print_board():
    for row in array:
        print('|'.join(row))
        print('-' * 5)

def jouer_coup(axe_x, axe_y, joueur):
    for i in range(array):
            if axe_x == i:
                for j in range(array(i)):
                    if j == axe_y:   
                        array(j) = joueur