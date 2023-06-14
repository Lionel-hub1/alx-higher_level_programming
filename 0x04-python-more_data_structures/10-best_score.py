#!/usr/bin/python3


def best_score(a_dictionary):
    # Check if the dictionary is empty
    if not a_dictionary:
        # If empty, return None
        return None

    # Find the key with the maximum value
    max_value_key = max(a_dictionary, key=a_dictionary.get)

    # Return the key with the maximum value
    return max_value_key
