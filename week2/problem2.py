import sys


def main():
    s = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur rhoncus tincidunt sem nec gravida. Sed id convallis quam. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus dui purus, ornare vitae metus vitae, feugiat ultricies ipsum. Etiam id ante quis purus rhoncus egestas. Donec vel ligula lacinia, iaculis ipsum vitae, vulputate nunc. Aliquam tellus libero, sagittis quis massa elementum, semper sodales lacus. Sed justo arcu, lobortis quis bibendum ac, fermentum ut mi. Quisque faucibus ex vitae sapien aliquam blandit. Donec fringilla sit amet augue id venenatis. Integer at nibh quis justo consectetur posuere. Nulla facilisis mi massa, sed congue lectus vehicula sed. Quisque placerat ultrices est congue vestibulum. Maecenas fermentum purus et ipsum volutpat, eu convallis risus interdum. Donec vel nunc suscipit, venenatis mi at, convallis sapien. Integer ut metus id neque rhoncus commodo."
    x = len(s)
    y = s.count('it')
    z = s.lower()
    print(f"How many characters does the string have? {x}")
    # How many characters does the string have? 920
    print(f"How many times does substring 'it' occur on it? {y}")
    # How many times does substring 'it' occur on it? 13
    print(f"Convert whole text into lowercase. {z}")
    # Convert whole text into lowercase. lorem ipsum dolor sit amet, consectetur adipiscing elit. curabitur rhoncus tincidunt sem nec gravida. sed id convallis quam. lorem ipsum dolor sit amet, consectetur adipiscing elit. phasellus dui purus, ornare vitae metus vitae, feugiat ultricies ipsum. etiam id ante quis purus rhoncus egestas. donec vel ligula lacinia, iaculis ipsum vitae, vulputate nunc. aliquam tellus libero, sagittis quis massa elementum, semper sodales lacus. sed justo arcu, lobortis quis bibendum ac, fermentum ut mi. quisque faucibus ex vitae sapien aliquam blandit. donec fringilla sit amet augue id venenatis. integer at nibh quis justo consectetur posuere. nulla facilisis mi massa, sed congue lectus vehicula sed. quisque placerat ultrices est congue vestibulum. maecenas fermentum purus et ipsum volutpat, eu convallis risus interdum. donec vel nunc suscipit, venenatis mi at, convallis sapien. integer ut metus id neque rhoncus commodo.
    print(s.replace("i", "*"))
    # Replace all instances of the letter 'i' with an asterisk '*'. Lorem *psum dolor s*t amet, consectetur ad*p*sc*ng el*t. Curab*tur rhoncus t*nc*dunt sem nec grav*da. Sed *d convall*s quam. Lorem *psum dolor s*t amet, consectetur ad*p*sc*ng el*t. Phasellus du* purus, ornare v*tae metus v*tae, feug*at ultr*c*es *psum. Et*am *d ante qu*s purus rhoncus egestas. Donec vel l*gula lac*n*a, *acul*s *psum v*tae, vulputate nunc. Al*quam tellus l*bero, sag*tt*s qu*s massa elementum, semper sodales lacus. Sed justo arcu, lobort*s qu*s b*bendum ac, fermentum ut m*. Qu*sque fauc*bus ex v*tae sap*en al*quam bland*t. Donec fr*ng*lla s*t amet augue *d venenat*s. Integer at n*bh qu*s justo consectetur posuere. Nulla fac*l*s*s m* massa, sed congue lectus veh*cula sed. Qu*sque placerat ultr*ces est congue vest*bulum. Maecenas fermentum purus et *psum volutpat, eu convall*s r*sus *nterdum. Donec vel nunc susc*p*t, venenat*s m* at, convall*s sap*en. Integer ut metus *d neque rhoncus commodo.


if __name__ == "__main__":
    sys.exit(main())

