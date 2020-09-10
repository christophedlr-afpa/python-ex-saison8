x: int = 0
y: int = 0
move: int = 0
checkerBoard: int = [[0 for i in range(8)] for j in range(8)]

x = int(input("Indiquez une ligne où vous positionner : "))
y = int(input("Indiquez une colonne où vous positionner : "))

checkerBoard[x][y] = 1

if move == 0 and (x < 0 or x > 8) and (y < 0 or y > 8):
    print("Position invalide")
else:
    while True:
        move = int(input("Indiquez le mouvement (0 => haut-gauche, 1 => haut-droite, 2 => bas-gauche, 3 => bas-droite) : "))

        # Validation of move
        if move == 0 and ( (x-1 <= 8 and x-1 >= 0) and (y-1 >= 0 and y-1 <= 8) ):
            checkerBoard[x][y] = 0
            x -= 1
            y -= 1
            checkerBoard[x][y] = 1
        elif move == 1 and ( (x-1 <= 8 and x-1 >= 0) and (y+1 <= 8 and y+1 >= 0) ):
            checkerBoard[x][y] = 0
            x -= 1
            y += 1
            checkerBoard[x][y] = 1
        elif move == 2 and ( (x+1 >= 0 and x+1 <= 8) and (y-1 >= 0 and y-1 <= 8) ):
            checkerBoard[x][y] = 0
            x += 1
            y -= 1
            checkerBoard[x][y] = 1
        elif move == 3 and ( (x+1 >= 0 and x+1 <= 8) and (y+1 <= 8 and y+1 >= 0) ):
            checkerBoard[x][y] = 0
            x += 1
            y += 1
            checkerBoard[x][y] = 1
        else:
            print("Déplacement impossible")
            break

        # Draw checkerboard
        for i in range(0, 8):
            for j in range(0, 8):
                if checkerBoard[i][j] == 0:
                    if j < 7:
                        print("O", end = '')
                    else:
                        print("O")
                if checkerBoard[i][j] == 1:
                    if j < 7:
                        print("X", end = '')
                    else:
                        print("X")
