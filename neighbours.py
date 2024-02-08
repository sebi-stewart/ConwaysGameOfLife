#!/usr/bin/env python3
"""
Test counting of alive neighbours.

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
        # temporarily shows number of neighbours
        return (ALIVE if (x, y) in board else str(counter[(x, y)]) for x in range(WIDTH))

    for y in range(HEIGHT):
        print("".join(row(y)))


board = {(2, 1), (2, 2), (2, 3)}

# for each living cell, include it in the count of its neighbours
counter = Counter((x + dx, y + dy) for x, y in board for dx, dy in NEIGHBOURS)

draw(board)
