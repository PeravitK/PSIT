"""Runner"""
def main():
    """Runner"""
    text = input()
    num_ = int(input())
    if num_ == 0:
        print("")
    else:
        print(("%s\n" %text)*(num_-1)+text)
main()
