#!/usr/bin/python3
"""Solves the N-queens puzzle.
Determines all possible solutions to placing N
N non-attacking queens on an NxN chessboard.
Example:
    $ ./101-nqueens.py N
N must be an integer greater than or equal to 4.
Attributes:
    board (list): A list of lists representing the chessboard.
    solutions (list): A list of lists containing solutions.
Solutions are represented in the format [[r, c], [r, c], [r, c], [r, c]]
where `r` and `c` represent the row and column, respectively, where a
queen must be placed on the chessboard.
"""
import sys


def n_queens(N, queens=[], xy_dif=set(), xy_sum=set()):
    if len(queens) == N:
        print(queens)
        return

    y = len(queens)
    for x in range(N):
        if x not in queens and y-x not in xy_dif and y+x not in xy_sum:
            n_queens(N, queens + [x], xy_dif.union([y-x]), xy_sum.union([y+x]))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)

    if N < 4:
        print("N must be at least 4")
        exit(1)

    n_queens(N)
    print(sol)
