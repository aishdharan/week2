import sys
import os
import cmath  # not necessary


def calculate(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    # looks like a google answer to me
    # simpler to stick to material learned in class
    """
    with a=1, b=2, c=1 I get:
        Traceback (most recent call last):
      File "/Users/paulkorir/sci2pro/aishdharan/week2/week2/problem7.py", line 28, in <module>
        sys.exit(main())
      File "/Users/paulkorir/sci2pro/aishdharan/week2/week2/problem7.py", line 20, in main
        x1, x2 = calculate(a, b, c)
      File "/Users/paulkorir/sci2pro/aishdharan/week2/week2/problem7.py", line 13, in calculate
        return x1, x2
    UnboundLocalError: local variable 'x1' referenced before assignment
    """
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
