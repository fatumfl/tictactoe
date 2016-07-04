#!/usr/bin/env python3
# Tic-Tac-Toe by FatumFL
# v0.1.2

from random import choice

class Board(object):
	# Gameboard
	
	def __init__ (self):
		self.board = [0, None, None, None, None, None, None, None, None, None] # Initializing board in class instances
	
	def add_mark(self, i, mark):
		# Add given mark to the specified cell of the board
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
	
	def store_board(self, winner):
		# Writes game result to a file. Winner should be either 0 or 1.
		if self.board[0]:
			with open("rounds.text", mode="a") as db:
				print(self.board, '\t', winner, file=db)
			return True
		else:
			return False

class AI(object):
	# Your rival
	
	def __init__(self):
		self.lvl = 1
	
	def _easy(self, empty_cells):
		cell = choice(empty_cells)
		return cell

	def _medium(self, board):
		pass

	def _hard(self, board):
		pass
	
	def ai_turn(self, data):
		if self.lvl == 1:
			return self._easy(data)
		if self.lvl == 2:
			return self._medium(data)
		if self.lvl == 3:
			return self._hard(data)

def greeting():
	# Defines who goes first and prints greeting.
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

def players_move(empty_cells):
	cell = int(input("Please enter number of the cell [1-9]:"))
	if cell > 9 or cell < 1:
		print("There is no such cell number. Max is 9, min is 1.")
		players_move(empty_cells)
	elif cell not in empty_cells:
			print("There is already mark in this cell.")
			players_move(empty_cells)
	return cell

def main():
	gameboard = Board()
	comp_ai = AI()
	player, comp, turn = greeting()
	
	while gameboard.check_board() == 0:
		empty_cells = gameboard.list_empty_cells()
		if turn == 0:
			cell = players_move(empty_cells)
			gameboard.add_mark(cell, player)
			turn = 1
		else:
			cell = comp_ai.ai_turn(empty_cells)
			gameboard.add_mark(cell, comp)
			turn = 0
			print("\nLet me choose this one:")
		gameboard.print_board()

if __name__ == "__main__":
	main()