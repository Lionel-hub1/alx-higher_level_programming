#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    # Create a list of keys to delete
    keys_to_delete = []

    # Iterate over the key-value pairs in the dictionary
    for key, val in a_dictionary.items():
        # Check if the value matches the specific value
        if val == value:
            # Add the key to the list of keys to delete
            keys_to_delete.append(key)

    # Delete the keys from the dictionary
    for key in keys_to_delete:
        del a_dictionary[key]

    # Return the modified dictionary
    return a_dictionary
