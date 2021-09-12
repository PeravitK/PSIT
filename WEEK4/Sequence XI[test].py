"""Sequence XI"""
def main():
    """Sequence XI"""
    num = int(input())
    for row in range(-(num-1), num):
        for col in range(-(num-1), num):
            if row == 0 and col == 0:
                if num >= 10:
                    print("%d" %(num), end=" ")
                else:
                    print("%s%d" %('0', num), end=" ")
            else:   
                max_ = max(abs(row), abs(col))
                if (num-max_) >= 10:
                    print("%d" %(num-max_), end=" ")
                else:
                    print("%s%d" %('0',num-max_), end=" ")
        print()
main()
