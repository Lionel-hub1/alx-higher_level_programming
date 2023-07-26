#!/usr/bin/python3
"""
The N queens puzzle is the challenge of placing N non-attacking queens
on an N×N chessboard.
Write a program that solves the N queens problem

Usage: nqueens N
    If the user called the program with the wrong number of arguments,
    print Usage: nqueens N, followed by a new line, and exit with the
    status 1
    where N must be an integer greater or equal to 4
"""
import sys


def nqueens(n):
    """
    Solves the N queens problem
    Args:
        n (int): The size of the board
    """
    if not isinstance(n, int):
        print("N must be a number")
        exit(1)

    if n < 4:
        print("N must be at least 4")
        exit(1)

    board = [[0 for i in range(n)] for j in range(n)]
    solve(board, 0, n)


def solve(board, col, n):
    """
    Solves the N queens problem
    Args:
        board (list): The board
        col (int): The column to place the queen
        n (int): The size of the board
    """
    if col == n:
        print_board(board)
        return True

    res = False
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            res = solve(board, col + 1, n) or res
            board[i][col] = 0

    return res


def is_safe(board, row, col, n):
    """
    Checks if it's safe to place a queen
    Args:
        board (list): The board
        row (int): The row to check
        col (int): The column to check
        n (int): The size of the board
    """
    for i in range(col):
        if board[row][i] == 1:
            return False

    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False

        i -= 1
        j -= 1

    i = row
    j = col
    while j >= 0 and i < n:
        if board[i][j] == 1:
            return False

        i = i + 1
        j = j - 1

    return True


def print_board(board):
    """
    Prints the board
    Args:
        board (list): The board
    """
    res = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                res.append([i, j])

    print(res)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        nqueens(int(sys.argv[1]))
    except ValueError:
        print("N must be a number")
        sys.exit(1)
