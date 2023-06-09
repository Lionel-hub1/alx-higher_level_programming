#!/usr/bin/python3
import sys

if __name__ == "__main__":
    summation = 0

    # Loop through all arguments and add each on existing summation
    for i in range(len(sys.argv) - 1):
        summation += int(sys.argv[i + 1])

    print("{}".format(summation))
