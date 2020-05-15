from Tkinter import *
import pygame
import os
import subprocess
import urllib
from enum import Enum
import tryout
from tryout import Piece
import copy
import requests
import threading
import tkMessageBox
import time
import json
import socket

def p_online():
    main_menu.pack_forget()
    online_menu.pack(fill = BOTH, expand = True)

def p_same():
    main_menu.pack_forget()
    play_game("white", "solo", grid)

def b_create():
    online_menu.pack_forget()
    create_menu.pack(fill = BOTH, expand = True)

def b_join():
    online_menu.pack_forget()
    join_menu.pack(fill = BOTH, expand = True)

def run_server():
    os.system("chess_server.py")   


"""def create():
    server = threading.Thread(target=run_server)
    room_creation = threading.Thread(target=create_room)
    server.start()
    room_creation.start()"""


def create():
    name = create_name.get()
    # activate connecting room
    create_menu.pack_forget()
    connecting.pack(fill = BOTH, expand = True)
    # create http request creating a room
    global room_num
    answer = requests.get("http://127.0.0.1:5000/connection/?name=" + name)
    if answer.status_code != 200:
        tkMessageBox.showerror("Error", "Something Went Wrong... Try Again")
        create_menu.pack(fill = BOTH, expand = True)
        return
    response = json.loads(answer.content)
    room_num = response[0]
    password = response[1]
    hostname = socket.gethostname() 
    ip = socket.gethostbyname(hostname) 
    Label(waiting, text= "Room Num: " + str(room_num), font=("Comic Sans MS", 16), bg="#394b50", fg="#fe6e38").place(relx=0.5, rely=0.4, anchor=CENTER)
    Label(waiting, text= "Password: " + str(password), font=("Comic Sans MS", 16), bg="#394b50", fg="#fe6e38").place(relx=0.5, rely=0.45, anchor=CENTER)
    Label(waiting, text= "Your IP: " + str(ip), font=("Comic Sans MS", 16), bg="#394b50", fg="#fe6e38").place(relx=0.5, rely=0.5, anchor=CENTER)
    # activate waiting room
    connecting.pack_forget()
    waiting.pack(fill = BOTH, expand = True)
    # handle error cases
    # wait for other player's connection
    # connection was established
    play_game("white", "online", grid)
    # recieve room number and wait for other player"""
    

def join():
    join_menu.pack_forget()
    name = join_name.get()
    room_num = roomNum.get()
    code = password.get()
    response = requests.post("http://127.0.0.1:5000/connection/?name=" + str(name) \
         + "&room=" + str(room_num) + "&password=" + str(code))
    if response.status_code == 404:
        tkMessageBox.showerror("Error 404", "Room Wasn't Found")
        join_menu.pack(fill = BOTH, expand = True)
        return
    if response.status_code == 401:
        tkMessageBox.showerror("Error 401", "Wrong Password")
        join_menu.pack(fill = BOTH, expand = True)
        return
    connecting.pack(fill = BOTH, expand = True)
    play_game("black", "online", grid)

def handle_client(side, move, start):
    # get move - gets: [was_row, was_column, row, column]
    if not side and start:
        received = False
        while not received:
            time.sleep(2)
            answer = json.loads(requests.get("http://127.0.0.1:5000/sync/").content)
            received = answer[0]
            window.update()
        next_move = answer[1]
        return next_move
    # send move
    requests.post("http://127.0.0.1:5000/sync/?move_x=" + str(move[2]) + "&move_y=" + str(move[3]) + \
                                "&was_x=" + str(move[0]) + "&was_y=" + str(move[1]))
    recieved = False
    while not recieved:
        time.sleep(2)
        answer = json.loads(requests.get("http://127.0.0.1:5000/sync/").content)
        recieved = answer[0]
        window.update()
    next_move = answer[1]
    return next_move

def back(page):
    print "x"
    """if page == "online_menu":
    if page == """

def exit():
    pygame.quit()

# ready
# handles screen closer
def callback():
    if tkMessageBox.askokcancel("Quit", "Are You Sure?"):
        global done
        done = True
        window.destroy()




# Definitions
# colors
LEFT_BUTTON = 1
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
LIGHT = (230, 204, 183) #(204, 204, 204) # (230, 204, 183)
DARK = 	(89,62,40) # (51, 51, 51) # 
BLUE = (0, 64, 255)
PINK = (255, 105, 180)
YELLOW = (255, 255, 0)
PURPLE = (148, 0, 211)
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 90
HEIGHT = 90
# This sets the margin between each cell
MARGIN = 1
# variables
done = False
MAT_W = False
MAT_B = False
WAS_W = False
WAS_B = False
WAS_EMPTY = False
KING_SAFE = True
PICK = False

W_TURN = True
KING_X = 0
KING_Y = 0
# GRIDS
global grid
grid = []
for row in range(8):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(8):
        grid[row].append(0)  # Append a cell
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




# pygame init
# pygame.init()
# tkinter window settings
# window initialization & configuration
window = Tk()
window.protocol("WM_DELETE_WINDOW", callback)
window.title("Guy Chess")
window.geometry("800x800")
signature = Label(window, text="All Copyrights Belong To Guy Hoffman", font=("Comic Sans MS", 10), bg="#394b50", fg="#fe6e38").place(relx=1.0, rely=1.0, anchor=SE)

# set frames
main_menu = Frame(window, bg="#394b50")
same_game = Frame(window, bg="#394b50")
online_menu = Frame(window, bg="#394b50")
create_menu = Frame(window, bg="#394b50")
join_menu = Frame(window, bg="#394b50")
connecting = Frame(window, bg="#394b50")
waiting = Frame(window, bg="#394b50")
game_page = Frame(window, bg="#394b50") 
game = Frame(window, height=720, width=720, bg="#394b50")

# main menu frame
main_menu.pack(fill = BOTH, expand = True)
Label(main_menu, text="The Knights Of The Squared Table", font=("Comic Sans MS", 24), bg="#fe6e38", fg="#394b50", width=30, height=2).place(relx=0.5, rely=0.1, anchor=CENTER)
Label(main_menu, text="Multi-Player Chess", font=("Comic Sans MS", 26), bg="#394b50", fg="#fe6e38").place(relx=0.5, rely=0.25, anchor=CENTER)
Button(main_menu, text="Play Online", width=27, command=p_online).place(relx=0.5, rely=0.5, anchor=CENTER)
Button(main_menu, text="Play 2-Players On Same Computer", width=27, command=p_same).place(relx=0.5, rely=0.55, anchor=CENTER)

# online menu frame
Label(online_menu, text="Online Menu", font=("Comic Sans MS", 26), bg="#fe6e38", fg="#394b50").place(relx=0.5, rely=0.25, anchor=CENTER)
Button(online_menu, text="Create Room", width=27, command=b_create).place(relx=0.5, rely=0.5, anchor=CENTER)
Button(online_menu, text="Join Room", width=27, command=b_join).place(relx=0.5, rely=0.55, anchor=CENTER)

# create room menu
Label(create_menu, text="Create Room", font=("Comic Sans MS", 26), bg="#fe6e38", fg="#394b50").place(relx=0.5, rely=0.25, anchor=CENTER)
Label(create_menu, text="Please Choose A Game Name", font=("Comic Sans MS", 16), bg="#394b50", fg="#fe6e38").place(relx=0.5, rely=0.45, anchor=CENTER)
create_name = Entry(create_menu, width=20, bg="white")
create_name.place(relx=0.5, rely=0.5, anchor=CENTER)
Button(create_menu, text="Create The Room", command=create).place(relx=0.5, rely=0.55, anchor=CENTER)

# join friend menu
Label(join_menu, text="Join Room", font=("Comic Sans MS", 26), bg="#fe6e38", fg="#394b50").place(relx=0.5, rely=0.25, anchor=CENTER)
Label(join_menu, text="Please Choose A Game Name",font=("Comic Sans MS", 16), bg="#394b50", fg="#fe6e38").place(relx=0.5, rely=0.4, anchor=CENTER)
join_name = Entry(join_menu, width=20, bg="white")
join_name.place(relx=0.5, rely=0.45, anchor=CENTER)
Label(join_menu, text="Please Enter Desired Room Number",font=("Comic Sans MS", 16), bg="#394b50", fg="#fe6e38").place(relx=0.5, rely=0.5, anchor=CENTER)
roomNum = Entry(join_menu, width=20, bg="white")
roomNum.place(relx=0.5, rely=0.55, anchor=CENTER)
Label(join_menu, text="Please Enter The Room's Password",font=("Comic Sans MS", 16), bg="#394b50", fg="#fe6e38").place(relx=0.5, rely=0.6, anchor=CENTER)
password = Entry(join_menu, width=20, bg="white")
password.place(relx=0.5, rely=0.65, anchor=CENTER)
Button(join_menu, text="Join The Room", command=join).place(relx=0.5, rely=0.7, anchor=CENTER)

# connecting frame
Label(connecting, text="Connecting", font=("Comic Sans MS", 16), bg="#394b50", fg="#fe6e38").place(relx=0.5, rely=0.5, anchor=CENTER)

# waiting room
Label(waiting, text="Waiting Room", font=("Comic Sans MS", 24), bg="#fe6e38", fg="#394b50", width=30, height=2).place(relx=0.5, rely=0.1, anchor=CENTER)
Label(waiting, text="Waiting For Other Player To Connect", font=("Comic Sans MS", 26), bg="#394b50", fg="#fe6e38").place(relx=0.5, rely=0.25, anchor=CENTER)

# PLAY MENU 
Button(game_page, text="exit", command=exit).place(relx=0.5, rely=0.6, anchor=CENTER)

def play_game(side, type, grid): # side, type
    global screen
    global MAT_B
    global MAT_W
    # p1 = Process(target=tk_loop)
    # p1.start()
    arrange = []
    temp = []
    temp1 = []
    WAS_ROW = 0
    WAS_COLUMN = 0
    # init the grid
    for x in range(8):
        for y in range(8):
            if board[x][y].value == 0:
                grid[x][y] = 0
            if board[x][y].value > 0:
                grid[x][y] = 1
            if board[x][y].value < 0:
                grid[x][y] = 2

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
    for x in range(8):
        for y in range(8):
            arrange[x][y] = grid[x][y]
    global done
    done = False
    # use variables
    if side == "white":
        W_TURN = True
    else:
        W_TURN = False
    # Used to manage how fast the screen updates
    global clock
    clock = pygame.time.Clock()
    # disconnected = False
    first = True
    # -------- Main Program Loop -----------
    """game.grid(columnspan = (600), rowspan = 500) # Adds grid
    game.pack(side = LEFT, fill = BOTH, expand = True) #packs window to the left
    game_page.pack(side = LEFT, fill = BOTH, expand = True)
    os.environ['SDL_WINDOWID'] = str(game.winfo_id())
    os.environ['SDL_VIDEODRIVER'] = 'windib'
    screen = pygame.display.set_mode((720,720))
    screen.fill(pygame.Color(0,0,0))
    pygame.display.init()
    pygame.display.update()
    display(grid, screen)
    pygame.display.flip()"""
    """answer = json.loads(requests.get("http://127.0.0.1:5000/approve/").content)
    connected = answer[0]"""
    while not done:
        approved = True
        if type == "solo":
            if first:
                game.grid(columnspan = (600), rowspan = 500) # Adds grid
                game.pack(side = LEFT, fill = BOTH, expand = True) #packs window to the left
                game_page.pack(side = LEFT, fill = BOTH, expand = True)
                os.environ['SDL_WINDOWID'] = str(game.winfo_id())
                os.environ['SDL_VIDEODRIVER'] = 'windib'
                screen = pygame.display.set_mode((720,720))
                screen.fill(pygame.Color(0,0,0))
                pygame.display.init()
                pygame.display.update()
                display(grid, screen)
                pygame.display.flip()
                first = False
        if type == "online":
            # first time running
            if first:
                # white - waits for other's connection, performs a move, sends, waits
                if W_TURN:
                    # wait for other player's connection
                    answer = json.loads(requests.get("http://127.0.0.1:5000/approve/").content)
                    connected = answer[0]
                    if not connected:
                        approved = False
                    else:
                        waiting.pack_forget()
                        game.grid(columnspan = (600), rowspan = 500) # Adds grid
                        game.pack(side = LEFT, fill = BOTH, expand = True) #packs window to the left
                        game_page.pack(side = LEFT, fill = BOTH, expand = True)
                        os.environ['SDL_WINDOWID'] = str(game.winfo_id())
                        os.environ['SDL_VIDEODRIVER'] = 'windib'
                        screen = pygame.display.set_mode((720,720))
                        screen.fill(pygame.Color(0,0,0))
                        pygame.display.init()
                        pygame.display.update()
                        display(grid, screen)
                        pygame.display.flip()
                        first = False
                # black - waits for other player's 
                else:
                    connecting.pack_forget()
                    game.grid(columnspan = (600), rowspan = 500) # Adds grid
                    game.pack(side = LEFT, fill = BOTH, expand = True) #packs window to the left
                    game_page.pack(side = LEFT, fill = BOTH, expand = True)
                    os.environ['SDL_WINDOWID'] = str(game.winfo_id())
                    os.environ['SDL_VIDEODRIVER'] = 'windib'
                    screen = pygame.display.set_mode((720,720))
                    screen.fill(pygame.Color(0,0,0))
                    pygame.display.init()
                    pygame.display.update()
                    display(grid, screen)
                    pygame.display.flip()
                    answer = handle_client(W_TURN, [], True)
                    WAS_ROW = int(answer[0])
                    WAS_COLUMN = int(answer[1])
                    row = int(answer[2])
                    column = int(answer[3])
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
                    first = False
        if approved:    
            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    done = True
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT_BUTTON:
                    # User clicks the mouse. Get the position
                    pos = pygame.mouse.get_pos()
                    # Change the x/y screen coordinates to grid coordinates
                    column = pos[0] // (WIDTH + MARGIN)
                    row = pos[1] // (HEIGHT + MARGIN)
                    for x in range(8):
                        for y in range(8):
                            if grid[x][y] == 3:
                                grid[x][y] = 3
                            elif grid[x][y] == 4:
                                grid[x][y] = 4
                            else:
                                grid[x][y] = arrange[x][y]
                    if row > 7 or column > 7:
                        break
                    else:
                        if grid[row][column] == 4:
                            validate, pos_mat = tryout.approve(W_TURN, board, [WAS_ROW, WAS_COLUMN], [row, column])
                            if validate == 2: # mat case
                                for x in range(8):
                                    for y in range(8):
                                        grid[x][y] = pos_mat[x][y]
                                if W_TURN:
                                    global MAT_B
                                    MAT_B = True
                                else:
                                    global MAT_W
                                    MAT_W = True
                                # making the move
                                arrange[row][column] = arrange[WAS_ROW][WAS_COLUMN]
                                arrange[WAS_ROW][WAS_COLUMN] = 0
                                board[row][column] = board[WAS_ROW][WAS_COLUMN]
                                board[WAS_ROW][WAS_COLUMN] = Piece(0)
                                grid[row][column] = arrange[row][column]
                                grid[WAS_ROW][WAS_COLUMN] = 0
                                for x in range(8):
                                    for y in range(8):
                                        if grid[x][y] != 10:
                                            grid[x][y] = arrange[x][y]
                                grid[row][column] = 10
                                done=True
                                if type == "online":
                                    requests.post("http://127.0.0.1:5000/sync/?move_x=" + str(row) + "&move_y=" + str(column) + \
                                "&was_x=" + str(WAS_ROW) + "&was_y=" + str(WAS_COLUMN))
                                break
                            if validate == 1: # chess case
                                for x in range(8):
                                    for y in range(8):
                                        grid[x][y] = arrange[x][y]
                                break # won't do the move and would wait for new one
                            if validate == 0: # approved, no chess, make the move
                                # grid recoil
                                for x in range(8):
                                    for y in range(8):
                                        grid[x][y] = arrange[x][y]
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
                                display(grid, screen)
                                pygame.display.flip()
                                window.update()
                                if type == "solo":
                                    W_TURN = not W_TURN
                                    break
                                if type == "online":
                                    answer = handle_client(W_TURN, [WAS_ROW, WAS_COLUMN, row, column], False)
                                    print "answer: ", answer
                                    WAS_ROW = int(answer[0])
                                    WAS_COLUMN = int(answer[1])
                                    row = int(answer[2])
                                    column = int(answer[3])
                                    validate, pos_mat = tryout.approve(not W_TURN, board, [WAS_ROW, WAS_COLUMN], [row, column])
                                    if validate == 2:
                                        # i was matted
                                        for x in range(8):
                                            for y in range(8):
                                                grid[x][y] = pos_mat[x][y]
                                        if W_TURN:
                                            MAT_W = True
                                        else:
                                            MAT_B = True
                                        # making the move
                                        arrange[row][column] = arrange[WAS_ROW][WAS_COLUMN]
                                        arrange[WAS_ROW][WAS_COLUMN] = 0
                                        board[row][column] = board[WAS_ROW][WAS_COLUMN]
                                        board[WAS_ROW][WAS_COLUMN] = Piece(0)
                                        grid[row][column] = arrange[row][column]
                                        grid[WAS_ROW][WAS_COLUMN] = 0
                                        for x in range(8):
                                            for y in range(8):
                                                if grid[x][y] != 10:
                                                    grid[x][y] = arrange[x][y]
                                        grid[row][column] = 10
                                        done = True
                                        break
                                    for x in range(8):
                                        for y in range(8):
                                            grid[x][y] = arrange[x][y]
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
                                    break    
                        if grid[row][column] == 3:
                            for x in range(8):
                                for y in range(8):
                                    grid[x][y] = arrange[x][y]
                            break
                        if grid[row][column] == 0 or grid[row][column] == 1 or grid[row][column] == 2:
                            for x in range(8):
                                for y in range(8):
                                    grid[x][y] = arrange[x][y]
                            WAS_ROW = row
                            WAS_COLUMN = column
                        if board[row][column] != Piece.Empty:
                            grid = tryout.mark(W_TURN, board, [row, column])
                            grid[row][column] = 3

        if not first:
            display(grid, screen)
            pygame.display.flip() 
        clock.tick(60)
        # Go ahead and update the screen with what we've drawn.
        window.update()

    if not first:
        display(grid, screen)
        pygame.display.flip()
        pygame.quit()


def display(grid, screen):
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
            if board[row][column] == Piece(2) and MAT_B:
                color = YELLOW
            if board[row][column] == Piece(-2) and MAT_W:
                color = YELLOW
            position_of_rect = [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT]
            pygame.draw.rect(screen, color,
                             position_of_rect)
            if board[row][column] != Piece(0):
                if board[row][column] == Piece(1):
                    IMAGE = pygame.image.load(r'ChessSprites\Chess_pdt.png').convert_alpha()
                elif board[row][column] == Piece(2):
                    IMAGE = pygame.image.load(r'ChessSprites\Chess_kdt.png').convert_alpha()
                elif board[row][column] == Piece(3):
                    IMAGE = pygame.image.load(r'ChessSprites\Chess_qdt.png').convert_alpha()
                elif board[row][column] == Piece(4):
                    IMAGE = pygame.image.load(r'ChessSprites\Chess_rdt.png').convert_alpha()
                elif board[row][column] == Piece(5):
                    IMAGE = pygame.image.load(r'ChessSprites\Chess_ndt.png').convert_alpha()
                elif board[row][column] == Piece(6):
                    IMAGE = pygame.image.load(r'ChessSprites\Chess_bdt.png').convert_alpha()
                elif board[row][column] == Piece(-1):
                    IMAGE = pygame.image.load(r'ChessSprites\Chess_plt.png').convert_alpha()
                elif board[row][column] == Piece(-2):
                    IMAGE = pygame.image.load(r'ChessSprites\Chess_klt.png').convert_alpha()
                elif board[row][column] == Piece(-3):
                    IMAGE = pygame.image.load(r'ChessSprites\Chess_qlt.png').convert_alpha()
                elif board[row][column] == Piece(-4):
                    IMAGE = pygame.image.load(r'ChessSprites\Chess_rlt.png').convert_alpha()
                elif board[row][column] == Piece(-5):
                    IMAGE = pygame.image.load(r'ChessSprites\Chess_nlt.png').convert_alpha()
                elif board[row][column] == Piece(-6):
                    IMAGE = pygame.image.load(r'ChessSprites\Chess_blt.png').convert_alpha()
                pygame.transform.scale(IMAGE, (WIDTH, HEIGHT))
                image_rect = IMAGE.get_rect()
                image_rect.center = ((MARGIN + WIDTH) * column + MARGIN + 0.5 * WIDTH,
                                     (MARGIN + HEIGHT) * row + MARGIN + 0.5 * HEIGHT)
                screen.blit(IMAGE, image_rect)

def printMat(arr):
    for row in arr:
        for val in row:
            print '{:8}'.format(val),
        print

# run
window.mainloop()

