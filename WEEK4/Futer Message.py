'''Future Message'''
def main():
    '''docstring'''
    text = input()
    if text.isnumeric() == 1:
        print("Number")
    elif text.isspace() == 1:
        print("Space")
    elif text.islower() == 1:
        print("Lowercase")
    elif text.isupper() == 1:
        print("Uppercase")
    elif text.istitle() == 1:
        print("Title")
    else:
        print("Other")
main()
