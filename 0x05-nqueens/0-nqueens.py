#!/usr/bin/python3
"""The code solves the n-queens challenge"""

import sys


def print_solution(solution):
    """Print a solution in the required format."""
    print(solution)

def is_safe(queens, row, col):
    """Check if a queen can be placed at (row, col)
       without being attacked."""
    for r, c in queens:
        if c == col or abs(r - row) == abs(c - col):
            return False
    return True

def solve_nqueens(N):
    """Find all solutions to the N-Queens problem."""
    solutions = []
    def backtrack(row, queens):
        if row == N:
            solutions.append(queens[:])
            return
        for col in range(N):
            if is_safe(queens, row, col):
                queens.append([row, col])
                backtrack(row + 1, queens)
                queens.pop()
    backtrack(0, [])
    for solution in solutions:
        print_solution(solution)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    solve_nqueens(N)

