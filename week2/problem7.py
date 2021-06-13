import sys
import os
import cmath  # not necessary

"""
Notes:
- A complex number is made up of two parts: real and imaginary. Python allows us 
to represent complex numbers by passing the real and imaginary parts as arguments 
to the complex() class. For example,

complex(1, 2) 

returns the complex number (1+2j): 1 is real and 2j is imaginary.

Now, when we are trying to solve (I will only handle the case with +; the one with - is the same) 

x = (-b + math.sqrt(b**2 - 4*a*c)/(2*a)

or
    -b + math.sqrt(b**2 - 4*a*c)
x = ----------------------------.
              2*a

We can write this as 

    ⎡   b ⎤ ⎡math.sqrt(b**2 - 4*a*c)⎤
x = ⎢- ---⎢+⎢-----------------------⎢
    ⎣  2*a⎦ ⎣      2*a              ⎦

Now the right has two values: the one first one is always real but the second one 
becomes imaginary when the discriminant is negative. Please see the slide titled
Complex Math in week3 slides.

This will give you enough to work on to solve the problem. I'd like you to experience
the joy of solving it for yourself.
"""


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
