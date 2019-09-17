#!/usr/bin/env python3
# Tic-Tac-Toe CLI Version by FatumFL
# v0.2.1

from random import choice
from sys import exit
from shared import *

def game_lvl():
	try:
		lvl = int(input(msg[15]))
	except:
		print(msg[16])
		return game_lvl()
	if lvl > 3 or lvl < 1:
		print(msg[17])
		return game_lvl()
	return lvl

def greeting():
	# Defines who goes first and prints greeting. 'X' always first.
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
	return player, comp, next_one

def players_move(empty_cells):
	cell = input(msg[4])
	if cell.startswith('q'):
		exit(0)
	try:
		cell = int(cell)
	except:
		print(msg[16])
		cell = players_move(empty_cells)
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
	comp_ai.lvl = game_lvl()
	player, comp, turn = greeting()
	comp_ai.mark = comp

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
