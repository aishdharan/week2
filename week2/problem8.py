import sys
import os
from random import randrange
# please stick to the material introduced in class
# import random
# random.randint() was expected


def main():
    n = int(input("Enter a number between 0 to 9: "))
    x = randrange(0, 10)
    print(x)
    print(f"random number is {x}")
    # we haven't quite covered if statements so I cannot give bonus for this
    if n > x:
        # good escape sequence but not needed with double quotes on outside
        print("user\'s number is greater than random number")
    else:
        print("user\'s number is less than the random number")
    return os.X_OK


if __name__ == "__main__":
    sys.exit(main())

