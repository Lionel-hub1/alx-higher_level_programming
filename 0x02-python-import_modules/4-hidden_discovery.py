#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    names = [name for name in dir(hidden_4) if not name.startswith("__")]
    if names:
        print("\n".join(names))
