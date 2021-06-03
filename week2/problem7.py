import sys
import os
import cmath


def calculate(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        x1 = complex((- b + (cmath.sqrt(discriminant))) / (2 * a))
        x2 = complex((- b - (cmath.sqrt(discriminant))) / (2 * a))
    return x1, x2


def main():
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    x1, x2 = calculate(a, b, c)
    print(f"x1={x1}, x2={x2}")
    # return value of exit status
    return os.X_OK


if __name__ == "__main__":
    # exit status went to os
    sys.exit(main())
