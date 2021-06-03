import sys


def main():
    s = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur rhoncus tincidunt sem nec gravida. Sed id convallis quam. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus dui purus, ornare vitae metus vitae, feugiat ultricies ipsum. Etiam id ante quis purus rhoncus egestas. Donec vel ligula lacinia, iaculis ipsum vitae, vulputate nunc. Aliquam tellus libero, sagittis quis massa elementum, semper sodales lacus. Sed justo arcu, lobortis quis bibendum ac, fermentum ut mi. Quisque faucibus ex vitae sapien aliquam blandit. Donec fringilla sit amet augue id venenatis. Integer at nibh quis justo consectetur posuere. Nulla facilisis mi massa, sed congue lectus vehicula sed. Quisque placerat ultrices est congue vestibulum. Maecenas fermentum purus et ipsum volutpat, eu convallis risus interdum. Donec vel nunc suscipit, venenatis mi at, convallis sapien. Integer ut metus id neque rhoncus commodo."
    x = len(s)
    y = s.count('it')
    print(f"How many characters does the string have? {x}")
    # How many characters does the string have? 920
    print(f"How many times does substring 'it' occur on it? {y}")
    # How many times does substring 'it' occur on it? 13



if __name__ == "__main__":
    sys.exit(main())
