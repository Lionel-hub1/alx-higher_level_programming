#!/usr/bin/python3
from magic_calculation_102 import add, sub


def magic_calculation(a, b):
    if a < b:
        c = add(a, b)

        for i in range(4, 6):  # Loop from 4 to 5 (exclusive)
            c = add(c, i)  # add values in each iteration
        return (c)

    else:  # for when a is not less than b
        return(sub(a, b))
