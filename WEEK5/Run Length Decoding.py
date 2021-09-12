"""Run Length Decoding"""
def main():
    """Run Length Decoding"""
    text = input()
    num = ''
    for i in text:
        if i.isnumeric():
            num += i
        else:
            print(str(i)*int(num), end='')
            num = ''
main()
