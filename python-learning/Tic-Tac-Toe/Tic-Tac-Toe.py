board = [["" for _ in range (3)] for _ in range (3)]
counter=1
sign=""
for i in range (3):
    for j in range(3):
        board [i][j] = counter
        counter +=1
def display_board(board):
    for i in range(3):
        print ("+-------+-------+-------+")
        print ("|       |       |       |")
        for j in range (3):
            print ("|  ",board[i][j], "  ",end="")
        print("|")
        print ("|       |       |       |")
    print ("+-------+-------+-------+")

def enter_move(board):
    move= (int(input("Enter your move: ")))
    free_numbers= (make_list_of_free_fields(board))
    while move<1 or move>9:
        print("Not valid number, try again")
        move= (int(input("Enter your move: ")))
    if move not in free_numbers :
        print("Occupied, try again")
        enter_move(board)
    elif move in free_numbers:
        for i in range (3):
            for j in range(3):
                if ( move == board [i][j]):
                    board[i][j] = "O"

def make_list_of_free_fields(board):
    free_numbers=[]
    free_fields=()
    for i in range (3):
        for j in range(3):
            if (board [i][j] in range(1,10)):
                free_fields=free_fields+([i]+[j],)
                free_numbers.append(board[i][j])
    if not free_numbers:
        return []
    else:
        return ((free_numbers))

def victory_for(board, sign):
    free_numbers= (make_list_of_free_fields(board))
    for i in range (3):
        if (board[i][0] == board[i][1] and board [i][0] == board[i][2]):
            sign =board[i][0]
            print (sign, "winning")
            return True
        elif (board[0][i] == board[1][i] and board [0][i] == board[2][i]):
            sign =board[0][i]
            print (sign, "winning")
            return True
    if (board[0][0] == board[1][1] and board [0][0] == board[2][2]):
            sign =board[0][0]
            print (sign, "winning")
            return True
    elif  (board[0][2] == board[1][1] and board [0][2] == board[2][0]):
            sign =board[0][2]
            print (sign, "winning")
            return True
    if not make_list_of_free_fields(board): 
        print ("X and O Tie, Thanks")
        return True

def draw_move(board):
    display_board (board)
    free_numbers= (make_list_of_free_fields(board))
    not_available=True
    from random import randrange
    while not_available:
        x= randrange(10)
        if not free_numbers:
            not_available=False
        elif x in (free_numbers):
            not_available=False
    for i in range (3):
            for j in range(3):
                if (board [i][j] == x):
                    board[i][j] = "X"
    display_board (board)

display_board (board)
while not (victory_for(board, sign)):
    enter_move (board)
    make_list_of_free_fields(board)
    draw_move (board)
    make_list_of_free_fields(board)

