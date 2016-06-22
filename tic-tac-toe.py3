#!/usr/bin/env python3

board = [[None,None,None], [None,None,None], [None,None,None]] # Gameboard
player = '' # Stores mark of the player
comp = '' # Stores mark of the computer
turn = 0 # Defines the order: 0 - player turn, 1 - comp turn

def greeting():
	# Defines who goes first and prints greeting.
	from random import choice
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
