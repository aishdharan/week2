import sys
import os


# f-string
def main():
    x = input("What is your name: ")
    y = input("What is your age: ")
    z = int(input("What is your year of birth: "))
    print(f"Your name is {x} and your age is {y} years old. You were born in {z}. You will be 77 years old on {z + 77}")
    return os.X_OK

if __name__ == "__main__":
    sys.exit(main())
