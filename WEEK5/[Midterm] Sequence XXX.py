"""[Midterm] Sequence XXX"""
def main():
    """[Midterm] Sequence XXX"""
    num1 = int(input())
    num2 = int(input())
    num3 = num2-1
    for row in range(-(int(num1/2)), int(num1/2)+1):
        while num2 > 0:
            for col in range(-(int(num1/2)), int(num1/2)+1):
                if row == int(num1/2) or col == int(num1/2) or \
                    row == -(int(num1/2)) or col == -(int(num1/2)):
                    print('*', end='')
                elif abs(row) == abs(col):
                    print('*', end='')
                else:
                    print(' ', end='')
            if num3 == 0:
                print()
                break
            print(end=' ')
            num3 -= 1
        num3 = num2-1
main()
