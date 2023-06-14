#!/usr/bin/python3


def uniq_add(my_list=[]):
    # Create an empty set to store unique integers
    unique_integers = set()

    # Iterate over the elements of the input list
    for element in my_list:
        # Check if the element is an integer
        if isinstance(element, int):
            # Add the integer to the set of unique integers
            unique_integers.add(element)

    # Compute the sum of the unique integers
    sum_unique_integers = sum(unique_integers)

    return sum_unique_integers
