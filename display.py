#!/usr/bin/env python3
"""
Display the world, no progression through time yet.

"""

ALIVE = "●"
DEAD = "○"

WIDTH = 5
HEIGHT = 5


def draw(board):
	def row(y):
		return (ALIVE if (x, y) in board else DEAD for x in range(WIDTH))

	for y in range(HEIGHT):
		print("".join(row(y)))


board = {(2, 1), (2, 2), (2, 3)}
draw(board)