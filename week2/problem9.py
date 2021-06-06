import sys
import os
import random


def main():
    # here is a sketch
    X = random.random()
    Y = random.random()
    print("Enter two numbers each between 0 and 1.")
    x = float(input("x? "))
    y = float(input("y? "))
    print(f"Ace: {x < X and y > Y}")
    # etc...
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
