#-------Global Variables-----

#Game Board
board = ["-", "-", "-",
         "-", "-", "-", 
         "-", "-", "-"]

#If Game is still going
game_still_going = True

#who won? or tie? 
winner = None

#whos turn is it 
current_player = "X"


# Display Board
def display_board():
  print(board[0] + " | " + board[1] + " | " + board[2])
  print(board[3] + " | " + board[4] + " | " + board[5])
  print(board[6] + " | " + board[7] + " | " + board[8])

def play_game():
  #display initial board
  display_board()

  #While the game is still going  
  while game_still_going:

    #handle a single turnof an arbitrary player 
    handle_turn(current_player)

    #check if the game has ended
    check_if_game_over()

    # Flip to other player
    flip_player()

  #The Game Has Ended
  if winner == "X" or winner == "O":
    print(winner + " won.")
  elif winner == None:
    print("Tie.")

#handle a single turnof an arbitrary player
def handle_turn(player):

  print(player + ";s Turn.")
  position = input("Choose a position from 1 - 9: ")

  valid = False
  while not valid:

    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      position = input("Invalid Input. Choose position from 1 - 9: ")

    
    position = int(position) - 1
    if board[position] == "-":
      valid = True
    else:
      print("You Can't go there. Go again.")

  board[position] = player
  display_board()

def check_if_game_over():
  check_for_winner()
  check_if_tie()


def check_for_winner():

  #set up global Variables
  global winner
  #check rows
  row_winner = check_rows()
  #check coloumns
  coloumn_winner = check_coloumns()
  #check diagonals
  diagonal_winner = check_diagonals()
  if row_winner: 
    winner = row_winner
  elif coloumn_winner:
    winner = coloumn_winner
  elif diagonal_winner:
    winner = diagonal_winner
  else:
    winner = None  
  return


def check_rows():
  #setup global variable
  global game_still_going

  #check if any of the rows have same values (and is not empty)
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"

  #If any row does have a match, flag that there is a win
  if row_1 or row_2 or row_3:
    game_still_going = False

  #Return The Winner( X or O)  
  if row_1:
    return board[0]
  elif row_2:
    return board[3]
  elif row_3:
    return board[6]  
  return

def check_diagonals():
  #setup global variable
  global game_still_going

  #check if any of the diagonals have same values (and is not empty)
  diagonal_1 = board[0] == board[4] == board[8] != "-"
  diagonal_2 = board[6] == board[4] == board[2] != "-"

  #If any row does have a match, flag that there is a win
  if diagonal_1 or diagonal_2:
    game_still_going = False

  #Return The Winner( X or O)  
  if diagonal_1:
    return board[0]
  elif diagonal_2:
    return board[6] 
  return
  
  
def check_coloumns():
  #setup global variable
  global game_still_going

  #check if any of the coloumns have same values (and is not empty)
  coloumn_1 = board[0] == board[3] == board[6] != "-"
  coloumn_2 = board[1] == board[4] == board[7] != "-"
  coloumn_3 = board[2] == board[5] == board[8] != "-"

  #If any row does have a match, flag that there is a win
  if coloumn_1 or coloumn_2 or coloumn_3:
    game_still_going = False

  #Return The Winner( X or O)  
  if coloumn_1:
    return board[0]
  elif coloumn_2:
    return board[1]
  elif coloumn_3:
    return board[2] 
  return


def check_if_tie(): 
  global game_still_going
  if "-" not in board:
    game_still_going = False

  return


def flip_player():
  #global variable we need
  global current_player
  #if the curr player is X then change it to O
  if current_player == "X":
    current_player = "O"
    #if curr player is O then change it to X
  elif current_player == "O":
    current_player = "X"  
  return

play_game()


#board
#display board  
#play game
#handle turn
#check win
   #check rows
   #check coloumns
   #check diagonals
#check tie
#flip player


