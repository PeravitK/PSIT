'''Sequence XII'''
def main():
    '''docstring'''
    num = int(input())
    for row in range(-(num-1), num):
        for col in range(-(num-1), num):
            if abs(row) == abs(col):
                if num >= 10:
                    print("%d" %(num), end=" ")
                else:
                    print("%s%d" %('0', num), end=" ")
            else:
                min_ = min(abs(row), abs(col))
                max_ = max(abs(row), abs(col))
                ans = num-max_+min_
                if ans >= 10:
                    print("%d" %(num-max_+min_), end=" ")
                else:
                    print("%s%d" %('0', num-max_+min_), end=" ")
        print()
main()
