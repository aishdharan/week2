import sys
import os
from random import randrange


def main():
    n = int(input("Enter a number between 0 to 9: "))
    x = randrange(0, 10)
    print(f"random number is {x}")
    if n > x:
        print("user\'s number is greater than random number")
    else:
        print("User' number is less than the random number")
    return os.X_OK


if __name__ == "__main__":
    sys.exit(main())

