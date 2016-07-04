#!/usr/bin/env python3
# Tic-Tac-Toe by FatumFL
# v0.1.1

class Board(object):
	# Gameboard
	
	def __init__ (self):
		self.board = [0, None, None, None, None, None, None, None, None, None] # Initializing board in class instances
	
	def add_mark(self, i, mark):
		# Add given mark to the board
		self.board[i] = mark
	
	def print_board(self):
		# Printing board to stdout
		for i in range(1, 10):
			if self.board[i] is None:
				print('_', end=' ')
			else:
				print(self.board[i], end=' ')
			if i % 3 == 0:
				print()
	
	def check_board(self):
		# Is there a winner? Let me check...
		if self.board[1] == self.board[2] == self.board[3] != None: # first row
			self.board[0] = self.board[1]
		elif self.board[4] == self.board[5] == self.board[6] != None: # second row
			self.board[0] = self.board[4]
		elif self.board[7] == self.board[8] == self.board[9] != None: # third row
			self.board[0] = self.board[7]
		elif self.board[1] == self.board[4] == self.board[7] != None: # first column
			self.board[0] = self.board[1]
		elif self.board[2] == self.board[5] == self.board[8] != None: # second column
			self.board[0] = self.board[2]
		elif self.board[3] == self.board[6] == self.board[9] != None: # third column
			self.board[0] = self.board[3]
		elif self.board[1] == self.board[5] == self.board[9] != None: # diagonal from left to right
			self.board[0] = self.board[1]
		elif self.board[3] == self.board[5] == self.board[7] != None: # diagonal from right to left
			self.board[0] = self.board[3]
		elif None not in self.board: # if board is full it's a tie
			self.board[0] = "tie"
		return self.board[0]
	
	def list_empty_cells(self):
		# Return a list of empty cells
		return [i for i in range(1, 10) if self.board[i] is None]
	
	def copy_board(self):
		# Returns a copy of the board
		return self.board[1:]
	
	def store_board(self):
		# Writes game result to a file
		if self.board[0]:
			db = open("rounds.text", mode="a")
			print(self.board, file=db)
			db.close()
			return True
		else:
			return False
















player = '' # Stores mark of the player
comp = '' # Stores mark of the computer
turn = 0 # Defines the order: 0 - player turn, 1 - comp turn

def greeting():
	# Defines who goes first and prints greeting.
	from random import choice, radint
	
	player = choice(['X', 'O'])
	if player == 'X':
		print("Hello, Mr. X! Make the first move.")
		comp = 'O'
		next_one = 0
	else:
		print("Hello, Mr. O! It's my turn.")
		comp = 'X'
		next_one = 1
	return player, comp, next_one

def players_move():
	global board
	row, column = map(int, input("Please enter number of the cell as follows ROWxCOLUMN: ").split('x'))
	if column > 3 or column < 1 or row > 3 or row < 1:
		print("There is no such column or/and row number. Max is 3, min is 1.")
		players_move()
	else:
		cell = board[row - 1][column - 1]
		if cell is not None:
			print("There is already {} in this cell.".format(cell))
			players_move()
		else:
			board[row - 1][column - 1] = player
	return 0

def comps_move():
	from random import randint
	global board
	row, column = randint(0,2), randint(0,2)
	cell = board[row][column]
	if cell is not None:
		comps_move()
	else:
		print("Let me think... My move will be:")
		board[row][column] = comp
	return 1

def check_board():
	# Checking rows:
	if board[0][0]==board[0][1]==board[0][2]!=None:
		print("Game over! Mr. {} wins!".format(board[0][0]))
		return 1
	elif board[1][0]==board[1][1]==board[1][2]!=None:
		print("Game over! Mr. {} wins!".format(board[1][0]))
		return 1
	elif board[2][0]==board[2][1]==board[2][2]!=None:
		print("Game over! Mr. {} wins!".format(board[2][0]))
		return 1
	elif board[0][0]==board[1][0]==board[2][0]!=None:
		print("Game over! Mr. {} wins!".format(board[0][0]))
		return 1
	elif board[0][1]==board[1][1]==board[2][1]!=None:
		print("Game over! Mr. {} wins!".format(board[0][1]))
		return 1
	elif board[0][2]==board[1][2]==board[2][2]!=None:
		print("Game over! Mr. {} wins!".format(board[0][2]))
		return 1
	elif board[0][0]==board[1][1]==board[2][2]!=None:
		print("Game over! Mr. {} wins!".format(board[0][0]))
		return 1
	elif board[0][2]==board[1][1]==board[2][0]!=None:
		print("Game over! Mr. {} wins!".format(board[0][2]))
		return 1
	else:
		trigger = 0
		for row in board:
			if None in row:
				trigger = 1
		if trigger == 0:
				print("Game over! It's a tie!")
				return 1
	return 0

def print_board():
	for row in board:
		for i in row:
			if i is None:
				print('_', end=' ')
			else:
				print(i, end=' ')
		print()

if __name__ == "__main__":
	player, comp, turn = greeting()
	
	while check_board() != 1:
		if turn == 0:
			players_move()
			turn = 1
		else:
			comps_move()
			turn = 0
		print_board()