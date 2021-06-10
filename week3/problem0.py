import os
import sys
import random


def main():
    r = int(input("Give a range: "))
    K = int(input("Give value of k: "))
    X = random.choices(range(r), k=K)
    X_list = list(X)
    print(X_list)

    return os.X_OK


if __name__ == "__main__":
    sys.exit(main())
