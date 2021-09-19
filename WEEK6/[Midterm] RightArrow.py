"""[Midterm] RightArrow"""
def main():
    """[Midterm] RightArrow"""
    num1 = int(input())
    num2 = int(input())
    for i in range(-(num2//2), (num2//2)+1):
        print(' '*((num2//2)-abs(i)), end='')
        for _ in range(num1):
            print('*', end='')
        print()
main()
