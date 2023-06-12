#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for elemet in row:
            print("{:d}".format(elemet), end=" " if elemet != row[-1] else "")
        print()
