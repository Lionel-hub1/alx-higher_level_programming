#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for element in my_list:
            print(element, end="")
            count += 1
            if count == x:
                break
    except TypeError:
        pass

    print()
    return count
