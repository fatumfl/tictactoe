#!/usr/bin/env python3
# Tic-Tac-Toe by FatumFL
# v0.1.4

from random import choice

msg = { # Applies a dictionary of all in-game messages.
	1:"\nHello, Mr. {}!",
	2:"You're first!",
	3:"I'm first!",
	4:"Please enter number of the cell [1-9]: ",
	5:"There is no such cell number. Max is 9, min is 1.",
	6:"There is already mark in this cell.",
	7:"It's my turn.",
	8:"Let me think... I'll choose this one:",
	9:"Game Over!",
	10:"You win!",
	11:"You lose!",
	12:"It's a tie!",
	13:"Want to start a new game (y/n)? ",
	14:"Input should be integer.",
	15:"Select game level: 1 - easy, 2 - normal, 3 - hard > "}

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
		return self.board[:]
	
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
	# AI logick defined in functions _easy, _normal and _hard
	
	def __init__(self):
		self.lvl = 1 # Defines game level
		self.mark = ''
	
	def _easy(self, cells):
		# Easy game level.
		cell = choice(cells)
		return cell

	def _normal(self, board):
		# Medium game level.
		localboard = Board()
		localboard.board = board[:]
		empty_cells = localboard.list_empty_cells()
		
		for i in empty_cells:
			localboard.board = board[:]
			localboard.add_mark(i, self.mark)
			if localboard.check_board() == self.mark:
				return i
		
		pl = "XO".replace(self.mark, '')
		for i in empty_cells:
			localboard.board = board[:]
			localboard.add_mark(i, pl)
			if localboard.check_board() == pl:
				return i


	def _hard(self, cells):
		# Hard game level.
		corner = list({1,3,7,9} & set(cells))
		sides = list({2,4,6,8} & set(cells))
		if 5 in cells:
			return 5
		elif corner:
			return choice(corner)
		elif sides:
			return choice(sides)
		
	
	def ai_turn(self, board):
		# Supports AI logic
	
		cells = [i for i in range(1, 10) if board[i] is None]

		if self.lvl == 1:
			return self._easy(cells)
		elif self.lvl == 2:
			return self._normal(board) or self._easy(cells)
		elif self.lvl == 3:
			return self._normal(board) or self._hard(cells)

def greeting():
	# Defines who goes first and prints greeting.
	lvl = int(input(msg[15]))
	player = choice(['X', 'O'])
	if player == 'X':
		print(msg[1].format(player), msg[2])
		comp = 'O'
		next_one = 0
	else:
		print(msg[1].format(player))
		print(msg[3])
		comp = 'X'
		next_one = 1
	return player, comp, next_one, lvl

def players_move(empty_cells):
	
	cell = int(input(msg[4]))
	if cell > 9 or cell < 1:
		print(msg[5])
		cell = players_move(empty_cells)
	elif cell not in empty_cells:
		print(msg[6])
		cell = players_move(empty_cells)
	return cell

def new_game_plus():
	if input(msg[13]).lower().startswith('y'):
		main()

def main():
	gameboard = Board()
	comp_ai = AI()
	print()
	player, comp, turn, lvl = greeting()
	comp_ai.mark = comp
	comp_ai.lvl = lvl
	
	while gameboard.check_board() == 0:
		board = gameboard.copy_board()
		cells = gameboard.list_empty_cells()
		if turn == 0:
			cell = players_move(cells)
			gameboard.add_mark(cell, player)
			turn = 1
		else:
			cell = comp_ai.ai_turn(board)
			gameboard.add_mark(cell, comp)
			turn = 0
			print()
			print(msg[8])
		gameboard.print_board()
	
	winner = gameboard.check_board()
	print('\n' + msg[9], end=' ')
	if winner == player:
		gameboard.store_board("player")
		print(msg[10])
	if winner == comp:
		gameboard.store_board("AI")
		print(msg[11])
	if winner == "tie":
		gameboard.store_board(winner)
		print(msg[12])
	
	new_game_plus()

if __name__ == "__main__":
	main()