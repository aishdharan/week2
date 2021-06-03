import sys
import os


def main():
    a = "apache license"
    a1 = a.title()
    print(a1.center(40))
    b = "version 2.0, January 2004"
    b1 = b.title()
    print(b1.center(40))
    c = "http://www.apache.org/licenses/"
    print(c.center(40))
    return os.X_OK


if __name__ == "__main__":
    sys.exit(main())
