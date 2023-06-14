#!/usr/bin/python3


def multiply_list_map(my_list=[], number=0):
    # Multiply each element in my_list by the given number
    multiplied_list = list(map(lambda x: x * number, my_list))

    # Return the resulting multiplied list
    return multiplied_list
