"""[Midterm] Left Arrow"""
def main():
    """[Midterm] Left Arrow"""
    num1 = int(input())
    num2 = int(input())
    for i in range(-(num2//2), (num2//2)+1):
        print(" "*abs(i) + "*"*num1)
main()
