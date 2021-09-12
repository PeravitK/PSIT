"""ChristmasTree"""
def main():
    """ChristmasTree"""
    num1 = int(input())
    num2 = int(input())
    for i in range(1, num1+1):
        print(' '*(num1-i)+'*'*((2*i)-1))
    for _ in range(1, num2+1):
        print(' '*(num1-2)+'-'*3)
main()
