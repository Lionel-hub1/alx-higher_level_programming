#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """
    Divides element by element of two lists and return new list with results

    Args:
    my_list_1: Is the first list
    my_list_2: Is the second list
    list_length: Is the desired length of the resulting list

    Returns:
    A new list with the division results
    """
    result = []
    try:
        for i in range(0, list_length):
            try:
                a = my_list_1[i]
                b = my_list_2[i]
                try:
                    division = a / b
                    result.append(division)
                except ZeroDivisionError:
                    result.append(0)
                    print("division by 0")
            except (ValueError, TypeError):
                result.append(0)
                print("wrong type")
    except IndexError:
        print("out of range")

    return result
