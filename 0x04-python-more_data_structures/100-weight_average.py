#!/usr/bin/python3


def weight_average(my_list=[]):
    # Check if the list is empty
    if not my_list:
        return 0

    # Initialize variables for sum of products and total weight
    sum_products = 0
    total_weight = 0

    # Iterate over the tuples in the list
    for score, weight in my_list:
        # Calculate the product of score and weight and add it to the sum
        sum_products += score * weight
        # Add the weight to the total weight
        total_weight += weight

    # Calculate the weighted average
    weighted_average = sum_products / total_weight

    return weighted_average
