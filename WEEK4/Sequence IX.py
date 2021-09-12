'''Sequence IX'''
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
        for k in range(i-1, 0, -1):
            if k >= 10:
                print("%d" %(k), end=" ")
            else:
                print("%s%d" %("0", k), end=" ")
        print()
main()
