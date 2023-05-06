#!/usr/bin/env python
# coding: utf-8

# In[5]:





# In[5]:


import random
# 1. Create a 3x3 board using a 2-dimensional array and initialize each element as empty.

# Define class, setup variables, define empty dictionary for symbols. We add variables for custom player names.
class TicTacToe:
    def __init__(self):
        self.board = [['{}' for _ in range(3)] for _ in range(3)]
        self.player1 = None
        self.player2 = None
        self.player_symbols = {}
        
# The inner lists, or rows, contain the individual cells of the board. 
# In this case, the board is initialized with empty '{}' symbols.    
        
            
# 2. Write a Function to check whether the board is filled or not.
#  a. Iterate over the board and return false if the board contains an empty sign or else return true.

    def is_board_filled(self):
        for row in self.board:
            for cell in row:
                if cell == '{}':
                    return False
        return True
    
    # We use two nested 'for' loops to iterate over the board. 
    # Outer loop iterates through each row, inner loop through each cell in the current row. 
    # The 'if' statement checks whether the cell is equal to an empty cell, and returns false if the cell is empty. 
    # If it completes without finding an empty cell, it will continue to next row with the outer loop. 
    # When both loops complete sucessfully, the method returns true indicating the board is filled.
    
    # 3. Write a Function to check whether a player has won or not.
    #  a. You have to check all possibilities mentioned in item 2.
    #  b. Check for all the rows, columns, and two diagonals.
    
    def has_player_won(self, player):
        player_symbol = self.player_symbols[player]
        
        # The first loop iterates through each row of the game board and checks if all the cells
        # in a row contain the player's symbol. If it returns true, the player wins.
       
        for row in self.board:
            if all(cell == player_symbol for cell in row):
                return True

        #  This loop iterates through each column of the board and checks if all the cells 
        #  in a column contain the player's symbol. If it returns true, the player wins.
        for col in range(3):
            if all(self.board[row][col] == player_symbol for row in range(3)):
                return True

        # These two loops check the two diagonals of the board to see if all the cells in a diagonal contain the player's symbol.
        # If either of these loops finds a diagonal where all the cells contain the player's symbol, then the player wins.
        if all(self.board[i][i] == player_symbol for i in range(3)):
            return True

        if all(self.board[i][2 - i] == player_symbol for i in range(3)):
            return True

        return False

    
    # 4. Write Function to show the board. (You will show the board multiple times to the users while they are playing).
    
    
    # We use the enumerate function to get both the row index and the row contents at the same time. 
    # "i" contains the row index, while "row" contains the contents of the row.
    # We then use the print function to display each row as a string, concatenating the elements of the 
    # row together with the string " | " as a separator so that each cell is separated by a vertical bar.
    def show_board(self):
        for i, row in enumerate(self.board):
            print(" | ".join(row))
            if i < len(self.board) - 1:
                print("-" * 9)
                
    # 5. Write a Function to start the game.
    #  a. Select the first turn of the player randomly.
    #  b. Write an infinite loop that breaks when the game is over (either win or draw).
    #    i. Show the board to the user to select the spot for the next move.
    #    ii. Ask the user to enter the row and column number.
    #    iii. Update the spot with the respective player sign.
    #    iv. Check whether the current player won the game or not.
    #    v. If the current player won the game, then print a winning message and break the infinite loop.
    #    vi. Next, check whether the board is filled or not.
    #    vii. If the board is filled, then print the draw message and break the infinite loop.
                
    
    def start_game(self): # # Initialize the game.
        self.player1 = input("Enter the name of Player 1 (X): ") # Store the input in player1 attribute
        self.player2 = input("Enter the name of Player 2 (O): ") # Store input in player2 attribute.
        self.player_symbols[self.player1] = 'X' # Pairs key with value in player_symbols dict. Key is player, value is symbol
        self.player_symbols[self.player2] = 'O'
        players = [self.player1, self.player2] # Create list containing both player names
        current_player = random.choice(players) # Randomly choose who goes first.
        
        # infinite loop that breaks when the game is over (either win or draw).
        while True: 
            print(f"\nPlayer {current_player}'s turn:")
            self.show_board() 
            
            try:
                # Ask the player to enter the row and column number for their move.
                row = int(input("Enter the row number (0, 1, or 2): "))
                col = int(input("Enter the column number (0, 1, or 2): "))

                # Check if the selected cell on the board is empty.
                if self.board[row][col] == '{}':
                    # Update the board with the current player's symbol.
                    self.board[row][col] = self.player_symbols[current_player]

                    # Check if the current player has won the game after their move.
                    if self.has_player_won(current_player):
                        self.show_board()
                        print(f"\nPlayer {current_player} wins")
                        break  # Exit the loop since the game has ended.

                    # Check if the board is filled, which indicates a draw.
                    if self.is_board_filled():
                        self.show_board()
                        print("\nDraw")
                        break  # Exit the loop since the game has ended.

                    # Switch the current player for the next turn.
                    current_player = self.player2 if current_player == self.player1 else self.player1
                else:
                    # Inform the player that their move is illegal and ask them to choose an empty spot.
                    print("\nIllegal move, please choose an empty spot.")
            except IndexError:
                # Handle the case when the player enters an invalid row or column number.
                print("\nInvalid row or column number. Please enter a valid number (0, 1, or 2).")
            except ValueError:
                # Handle the case when the player enters a value that cannot be converted to an integer.
                print("\nInvalid input. Please enter a valid number (0, 1, or 2).")


        
game = TicTacToe()
game.start_game()

