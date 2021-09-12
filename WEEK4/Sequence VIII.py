'''Sequence VIII'''
def main():
    '''docstring'''
    num = int(input())
    for i in range(1, num+1):
        space = (num-i)*3
        for j in range(1, i+1):
            if j >= 10:
                print("%s%d" %(" " *space, j), end=" ")
            else:
                print("%s%s%d" %(" " *space, "0", j), end=" ")
            space = 0
        print()
main()
