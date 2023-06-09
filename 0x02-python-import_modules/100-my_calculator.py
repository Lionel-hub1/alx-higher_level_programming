#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

if __name__ == "__main__":
    argc = len(sys.argv)

    if argc - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    oper = {"+": add, "-": sub, "*": mul, "/": div}

    if sys.argv[2] not in list(oper.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    o = sys.argv[2]

    print("{} {} {} = {}".format(a, o, b, oper[o](a, b)))
