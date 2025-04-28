# morpion game

array = [[' ' for _ in range(3)] for _ in range(3)]

print(array)

def print_board():
    for row in array:
        print('|'.join(row))
        print('-' * 5)