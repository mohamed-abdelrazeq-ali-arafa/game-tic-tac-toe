

'''
Assigning values to the grid
The grid will look like this:
  0,0 | 0,1 | 0,2
  1,0 | 1,1 | 1,2
  2,0 | 2,1 | 2,2
'''
N = 3
grid = [ [".", ". ", ". "],
         [". ", " .", ". "],
         [". ", ". ", " ."] ]

#This function prints the grid of Tic-Tac-Toe as the game progresses
def print_grid():
    print("Player 1: X  vs  Player 2: O")
    print('--' + '---' * N + '--')
    for i in range(N):
        print(end='|  ')
        for j in range(N):
            print(grid[i][j], end='  ')
        print(end='|')
        print()
        print('--' + '---' * N + '--')

#This function checks if row or column or diagonal is full with same characters
def check_win():
     # check for rows
    for row in range(0,3) :
       if (grid[row][0] ==grid[row][1]  == grid[row][2]=='X'):
           return True
    for row in range(0,3) :
       if (grid[row][0] == grid[row][1] ==  grid[row][2]=='O'):
           return True
     #check for colum
    for colum in range(0,3):
      if(grid[0][colum] == grid[1][colum]== grid[2][colum]=='X'):
           return True 
      for colum in range(0,3): 
       if(grid[0][colum] == grid[1][colum] == grid[2][colum]=='O'):
           return True 
     #check for diagonal
       if grid[0][0] == grid[1][1] == grid[2][2] == "X":
           return True
       elif grid[0][0] == grid[1][1] == grid[2][2] == "O":
           return True
    
       elif grid[0][2] == grid[1][1] == grid[2][0] == "X":
           return True
       elif grid[0][2] == grid[1][1] == grid[2][0] == "O":
           return True
    
 
 
#This function checks if row or column or diagonal is full with same characters
def check_tie(mark):
   counter=0
   for i in range(0,3):
    for j in range(0,3):
        if grid[i][j]!=".":
            counter=counter+1
        if counter==9 and not check_win() :
            return True

#This function checks if given cell is empty or not 
def check_empty(i, j):
    
            while grid[i][j]==".":
                return True
            else:
                return False
            
            

#This function checks if given position is valid or not 
def check_valid_position(i, j):
    if i in range (0,3) and j in range (0,3):
        return True

#This function sets a value to a cell
def set_cell(i, j, mark):
    grid[i][j]=mark
    

#This function clears the grid
def grid_clear():
    for row in range(0,3):
      for colum in range(0,3):
          grid[row][colum]="."

#MAIN FUNCTION
def play_game():
    print("Tic-Tac-Toe Game!")
    print("Welcome...")
    print("============================")
    player = 0
    while True:
        #Prints the grid
        print_grid()
        #Set mark value based on the player
        mark = 'X' if player == 0 else 'O'
        #Takes input from the user to fill in the grid
        print('Player %s' % mark)
        i, j = map(int, input('Enter the row index and column index: ').split())
        while not check_valid_position(i, j) or not check_empty(i, j):
            i, j = map(int, input('Enter a valid row index and a valid column index: ').split())
      
        #Set the input position with the mark
        set_cell(i, j, mark)
        #Check if the state of the grid has a win state
        if check_win():
            #Prints the grid
            print_grid()
            print('Congrats, Player %s is won!' % mark)
            break
        #Check if the state of the grid has a tie state
        if check_tie(mark):
            #Prints the grid
            print_grid()
            print("Woah! That's a tie!")
            break		
        #Player number changes after each turn
        player = 1 - player 


while True:
	grid_clear()
	play_game()
	c = input('Play Again [Y/N] ')
	if c not in 'yY':
		break
