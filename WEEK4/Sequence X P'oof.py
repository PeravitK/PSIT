'''Sequence XI'''
def main():
    '''docstring'''
    num = int(input())
    for row in range(-(num-1), num):
        for col in range(-(num-1), num):
            if abs(row) + abs(col) < num:
                print("%d" %(num-abs(row)-abs(col)), end=" ")
            else:
                print(" ", end=" ")
        print()
main()
