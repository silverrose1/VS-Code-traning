board = [["" for _ in range (3)] for _ in range (3)]
counter=1
sign=""
player_name=""
for i in range (3):
    for j in range(3):
        board [i][j] = counter
        counter +=1

def player_name(board):
    global player_name 
    player_name = input("Enter your name: ")
    print("Welcome", player_name, "to the game!")

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
    while True:
        try: # Handle invalid input
            move= (int(input("Enter your move (1-9): "))) # Get the user's move
            if move<1 or move>9:
                print("Not valid number, try again")
            elif move not in make_list_of_free_fields(board) :
                print("Occupied, try again")
            else: # Check if the move is valid
                for i in range (3):
                    for j in range(3):
                        if ( move == board [i][j]):
                            board[i][j] = "O"
                break # Exit the loop when a valid move is made

        except ValueError: # Handle invalid input
            print("Invalid input. Please enter a number between 1 and 9.")

def make_list_of_free_fields(board): 
    free_numbers = [] # Initialize the list here
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
            if sign == "O": print (player_name, "winning")
            else: print ("Computer winning")
            return True
        elif (board[0][i] == board[1][i] and board [0][i] == board[2][i]):
            sign =board[0][i]
            if sign == "O": print (player_name, "winning")
            else: print ("Computer winning")
            return True
    if (board[0][0] == board[1][1] and board [0][0] == board[2][2]):
            sign =board[0][0]
            if sign == "O": print (player_name, "winning")
            else: print ("Computer winning")
            return True
    elif  (board[0][2] == board[1][1] and board [0][2] == board[2][0]):
            sign =board[0][2]
            print (player_name, "winning")
            return True
    if not make_list_of_free_fields(board):
        print ("X and O Tie, Thanks")
        return True
    return False

def draw_move(board):
    display_board (board)
    free_numbers= (make_list_of_free_fields(board))
    if free_numbers:  # Check if free_numbers is not empty
        best_move = minimax(board, "X")  # Call the minimax function
        for i in range (3):
                for j in range(3):
                    if (board [i][j] == best_move):
                        board[i][j] = "X"
        
    display_board (board)

def minimax(board, player):
    free_numbers = make_list_of_free_fields(board)
    if victory_for(board, "X"):
        return 10  # Computer wins
    elif victory_for(board, "O"):
        return -10 # Player wins
    elif not free_numbers:
        return 0 # Tie

    if player == "X":  # Maximizing player
        best_score = -float("inf")
        for move in free_numbers:
            board_copy = [row[:] for row in board] # Create a copy to avoid modifying original
            for i in range(3):
                for j in range(3):
                    if board_copy[i][j] == move:
                        board_copy[i][j] = "X"
            score = minimax(board_copy, "O")
            best_score = max(best_score, score)
            if best_score == 10: # Early pruning - computer wins
                return best_score
            board_copy[i][j] = move # Restore original move
        return best_score
    else:  # Minimizing player
        best_score = float("inf")
        for move in free_numbers:
            board_copy = [row[:] for row in board]
            for i in range(3):
                for j in range(3):
                    if board_copy[i][j] == move:
                        board_copy[i][j] = "O"
            score = minimax(board_copy, "X")
            best_score = min(best_score, score)
            if best_score == -10: # Early pruning - player wins
                return best_score
            board_copy[i][j] = move
        return best_score

player_name(board)
display_board (board)
while not (victory_for(board, sign)):
    enter_move (board)
    free_numbers = make_list_of_free_fields(board)  # Only call once
    draw_move (board)

#Test the code