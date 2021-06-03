import os
import sys
import math
import cmath


def calculate(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if a != 0:
        if discriminant == 0:
            x = -b / (2 * a)
            print("x=", x)
            print("equal root")

        elif discriminant > 0:
            x1 = (-b + math.sqrt(d)) / (2 * a)
            x2 = (-b - math.sqrt(d)) / (2 * a)
            print("x1=", x1, " and x2=", x2)
            print("real root")

        elif discriminant < 0:
            x1 = complex((- b + (cmath.sqrt(discriminant))) / (2 * a))
            x2 = complex((- b - (cmath.sqrt(discriminant))) / (2 * a))
            print("x1=", x1, " and x2=", x2)
            print("complex root")
    return x1, x2

def main():
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))
    x1, x2 = calculate(a, b, c)
    # return value of exit status
    return os.X_OK


if __name__ == "__main__":
    # exit status went to os
    sys.exit(main())
