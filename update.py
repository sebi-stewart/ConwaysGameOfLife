#!/usr/bin/env python3
"""
Update the board over time.

"""
import itertools

from collections import Counter


ALIVE = "●"
DEAD = "○"

WIDTH = 5
HEIGHT = 5

NEIGHBOURS = list(itertools.product([0, 1, -1], repeat=2))[1:]


def draw(board):
	def row(y):
		return (ALIVE if (x, y) in board else DEAD for x in range(WIDTH))

	for y in range(HEIGHT):
		print("".join(row(y)))


def update(board):
	# for each living cell, include it in the count of its neighbours
	counter = Counter((x + dx, y + dy) for x, y in board for dx, dy in NEIGHBOURS)
	# apply rules for reproduction and survival
	return {cell for cell, count in counter.items()
		if count == 3 or (count == 2 and cell in board)}

def play(board, n=5):
	for i in range(n):
		draw(board)
		print("---")
		board = update(board)


board = {(2, 1), (2, 2), (2, 3)}
play(board)