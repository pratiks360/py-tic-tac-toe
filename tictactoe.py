'''
Author: Pratik Shukla
Email: pratiks@pratiks.net
desc: python console based tic-tac-toe using 3D matrix
'''

import copy

matrix = ""
player1 = ""
player2 = ""


def printBoard():
    print(str(matrix[0][0]) + "   ||  " + str(matrix[0][1]) + "  ||  " + str(matrix[0][2]))
    print("==============")
    print(str(matrix[1][0]) + "   ||  " + str(matrix[1][1]) + "  ||  " + str(matrix[1][2]))
    print("==============")
    print(str(matrix[2][0]) + "   ||  " + str(matrix[2][1]) + "  ||  " + str(matrix[2][2]))
    print("\n\n\n")


def checkvaluepresent(location):
    if len(location) > 0:
        return False
    else:
        return True


def readinput(player):
    selection = int(input("Mr." + player.upper() + " please select position based on NUM PAD\n"))
    if selection == 1 and checkvaluepresent(matrix[2][0]):
        matrix[2][0] = player
    elif selection == 2 and checkvaluepresent(matrix[2][1]):
        matrix[2][1] = player
    elif selection == 3 and checkvaluepresent(matrix[2][2]):
        matrix[2][2] = player
    elif selection == 4 and checkvaluepresent(matrix[1][0]):
        matrix[1][0] = player
    elif selection == 5 and checkvaluepresent(matrix[1][1]):
        matrix[1][1] = player
    elif selection == 6 and checkvaluepresent(matrix[1][2]):
        matrix[1][2] = player
    elif selection == 7 and checkvaluepresent(matrix[0][0]):
        matrix[0][0] = player
    elif selection == 8 and checkvaluepresent(matrix[0][1]):
        matrix[0][1] = player
    elif selection == 9 and checkvaluepresent(matrix[0][2]):
        matrix[0][2] = player
    elif player not in ["x", "o"]:
        print("wrong input detected Mr." + player + " only select between 1-9\n")
        readinput(player)
    else:
        print("Location already booked select another location for " + player)
        readinput(player)


def selectplayers():
    global player1
    global player2
    player1 = input("SELECT x OR o FOR PLAYER 1::\n")
    if player1 == "x".lower():
        player2 = "o"
        print("Player 2 is now:: " + player2.upper())
    elif player1 == "o".lower():
        player2 = "x"
        print("Player 2 is now:: " + player2.upper())
    else:
        print("Wrong input provided\n")
        selectplayers()
    print("\n\n")


def mainGame():
    global matrix
    matrix = [["", "", ""],
              ["", "", ""],
              ["", "", ""]]
    in_progress = True

    selectplayers()

    while in_progress:
        printBoard()
        readinput(player1)
        printBoard()
        if checkwinner(player1):
            print("MR." + player1 + " wins")
            in_progress = False
            print("\n\n")
            game = input("Do you want to play another Game? Y/N\n")
            if (game == 'Y'):
                mainGame()
            else:
                break

        readinput(player2)

        printBoard()
        if checkwinner(player2):
            print("MR." + player2 + " wins")
            in_progress = False
            game = input("Do you want to play another Game? Y/N\n")
            if (game == 'Y'):
                mainGame()
            else:
                break


def checkwinner(player):
    win = False
    if checkdiagonal('L', player):
        return True
    if checkdiagonal('R', player):
        return True
    if checklines('H', player):
        return True
    if checklines('V', player):
        return True
    else:
        return win


def checkdiagonal(side, player):
    list = []
    rmatrix = copy.copy(matrix)
    rmatrix == matrix.copy()
    if side == 'R':
        rmatrix.reverse()
    for x in range(3):
        list.append(rmatrix[x][x])
    if checkifsame(list, player):
        return True


def checklines(inverse, player):
    for x in range(3):
        list = []
        for y in range(3):
            if inverse == 'V':
                list.append(matrix[y][x])
            elif inverse == 'H':
                list.append(matrix[x][y])
        if checkifsame(list, player):
            return True
            break


def checkifsame(list, player):
    # print("CALLED")
    if list.count(player) == 3:
        return True


mainGame()
