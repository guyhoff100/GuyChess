import pygame
from enum import Enum
import tryout

remove_worker(worker_socket,
              (client_socket, content_img, style_img, num_iter))
    """
    |SERVER >>  [content_image]<EOF>

# Definitions
LEFT = 1
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
LIGHT = (232, 235, 239)
DARK = (125, 135, 150)
BLUE = (0, 64, 255)
PINK = (255, 105, 180)
YELLOW = (255, 255, 0)
PURPLE = (148, 0, 211)
pygame.font.init()
largeText = pygame.font.Font('freesansbold.ttf', 15)
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 90
HEIGHT = 90

# This sets the margin between each cell
MARGIN = 1


class Piece(Enum):
    Empty = 0
    BPawn = 1
    BKing = 2
    BQueen = 3
    BBishop = 4
    BKnight = 5
    BRook = 6
    WPawn = -1
    WKing = -2
    WQueen = -3
    WBishop = -4
    WKnight = -5
    WRook = -6


def main():
    global MAT_W
    MAT_W = False
    global MAT_B
    MAT_B = False
    global WAS_W
    WAS_W = False
    global WAS_B
    WAS_B = False
    global WAS_EMPTY
    WAS_EMPTY = False
    global KING_SAFE
    KING_SAFE = True
    global PICK
    PICK = False
    global WAS_ROW
    WAS_ROW = 0
    global WAS_COLUMN
    WAS_COLUMN = 0
    global W_TURN
    W_TURN = True
    global KING_X
    KING_X = 0
    global KING_Y
    KING_Y = 0
    global grid
    grid = []
    global arrange
    arrange = []
    global temp
    temp = []
    global temp1
    temp1 = []
    global board
    board = [[Piece.BBishop, Piece.BKnight, Piece.BRook, Piece.BQueen,
              Piece.BKing, Piece.BRook, Piece.BKnight, Piece.BBishop],
             [Piece.BPawn, Piece.BPawn, Piece.BPawn, Piece.BPawn,
              Piece.BPawn, Piece.BPawn, Piece.BPawn, Piece.BPawn],
             [Piece.Empty, Piece.Empty, Piece.Empty, Piece.Empty,
              Piece.Empty, Piece.Empty, Piece.Empty, Piece.Empty],
             [Piece.Empty, Piece.Empty, Piece.Empty, Piece.Empty,
              Piece.Empty, Piece.Empty, Piece.Empty, Piece.Empty],
             [Piece.Empty, Piece.Empty, Piece.Empty, Piece.Empty,
              Piece.Empty, Piece.Empty, Piece.Empty, Piece.Empty],
             [Piece.Empty, Piece.Empty, Piece.Empty, Piece.Empty,
              Piece.Empty, Piece.Empty, Piece.Empty, Piece.Empty],
             [Piece.WPawn, Piece.WPawn, Piece.WPawn, Piece.WPawn,
              Piece.WPawn, Piece.WPawn, Piece.WPawn, Piece.WPawn],
             [Piece.WBishop, Piece.WKnight, Piece.WRook, Piece.WQueen,
              Piece.WKing, Piece.WRook, Piece.WKnight, Piece.WBishop]]

    for row in range(8):
        # Add an empty array that will hold each cell
        # in this row
        grid.append([])
        for column in range(8):
            grid[row].append(0)  # Append a cell

    # init the grid
    for x in range(8):
        for y in range(8):
            if board[x][y].value == 0:
                grid[x][y] = 0
            if board[x][y].value > 0:
                grid[x][y] = 1
            if board[x][y].value < 0:
                grid[x][y] = 2

    # tryout

    # end of tryout

    for row in range(8):
        # Add an empty array that will hold each cell
        # in this row
        arrange.append([])
        for column in range(8):
            arrange[row].append(0)  # Append a cell

    for row in range(8):
        # Add an empty array that will hold each cell
        # in this row
        temp.append([])
        for column in range(8):
            temp[row].append(0)  # Append a cell

    for row in range(8):
        # Add an empty array that will hold each cell
        # in this row
        temp1.append([])
        for column in range(8):
            temp1[row].append(0)  # Append a cell

    for row in range(8):
        for column in range(8):
            arrange[row][column] = grid[row][column]

    # Initialize pygame
    pygame.init()

    # Set the HEIGHT and WIDTH of the screen
    WINDOW_SIZE = [720, 720]
    global screen
    screen = pygame.display.set_mode(WINDOW_SIZE)

    # Set title of screen
    pygame.display.set_caption("Guy Chess")

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    global clock
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
            # changing the screen size - need to be checked !!
            # elif event.type==VIDEORESIZE:
            # screen=pygame.display.set_mode(event.dict['size'],HWSURFACE|DOUBLEBUF|RESIZABLE)
            # screen.blit(pygame.transform.scale(pic,event.dict['size']),(0,0))

            # meaning of numbers:

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                # User clicks the mouse. Get the position
                pos = pygame.mouse.get_pos()
                # Change the x/y screen coordinates to grid coordinates
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                for x in range(8):
                    for y in range(8):
                        if grid[x][y] == 3:
                            grid[x][y] = 3
                        if grid[x][y] == 4:
                            grid[x][y] = 4

                        else:
                            grid[x][y] = arrange[x][y]
                if row > 7 or column > 7:
                    break
                else:
                    if grid[row][column] == 4:
                        if W_TURN:
                            # make a grid save
                            for x in range(8):
                                for y in range(8):
                                    grid[x][y] = arrange[x][y]
                            # find the white king's place
                            for x in range(8):
                                for y in range(8):
                                    if board[x][y] == Piece(-2):
                                        KING_X = x
                                        KING_Y = y
                                        break
                            # check if the white is in chess
                            check_black(KING_X, KING_Y)
                            if grid[KING_X][KING_Y] == 6:
                                # grid recoil
                                for x in range(8):
                                    for y in range(8):
                                        grid[x][y] = arrange[x][y]
                                # arrange and board save
                                for x in range(8):
                                    for y in range(8):
                                        temp[x][y] = arrange[x][y]
                                        temp1[x][y] = board[x][y]
                                # making the move
                                arrange[row][column] = arrange[WAS_ROW][WAS_COLUMN]
                                arrange[WAS_ROW][WAS_COLUMN] = 0
                                board[row][column] = board[WAS_ROW][WAS_COLUMN]
                                board[WAS_ROW][WAS_COLUMN] = Piece(0)
                                grid[row][column] = arrange[row][column]
                                grid[WAS_ROW][WAS_COLUMN] = 0
                                for x in range(8):
                                    for y in range(8):
                                        grid[x][y] = arrange[x][y]
                                for x in range(8):
                                    for y in range(8):
                                        if board[x][y] == Piece(-2):
                                            KING_X = x
                                            KING_Y = y
                                            break
                                check_black(KING_X, KING_Y)
                                if grid[KING_X][KING_Y] == 6:
                                    for x in range(8):
                                        for y in range(8):
                                            arrange[x][y] = temp[x][y]
                                            grid[x][y] = arrange[x][y]
                                            board[x][y] = temp1[x][y]
                                    break
                            else:
                                # recoil the grid
                                for x in range(8):
                                    for y in range(8):
                                        grid[x][y] = arrange[x][y]
                                # make the move
                                for x in range(8):
                                    for y in range(8):
                                        temp[x][y] = arrange[x][y]
                                        temp1[x][y] = board[x][y]
                                arrange[row][column] = arrange[WAS_ROW][WAS_COLUMN]
                                arrange[WAS_ROW][WAS_COLUMN] = 0
                                board[row][column] = board[WAS_ROW][WAS_COLUMN]
                                board[WAS_ROW][WAS_COLUMN] = Piece(0)
                                grid[row][column] = arrange[row][column]
                                grid[WAS_ROW][WAS_COLUMN] = 0
                                for x in range(8):
                                    for y in range(8):
                                        grid[x][y] = arrange[x][y]
                                # after the move, am i in chess?
                                for x in range(8):
                                    for y in range(8):
                                        if board[x][y] == Piece(-2):
                                            KING_X = x
                                            KING_Y = y
                                            break
                                check_black(KING_X, KING_Y)
                                if grid[KING_X][KING_Y] == 6:
                                    for x in range(8):
                                        for y in range(8):
                                            arrange[x][y] = temp[x][y]
                                            grid[x][y] = arrange[x][y]
                                            board[x][y] = temp1[x][y]
                                    break
                                for x in range(8):
                                    for y in range(8):
                                        grid[x][y] = arrange[x][y]
                                # finding black king
                                for x in range(8):
                                    for y in range(8):
                                        if board[x][y] == Piece(2):
                                            KING_X = x
                                            KING_Y = y
                                            break
                                # did i attacked the black king?
                                check_white(KING_X, KING_Y)
                                if grid[KING_X][KING_Y] == 8:
                                    # can he protect himself
                                    neighbors = [
                                        grid[KING_X + dx][KING_Y + dy]
                                        for dx in [0, 1, -1]
                                        for dy in [0, 1, -1]
                                        if (dx != 0 or dy != 0) and (0 <= KING_X + dx <= 7) \
                                           and (0 <= KING_Y + dy <= 7)
                                    ]
                                    print "kapara"
                                    printMat()
                                    print "Careless"
                                    print len(neighbors)
                                    for i in neighbors:
                                        print i
                                    print "whisper"
                                    if all(ans in (7, 8, 1, 2, 10) for ans in neighbors):
                                        print "son"
                                        for x in range(8):
                                            for y in range(8):
                                                if grid[x][y] != 10:
                                                    grid[x][y] = arrange[x][y]
                                        if (check_b_mat()):
                                            print "mat"
                                            MAT_W = True
                                            mat()

                        if not W_TURN:
                            # make a grid save
                            for x in range(8):
                                for y in range(8):
                                    grid[x][y] = arrange[x][y]
                            # find the white king's place
                            for x in range(8):
                                for y in range(8):
                                    if board[x][y] == Piece(2):
                                        KING_X = x
                                        KING_Y = y
                                        break
                            # check if the white is in chess
                            check_white(KING_X, KING_Y)
                            if grid[KING_X][KING_Y] == 8:
                                # grid recoil
                                for x in range(8):
                                    for y in range(8):
                                        grid[x][y] = arrange[x][y]
                                # arrange and board save
                                for x in range(8):
                                    for y in range(8):
                                        temp[x][y] = arrange[x][y]
                                        temp1[x][y] = board[x][y]
                                # making the move
                                arrange[row][column] = arrange[WAS_ROW][WAS_COLUMN]
                                arrange[WAS_ROW][WAS_COLUMN] = 0
                                board[row][column] = board[WAS_ROW][WAS_COLUMN]
                                board[WAS_ROW][WAS_COLUMN] = Piece(0)
                                grid[row][column] = arrange[row][column]
                                grid[WAS_ROW][WAS_COLUMN] = 0
                                for x in range(8):
                                    for y in range(8):
                                        grid[x][y] = arrange[x][y]
                                for x in range(8):
                                    for y in range(8):
                                        if board[x][y] == Piece(2):
                                            KING_X = x
                                            KING_Y = y
                                            break
                                check_white(KING_X, KING_Y)
                                if grid[KING_X][KING_Y] == 8:
                                    for x in range(8):
                                        for y in range(8):
                                            arrange[x][y] = temp[x][y]
                                            grid[x][y] = arrange[x][y]
                                            board[x][y] = temp1[x][y]
                                    break
                            else:
                                # im not in chess
                                # recoil the grid
                                for x in range(8):
                                    for y in range(8):
                                        grid[x][y] = arrange[x][y]
                                # make the move
                                for x in range(8):
                                    for y in range(8):
                                        temp[x][y] = arrange[x][y]
                                        temp1[x][y] = board[x][y]
                                arrange[row][column] = arrange[WAS_ROW][WAS_COLUMN]
                                arrange[WAS_ROW][WAS_COLUMN] = 0
                                board[row][column] = board[WAS_ROW][WAS_COLUMN]
                                board[WAS_ROW][WAS_COLUMN] = Piece(0)
                                grid[row][column] = arrange[row][column]
                                grid[WAS_ROW][WAS_COLUMN] = 0
                                for x in range(8):
                                    for y in range(8):
                                        grid[x][y] = arrange[x][y]
                                # after the move, am i in chess?
                                for x in range(8):
                                    for y in range(8):
                                        if board[x][y] == Piece(2):
                                            KING_X = x
                                            KING_Y = y
                                            break
                                check_white(KING_X, KING_Y)
                                print "kuson"
                                printMat()
                                if grid[KING_X][KING_Y] == 8:
                                    for x in range(8):
                                        for y in range(8):
                                            arrange[x][y] = temp[x][y]
                                            grid[x][y] = arrange[x][y]
                                            board[x][y] = temp1[x][y]
                                    break
                                for x in range(8):
                                    for y in range(8):
                                        grid[x][y] = arrange[x][y]
                                # finding black king
                                for x in range(8):
                                    for y in range(8):
                                        if board[x][y] == Piece(-2):
                                            KING_X = x
                                            KING_Y = y
                                            break
                                # did i attacked the black king?
                                check_black(KING_X, KING_Y)
                                if grid[KING_X][KING_Y] == 6:
                                    # can he protect himself
                                    neighbors = [
                                        grid[KING_X + dx][KING_Y + dy]
                                        for dx in [0, 1, -1]
                                        for dy in [0, 1, -1]
                                        if (dx != 0 or dy != 0) and (0 <= KING_X + dx <= 7) \
                                           and (0 <= KING_Y + dy <= 7)
                                    ]
                                    if all(ans in (5, 6, 1, 2, 10) for ans in neighbors):
                                        print "son1"
                                        for x in range(8):
                                            for y in range(8):
                                                if grid[x][y] != 10:
                                                    grid[x][y] = arrange[x][y]
                                        if (check_w_mat()):
                                            print "mat"
                                            MAT_B = True
                                            mat()

                        for x in range(8):
                            for y in range(8):
                                grid[x][y] = arrange[x][y]
                        W_TURN = not W_TURN
                        printMat()
                        break
                    if grid[row][column] == 3:
                        for x in range(8):
                            for y in range(8):
                                grid[x][y] = arrange[x][y]
                        break
                    if grid[row][column] == 0 or grid[row][column] == 1 or grid[row][column] == 2:
                        for x in range(8):
                            for y in range(8):
                                if grid[x][y] == 4:
                                    grid[x][y] = arrange[x][y]
                        WAS_ROW = row
                        WAS_COLUMN = column
                        grid[row][column] = 3
                    # insert king threat func?

                    # insert func to find which piece
                    if board[row][column] != Piece.Empty:
                        if not W_TURN:
                            # black pawn - CHECKED
                            if board[row][column] == Piece(1):
                                if row + 1 < 8:
                                    if row == 1:
                                        if grid[row + 1][column] == 0:
                                            if grid[row + 2][column] == 0:
                                                grid[row + 2][column] = 4
                                    if grid[row + 1][column] == 0:
                                        grid[row + 1][column] = 4
                                    if column + 1 < 8:
                                        if grid[row + 1][column + 1] == 2:
                                            grid[row + 1][column + 1] = 4
                                    if column - 1 > -1:
                                        if grid[row + 1][column - 1] == 2:
                                            grid[row + 1][column - 1] = 4

                            # black king - CHECKED
                            if board[row][column] == Piece(2):
                                if row + 1 < 8:
                                    if column + 1 < 8:
                                        if grid[row + 1][column + 1] == 2 or grid[row + 1][column + 1] == 0:
                                            grid[row + 1][column + 1] = 4
                                    if column - 1 > -1:
                                        if grid[row + 1][column - 1] == 2 or grid[row + 1][column - 1] == 0:
                                            grid[row + 1][column - 1] = 4
                                    if grid[row + 1][column] == 2 or grid[row + 1][column] == 0:
                                        grid[row + 1][column] = 4
                                if row - 1 > -1:
                                    if column - 1 > -1:
                                        if grid[row - 1][column - 1] == 2 or grid[row - 1][column - 1] == 0:
                                            grid[row - 1][column - 1] = 4
                                    if column + 1 < 8:
                                        if grid[row - 1][column + 1] == 2 or grid[row - 1][column + 1] == 0:
                                            grid[row - 1][column + 1] = 4
                                    if grid[row - 1][column] == 2 or grid[row - 1][column] == 0:
                                        grid[row - 1][column] = 4
                                if column + 1 < 8:
                                    if grid[row][column + 1] == 2 or grid[row][column + 1] == 0:
                                        grid[row][column + 1] = 4
                                if column - 1 > -1:
                                    if grid[row][column - 1] == 2 or grid[row][column - 1] == 0:
                                        grid[row][column - 1] = 4
                            # Black knight - CHECKED
                            if board[row][column] == Piece(5):
                                if row - 2 in range(8):
                                    if column + 1 in range(8):
                                        if grid[row - 2][column + 1] == 0 or grid[row - 2][column + 1] == 2:
                                            grid[row - 2][column + 1] = 4
                                if row - 2 in range(8):
                                    if column - 1 in range(8):
                                        if grid[row - 2][column - 1] == 0 or grid[row - 2][column - 1] == 2:
                                            grid[row - 2][column - 1] = 4
                                if row + 2 in range(8):
                                    if column + 1 in range(8):
                                        if grid[row + 2][column + 1] == 0 or grid[row + 2][column + 1] == 2:
                                            grid[row + 2][column + 1] = 4
                                if row + 2 in range(8):
                                    if column - 1 in range(8):
                                        if grid[row + 2][column - 1] == 0 or grid[row + 2][column - 1] == 2:
                                            grid[row + 2][column - 1] = 4
                                if row - 1 in range(8):
                                    if column + 2 in range(8):
                                        if grid[row - 1][column + 2] == 0 or grid[row - 1][column + 2] == 2:
                                            grid[row - 1][column + 2] = 4
                                if row - 1 in range(8):
                                    if column - 2 in range(8):
                                        if grid[row - 1][column - 2] == 0 or grid[row - 1][column - 2] == 2:
                                            grid[row - 1][column - 2] = 4
                                if row + 1 in range(8):
                                    if column + 2 in range(8):
                                        if grid[row + 1][column + 2] == 0 or grid[row + 1][column + 2] == 2:
                                            grid[row + 1][column + 2] = 4
                                if row + 1 in range(8):
                                    if column - 2 in range(8):
                                        if grid[row + 1][column - 2] == 0 or grid[row + 1][column - 2] == 2:
                                            grid[row + 1][column - 2] = 4
                            # Black Bishop
                            if board[row][column] == Piece(4):
                                for i in range(row + 1, 8):
                                    if grid[i][column] == 1:
                                        break
                                    if grid[i][column] == 2:
                                        grid[i][column] = 4
                                        break
                                    grid[i][column] = 4
                                for i in range(row - 1, -1, -1):
                                    if grid[i][column] == 1:
                                        break
                                    if grid[i][column] == 2:
                                        grid[i][column] = 4
                                        break
                                    grid[i][column] = 4
                                for i in range(column + 1, 8):
                                    if grid[row][i] == 1:
                                        break
                                    if grid[row][i] == 2:
                                        grid[row][i] = 4
                                        break
                                    grid[row][i] = 4
                                for i in range(column - 1, -1, -1):
                                    if grid[row][i] == 1:
                                        break
                                    if grid[row][i] == 2:
                                        grid[row][i] = 4
                                        break
                                    grid[row][i] = 4
                            # black rook
                            if board[row][column] == Piece(6):
                                x = row + 1
                                y = column + 1
                                while x < 8 and y < 8:
                                    if grid[x][y] == 1:
                                        break
                                    if grid[x][y] == 2:
                                        grid[x][y] = 4
                                        break
                                    if grid[x][y] == 0:
                                        grid[x][y] = 4
                                        x += 1
                                        y += 1
                                x = row - 1
                                y = column - 1
                                while x > -1 and y > -1:
                                    if grid[x][y] == 1:
                                        break
                                    if grid[x][y] == 2:
                                        grid[x][y] = 4
                                        break
                                    if grid[x][y] == 0:
                                        grid[x][y] = 4
                                        x -= 1
                                        y -= 1
                                x = row + 1
                                y = column - 1
                                while x < 8 and y > -1:
                                    if grid[x][y] == 1:
                                        break
                                    if grid[x][y] == 2:
                                        grid[x][y] = 4
                                        break
                                    if grid[x][y] == 0:
                                        grid[x][y] = 4
                                        x += 1
                                        y -= 1
                                x = row - 1
                                y = column + 1
                                while y < 8 and x > -1:
                                    if grid[x][y] == 1:
                                        break
                                    if grid[x][y] == 2:
                                        grid[x][y] = 4
                                        break
                                    if grid[x][y] == 0:
                                        grid[x][y] = 4
                                        x -= 1
                                        y += 1
                            # black queen
                            if board[row][column] == Piece(3):
                                for i in range(row + 1, 8):
                                    if grid[i][column] == 1:
                                        break
                                    if grid[i][column] == 2:
                                        grid[i][column] = 4
                                        break
                                    grid[i][column] = 4
                                for i in range(row - 1, -1, -1):
                                    if grid[i][column] == 1:
                                        break
                                    if grid[i][column] == 2:
                                        grid[i][column] = 4
                                        break
                                    grid[i][column] = 4
                                for i in range(column + 1, 8):
                                    if grid[row][i] == 1:
                                        break
                                    if grid[row][i] == 2:
                                        grid[row][i] = 4
                                        break
                                    grid[row][i] = 4
                                for i in range(column - 1, -1, -1):
                                    if grid[row][i] == 1:
                                        break
                                    if grid[row][i] == 2:
                                        grid[row][i] = 4
                                        break
                                    grid[row][i] = 4
                                x = row + 1
                                y = column + 1
                                while x < 8 and y < 8:
                                    if grid[x][y] == 1:
                                        break
                                    if grid[x][y] == 2:
                                        grid[x][y] = 4
                                        break
                                    if grid[x][y] == 0:
                                        grid[x][y] = 4
                                        x += 1
                                        y += 1
                                x = row - 1
                                y = column - 1
                                while x > -1 and y > -1:
                                    if grid[x][y] == 1:
                                        break
                                    if grid[x][y] == 2:
                                        grid[x][y] = 4
                                        break
                                    if grid[x][y] == 0:
                                        grid[x][y] = 4
                                        x -= 1
                                        y -= 1
                                x = row + 1
                                y = column - 1
                                while x < 8 and y > -1:
                                    if grid[x][y] == 1:
                                        break
                                    if grid[x][y] == 2:
                                        grid[x][y] = 4
                                        break
                                    if grid[x][y] == 0:
                                        grid[x][y] = 4
                                        x += 1
                                        y -= 1
                                x = row - 1
                                y = column + 1
                                while y < 8 and x > -1:
                                    if grid[x][y] == 1:
                                        break
                                    if grid[x][y] == 2:
                                        grid[x][y] = 4
                                        break
                                    if grid[x][y] == 0:
                                        grid[x][y] = 4
                                        x -= 1
                                        y += 1
                    # white pieces
                    if board[row][column] != Piece.Empty:
                        if W_TURN:
                            # white pawn - CHECKED
                            if board[row][column] == Piece(-1):
                                if row - 1 > -1:
                                    if row == 6:
                                        if grid[row - 1][column] == 0:
                                            if grid[row - 2][column] == 0:
                                                grid[row - 2][column] = 4
                                    if grid[row - 1][column] == 0:
                                        grid[row - 1][column] = 4
                                    if column + 1 < 8:
                                        if grid[row - 1][column + 1] == 1:
                                            grid[row - 1][column + 1] = 4
                                    if column - 1 > -1:
                                        if grid[row - 1][column - 1] == 1:
                                            grid[row - 1][column - 1] = 4

                            # White knight - CHECKED
                            if board[row][column] == Piece(-5):
                                if row - 2 in range(8):
                                    if column + 1 in range(8):
                                        if grid[row - 2][column + 1] == 0 or grid[row - 2][column + 1] == 1:
                                            grid[row - 2][column + 1] = 4
                                if row - 2 in range(8):
                                    if column - 1 in range(8):
                                        if grid[row - 2][column - 1] == 0 or grid[row - 2][column - 1] == 1:
                                            grid[row - 2][column - 1] = 4
                                if row + 2 in range(8):
                                    if column + 1 in range(8):
                                        if grid[row + 2][column + 1] == 0 or grid[row + 2][column + 1] == 1:
                                            grid[row + 2][column + 1] = 4
                                if row + 2 in range(8):
                                    if column - 1 in range(8):
                                        if grid[row + 2][column - 1] == 0 or grid[row + 2][column - 1] == 1:
                                            grid[row + 2][column - 1] = 4
                                if row - 1 in range(8):
                                    if column + 2 in range(8):
                                        if grid[row - 1][column + 2] == 0 or grid[row - 1][column + 2] == 1:
                                            grid[row - 1][column + 2] = 4
                                if row - 1 in range(8):
                                    if column - 2 in range(8):
                                        if grid[row - 1][column - 2] == 0 or grid[row - 1][column - 2] == 1:
                                            grid[row - 1][column - 2] = 4
                                if row + 1 in range(8):
                                    if column + 2 in range(8):
                                        if grid[row + 1][column + 2] == 0 or grid[row + 1][column + 2] == 1:
                                            grid[row + 1][column + 2] = 4
                                if row + 1 in range(8):
                                    if column - 2 in range(8):
                                        if grid[row + 1][column - 2] == 0 or grid[row + 1][column - 2] == 1:
                                            grid[row + 1][column - 2] = 4
                            # White Bishop
                            if board[row][column] == Piece(-4):
                                for i in range(row + 1, 8):
                                    if grid[i][column] == 2:
                                        break
                                    if grid[i][column] == 1:
                                        grid[i][column] = 4
                                        break
                                    grid[i][column] = 4
                                for i in range(row - 1, -1, -1):
                                    if grid[i][column] == 2:
                                        break
                                    if grid[i][column] == 1:
                                        grid[i][column] = 4
                                        break
                                    grid[i][column] = 4
                                for i in range(column + 1, 8):
                                    if grid[row][i] == 2:
                                        break
                                    if grid[row][i] == 1:
                                        grid[row][i] = 4
                                        break
                                    grid[row][i] = 4
                                for i in range(column - 1, -1, -1):
                                    if grid[row][i] == 2:
                                        break
                                    if grid[row][i] == 1:
                                        grid[row][i] = 4
                                        break
                                    grid[row][i] = 4
                            # white rook
                            if board[row][column] == Piece(-6):
                                x = row + 1
                                y = column + 1
                                while x < 8 and y < 8:
                                    if grid[x][y] == 2:
                                        break
                                    if grid[x][y] == 1:
                                        grid[x][y] = 4
                                        break
                                    if grid[x][y] == 0:
                                        grid[x][y] = 4
                                        x += 1
                                        y += 1
                                x = row - 1
                                y = column - 1
                                while x > -1 and y > -1:
                                    if grid[x][y] == 2:
                                        break
                                    if grid[x][y] == 1:
                                        grid[x][y] = 4
                                        break
                                    if grid[x][y] == 0:
                                        grid[x][y] = 4
                                        x -= 1
                                        y -= 1
                                x = row + 1
                                y = column - 1
                                while x < 8 and y > -1:

                                    if grid[x][y] == 2:
                                        break
                                    if grid[x][y] == 1:
                                        grid[x][y] = 4
                                        break
                                    if grid[x][y] == 0:
                                        grid[x][y] = 4
                                        x += 1
                                        y -= 1
                                x = row - 1
                                y = column + 1
                                while y < 8 and x > -1:

                                    if grid[x][y] == 2:
                                        break
                                    if grid[x][y] == 1:
                                        grid[x][y] = 4
                                        break
                                    if grid[x][y] == 0:
                                        grid[x][y] = 4
                                        x -= 1
                                        y += 1
                            # white queen
                            if board[row][column] == Piece(-3):
                                for i in range(row + 1, 8):
                                    if grid[i][column] == 2:
                                        break
                                    if grid[i][column] == 1:
                                        grid[i][column] = 4
                                        break
                                    grid[i][column] = 4
                                for i in range(row - 1, -1, -1):
                                    if grid[i][column] == 2:
                                        break
                                    if grid[i][column] == 1:
                                        grid[i][column] = 4
                                        break
                                    grid[i][column] = 4
                                for i in range(column + 1, 8):
                                    if grid[row][i] == 2:
                                        break
                                    if grid[row][i] == 1:
                                        grid[row][i] = 4
                                        break
                                    grid[row][i] = 4
                                for i in range(column - 1, -1, -1):
                                    if grid[row][i] == 2:
                                        break
                                    if grid[row][i] == 1:
                                        grid[row][i] = 4
                                        break
                                    grid[row][i] = 4
                                x = row + 1
                                y = column + 1
                                while x < 8 and y < 8:
                                    if grid[x][y] == 2:
                                        break
                                    if grid[x][y] == 1:
                                        grid[x][y] = 4
                                        break
                                    if grid[x][y] == 0:
                                        grid[x][y] = 4
                                        x += 1
                                        y += 1
                                x = row - 1
                                y = column - 1
                                while x > -1 and y > -1:
                                    if grid[x][y] == 2:
                                        break
                                    if grid[x][y] == 1:
                                        grid[x][y] = 4
                                        break
                                    if grid[x][y] == 0:
                                        grid[x][y] = 4
                                        x -= 1
                                        y -= 1
                                x = row + 1
                                y = column - 1
                                while x < 8 and y > -1:

                                    if grid[x][y] == 2:
                                        break
                                    if grid[x][y] == 1:
                                        grid[x][y] = 4
                                        break
                                    if grid[x][y] == 0:
                                        grid[x][y] = 4
                                        x += 1
                                        y -= 1
                                x = row - 1
                                y = column + 1
                                while y < 8 and x > -1:

                                    if grid[x][y] == 2:
                                        break
                                    if grid[x][y] == 1:
                                        grid[x][y] = 4
                                        break
                                    if grid[x][y] == 0:
                                        grid[x][y] = 4
                                        x -= 1
                                        y += 1
                            # white king - CHECKED
                            if board[row][column] == Piece(-2):
                                if row + 1 < 8:
                                    if column + 1 < 8:
                                        if grid[row + 1][column + 1] == 1 or grid[row + 1][column + 1] == 0:
                                            grid[row + 1][column + 1] = 4
                                    if column - 1 > -1:
                                        if grid[row + 1][column - 1] == 1 or grid[row + 1][column - 1] == 0:
                                            grid[row + 1][column - 1] = 4
                                    if grid[row + 1][column] == 1 or grid[row + 1][column] == 0:
                                        grid[row + 1][column] = 4
                                if row - 1 > -1:
                                    if column - 1 > -1:
                                        if grid[row - 1][column - 1] == 1 or grid[row - 1][column - 1] == 0:
                                            grid[row - 1][column - 1] = 4
                                    if column + 1 < 8:
                                        if grid[row - 1][column + 1] == 1 or grid[row - 1][column + 1] == 0:
                                            grid[row - 1][column + 1] = 4
                                    if grid[row - 1][column] == 1 or grid[row - 1][column] == 0:
                                        grid[row - 1][column] = 4
                                if column + 1 < 8:
                                    if grid[row][column + 1] == 1 or grid[row][column + 1] == 0:
                                        grid[row][column + 1] = 4
                                if column - 1 > -1:
                                    if grid[row][column - 1] == 1 or grid[row][column - 1] == 0:
                                        grid[row][column - 1] = 4


                    # end of movement functions
                    print("Click ", pos, "Grid coordinates: ", row, column,
                          board[row][column], grid[row][column])
                    # TODO: CHECK IF KING THEN UNDO MOVE
        display()
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    finish()



def display():
    # Draw the grid
    for row in range(8):
        for column in range(8):
            # delete green and red before finish
            if grid[row][column] == 1:
                color = GREEN
            elif grid[row][column] == 2:
                color = RED
            elif grid[row][column] == 3:
                color = BLUE
            elif grid[row][column] == 4:
                color = PINK
            elif grid[row][column] == 5:
                color = YELLOW
            elif grid[row][column] == 10:
                color = PURPLE

            else:
                if row % 2 == 0 and column % 2 == 0:
                    color = DARK
                if row % 2 == 0 and column % 2 != 0:
                    color = LIGHT
                if row % 2 != 0 and column % 2 == 0:
                    color = LIGHT
                if row % 2 != 0 and column % 2 != 0:
                        color = DARK
            if board[row][column] == Piece(2) and MAT_W:
                color = YELLOW
            if board[row][column] == Piece(-2) and MAT_B:
                color = YELLOW
            position_of_rect = [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT]
            pygame.draw.rect(screen, color,
                             position_of_rect)
            if board[row][column] != Piece(0):
                if board[row][column] == Piece(1):
                    IMAGE = pygame.image.load('ChessSprites\Chess_pdt.png').convert_alpha()
                elif board[row][column] == Piece(2):
                    IMAGE = pygame.image.load('ChessSprites\Chess_kdt.png').convert_alpha()
                elif board[row][column] == Piece(3):
                    IMAGE = pygame.image.load('ChessSprites\Chess_qdt.png').convert_alpha()
                elif board[row][column] == Piece(4):
                    IMAGE = pygame.image.load('ChessSprites\Chess_rdt.png').convert_alpha()
                elif board[row][column] == Piece(5):
                    IMAGE = pygame.image.load('ChessSprites\Chess_ndt.png').convert_alpha()
                elif board[row][column] == Piece(6):
                    IMAGE = pygame.image.load('ChessSprites\Chess_bdt.png').convert_alpha()
                elif board[row][column] == Piece(-1):
                    IMAGE = pygame.image.load('ChessSprites\Chess_plt.png').convert_alpha()
                elif board[row][column] == Piece(-2):
                    IMAGE = pygame.image.load('ChessSprites\Chess_klt.png').convert_alpha()
                elif board[row][column] == Piece(-3):
                    IMAGE = pygame.image.load('ChessSprites\Chess_qlt.png').convert_alpha()
                elif board[row][column] == Piece(-4):
                    IMAGE = pygame.image.load('ChessSprites\Chess_rlt.png').convert_alpha()
                elif board[row][column] == Piece(-5):
                    IMAGE = pygame.image.load('ChessSprites\Chess_nlt.png').convert_alpha()
                elif board[row][column] == Piece(-6):
                    IMAGE = pygame.image.load('ChessSprites\Chess_blt.png').convert_alpha()
                pygame.transform.scale(IMAGE, (WIDTH, HEIGHT))
                image_rect = IMAGE.get_rect()
                image_rect.center = ((MARGIN + WIDTH) * column + MARGIN + 0.5 * WIDTH,
                                     (MARGIN + HEIGHT) * row + MARGIN + 0.5 * HEIGHT)
                screen.blit(IMAGE, image_rect)


def check_black(kx, ky):
    WAS_ATK = False
    for y in range(8):
        for x in range(8):
            # black pawn - CHECKED
            if board[x][y] == Piece(1):
                if x + 1 < 8:
                    if y + 1 < 8:
                        if grid[x + 1][y + 1] == 2 or grid[x + 1][y + 1] == 6:
                            grid[x + 1][y + 1] = 6
                        if grid[x + 1][y + 1] == 0:
                            grid[x + 1][y + 1] = 5
                    if y - 1 > -1:
                        if grid[x + 1][y - 1] == 2 or grid[x + 1][y - 1] == 6:
                            grid[x + 1][y - 1] = 6
                        if grid[x + 1][y - 1] == 0:
                            grid[x + 1][y - 1] = 5
                if grid[kx][ky] == 6 and not WAS_ATK:
                    print "b1", x, y
                    grid[x][y] = 10
                    WAS_ATK = True
            # black king - CHECKED
            elif board[x][y] == Piece(2):
                if x + 1 < 8:
                    if y + 1 < 8:
                        if grid[x + 1][y + 1] == 2:
                            grid[x + 1][y + 1] = 6
                        if grid[x + 1][y + 1] == 0:
                            grid[x + 1][y + 1] = 5
                    if y - 1 > -1:
                        if grid[x + 1][y - 1] == 0:
                            grid[x + 1][y - 1] = 5
                        if grid[x + 1][y - 1] == 2:
                            grid[x + 1][y - 1] = 6
                    if grid[x + 1][y] == 0:
                        grid[x + 1][y] = 5
                    if grid[x + 1][y] == 2:
                        grid[x + 1][y] = 6
                if x - 1 > -1:
                    if y - 1 > -1:
                        if grid[x - 1][y - 1] == 2:
                            grid[x - 1][y - 1] = 6
                        if grid[x - 1][y - 1] == 0:
                            grid[x - 1][y - 1] = 5
                    if y + 1 < 8:
                        if grid[x - 1][y + 1] == 2:
                            grid[x - 1][y + 1] = 6
                        if grid[x - 1][y + 1] == 0:
                            grid[x - 1][y + 1] = 5
                    if grid[x - 1][y] == 2:
                        grid[x - 1][y] = 6
                    if grid[x - 1][y] == 0:
                        grid[x - 1][y] = 5
                if y + 1 < 8:
                    if grid[x][y + 1] == 2:
                        grid[x][y + 1] = 6
                    if grid[x][y + 1] == 0:
                        grid[x][y + 1] = 5
                if y - 1 > -1:
                    if grid[x][y - 1] == 2:
                        grid[x][y - 1] = 6
                    if grid[x][y - 1] == 0:
                        grid[x][y - 1] = 5
            # Black knight - CHECKED
            elif board[x][y] == Piece(5):
                if x - 2 in range(8):
                    if y + 1 in range(8):
                        if grid[x - 2][y + 1] in (0, 5):
                            grid[x - 2][y + 1] = 5
                        if grid[x - 2][y + 1] in (2, 6):
                            grid[x - 2][y + 1] = 6
                if x - 2 in range(8):
                    if y - 1 in range(8):
                        if grid[x - 2][y - 1] in (0, 5):
                            grid[x - 2][y - 1] = 5
                        if grid[x - 2][y - 1] in (2, 6):
                            grid[x - 2][y - 1] = 6
                if x + 2 in range(8):
                    if y + 1 in range(8):
                        if grid[x + 2][y + 1] in (0, 5):
                            grid[x + 2][y + 1] = 5
                        if grid[x + 2][y + 1] in (2, 6):
                            grid[x + 2][y + 1] = 6
                if x + 2 in range(8):
                    if y - 1 in range(8):
                        if grid[x + 2][y - 1] in (0, 5):
                            grid[x + 2][y - 1] = 5
                        if grid[x + 2][y - 1] in (2, 6):
                            grid[x + 2][y - 1] = 6
                if x - 1 in range(8):
                    if y + 2 in range(8):
                        if grid[x - 1][y + 2] in (0, 5):
                            grid[x - 1][y + 2] = 5
                        if grid[x - 1][y + 2] in (2, 6):
                            grid[x - 1][y + 2] = 6
                if x - 1 in range(8):
                    if y - 2 in range(8):
                        if grid[x - 1][y - 2] in (0, 5):
                            grid[x - 1][y - 2] = 5
                        if grid[x - 1][y - 2] in (2, 6):
                            grid[x - 1][y - 2] = 6
                if x + 1 in range(8):
                    if y + 2 in range(8):
                        if grid[x + 1][y + 2] in (0, 5):
                            grid[x + 1][y + 2] = 5
                        if grid[x + 1][y + 2] in (2, 6):
                            grid[x + 1][y + 2] = 6
                if x + 1 in range(8):
                    if y - 2 in range(8):
                        if grid[x + 1][y - 2] in (0, 5):
                            grid[x + 1][y - 2] = 5
                        if grid[x + 1][y - 2] in (2, 6):
                            grid[x + 1][y - 2] = 6
                if grid[kx][ky] == 6 and not WAS_ATK:
                    WAS_ATK = True
                    grid[x][y] = 10
            # Black Bishop
            elif board[x][y] == Piece(4):
                for i in range(x + 1, 8):
                    if grid[i][y] in (1, 6):
                        break
                    if grid[i][y] == 2:
                        grid[i][y] = 6
                        break
                    grid[i][y] = 5
                if grid[kx][ky] == 6 and not WAS_ATK:
                    WAS_ATK = True
                    grid[x][y] = 10
                    for i in range(x + 1, 8):
                        if grid[i][y] == 6:
                            break
                        grid[i][y] = 10
                for i in range(x - 1, -1, -1):
                    if grid[i][y] in (1, 6):
                        break
                    if grid[i][y] == 2:
                        grid[i][y] = 6
                        break
                    grid[i][y] = 5
                if grid[kx][ky] == 6 and not WAS_ATK:
                    WAS_ATK = True
                    grid[x][y] = 10
                    for i in range(x - 1, -1, -1):
                        if grid[i][y] == 6:
                            break
                        grid[i][y] = 10
                for i in range(y + 1, 8):
                    if grid[x][i] in (1, 6):
                        break
                    if grid[x][i] == 2:
                        grid[x][i] = 6
                        break
                    grid[x][i] = 5
                if grid[kx][ky] == 6 and not WAS_ATK:
                    WAS_ATK = True
                    grid[x][y] = 10
                    for i in range(y + 1, 8):
                        if grid[x][i] == 6:
                            break
                        grid[x][i] = 10
                for i in range(y - 1, -1, -1):
                    if grid[x][i] in (1, 6):
                        break
                    if grid[x][i] == 2:
                        grid[x][i] = 6
                        break
                    grid[x][i] = 5
                if grid[kx][ky] == 6 and not WAS_ATK:
                    WAS_ATK = True
                    grid[x][y] = 10
                    for i in range(y - 1, -1, -1):
                        if grid[x][i] == 6:
                            break
                        grid[x][i] = 10
            # black rook
            elif board[x][y] == Piece(6):
                a = x + 1
                b = y + 1
                while a < 8 and b < 8:
                    if grid[a][b] in (1, 6):
                        break
                    if grid[a][b] == 2:
                        grid[a][b] = 6
                        break
                    if grid[a][b] in (0, 5):
                        grid[a][b] = 5
                        a += 1
                        b += 1
                if grid[kx][ky] == 6 and not WAS_ATK:
                    WAS_ATK = True
                    grid[x][y] = 10
                    a = x + 1
                    b = y + 1
                    while a < 8 and b < 8:
                        if grid[a][b] == 6:
                            break
                        grid[a][b] = 10
                        a += 1
                        b += 1
                a = x - 1
                b = y - 1
                while a > -1 and b > -1:
                    if grid[a][b] in (1, 6):
                        break
                    if grid[a][b] == 2:
                        grid[a][b] = 6
                        break
                    if grid[a][b] in (0, 5):
                        grid[a][b] = 5
                        a -= 1
                        b -= 1
                if grid[kx][ky] == 6 and not WAS_ATK:
                    WAS_ATK = True
                    grid[x][y] = 10
                    a = x - 1
                    b = y - 1
                    while a < 8 and b < 8:
                        if grid[a][b] == 6:
                            break
                        grid[a][b] = 10
                        a -= 1
                        b -= 1
                a = x + 1
                b = y - 1
                while a < 8 and b > -1:
                    if grid[a][b] in (1, 6):
                        break
                    if grid[a][b] == 2:
                        grid[a][b] = 6
                        break
                    if grid[a][b] in (0, 5):
                        grid[a][b] = 5
                        a += 1
                        b -= 1
                if grid[kx][ky] == 6 and not WAS_ATK:
                    WAS_ATK = True
                    grid[x][y] = 10
                    a = x + 1
                    b = y - 1
                    while a < 8 and b < 8:
                        if grid[a][b] == 6:
                            break
                        grid[a][b] = 10
                        a += 1
                        b -= 1
                a = x - 1
                b = y + 1
                while b < 8 and a > -1:
                    if grid[a][b] in (1, 6):
                        break
                    if grid[a][b] == 2:
                        grid[a][b] = 6
                        break
                    if grid[a][b] in (0, 5):
                        grid[a][b] = 5
                        a -= 1
                        b += 1
                if grid[kx][ky] == 6 and not WAS_ATK:
                    WAS_ATK = True
                    grid[x][y] = 10
                    a = x - 1
                    b = y + 1
                    while a < 8 and b < 8:
                        if grid[a][b] == 6:
                            break
                        grid[a][b] = 10
                        a -= 1
                        b += 1
            # black queen
            elif board[x][y] == Piece(3):
                for i in range(x + 1, 8):
                    if grid[i][y] in (1, 6):
                        break
                    if grid[i][y] == 2:
                        grid[i][y] = 6
                        break
                    grid[i][y] = 5
                if grid[kx][ky] == 6 and not WAS_ATK:
                    WAS_ATK = True
                    grid[x][y] = 10
                    for i in range(x + 1, 8):
                        if grid[i][y] == 6:
                            break
                        grid[i][y] = 10
                for i in range(x - 1, -1, -1):
                    if grid[i][y] in (1, 6):
                        break
                    if grid[i][y] == 2:
                        grid[i][y] = 6
                        break
                    grid[i][y] = 5
                if grid[kx][ky] == 6 and not WAS_ATK:
                    WAS_ATK = True
                    grid[x][y] = 10
                    for i in range(x - 1, -1, -1):
                        if grid[i][y] == 6:
                            break
                        grid[i][y] = 10
                for i in range(y + 1, 8):
                    if grid[x][i] in (1, 6):
                        break
                    if grid[x][i] == 2:
                        grid[x][i] = 6
                        break
                    grid[x][i] = 5
                if grid[kx][ky] == 6 and not WAS_ATK:
                    WAS_ATK = True
                    grid[x][y] = 10
                    for i in range(y + 1, 8):
                        if grid[x][i] == 6:
                            break
                        grid[x][i] = 10
                for i in range(y - 1, -1, -1):
                    if grid[x][i] in (1, 6):
                        break
                    if grid[x][i] == 2:
                        grid[x][i] = 6
                        break
                    grid[x][i] = 5
                if grid[kx][ky] == 6 and not WAS_ATK:
                    WAS_ATK = True
                    grid[x][y] = 10
                    for i in range(y - 1, -1, -1):
                        if grid[i][y] == 6:
                            break
                        grid[i][y] = 10
                a = x + 1
                b = y + 1
                while a < 8 and b < 8:
                    if grid[a][b] in (1, 6):
                        break
                    if grid[a][b] == 2:
                        grid[a][b] = 6
                        break
                    if grid[a][b] in (0, 5):
                        grid[a][b] = 5
                        a += 1
                        b += 1
                if grid[kx][ky] == 6 and not WAS_ATK:
                    WAS_ATK = True
                    grid[x][y] = 10
                    a = x + 1
                    b = y + 1
                    while a < 8 and b < 8:
                        if grid[a][b] == 6:
                            break
                        grid[a][b] = 10
                        a += 1
                        b += 1
                a = x - 1
                b = y - 1
                while a > -1 and b > -1:
                    if grid[a][b] in (1, 6):
                        break
                    if grid[a][b] == 2:
                        grid[a][b] = 6
                        break
                    if grid[a][b] in (0, 5):
                        grid[a][b] = 5
                        a -= 1
                        b -= 1
                if grid[kx][ky] == 6 and not WAS_ATK:
                    print "b10", x, y
                    WAS_ATK = True
                    grid[x][y] = 10
                    a = x - 1
                    b = y - 1
                    while a < 8 and b < 8:
                        if grid[a][b] == 6:
                            break
                        grid[a][b] = 10
                        a -= 1
                        b -= 1
                a = x + 1
                b = y - 1
                while a < 8 and b > -1:
                    if grid[a][b] in (1, 6):
                        break
                    if grid[a][b] == 2:
                        grid[a][b] = 6
                        break
                    if grid[a][b] in (0, 5):
                        grid[a][b] = 5
                        a += 1
                        b -= 1
                if grid[kx][ky] == 6 and not WAS_ATK:
                    WAS_ATK = True
                    grid[x][y] = 10
                    a = x + 1
                    b = y - 1
                    while a < 8 and b < 8:
                        if grid[a][b] == 6:
                            break
                        grid[a][b] = 10
                        a += 1
                        b -= 1
                a = x - 1
                b = y + 1
                while b < 8 and a > -1:
                    if grid[a][b] in (1, 6):
                        break
                    if grid[a][b] == 2:
                        grid[a][b] = 6
                        break
                    if grid[a][b] in (0, 5):
                        grid[a][b] = 5
                        a -= 1
                        b += 1
                if grid[kx][ky] == 6 and not WAS_ATK:
                    WAS_ATK = True
                    grid[x][y] = 10
                    a = x - 1
                    b = y + 1
                    while a < 8 and b < 8:
                        if grid[a][b] == 6:
                            break
                        grid[a][b] = 10
                        a -= 1
                        b += 1


def check_white(kx, ky):
    WAS_ATK = False
    for y in range(8):
        for x in range(8):
            # white pawn - CHECKED
            if board[x][y] == Piece(-1):
                if x - 1 > -1:
                    if y + 1 < 8:
                        if grid[x - 1][y + 1] == 1:
                            grid[x - 1][y + 1] = 8
                        if grid[x - 1][y + 1] == 0:
                            grid[x - 1][y + 1] = 7
                    if y - 1 > -1:
                        if grid[x - 1][y - 1] == 1:
                            grid[x - 1][y - 1] = 8
                        if grid[x - 1][y - 1] == 0:
                            grid[x - 1][y - 1] = 7
                if grid[kx][ky] == 8 and not WAS_ATK:
                    grid[x][y] = 10
                    WAS_ATK = True
            # White knight - CHECKED
            if board[x][y] == Piece(-5):
                if x - 2 in range(8):
                    if y + 1 in range(8):
                        if grid[x - 2][y + 1] == 0:
                            grid[x - 2][y + 1] = 7
                        if grid[x - 2][y + 1] == 1:
                            grid[x - 2][y + 1] = 8
                if x - 2 in range(8):
                    if y - 1 in range(8):
                        if grid[x - 2][y - 1] == 0:
                            grid[x - 2][y - 1] = 7
                        if grid[x - 2][y - 1] == 1:
                            grid[x - 2][y - 1] = 8
                if x + 2 in range(8):
                    if y + 1 in range(8):
                        if grid[x + 2][y + 1] == 0:
                            grid[x + 2][y + 1] = 7
                        if grid[x + 2][y + 1] == 1:
                            grid[x + 2][y + 1] = 8
                if x + 2 in range(8):
                    if y - 1 in range(8):
                        if grid[x + 2][y - 1] == 0:
                            grid[x + 2][y - 1] = 7
                        if grid[x + 2][y - 1] == 1:
                            grid[x + 2][y - 1] = 8
                if x - 1 in range(8):
                    if y + 2 in range(8):
                        if grid[x - 1][y + 2] == 0:
                            grid[x - 1][y + 2] = 7
                        if grid[x - 1][y + 2] == 1:
                            grid[x - 1][y + 2] = 8
                if x - 1 in range(8):
                    if y - 2 in range(8):
                        if grid[x - 1][y - 2] == 0:
                            grid[x - 1][y - 2] = 7
                        if grid[x - 1][y - 2] == 1:
                            grid[x - 1][y - 2] = 8
                if x + 1 in range(8):
                    if y + 2 in range(8):
                        if grid[x + 1][y + 2] == 0:
                            grid[x + 1][y + 2] = 7
                        if grid[x + 1][y + 2] == 1:
                            grid[x + 1][y + 2] = 8
                if x + 1 in range(8):
                    if y - 2 in range(8):
                        if grid[x + 1][y - 2] == 0:
                            grid[x + 1][y - 2] = 7
                        if grid[x + 1][y - 2] == 1:
                            grid[x + 1][y - 2] = 8
                if grid[kx][ky] == 8 and not WAS_ATK:
                    grid[x][y] = 10
                    WAS_ATK = True
            # White Bishop
            if board[x][y] == Piece(-4):
                for i in range(x + 1, 8):
                    if grid[i][y] in (2, 8):
                        break
                    if grid[i][y] == 1:
                        grid[i][y] = 8
                        break
                    grid[i][y] = 7
                if grid[kx][ky] == 8 and not WAS_ATK:
                    grid[x][y] = 10
                    WAS_ATK = True
                    for i in range(x + 1, 8):
                        if grid[i][y] == 8:
                            break
                        grid[i][y] = 10
                for i in range(x - 1, -1, -1):
                    if grid[i][y] in (2, 8):
                        break
                    if grid[i][y] == 1:
                        grid[i][y] = 8
                        break
                    grid[i][y] = 7
                if grid[kx][ky] == 8 and not WAS_ATK:
                    grid[x][y] = 10
                    WAS_ATK = True
                    for i in range(x - 1, -1, -1):
                        if grid[i][y] == 8:
                            break
                        grid[i][y] = 10
                for i in range(y + 1, 8):
                    if grid[x][i] in (2, 8):
                        break
                    if grid[x][i] == 1:
                        grid[x][i] = 8
                        break
                    grid[x][i] = 7
                if grid[kx][ky] == 8 and not WAS_ATK:
                    grid[x][y] = 10
                    WAS_ATK = True
                    for i in range(y + 1, 8):
                        if grid[x][i] == 8:
                            break
                        grid[x][i] = 10
                for i in range(y - 1, -1, -1):
                    if grid[x][i] in (2, 8):
                        break
                    if grid[x][i] == 1:
                        grid[x][i] = 8
                        break
                    grid[x][i] = 7
                if grid[kx][ky] == 8 and not WAS_ATK:
                    grid[x][y] = 10
                    WAS_ATK = True
                    for i in range(y - 1, -1, -1):
                        if grid[x][i] == 8:
                            break
                        grid[x][i] = 10
            # white rook
            if board[x][y] == Piece(-6):
                a = x + 1
                b = y + 1
                while a < 8 and b < 8:
                    if grid[a][b] in (2, 8):
                        break
                    if grid[a][b] == 1:
                        grid[a][b] = 8
                        break
                    if grid[a][b] in (0, 7):
                        grid[a][b] = 7
                        a += 1
                        b += 1
                if grid[kx][ky] == 8 and not WAS_ATK:
                    grid[x][y] = 10
                    WAS_ATK = True
                    a = x + 1
                    b = y + 1
                    while a < 8 and b < 8:
                        if grid[a][b] == 8:
                            break
                        grid[a][b] = 10
                        a += 1
                        b += 1
                a = x - 1
                b = y - 1
                while a > -1 and b > -1:
                    if grid[a][b] in (2, 8):
                        break
                    if grid[a][b] == 1:
                        grid[a][b] = 8
                        break
                    if grid[a][b] in (0, 7):
                        grid[a][b] = 7
                        a -= 1
                        b -= 1
                if grid[kx][ky] == 8 and not WAS_ATK:
                    grid[x][y] = 10
                    WAS_ATK = True
                    a = x - 1
                    b = y - 1
                    while a < 8 and b < 8:
                        if grid[a][b] == 8:
                            break
                        grid[a][b] = 10
                        a -= 1
                        b -= 1
                a = x + 1
                b = y - 1
                while a < 8 and b > -1:
                    if grid[a][b] in (2, 8):
                        break
                    if grid[a][b] == 1:
                        grid[a][b] = 8
                        break
                    if grid[a][b] in (0, 7):
                        grid[a][b] = 7
                        a += 1
                        b -= 1
                if grid[kx][ky] == 8 and not WAS_ATK:
                    grid[x][y] = 10
                    WAS_ATK = True
                    a = x + 1
                    b = y - 1
                    while a < 8 and b < 8:
                        if grid[a][b] == 8:
                            break
                        grid[a][b] = 10
                        a += 1
                        b -= 1
                a = x - 1
                b = y + 1
                while b < 8 and a > -1:
                    if grid[a][b] in (2, 8):
                        break
                    if grid[a][b] == 1:
                        grid[a][b] = 8
                        break
                    if grid[a][b] in (0, 7):
                        grid[a][b] = 7
                        a -= 1
                        b += 1
                if grid[kx][ky] == 8 and not WAS_ATK:
                    grid[x][y] = 10
                    WAS_ATK = True
                    a = x - 1
                    b = y + 1
                    while a < 8 and b < 8:
                        if grid[a][b] == 8:
                            break
                        grid[a][b] = 10
                        a -= 1
                        b += 1
            # white queen
            if board[x][y] == Piece(-3):
                for i in range(x + 1, 8):
                    if grid[i][y] in (2, 8):
                        break
                    if grid[i][y] == 1:
                        grid[i][y] = 8
                        break
                    grid[i][y] = 7
                if grid[kx][ky] == 8 and not WAS_ATK:
                    grid[x][y] = 10
                    WAS_ATK = True
                    for i in range(x + 1, 8):
                        if grid[i][y] == 8:
                            break
                        grid[i][y] = 10
                for i in range(x - 1, -1, -1):
                    if grid[i][y] in (2, 8):
                        break
                    if grid[i][y] == 1:
                        grid[i][y] = 8
                        break
                    grid[i][y] = 7
                if grid[kx][ky] == 8 and not WAS_ATK:
                    grid[x][y] = 10
                    WAS_ATK = True
                    for i in range(x - 1, -1, -1):
                        if grid[i][y] == 8:
                            break
                        grid[i][y] = 10
                for i in range(y + 1, 8):
                    if grid[x][i] in (2, 8):
                        break
                    if grid[x][i] == 1:
                        grid[x][i] = 8
                        break
                    grid[x][i] = 7
                if grid[kx][ky] == 8 and not WAS_ATK:
                    grid[x][y] = 10
                    WAS_ATK = True
                    for i in range(y + 1, 8):
                        if grid[i][y] == 8:
                            break
                        grid[i][y] = 10
                for i in range(y - 1, -1, -1):
                    if grid[x][i] in (2, 8):
                        break
                    if grid[x][i] == 1:
                        grid[x][i] = 8
                        break
                    grid[x][i] = 7
                if grid[kx][ky] == 8 and not WAS_ATK:
                    grid[x][y] = 10
                    WAS_ATK = True
                    for i in range(y - 1, -1, -1):
                        if grid[i][y] == 8:
                            break
                        grid[i][y] = 10
                a = x + 1
                b = y + 1
                while a < 8 and b < 8:
                    if grid[a][b] in (2, 8):
                        break
                    if grid[a][b] == 1:
                        grid[a][b] = 8
                        break
                    if grid[a][b] in (0, 7):
                        grid[a][b] = 7
                        a += 1
                        b += 1
                if grid[kx][ky] == 8 and not WAS_ATK:
                    grid[x][y] = 10
                    WAS_ATK = True
                    a = x + 1
                    b = y + 1
                    while a < 8 and b < 8:
                        if grid[a][b] == 8:
                            break
                        grid[a][b] = 10
                        a += 1
                        b += 1
                a = x - 1
                b = y - 1
                while a > -1 and b > -1:
                    if grid[a][b] in (2, 8):
                        break
                    if grid[a][b] == 1:
                        grid[a][b] = 8
                        break
                    if grid[a][b] in (0, 7):
                        grid[a][b] = 7
                        a -= 1
                        b -= 1
                if grid[kx][ky] == 8 and not WAS_ATK:
                    grid[x][y] = 10
                    WAS_ATK = True
                    a = x - 1
                    b = y - 1
                    while a < 8 and b < 8:
                        if grid[a][b] == 8:
                            break
                        grid[a][b] = 10
                        a -= 1
                        b -= 1
                a = x + 1
                b = y - 1
                while a < 8 and b > -1:
                    if grid[a][b] in (2, 8):
                        break
                    if grid[a][b] == 1:
                        grid[a][b] = 8
                        break
                    if grid[a][b] in (0, 7):
                        grid[a][b] = 7
                        a += 1
                        b -= 1
                if grid[kx][ky] == 8 and not WAS_ATK:
                    grid[x][y] = 10
                    WAS_ATK = True
                    a = x + 1
                    b = y - 1
                    while a < 8 and b < 8:
                        if grid[a][b] == 8:
                            break
                        grid[a][b] = 10
                        a += 1
                        b -= 1
                a = x - 1
                b = y + 1
                while b < 8 and a > -1:
                    if grid[a][b] in (2, 8):
                        break
                    if grid[a][b] == 1:
                        grid[a][b] = 8
                        break
                    if grid[a][b] in (0, 7):
                        grid[a][b] = 7
                        a -= 1
                        b += 1
                if grid[kx][ky] == 8 and not WAS_ATK:
                    grid[x][y] = 10
                    WAS_ATK = True
                    a = x - 1
                    b = y + 1
                    while a < 8 and b < 8:
                        if grid[a][b] == 8:
                            break
                        grid[a][b] = 10
                        a -= 1
                        b += 1

            # white king - CHECKED
            if board[x][y] == Piece(-2):
                if x + 1 < 8:
                    if y + 1 < 8:
                        if grid[x + 1][y + 1] == 1:
                            grid[x + 1][y + 1] = 8
                        if grid[x + 1][y + 1] == 0:
                            grid[x + 1][y + 1] = 7
                    if y - 1 > -1:
                        if grid[x + 1][y - 1] == 0:
                            grid[x + 1][y - 1] = 7
                        if grid[x + 1][y - 1] == 1:
                            grid[x + 1][y - 1] = 8
                    if grid[x + 1][y] == 0:
                        grid[x + 1][y] = 7
                    if grid[x + 1][y] == 1:
                        grid[x + 1][y] = 8
                if x - 1 > -1:
                    if y - 1 > -1:
                        if grid[x - 1][y - 1] == 1:
                            grid[x - 1][y - 1] = 8
                        if grid[x - 1][y - 1] == 0:
                            grid[x - 1][y - 1] = 7
                    if y + 1 < 8:
                        if grid[x - 1][y + 1] == 1:
                            grid[x - 1][y + 1] = 8
                        if grid[x - 1][y + 1] == 0:
                            grid[x - 1][y + 1] = 7
                    if grid[x - 1][y] == 1:
                        grid[x - 1][y] = 8
                    if grid[x - 1][y] == 0:
                        grid[x - 1][y] = 7
                if y + 1 < 8:
                    if grid[x][y + 1] == 1:
                        grid[x][y + 1] = 8
                    if grid[x][y + 1] == 0:
                        grid[x][y + 1] = 7
                if y - 1 > -1:
                    if grid[x][y - 1] == 1:
                        grid[x][y - 1] = 8
                    if grid[x][y - 1] == 0:
                        grid[x][y - 1] = 7


def check_w_mat():
    print "hola"
    printMat()
    for y in range(8):
        for x in range(8):
            # INITIALIZE chess method to detect crossing
            # white pawn
            if board[x][y] == Piece(-1):
                if x - 1 < 8:
                    if y + 1 < 8:
                        if grid[x - 1][y + 1] == 10:
                            if board[x - 1][y + 1] != Piece(0):
                                return False
                    if y - 1 > -1:
                        if grid[x - 1][y - 1] == 10:
                            if board[x - 1][y - 1] != Piece(0):
                                return False
                    if grid[x - 1][y] == 10:
                        print "b3", x, y
                        return False
            # white rook
            if board[x][y] == Piece(6):
                a = x + 1
                b = y + 1
                while a < 8 and b < 8:
                    if grid[a][b] == 10:
                        return False
                    if grid[a][b] in (1, 2):
                        break
                    else:
                        a += 1
                        b += 1
                a = x - 1
                b = y - 1
                while a > -1 and b > -1:
                    if grid[a][b] == 10:
                        return False
                    if grid[a][b] in (1, 2):
                        break
                    else:
                        a -= 1
                        b -= 1
                a = x + 1
                b = y - 1
                while a < 8 and b > -1:
                    if grid[a][b] == 10:
                        return False
                    if grid[a][b] in (1, 2):
                        break
                    else:
                        a += 1
                        b -= 1
                a = x - 1
                b = y + 1
                while b < 8 and a > -1:
                    if grid[a][b] == 10:
                        return False
                    if grid[a][b] in (1, 2):
                        break
                    else:
                        a -= 1
                        b += 1
            # white bishop
            if board[x][y] == Piece(4):
                for i in range(x + 1, 8):
                    if grid[i][y] == 10:
                        return False
                    if grid[i][y] in (1, 2):
                        break
                for i in range(x - 1, -1, -1):
                    if grid[i][y] == 10:
                        return False
                    if grid[i][y] in (1, 2):
                        break
                    grid[i][y] = 7
                for i in range(y + 1, 8):
                    if grid[i][y] == 10:
                        return False
                    if grid[i][y] in (1, 2):
                        break
                for i in range(y - 1, -1, -1):
                    if grid[i][y] == 10:
                        return False
                    if grid[i][y] in (1, 2):
                        break
            if board[x][y] == Piece(3):
                for i in range(x + 1, 8):
                    if grid[i][y] == 10:
                        return False
                    if grid[i][y] in (1, 2):
                        break
                for i in range(x - 1, -1, -1):
                    if grid[i][y] == 10:
                        return False
                    if grid[i][y] in (1, 2):
                        break
                    grid[i][y] = 7
                for i in range(y + 1, 8):
                    if grid[i][y] == 10:
                        return False
                    if grid[i][y] in (1, 2):
                        break
                for i in range(y - 1, -1, -1):
                    if grid[i][y] == 10:
                        return False
                    if grid[i][y] in (1, 2):
                        break
                a = x + 1
                b = y + 1
                while a < 8 and b < 8:
                    if grid[a][b] == 10:
                        return False
                    if grid[a][b] in (1, 2):
                        break
                    else:
                        a += 1
                        b += 1
                a = x - 1
                b = y - 1
                while a > -1 and b > -1:
                    if grid[a][b] == 10:
                        return False
                    if grid[a][b] in (1, 2):
                        break
                    else:
                        a -= 1
                        b -= 1
                a = x + 1
                b = y - 1
                while a < 8 and b > -1:
                    if grid[a][b] == 10:
                        return False
                    if grid[a][b] in (1, 2):
                        break
                    else:
                        a += 1
                        b -= 1
                a = x - 1
                b = y + 1
                while b < 8 and a > -1:
                    if grid[a][b] == 10:
                        return False
                    if grid[a][b] in (1, 2):
                        break
                    else:
                        a -= 1
                        b += 1
            if board[x][y] == Piece(5):
                if x - 2 in range(8):
                    if y + 1 in range(8):
                        if grid[x - 2][y + 1] == 10:
                            return False
                if x - 2 in range(8):
                    if y - 1 in range(8):
                        if grid[x - 2][y - 1] == 10:
                            return False
                if x + 2 in range(8):
                    if y + 1 in range(8):
                        if grid[x + 2][y + 1] == 10:
                            return False
                if x + 2 in range(8):
                    if y - 1 in range(8):
                        if grid[x + 2][y - 1] == 10:
                            return False
                if x - 1 in range(8):
                    if y + 2 in range(8):
                        if grid[x - 1][y + 2] == 10:
                            return False
                if x - 1 in range(8):
                    if y - 2 in range(8):
                        if grid[x - 1][y - 2] == 10:
                            return False
                if x + 1 in range(8):
                    if y + 2 in range(8):
                        if grid[x + 1][y + 2] == 10:
                            return False
                if x + 1 in range(8):
                    if y - 2 in range(8):
                        if grid[x + 1][y - 2] == 10:
                            return False
    print "didnt b cross"
    return True


def check_b_mat():
    for y in range(8):
        for x in range(8):
            # INITIALIZE chess method to detect crossing
            # white pawn
            if board[x][y] == Piece(1):
                if x + 1 < 8:
                    if y + 1 < 8:
                        if grid[x + 1][y + 1] == 10:
                            if board[x + 1][y + 1] != Piece(0):
                                return False
                    if y - 1 > -1:
                        if grid[x + 1][y - 1] == 10:
                            if board[x + 1][y - 1] != Piece(0):
                                return False
                    if grid[x + 1][y] == 10:
                        return False
            # white rook
            if board[x][y] == Piece(6):
                a = x + 1
                b = y + 1
                while a < 8 and b < 8:
                    if grid[a][b] == 10:
                        return False
                    if grid[a][b] in (1, 2):
                        break
                    else:
                        a += 1
                        b += 1
                a = x - 1
                b = y - 1
                while a > -1 and b > -1:
                    if grid[a][b] == 10:
                        return False
                    if grid[a][b] in (1, 2):
                        break
                    else:
                        a -= 1
                        b -= 1
                a = x + 1
                b = y - 1
                while a < 8 and b > -1:
                    if grid[a][b] == 10:
                        return False
                    if grid[a][b] in (1, 2):
                        break
                    else:
                        a += 1
                        b -= 1
                a = x - 1
                b = y + 1
                while b < 8 and a > -1:
                    if grid[a][b] == 10:
                        return False
                    if grid[a][b] in (1, 2):
                        break
                    else:
                        a -= 1
                        b += 1
            # white bishop
            if board[x][y] == Piece(4):
                for i in range(x + 1, 8):
                    if grid[i][y] == 10:
                        return False
                    if grid[i][y] in (1, 2):
                        break
                for i in range(x - 1, -1, -1):
                    if grid[i][y] == 10:
                        return False
                    if grid[i][y] in (1, 2):
                        break
                    grid[i][y] = 7
                for i in range(y + 1, 8):
                    if grid[i][y] == 10:
                        return False
                    if grid[i][y] in (1, 2):
                        break
                for i in range(y - 1, -1, -1):
                    if grid[i][y] == 10:
                        return False
                    if grid[i][y] in (1, 2):
                        break
            if board[x][y] == Piece(3):
                for i in range(x + 1, 8):
                    if grid[i][y] == 10:
                       return False
                    if grid[i][y] in (1, 2):
                        break
                for i in range(x - 1, -1, -1):
                    if grid[i][y] == 10:
                       return False
                    if grid[i][y] in (1, 2):
                        break
                    grid[i][y] = 7
                for i in range(y + 1, 8):
                    if grid[i][y] == 10:
                       return False
                    if grid[i][y] in (1, 2):
                        break
                for i in range(y - 1, -1, -1):
                    if grid[i][y] == 10:
                       return False
                    if grid[i][y] in (1, 2):
                        break
                a = x + 1
                b = y + 1
                while a < 8 and b < 8:
                    if grid[a][b] == 10:
                        return False
                    if grid[a][b] in (1, 2):
                        break
                    else:
                        a += 1
                        b += 1
                a = x - 1
                b = y - 1
                while a > -1 and b > -1:
                    if grid[a][b] == 10:
                        return False
                    if grid[a][b] in (1, 2):
                        break
                    else:
                        a -= 1
                        b -= 1
                a = x + 1
                b = y - 1
                while a < 8 and b > -1:
                    if grid[a][b] == 10:
                        return False
                    if grid[a][b] in (1, 2):
                        break
                    else:
                        a += 1
                        b -= 1
                a = x - 1
                b = y + 1
                while b < 8 and a > -1:
                    if grid[a][b] == 10:
                        return False
                    if grid[a][b] in (1, 2):
                        break
                    else:
                        a -= 1
                        b += 1
            if board[x][y] == Piece(5):
                if x - 2 in range(8):
                    if y + 1 in range(8):
                        if grid[x - 2][y + 1] == 10:
                            return False
                if x - 2 in range(8):
                    if y - 1 in range(8):
                        if grid[x - 2][y - 1] == 10:
                            return False
                if x + 2 in range(8):
                    if y + 1 in range(8):
                        if grid[x + 2][y + 1] == 10:
                            return False
                if x + 2 in range(8):
                    if y - 1 in range(8):
                        if grid[x + 2][y - 1] == 10:
                            return False
                if x - 1 in range(8):
                    if y + 2 in range(8):
                        if grid[x - 1][y + 2] == 10:
                            return False
                if x - 1 in range(8):
                    if y - 2 in range(8):
                        if grid[x - 1][y - 2] == 10:
                            return False
                if x + 1 in range(8):
                    if y + 2 in range(8):
                        if grid[x + 1][y + 2] == 10:
                            return False
                if x + 1 in range(8):
                    if y - 2 in range(8):
                        if grid[x + 1][y - 2] == 10:
                            return False
    print "didnt b cross"
    return True


def mat():
    print "yala"
    # Set the screen background
    display()
    pygame.display.flip()
    end = False
    while not end:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                end = True
    finish()


def finish():
    print "complete"
    pygame.quit()


def printMat():
    for row in grid:
        for val in row:
            print '{:8}'.format(val),
        print










if __name__ == "__main__":
    main()
